### Attack Summary

***JIT-ROP*** is a code-reuse attack that abuses a memory disclosure to ***map an application's memory layout*** on the fly, dynamically discovering functions and gadgets and JIT-compiling a target program using those gadgets.

### Attacker Threat Model

The stack and heap are ***NX (or DEP)***. JIT-spraying mitigations are in place: ***W+X, constant elimination, random nop insertions***. ***ASLR*** and ***fine-grained  ASLR*** are in place which deploys base address randomization, all useful, predictable mappings have been eliminated, order of functions and basic blocks is permuted, registers are swapped and instructions replaced, the location of each instruction is randomized and a randomization is performed upon each run of an application.

### Recipe

The first step of the attack is to map the code page memory. The attacker needs to find a ***memory disclosure*** then 

