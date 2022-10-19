<!-- Please prefix the notes with the date as in [22/12/2020] -->

**Flow Integrity eXtension for Embedded RISC-V (FIXER)**  is a low energy, low overhead solution that ensures integrity of backward and forward edge control flow of programs running on a RISC-V core. The unmodified RISC-V core is a hard IP, while the dynamically reconfigurable FIXER coprocessor is implemented on an on-chip FPGA.

**RoCC:**  The architecture is based on the Rocket chip using the RocketChip generator to generate a Rocket Tile (scalar 64-bit RISC-V core, L1 instruction and data caches and the Rocket Custom Coprocessor **RoCC**). The communication between the core and RoCC goes through the **RoCCIO** interface. RoCC instructions extend the RISC-V ISA with 4 custom instructions. These instructions take the usual register/register fields:`opcode`, `rd`, `rs1`, `rs2` and `funct7`. The `funct3` is used by the RoCC interface and split in `xs1`, `xs2` and `xd` controlling the read and write of the core registers by the RoCC instruction. If `xs1` is 1, then the 64-bit value in the integer register specified by `rs1` is passed to the RoCC (and it is not if `xs1` is clear). The same idea applies to `xs2`, controlling the read of register specified by `rs2`. If the `xd` bit is 1 and `rd` is not 0, the core will wait for a value returned by the co-processor over RoCCIO after issuing the instruction to it. While the `funct7` field can be used to select user-defined functions on top of the already present 4 custom instructions, RoCC already defines 4 opcodes:

| RoCC Instruction | Opcode  |
| ---------------- | ------- |
| custom0          | 0001011 |
| custom1          | 0101011 |
| custom2          | 1011011 |
| custom3          | 1111011 |

**CFI:** For backward-edge CFI, FIXER implements a **shadow stack** in a hardware memory on the RoCC. When a function call occurs, the return address is both set on the stack and simultaneously passed to the RoCC. When returning it retrieves the return address from the RoCC and compares it to the actual one, raising a CFI error in the case of a mismatch. The forward-edge protection uses a **control-flow graph (CFG)** represented as a **policy matrix** that indicates the valid call targets for each function call. The policy matrix is loaded in memory at runtimeand is queried to validate the call target for every indirect function call.

**Software design:** Any program that wants to be backward-edge protected needs to go through three steps: (1) **source code annotation** to add `CFI_CALL` tags before function calls and a corresponding `CFI_RET` before a return from the called function (presented in the code snippet) (2) **tag expansion** to translate the tags to actual RISC-V assembly instructions (expansion presented in the code snippet below), and (3) **compilation** to assemble, link and generate the final executable (**no change to the compiler since it is passed as a word!**). For forward-edge integrity, a matrix is derived from a CFG. A RoCC instruction `cfi_matld` is used to load the policy from the policy matrix (64x64 - callee/caller addresses -, where a set/unset bit indicates a valid/invalid call). Another RoCC instruction `cfi_fwd` is inserted before every indirect function call in the source code. 

```
void main() {                   void myFunc()) {
	...                             ...
	CFI_CALL                        CFI_RET
	myFunc();                       return;
}

# CFI_CALL                      # CFI_RET
auipc  t0,0                     .word   0x0200428b
add    t0,0,14                  bne     t0,ra,_cfi_error  
.word  0x0002a00b               jr      ra
call   myFunc
```

> `CFI_CALL` extends to: retrieve the current value of the pc, add 14 bytes of offset to calculate the return address, then a custom instruction is used - custom0 is used, `funct7` is set to `0000000` for `CFI_CALL` , `rs1` is set to use `t0` (X5 or `00101`) and `xs1` is set to 1 to transfer the computed value to the RoCC. The resulting instruction is `0x0002a00b`!
>
> `CFI_RET` extends to: compare the actual return value to the stored one where `funct7` is set to `0000001` for `CFI_RET` , `rd` is set to use `t0` (X5 or `00101`) and `xd` is set to 1 to transfer the computed value back to the core. The resulting instruction is `0x0200428b`! It should then be coupled with a `bne` to check equality between the actual `ra` and the one retrieved from the shadow stack.

**Hardware design:** The program binary runs on the Rocket Core and sends RoCC instruction over the RoCCIO whenever a security validation is required. The RoCC instruction is passed to through the command decoder which extracts the individual fields of the RoCC instruction. The `funct7` decodes a `cfi_call` or `cfi_ret`. for a `cfi_call`, the contents of `t0` is sent through and stored in the shadow stack memory (in SRAM, that can store up to 1000 addresses but is parameterizable). It is accessed through a top-of-stack register. For a `cfi_ret`, the address pointed by the top-of-stack register is returned to the core. No presentation of the forward-edge implementation...

##### tags: cfi, fpga, hardware, riscv, security