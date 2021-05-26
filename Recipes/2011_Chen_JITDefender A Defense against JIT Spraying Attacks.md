### Defense Summary

JITDefender re-enforces ***W+X*** policies by marking the native code pages as ***non-executable*** on generation, then ***executable*** before execution then ***non-executable*** again right after the execution.

### Attacker Threat Model

The attacker has access to the VM of a dynamically typed language ((ECMA|Java|Action)Script, Java, Python, etc.) can write a script and execute it. DEP and ASLR memory protection are in action. The return address from a vulnerable function can be changed to give control to code in the JITed pages. 

### Recipe

JITDefender modifies the ***Native Code Execution Controller*** that sits in-between the ***Machine Code Generator*** and the ***Runtime System***. In Tamarin (Flash VM), when an ABC or SWF file is loaded, the JIT compiler will translate the source code into native code at the ***unit of a function***. Tamarin uses the class `MethodInfo` to store information on the functions that can be executed by the VM (native, user-defined, etc.). **First**, related information at the **code compilation point** when native code has been generated is needed. It is stored in the class `PoolObject` through the `codeMgr` variable. The start and end address of the compiled code memory are extracted and `VMPI_setPageProtection` is used to set the code page as ***non-executable***. **Second**, the **code execution point** begins by calling `coerceEnter` to execute the compiled code, and at the end of this function, a handler is invoked by `endCoerce()`. `VMPI_setPageProtection` can be used to set the related pages as ***executable*** and, after executing the function, the same to set the pages as ***non-executable***.



