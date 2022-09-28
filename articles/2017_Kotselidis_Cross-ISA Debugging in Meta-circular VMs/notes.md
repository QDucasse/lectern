<!-- Please prefix the notes with the date as in [22/12/2020] -->

[30/04/2021]

Maxine VM is a meta-circular VM for Java written in Java. It adopts a modular approach in *schemes* that comprises the VM. The transition to a new ISA (x86_64 to ARMv7 32) brought several challenges.

Maxine VM offers three compilers: **T1X** (fast template compiler similar to an interpreter), **C1X** (JIT optimizing compiler based on statistics gathered by T1X) and **Graal** (aggressive JIT optimizing compiler). The fact that it is meta-circular makes the port to a new ISA complicated. The VM's bootimage is ahead-of-time compiled by one of its runtime compiler.  The 64 to 32-bits transition brings issues to the **object identification** (hashcode is 32-bits long and leaves no place for metadata) and **register allocation** (need for efficient 32 bits register allocations).

A **QEMU-based toolchain** is developed to be able to debug the whole flow of the Maxine VM port:

1. **`MaxineTester` Initialization:** Every unit test invokes the `MaxineTester` which resets all internal states and QEMU output files. Once the initialization is complete, a code buffer is returned to the unit tests which serves as placeholder for the generated assembly code.
2. **Unit Test Generation:** Depending on the nature of the unit test (assmbly instruction, T1X, C1X, ...) the code buffer is filled differently. When filled, it is passed to the `MaxineTester` for emulation.
3. **QEMU Binary Composition:** The `MaxineTester` assembles the binary that will be passed to QEMU for emulation. First, the assembly code of two helpers (`asm_startup.s` and `entry.s`) are linked together with the binary code of the unit test. The code buffer is inlined to a C file and a function pointer to its first entry is installed. Finally, the actual test that links the code buffer and the two assembly files is compiled and the binary is generated.
4. **QEMU Emulation:** The corresponding processor is simulated and the binary generated before is emulated. Upon completion, the register file is dumped to an output file defined in the `MaxineTester` class.
5. **Output Validation:** The dump file is validated against the expected values as set in the unit test definition.

Three kinds of unit tests can be ran into the toolchain: individual assembly instructions, T1X compiled methods and C1X compiled methods.

Then, tracking faulty methods at runtime is comple as bootstraping a meta-circular VM in a new ISA holds many parts that are untested. A unique identifier called `MethodID` was injected during compilation to keep track execution. Another approach would be to check the address of the faulty instructions through the PC, against the code cache to find the boundaries of the faulty method. Inlined methods would not be taken in consideration so a dedicated `MethodIDNode` is attached to the IR graph before the inlined code to overcome this issue.