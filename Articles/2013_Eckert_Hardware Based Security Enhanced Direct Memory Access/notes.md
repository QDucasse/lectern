<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[15/12/2020]*

Prevention against **Direct Memory Access (DMA)** attacks adding a **watchdog mechanism** that scans the data passing by and interrupts the processor after the detection of a malicious data or instruction sequence.

*REFERENCES TO OTHER ARTICLES IN THE FIELD OF PROCESSOR SECURITY*

[1] Chhabra et al., *An analysis of secure processor architectures*

[2] Wang et al., *Computer Architecture and Security: Fundamentals of Designing Secure Computer Systems*



DMA is a well-known technique to release processors from time consuming workload caused by simple data transfers. **Those transfers are performed without supervision**. Data and instruction are communicated between the memory as sink and source or between the memory and mass storage or interfaces. They reach their destination block-wise without completely before being checked by anti-malware agents. To complete the success of a DMA attack, **the attack pattern needs to launch the code before it has been checked** by the anti-malware agent. Another opportunity is to infect the **anti-malware** software directly.

The introduction of a **DMA-watchdog** can solve the issue. The watchdog resides between the *DMA-Controller* and the *Memory Controller*. It supervises the data part of the memory-bus with a number of sensors that provide a pattern matching functionality to identify malware. If one of the sensors is matching, it signals the watchdog that will, in turn, block the current DMA-transfer. The pattern matching is performed in parallel.

*PRHS (Partially Reconfigurable Heterogeneous System)* framework used to deploy the project on FPGA. 

*DESCRIPTION AND FIGURE*

**Proof-of-concept**: A DMA Simulator is added to the secondary data bus of the system and to the RAM via an SD-Arbiter. Its task is to *copy the content of internal Block-RAM (8KiB) to a given RAM address*. It does not take additional CPU time as it is completely independent.

