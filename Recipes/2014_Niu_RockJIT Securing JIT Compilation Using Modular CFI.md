### Defense Summary

***RockJIT*** builds a fine-grained control-flow graph from the C++ source code of the JIT compiler and dynamically updates the control-flow policy when new code is generated on the fly.

### Attacker Threat Model

An attacker is modeled as a concurrent user-level thread, running in parallel with other threads in the JIT compiler. The attacker thread an read and write any memory, subject to memory page protection. It is assumed the context switches between the JIT compiler and JITed code are conducted through a set of interfaces. The JITed code is assumed to not contain direct system call invocations and privileged instructions (it is however possible for the JITed call to request OS system calls from the JIT compiler itself).

### Background

***Modular Control-Flow Integrity***, a program is divided in modules and each module contains not only code and data but also auxiliary information used to generate a new CFG when linking with other modules. MCFI represents the CFG in tables during runtime. Thread-safe table transactions are used to access and update the tables.

### Recipe

![](../Articles/2014_Niu_RockJIT Securing Just-In-Time Compilation Using Modular Control-Flow Integrity/RockJIT.png)

**Verification:** The verifier maintains three sets of addresses that are code addresses in the code heap. **(1)** ***Pseudo-instruction start addresses (PSA)***, this set remembers the start addresses of all pseudo instructions (defined either as a checked indirect branch, a masked memory write or an instruction that is neither an indirect branch nor an indirect memory write). **(2)** ***Indirect branch targets (IBT)***  and **(3)** ***Direct branch targets***. It verifies several conditions on those sets. Those verifications are performed on native code emission, deletion or modification.
