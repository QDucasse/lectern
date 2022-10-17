<!-- Please prefix the notes with the date as in [22/12/2020] -->

[04/05/2021]

Initially JIT compilers wrote all run-time generated code onto memory pages that were simultaneously writable and executable throughout the execution of the script. This led to **code-injection** attacks. Later JIT engines added support for **W+X policies** by doubly-mapping JIT pages instead. This meant that JIT code could no longer be found on memory pages that were simultaneously writable and executable. **JIT spraying** attacks still made their way through injecting instructions without writing directly to the pages. This led to the use of **constant blinding**, **constant elimination and code obfuscation**, **code randomization** or **control-flow integrity**. Successfully defending against **code-reuse** is more challenging since an attacker can traverse and disassemble ode pages to dynamically generate a **ROP chain** at run-time. **Randomization** and **execute-only memory** leverage this type of attacks. An attacker can still inject code with **data-only attacks**. Corrupting the intermediate representation without overwriting any code pointers can make the JIT generate malicious code. Defenses propose isolating the compilation from the execution of JIT code through **separate processes** or **hardware-based trusted execution environments**.

**Threat model:** Assume that the system has ***code-injection defense*** (W+X) set, ***code-reuse defense*** (ASLR, CFI) set, ***hardware-based memory protection features*** (Intel MPK) in place and a ***memory-corruption vulnerability*** (ability to arbitrarily corrupt any part of the program's address space).

**SpiderMonkey Implementation:** *Speculative optimization* makes the hypothesis of some type for example and checks that it holds at runtime otherwise it goes back to the standard path through the interpreter. *Native functions* are C++ functions that are registered as `JSNative` functions and are often not inlined and the control is transferred to an internal calling convention. Several regions play a crucial role in ensuring the correct and secure operation of the script engine: (1) bytecode region, (2) the JIT code cache (3) the JIT compiler data, (4) the JavaScript data objects and (5) the object tables.

**Interpreter Attack:** First, the attacker **locates** the **JavaScript context object** and the **JavaScript function objects** of a victim function (i.e. any function we can call from JavaScript). Once the two objects are located, the attacker **overwrites** the f**unction address** contained in the function object with the **address of a target function**. Finally, the attacker **invokes the victim function**. 

---

**NoJITsu design**

 A novel defense that provides fine-grained memory protection to lock down real-world scripting engines. As switching between interpreted and JIT'ed code happens frequently (on a per-function basis), an efficient implementation is key. The interpreter *cannot* be moved out-of-process as proposed for the JIT compiler. Automated dynamic and static analysis are used to restrict memory-access permissions within the scripting engine to the bare minimum. 

Current JIT engines do not distinguish between different kinds of data sections and have little to no security policies. Bytecodes, Objects table, Objects, JIT IR are usually stored in writable memory even though they are rarely overwritten. **This space can be used to manipulate the data structures.** JIT'ed code is usually protected as R/X memory only putting them to R/W when recompiling code. **A code-reuse attack is possible on this region.**

These threats can be countered by deploying **fine-grained security policies** to lock down access permissions for each of the main data regions we identified based on their lifetime and usage within the JIT engine. The data structures mentioned earlier are placed in different memory domains, enabling *write* when, where and as long it is needed before revoking it. Each new type of data is given a specific key. The different regions are:

**JIT Code:** The main goal of the approach is to implement ***execute-only support for JIT code***. The JIT code has to remain ***non-writable*** to prevent attackers to have direct access to the CPU, however this has to be leveraged when emitting a new compiled version of the code. It also needs to be ***non-readable*** to avoid JIT-ROP attacks that need to discover code-reuse gadgets at runtime. However, it needs to be readable because of constant values or target addresses in jump tables. The readable data needs to be separated into a dedicated read-only region.

**Static Code:** The static code regions include the code sections of the JavaScript engine itself and the dynamic libraries loaded into memory. Unlike the JIT code region, it cannot be subject to malicious code injection but can be used as a large code base for code-reuse gadgets. It has to be set to execute-only so the attacker cannot disclose executable memory regions to chain gadgets. **XOM-Switch** is used to enforce execute-only permissions.

**JIT IR:** The IR can be corrupted from another thread and the thread compiling the IR into machine code is the ***only one with write permission***.

**Bytecodes and Object Tables:** Similar to the JIT code, they should be writable only when they are generated during compilation. They then remain read-only throughout the execution. Write access is allowed only when the script parser generates them and immediately made non-writable afterwards.

**JavaScript Objects:** The JS objects can be written to frequently at any point of the program execution and several flags must be updated at run time (reference counter, GC flag). They are separated into two protection domains depending on the types they encapsulate: one for s**ensitive data objects** and the other for **primitive data objects**. An object is *sensitive* if it contains sensitive information such as *function pointers,* *object shape metadata*, *scope metadata* or *JIT code*. By separating the two types, those object classes are not writable at the same time, this way an attacker cannot setup an object type confusion to corrupt sensitive objects using primitive data types. Changing object permissions while the JIT code executes is too costly in terms of overhead so *all access restrictions to primitive data* are lifted during JIT code execution and set back again when the control is transferred back to the JS engine itself. Protections for *sensitive* objects are still enforced to prevent the attacker to manipulate frequently exploited objects (Shapes, Cells, Functions, etc.).

---

**Implementation**

**Intel's MPK (Memory Protection Key):** Allow user-space programs to manage access permissions for up to 16 memory domains. To change the access permissions for a domain, the program uses an unprivileged instruction to write to the thread-local PKRU register. While PKRU write is unprivileged, an attacker has to acquire arbitrary code execution to set its value.

**Compartmentalization:** 

- (1) *Jump table separation* to split jump target addresses from the rest of the jump table. This allows the jump addresses to be read-only and not executable.
- (2) *Permission change routine*: before writing to a protected region, we insert a call to `set_pkru` to change the value of the `PKRU` register to enable write access. The function first checks if the current `PKRU` value is already correct to avoid losing cycles by flushing the CPU pipeline.
- (3) *JS object protection*: In JS, the GC is responsible for allocating and reclaiming S objects on the heap. SpiderMonkey provides data isolation through *compartments* by keeping objects from the same origin within the same compartment with strict isolation. JS objects protected by NoJITsu include *shapes* which contain the object layout information, *script  objects* that point to bytecode. The unit of management is a *cell* that are classified on their allocation kind.

**Instrumenting Memory Accesses:**  

- (1) *Code Transformation and Signal handler*: Intentional traps when write accesses  to a protected region occur and catches the resulting segmentation faults in a custom signal handler.
- (2) *Dynamic Object-Flow Analysis*: Only read permissions are granted to JavaScript objects. At runtime, when a `segfault` is obtained, if it is caused by an MPK violation, it logs the faulting code to be processed later by the LLVM passes. Before entering the signal handler, the OS saves the register state of the interrupted process in memory and recovers the registers after the signal handler returns.
- (3) *Accessor Functions*: Only a limited number of functions can directly write to an object. Based on SpiderMonkey, any other function should invoke one of these accessor functions to modify a JS object. These functions can be decoupled in *Member Accessors* (private attributes), *Payload Accessors*, *Initialization Accessors* or *GC Accessors*.

##### tags: jit, mpk, non-control data attack, security 