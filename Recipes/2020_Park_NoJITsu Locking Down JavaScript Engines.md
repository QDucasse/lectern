### Attack Summary

***Interpreter data-only attack*** in which the attacker only corrupts heap objects to successfully issue a system call from within byte code execution at run time.

### Attacker Threat Model

The attacker knows a memory-corruption bug in some part of the scripting engine that enables him to corrupt any part of the program's address space. The scripting engine enforces W+X by offloading the JIT compilation to an external process or trusted execution environment or simply toggle the writable and executable permissions on JIT pages at run time. Code reuse defenses are in place ***(ASLR, CFI)***. Hardware-based memory protection features are available.

### Recipe

<img src="../Articles/2020_Taemin_NoJITsu Locking Down Javascript/DOAttack.png" style="zoom:80%;" />

---

### Defense Summary

The objective of ***NoJITsu*** is to deploy fine-grained security policies to lock down access permissions for each of the main data regions identified based on their lifetime and usage within the JIT engine. The data structures are placed in different memory domains, enabling *write* when, where and as long as it is needed before revoking it.

<img src="../Articles/2020_Taemin_NoJITsu Locking Down Javascript/NOJITsu.png" style="zoom:80%;" />

The implementation combines ***automated analysis***, the signal handler is used to trigger a segfault in case of a write access to objects, if the access was justified the `PKRU` value is modified ; ***compartmentalization***, jump table is split, JS objects are protected with strict isolation enforced by the GC. ***Intel's Memory Protection Keys (MPK)*** enforce the different policies.
