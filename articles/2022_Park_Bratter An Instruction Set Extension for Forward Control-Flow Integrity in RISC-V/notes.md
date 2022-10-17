<!-- Please prefix the notes with the date as in [22/12/2020] -->

[28/09/2022]

**Introduction to CFI:**

**Control-flow Integrity (CFI)** is considered as an effective way to prevent a number of control hijacking attacks such as **return-oriented programming (ROP)**.

CFI checks if the **control transfer instruction** (CTI) is legitimate before executing the instruction. The solutions can be categorized in **forward CFI** for **indirect call/jump** and **backward CFI** for **return addresses**. Backward CFI is usually performed using a **shadow stack** but various methods are available for forward CFI: using a **control flow graph (CFG)** or making use of the **function type**.

**Background:**

There are two types of CTIs: **direct** and **indirect**. In RISC-V `beq`, `blt`, `j` and `jal` correspond to direct CTIs whereas `jalr` and `jr` are indirect. In direct CTIs, the target address is **obtained from the offset** (12 bits sign-extended for branches and 22 bits sign-extended for jumps). In indirect CTIs, it is **processed by adding a 12-bits sign-extended offset to an address in a general purpose register**. This register is a target of choice for attackers! Indirect CTIs are categorized according to their expression in the CFG: indirect branches and indirect calls are called **forward-edges** while return instructions are called **backward-edges**.

The RISC-V ISA provides **hint instructions**, instructions that do not require processing under particular circumstances. They are treated as `nop` instructions when the behavior is not implemented. The *constraints* are the conditions for the instruction to be detected as a hint.

| Instructions | Constraints | Code Points | Purpose             |
| ------------ | ----------- | ----------- | ------------------- |
| LUI          | rd = x0     | 2^20        | Future standard use |
| AND          | rd = x0     | 2^10        | -                   |
| SLLI         | rd = x0     | 2^10        | Custom use          |
| SRLI         | rd = x0     | 2^10        | -                   |

**Issues with existing solutions:**

Software-based techniques insert additional instructions to every CTI. They consist of a couple of arithmetic/logic instructions and are applicable to any processor/software but add considerable performance overhead. Manufacturers added dedicated instruction extensions (ARM BTI and Intel CETS). While these provide a good basis, they cannot be used to implement finer-grain CFI solutions that enforce different rules for every indirect CTI.

For example, ARM BTI and Intel CETS expects every indirect branch to land on a specific **landing pad instruction (`bti` for ARM, `endbranch`)** with the corresponding operand (`c` for a call, `j` for a jump). While this prevent jumping to attacker controlled data, function reuse attack are still possible by jumping to an attacker-controlled function with the correct operand. 

An extension of it provides a value for each function and stores it in a dedicated register and the entry point of a function is compared against this register. This approach needs to duplicate most of the functions to have different signatures and be sure that the access to one function is restricted to another given one.

**Bratter:**

The authors present **Bratter, an instruction set extension for forward CFI on RISC-V**. Bratter introduces a **branch tag register** and **special instructions** to allow developers to set and verify the value of the register. This register supports **multiple 8-bit long branch tags** and can effectively support various CFI policies.

Bratter is composed of the following:

1. **Branch tag register (BTR)**, a control status register (CSR) that holds branch tag values.

2. **Dedicated instructions**, `sbtag` (set branch tag register to BTR) and `cbtag` (check branch tag register in BTR is legitimate)

3. **Dedicated exception**, that triggers when a check of branch tag fails.

(1) The branch tag register has four fields to hold up to four 8-bits tag values. It is a CSR that can only be accessed through dedicated instructions. The solution can be extended to have multiple BTR.

(2) Setting and checking branch tags is performed through `sbtag` and `cbtag`. They both take two operands, a 2-bit `id` and an 8-bit `value`. `sbtag` assigns a value to the `id`-th branch tag and `cbtag` checks whether the assigned value is the same. The instructions are implemented by extending `slli` and `srli` hint instructions, and therefore provides backwards compatibility with systems that do not use Bratter.

(3) To ensure CFI, the processor needs to guarantee `cbtag` instruction after the control transfer. This means that after the control transfer, when the next instruction is not `cbtag`, the processor should halt the process and an exception occurs. The exception raised is for now an *illegal instruction*.

The two CFI solutions presented are **function signature check**, check at the granularity of a function and **branch regulation**, check at the granularity of a basic block. 

**Evaluation:**

The solution is presented on top of the Spike RISC-V simulator ans as an LLVM pass. The code size overhead usually is lower than 1% for the function signature solution and around 2% for the other (up to 11% in worst-case scenario!). Execution time overhead is less than 6%!

 ##### tags: cfi, hardware, risc-v, security