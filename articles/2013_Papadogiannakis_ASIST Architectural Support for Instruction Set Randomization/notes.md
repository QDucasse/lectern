<!-- Please prefix the notes with the date as in [22/12/2020] -->

**Instruction Set Randomization (ISR)** has been proposed to defend against any type of code injection attack. It randomizes the instruction set of a processor so that an attacker is not able to inject meaningful code. ISR techniques encrypt the instructions of a possibly vulnerable program with a program-specific key. Instructions are decrypted at runtime. 

**ASIST** is a hardware/software scheme that supports ISR on top of an unmodified ISA. It uses distinct per-process keys and another system kernel's key. Two registers, `oskey` and `usrkey` are added to processor, which contains the kernel's key and the user-level key of the running process. These registers are only accessible by the operating system via privileged instructions.

The solution is built on top of a **SPARC** architecture. The decryption unit is added at the instruction fetch pipeline stage. It implements two (weak) encryption algorithms: XOR and transposition. The encryption comes with two different techniques: **statically** by adding a new section in the ELF that contains the key and encrypting code section using it and **dynamically** by generating a random key at load time and encrypting with this key.

##### tags: defense, isr, security