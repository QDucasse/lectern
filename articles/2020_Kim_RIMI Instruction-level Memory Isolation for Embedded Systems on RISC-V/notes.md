<!-- Please prefix the notes with the date as in [22/12/2020] -->

[23/08/2021]

**Previous techniques:** Usual isolation techniques such as *hardware virtualization extension*, *enclaves* and *tagged memory architectures* are not suitable for low-end embedded systems due to hardware costs or power consumption. Memory isolation ensures data can only be accessed by authorized code. Two types of isolation coexist, software- and hardware-based solutions. The first ones instrument program code by inserting instruction sequences to assign different memory permissions or sensitive data to legitimate code. These solutions often come with a significant overhead and scalability issues. Hardware-based solutions enable legitimate code to have another memory view from other code without the need for code instrumentation. These solutions are not scalable due to the limited number of memory regions that can be defined.

**RISC-V native options:** RISC-V defines three privilege modes from least to most privileged: user (U), supervisor (S) and machine (M). The supervisor mode is the one the operating system runs on. Each of these mode use *control and status registers* to configure the system operation and status. RISC-V also provides *physical memory protection (PMP)* that divides memory space into up to 16 regions and assigns specific memory permissions to each region. Two CSRs `pmpcfg` (permissions) and `pmpaddr` (regions) configure the PMP.

**Threat model:** Memory vulnerabilities exist in the software of the embedded system. The goal of the attacker would be to modify or leak sensitive data in the embedded system. A trusted privileged software is present in the system as *trusted computing base (TCB)*. This component guarantees the integrity of critical resources such as W+X policy on PMP regions.

**RIMI: ** RIMI is a technique for instruction-level memory isolation. It introduces two domains, `domain0` and `domain1`. Each domain consists of PMP regions and dedicated instructions to access its PMP regions. The access permission is bound to the dedicated instructions for each domain and the domain switch is only allowed by the dedicated control transfer instructions. To decide which PMP regions are included in each domain, a special CSR is added.

All existing instructions for memory access and control transfer are duplicated and the PMP is adjusted to check the permission according to the instructions. The control signal for added instructions is processed at the same time as the original instructions after the decoding stage. It does not affect the internal states of the core and the method can be applied to various RISC-V cores at a very small cost.

For *memory instructions*, RIMI uses replicated instructions for `domain1` and existing memory instructions for `domain0`. To distinguish which domains those instructions belong to, a small logic is added at the decode stage of the processor. The signal is then passed to PMP to check memory access. For *control transfer instructions*, RIMI defines the existing `branch`, `jal` and `jalr` instructions as the ones allowed to branch to the same domain and `jalx` and `jalrx` the ones to switch domains. Control transfer instructions do not access memory directly but access in the fetch state of the pipeline. The memory access is verified in the next pipeline state and information on the executed instruction is kept until the next fetch cycle.

**Domain Memory Protection (DMP):** DMP adjusts the memory permission so that only dedicated instructions can access isolated memory. It is implemented by bit-masking the PMP permission for the memory region and errors in the PMP always take precedence on the DMP ones. DMP defines an additional control status register `dmpcfg` to state from which domain the memory is accessible. 

**Evaluation:** Bristol/Embescom Embedded Benchmark Suite (BEEBS) shows that RIMI presents a 0.88% overhead against the 7.74% reached by other software solutions.

