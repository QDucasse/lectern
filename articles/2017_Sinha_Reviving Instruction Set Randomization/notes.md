<!-- Please prefix the notes with the date as in [22/12/2020] -->

**Instruction Set Randomization (ISR)** is ineffective against code-reuse attacks which are the cornerstone of modern attacks. Previous solutions propose **(1)** unfavorable performance-security trade-offs, **(2)** no self-protection, **(3)** no support for shared libraries and page sharing, and **(4)** archaic threat models.

**Polyglot** is a hardware-based ISR schemes that uses strong encryption (AES and ECC). It removes decryption from the critical path in the processor to improve performance. The encryption is performed at the page granularity and enables page sharing between applications. It comes with strong encryption and a low overhead. Instructions are encrypted right from system boot.

##### tags: defense, isr, security