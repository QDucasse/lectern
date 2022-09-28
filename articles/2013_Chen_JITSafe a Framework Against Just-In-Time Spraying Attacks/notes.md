<!-- Please prefix the notes with the date as in [22/12/2020] -->

[19/05/2021]

Modern OS adopted ***data execution prevention (DEP)*** or ***writable XOR executable (W+X)*** policies to overcome code-injection attacks. Along with code-injection attacks, code-reuse techniques such as `return-to-libc` or ***return-oriented programming (ROP)*** have been proposed to overcome DEP or W+X. ***Address Space Layout Randomization*** was proposed to mitigate this type of attacks. However, JIT spraying attacks demonstrate that it is possible to overcome the defense mechanisms. 

**JITSafe presentation:** JIT compilation needs to store the JITed code as writable *and* executable, breaking the W+X policy and opening the door to JIT spraying attacks. The objective of JITSafe is to ***enforce the W+X protection within the VM***, ***eliminate the immediate values*** and ***obfuscate the JITed code***. 

**Immediate value  elimination:** To eliminate immediate values, when the machine code generator comes across a XOR instruction, it first allocates the memory on the heap to pre-store the immediate value. Then it inserts the instruction that obtains the value from the memory to one register and replaces the original instruction with the new one that uses the register instead of the immediate value.

**Code Obfuscation:** To add more complexity, code obfuscation randomly selects the register that obtains the immediate value and inserts the padding between the instructions. The new XOR operation will use the randomly chosen register as an operand. Moreover, NOP instructions are added in between compiled instructions. 

**W+X:** Two important points during the execution of JIT compiled code  have to be noted: (1) the code compilation point where the JIT compiler generates the native code and (2) the code execution point when the VM executes the native code. When entering (1), the memory pages are marked as writable and non-executable. Shortly before (2), memory pages are marked as executable, and afterwards, non-executable again.

