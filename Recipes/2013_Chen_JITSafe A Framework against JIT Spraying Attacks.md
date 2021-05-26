### Attack Summary

JITSafe is a framework that re-enforces ***W+X*** policies by marking the native code pages as ***non-executable*** on generation, then ***executable*** before execution then ***non-executable*** again right after the execution. It also defines ***Immediate Value Elimination*** and ***Code Obfuscation*** to counter advanced code-reuse attacks.

### Attacker Threat Model

The attacker has access to the VM of a dynamically typed language ((ECMA|Java|Action)Script, Java, Python, etc.) can write a script and execute it. DEP and ASLR memory protection are in action. The return address from a vulnerable function can be changed to give control to code in the JITed pages. 

### Recipe

(1) ***Immediate Value Elimination:*** When the ***Machine Code Generator*** comes across a XOR instruction, it first allocates the memory on the heap to pre-store the immediate value, then it inserts the instruction that obtains the value from the memory to one register, and replaces the original instruction with the new one that uses the register instead of the immediate value.

(2) ***Code Obfuscation:*** Random selection of the register that holds the immediate value and inserts the padding between the instructions (`NOP` instructions).

(3) ***W+X:*** The ***code compilation point*** creates the JITed code page and sets it as **non-executable** and the ***code execution point*** sets it as **executable** before running then **non-executable** right after.

