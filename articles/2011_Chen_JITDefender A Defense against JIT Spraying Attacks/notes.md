<!-- Please prefix the notes with the date as in [22/12/2020] -->

[03/05/2021]

Code-reuse attacks can be used instead of injecting a malicious piece of code. The different techniques consist of **ROP** (*return-oriented programming*), **BCR** (*binary code extraction*) or **Inspector** (*automatic extraction of proprietary gadgets from malware binaries*). A new attack aimed at JIT-compiled code is called **JIT spraying** that reuses code on the Flash VM's heap to construct the attack. JIT spraying can prevent the usual counter-measures sucha s **data execution prevention (DEP)** or **address space layout randomization (ASLR)**. JIT spraying consists of coercing the JIT compiler to generate native code with the malicious code on the heap of the VM, then exploits bugs in the browser to execute it.

**Attack example:** By writing the objects using dynamic languages, the attacker coerces the JIT compiler to generate malicious code on the heap of the VM. It does so by writing several objects which contains many uniform statements with dedicated constructed integers. If the integer is correctly chosen, the native code may be transferred into the malicious code with one byte offset.

**JIT Compilation:** The dynamic translation of source code into native code on the heap needs to mark the page containing the JIT-code as executable and reuse the code repeatedly without recompiling or interpreting in order to boost the performance. The W+X protection is turned off.

**JIT Defender design:** When designing JITDefender, the two key points are the *cod compilation point* (native code generation) and the *code execution point* (native code execution by the VM). The idea is to mark the native code pages as non-executable at the first point, then executable right before the second point and finally non-executable again right after. Under this protection, if an attacker hijacks the control flow to the code snippet on the heap for JIT spraying attacks, the **access will be blocked because the pages are kept as non-executable**. **Different views of the compiled code are provided for the VM and attacker with the native code execution policy.**

**Flash engine:** The source code is actionscript language. It is translated into actionscript bytecode (ABC) or ShockWave File (SWF). This code can be JIT compiled or interpreted on the flash engine. JIT compiling is done through **Machine Code IR generation** the **Machine Code generation**. The native code is stored in the newly allocated heap memory. The JIT then provides a **Native Code Execution Controller** to control whether the compiled code is on the heap or not.

**Implementation in Flash engine:** The class `MethodInfo` holds the information needed of the functions that can be executed by the VM. The class `CodeMgr` is the one responsible to manage memory of compiled code. Adding a reference to this instance from the class `MethodInfo` allows to modify some attributes later on. The stored compiled function is defined as non-executable and before entering it through the function `coerceEnter` defined in the VM, it is set as executable then non-executable again when `endCoerce` is called.

**Implementation in Javascript engine:** In V8, Native code is stored as `SharedFunctionInfo`. At the end of `Compiler::Compile`, the page is set as non-executable. Before `Execution::call`, it is set as executable then non-executable again after the execution. In Safari's engine, the same idea is used: non-executable after `JIT::compile`, executable before `JITStubCall::call` then non-executable again.

 
##### tags: defense, jit, w xor x, 