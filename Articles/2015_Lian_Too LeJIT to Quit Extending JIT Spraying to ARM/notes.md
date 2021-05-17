<!-- Please prefix the notes with the date as in [22/12/2020] -->

[12/05/2021]

JIT spraying has always be an x86-only attack thanks to its reliance on variable-length, unaligned instructions. ARM and RISC-like architectures work differently as presented.

**ARM Layout:** The ARM architecture has ***13 32-bit general purpose registers*** (`R0-R12`) and ***3 32-bit special-purpose registers*** (`R13-R15`). The usage convention is defined by the Procedure Call Standard (AAPCS). The ***stack pointer register*** (`SP/R13`) is used to hold a pointer to the top of the current execution stack. Special variants of `add` and `sub` are hardwired to `SP` to accelerate stack operations. The ***link register*** (`LR/R14`) is used to hold subroutine return addresses. The ARM analogs of x86 `call` instruction are the branch with link (`bl`) and the exchange (`blx`) instructions. The ***program counter register*** (`PC/R15`) holds the address of the currently-executing instruction plus 8. ARM is a ***bi-endian architecture***, meaning that it can interpret words and halfwords as either big or little endian. The `ENDIANSTATE` execution register stores a bit determining the endianness and the instruction `setend` can modify its value. The ARM architecture also supports the Thumb instruction set that contains mixed 16- and 32-bits instructions (Thumb-2 consists of two instructions close to each other). The choice of the current instruction set is determined by the instruction set state register (`ISETSTATE`). The ARM-Thumb interworking and variable-length instructions can be used as possible vectors for creating instruction confusion.

**JavaScriptCore:** JSC is a multi-tier JavaScript engine, source code is initially compiled to bytecode that is interpreted by an ***interpreter*** but once it has been executed several times (6 for functions, 100 for loops), the bytecode is compiled down to unoptimized native code by the ***baseline JIT***. Once the ***baseline JIT*** has been executed many times (60 for functions, 1000 for loops), the ***DFG JIT*** emits optimized Thumb-2. 

- The ***Low-Level Interpreter (LLInt)*** interprets bytecodes, 32-bit opcodes followed by as many operands as are required. The opcodes are pointers to pre-compiled code snippets in the interpreter's text section. During bytecode execution, a virtual program counter (vPC) register points to the currently-executing opcode in the bytecode while the real `PC` is in the code snippet pointed to by the opcode. The snippet accesses the opcode's operands via vPC-relative memory loads, performs the desired computation, advances the vPC and finally branches o the next opcode's snippet with a register-indirect jump through the vPC.
- The ***Baseline JIT*** generates native code. The instruction stream produced differs from the one executed by the ***LLInt*** since it does not need to manage the vPC. The code has clear boundaries where the execution of one bytecode instruction ends and the next begins, and it does not flow scratch values in registers across those boundaries. Instead, they are stored onto the JavaScript stack and read back by other bytecode operations.
- The ***Data Flow Graph JIT*** uses *dead code elimination analysis*, *function inlining* and a *basic register allocator* to optimize the JITed code better.

On x86, the attacker uses back-to-back sequences of one non-attacker controlled byte (opcode) followed by four bytes of attacker controlled data (an immediate operand). ARM and Thumb need to split a 32-bit immediate value into halfwords and loaded into registers one value at a time. An attacker can control the immediate bits in arithmetic operations (up to 16 bits) or in a PC-relative branch (up to 25 for ARM, 24 for Thumb). Aside from immediate, an attacker can control the choice of operand and destination registers used in instructions by carefully crafting an input.

An attacker can control the content of 8 different registers along with different operations between them:

```javascript
function (R0, R2, R8, R10) {
	var R1  = R0  ^ 0x1234;
	var R4  = R2  ^ 0x2345;
	var R9  = R8  ^ 0x3456;
	var R11 = R10 ^ 0x4567;
    // The values of all 8 registers are known 
	return (R1 ^ R2) | (R4 ^ R8) | (R10 ^ R9) | (R11 ^ R0);
}
```

```assembly
4051       eors   r1 , r2
ea84 0408  eor.w  r4 , r4 , r8
4321       orrs   r1 , r4
ea8a 0a09  eor.w  r10, r10, r9
ea41 010a  orr.w  r1 , r1 , r10
ea8b 0b00  eor.w  r11, r11, r0
ea41 010b  orr.w  r1 , r1 , r11
```



Three JIT spraying attacks are presented: first the ***original attack shown to be unfeasible***, then the attack with the ***`ISETSTATE` register*** and finally an attack using ***gadget chaining***. 

The original attack is unfeasible because ARM expects instruction to be 4-byte aligned and shifting it by a byte (the opcode) as it was done in the original attack is not possible here. However, while it is necessary to fetch and decode two-bytes aligned instructions, the mixing of 16- and 32-bits Thumb-2 instructions allows for the second halfword of a 32-bit Thumb-2 instruction to be interpreted as the first halfword of an (unintended) instruction. This way, all ***unintended instructions*** must be ***32-bit Thumb-2 instructions*** and the ***intended instructions encoding them*** as well. **The attack consists of a chain of intended 32-bits Thumb-2 instructions executed one halfword out of phase.** Inducing the JIT to compile correct second halfwords of intended instructions mean that they have to be a valid first word as well. Using a chain of Thumb-2 only instructions makes it impossible to generate a payload because the second halfwords cannot be used as first and vice-versa.

 However, using the switch between ARM and Thumb-2 can be exploited: the attacker needs to induce the JIT to produce Thumb-2 instructions whose bytes in instruction memory decode to a useful stream of ARM instructions and execute it in ARM mode via an inter-working branch instruction. The two ARM instruction fields that make it difficult to encode ARM instructions in a Thumb instruction stream are the ***condition code*** and ***ALU result destination register***. The condition code is expected before most ARM instructions and consists of a 4-bits flag that predicates the runtime execution of the instruction on the status of condition flags (e.g. ***negative, zero, carry, overflow, etc.***). The `1111` code is illegal as a condition but can be used by specific instructions (SIMD, hint or unconditional PC-relative branch with a forced instruction set change to Thumb) that are not useful to an attacker. However, with this technique it is still complex to generate and construct a Turing-complete ARM shellcode.

***Gadget chaining*** consists of using the already available sequences of instructions called ***gadgets*** to generate 

