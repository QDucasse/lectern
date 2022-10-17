<!-- Please prefix the notes with the date as in [22/12/2020] -->

[12/05/2021]

ROP attacks consist of linking several *gadgets* (blocks of instructions ending with a `ret`). The threat model consists of a system with defenses present i most modern systems: DEP, W+X, ASLR, stack smashing protection (canaries or function cookies), EMET.

**Goal of the attack:** (1) The browser ***renders a malicious web page*** (2) The JavaScript code in this page, once compiled, ***produces a series of gadgets in the JIT buffer*** (3)  A memory-disclosure bug ***reveals the locations of the gadgets*** (4) A ROP chain ***is built with the just constructed gadgets*** and control is transferred to it (5) The ROP chain ***calls `VirtualProtect` (or `mprotect`) and makes the page where the shellcode is stored executable*** (6) Control is transferred to the shellcode and the ***browser is compromised***.

**Exploits:**

**Firefox:** The preparation is as follows, the idea is to produce a series of gadgets that eventually lead to a call to `mprotect`. To do so, the attacker needs to control four registers. First,  the corresponding system call number `0xb` is stored in `%eax`. Then, the address of the page the attacker wants to change is stored in `%ebx`. The length of the region is stored in `%ecx` and the desired access rights, `0x7` here are stored in `%edx`. To accomplish this, the attacker needs a ROP chain which will load the four registers with the required values and then a gadget will call `mprotect`. In Linux for x86 architectures, system calls are performed by using `int 0x80`. Loading a register with the required value can be done in two ways. Either place the required value on the stack and use `pop` or a `mov`-like command to copy the value to the register. For the JIT to work properly, the stack and `pop` are used for *large values* while *small values* are used with `mov` and registers. In the case a `mov` is used, it affects only part of the register and the attacker needs to zero the register before moving the value which is done by using a `xor` gadget.

In the end, the ROP chain involves seven gadgets:

```assembly
pop %ebx; ret;       // page address
pop %ecx; ret;       // region length
xor %eax; %eax; ret; // 0 before mov
mov 0x7d; %a1; ret;  // mprotect set
xor %edx; %edx; ret; // 0 before mov
mov 0x7; %d1; ret;   // permissions to WRX
int 0x80; ret;       // mprotect call
```

The gadgets need to be added to the JIT buffer and the attacker needs to: (1) trigger a JIT compilation (2) add the gadgets to memory. For (1), creating a "hot loop" will most likely trigger the JIT compilation and for (2), variable are initialized with specially crafted immediate values.

```javascript
var g1 = 0;
// ...
var g7 = 0;
for (var i=0; i<10000; ++i) {
    g1 = 50011;
    g2 = 50009;
    g3 = 12828721;
    g4 = 12811696;
    g5 = 12833329;
    g6 = 12781490;
    g7 = 12812493;
}
```

**Chakra:** function to change memory rights is `VirtualProtect` and needs 4 arguments. The attacker needs to adjust the real stack to the fake stack controlled by himself, this can be done by using ***stack pivoting***. It consists of exchanging a register the attacker controls with `%rsp` so the stack pointer points to an arbitrary value. This exchange can be done with `xchg` but unfortunately, it is 2 bytes long (3 with the `ret`) and these gadgets cannot be constructed trivially. 

Chakra uses several protections: (a) ***constant blinding*** where any value less than 2 bytes long is emitted XORed with a random value (and re-XORed when used), (b) ***long gadgets*** cannot be encapsulated in immediate values and have to be split in several parts, moreover Chakra places several checks when compiling such gadgets (c) ***code diversification*** where Chakra emits a random number of `nop` instructions hat change the layout of the JIT buffer and randomize the location of all important gadgets each time they are generated.

The gadgets have to be generated differently:

```javascript
function r8 (addr) {
    return addr + 0x5841;
}

function r9 (addr) {
    returnn addr + 0x5941;
}

function emit_gadgets() {
    for (i=0; i<10000; i++) {
        rax = 0xc358; // pop rax
        rcx = 0xc359; // pop rcx
        rdx = 0xc35a; // pop rdx
        r8(0);
        r9(0);
    }
    return 0;
}

emit_gadgets();
```

**Discovering the Gadgets:** This can be done using ***information leaks*** such as heap overwrites to obtain essential information to discover gadgets. Instead of revealing the code segment of a given object in a typical JS object layout, the attacker reveals the JIT buffer which contains the artificially constructed gadgets. The following code generates an object with a memory layout that can help access the JIT buffer. Accessing `O` then `foo` will give an access to the JIT buffer.

```javascript
O = new Object();
O.g1 = 0xc358;
O.g2 = 0xc359;
function foo(x) { return 0x 5841; }
O.func = foo;
```

**Defenses:** Enhance the JIT buffer with G-Free to remove all gadgets. The produced code is safe and gadget-free.

##### tags: attack, jit, rop, security