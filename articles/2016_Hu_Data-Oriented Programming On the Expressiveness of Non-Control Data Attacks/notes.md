<!-- Please prefix the notes with the date as in [22/12/2020] -->

[12/10/2022]

Authors present and qualify **non-control data attacks** that tamper with or leak security-sensitive memory that is not directly used in control transfer instructions. Data-oriented programming can offer rich exploits from common vulnerabilities. Corrupting simple local variables (through a buffer overflow for example) can allow an attacker to take control of simple operations (condition, dereference, assignment, addition, etc.) and extract these micro-operations as **data-oriented gadgets**. Executing them on attacker-controlled inputs chained in a sequence makes it possible to perform an expressive computation. A loop that allows to chain gadgets in an infinite sequence (*e.g.:* `while` on a local variable) are called **gadget dispatchers** and help attackers chaining the gadgets.

| **Semantics**      | Instructions in C | Data-Oriented gadgets in DOP |
| ------------------ | ----------------- | ---------------------------- |
| arithmetic/logical | `a op b`          | `*p op *q`                   |
| assignment         | `a = b`           | `*p = *q`                    |
| load               | `a = *b`          | `*p = **q`                   |
| store              | `*a = b`          | `**p = *q`                   |
| jump               | `goto L`          | `vpc = &input`               |
| conditional jump   | `if a goto L`     | `vpc = &input if *p`         |

The authors define **MinDOP**, a small language that uses a virtual instruction set and virtual register operands in which the attacker's payload can be specified. The 6 kind of virtual instructions are presented in the above table and allow to perform arithmetic/logical calculations, load and stores as well as conditional and unconditional jumps . Note that `vpc` is the virtual input pointer that is modified to simulate jumps. Each virtual operation is simulated by real x86 instruction sequences available in the vulnerable program. **None of the gadgets or dispatchers modify any code-pointers or violate CFI in the real-program execution**. To avoid tampering with the CFG, virtual registers are implemented with carefully-chosen memory locations (**not** hardware registers) used only through gadget operations.

A **data-oriented gadget** simulates three logical micro-operations: (**1**) loading the micro-operation, (**2**) the intended virtual operation's semantics (**3**) final store micro-operation. (1) simulates the read of the virtual register operand(s) from memory and (3) writes the result back to memory. The main differences with ROP/JOP gadgets is that: data-oriented gadgets require to write the operation result back in memory and they must execute in at least one legitimate control flow without the requirement of executing immediately one after the other. The **gadget dispatcher** is simulated by a loop which iterates over computation that simulates gadgets and has a selector in it. Each iteration executes a subset of gadgets using outputs from gadgets in the previous iteration. 

An **interactive attack** rewrites local variables at each iteration so that the desired gadget works as required. Given *Mj* the memory state for executing gadget *j*, the attacker can corrupt local variables to configure *Mj* to execute a *j* in a round, provide multiple rounds of malicious inputs to perform an expressive computation the corrupt the loop condition variable to stop. A **non-interactive attack** consists of the attacker providing the entire malicious input as a single data transmission, *i.e.* all the memory setup and conditions for deciding loop termination and selective gadget activation. MinDOP adds two virtual operations that enable conditional chaining of operations, or virtual jumps. It keeps a pointer called **virtual PC** that points to the desired configuration *Mj*. 

##### tags: attack, cfi, non-control data attack, security