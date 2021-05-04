<!-- Please prefix the notes with the date as in [22/12/2020] -->

[04/05/2021]

Initially JIT compilers wrote all run-time generated code onto memory pages that were simultaneously writable and executable throughout the execution of the script. This led to **code-injection** attacks. Later JIT engines added support for **W+X policies** by doubly-mapping JIT pages instead. This meant that JIT code could no longer be found on memory pages that were simultaneously writable and executable. **JIT spraying** attacks still made their way through injecting instructions without writing directly to the pages. This led to the use of **constant blinding**, **constant elimination and code obfuscation**, **code randomization** or **control-flow integrity**. Successfully defending against **code-reuse** is more challenging since an attacker can traverse and disassemble ode pages to dynamically generate a **ROP chain** at run-time. **Randomization** and **execute-only memory** leverage this type of attacks. An attacker can still inject code with **data-only attacks**. Corrupting the intermediate representation without overwriting any code pointers can make the JIT generate malicious code. Defenses propose isolating the compilation from the execution of JIT code through **separate processes** or **hardware-based trusted execution environments**.

**Threat model:** Assume that the system has ***code-injection defense*** (W+X) set, ***code-reuse defense*** (ASLR, CFI) set, ***hardware-based memory protection features*** (Intel MPK) in place and a ***memory-corruption vulnerability*** (ability to arbitrarily corrupt any part of the program's address space).

**SpiderMonkey Implementation:** *Speculative optimization* makes the hypothesis of some type for example and checks that it holds at runtime otherwise it goes back to the standard path through the interpreter. *Native functions* are C++ functions that are registered as `JSNative` functions and are often not inlined and the control is transferred to an internal calling convention. Several regions play a crucial role in ensuring the correct and secure operation of the script engine: (1) bytecode region, (2) the JIT code cache (3) the JIT compiler data, (4) the JavaScript data objects and (5) the object tables.

**Interpreter Attack:** First, the attacker **locates** the **JavaScript context object** and the **JavaScript function objects** of a victim function (i.e. any function we can call from JavaScript). Once the two objects are located, the attacker **overwrites** the f**unction address** contained in the function object with the **address of a target function**. Finally, the attacker **invokes the victim function**. 

**NoJITsu:** A novel defense that provides fine-grained memory protection to lock down real-world scripting engines. As switching between interpreted and JIT'ed code happens frequently (on a per-function basis), an efficient implementation is key. The interpreter *cannot* be moved out-of-process as proposed for the JIT compiler. Automated dynamic and static analysis are used to restrict memory-access permissions within the scripting engine to the bare minimum. 

Current JIT engines do not distinguish between different kinds of data sections and have little to no security policies. Bytecodes, Objects table, Objects, JIT IR are usually stored in writable memory even though they are rarely overwritten. **This space can be used to manipulate the data structures.** JIT'ed code is usually protected as R/X memory only putting them to R/W when recompiling code. **A code-reuse attack is possible on this region.**

These threats can be countered by deploying **fine-grained security policies** to lock down access permissions for each of the main data regions we identified based on their lifetime and usage within the JIT engine. The data structures mentioned earlier are placed in different memory domains, enabling *write* when, where and as long it is needed before revoking it. Each new type of data is given a specific key. The different regions are:

**JIT Code:** The main goal of the approach is to implement ***execute-only support for JIT code***. The JIT code has to remain ***non-writable*** to prevent attackers to have direct access to the CPU, however this has to be leveraged when emitting a new compiled version of the code. It also needs to be ***non-readable*** to avoid JIT-ROP attacks that need to discover code-reuse gadgets at runtime. However, it needs to be readable because of constant values or target addresses in jump tables. The readable data needs to be separated into a dedicated read-only region.

**Static Code:** The static code regions include the code sections of the JavaScript engine itself and the dynamic libraries loaded into memory. Unlike the JIT code region, it cannot be subject to malicious code injection but can be used as a large code base for code-reuse gadgets. It has to be set to execute-only so the attacker cannot disclose executable memory regions to chain gadgets. **XOM-Switch** is used to enforce execute-only permissions.

**JIT IR:** The IR can be corrupted from another thread and the thread compiling the IR into machine code is the ***only one with write permission***.

**Bytecodes and Object Tables:**

**JavaScript Objects:**

