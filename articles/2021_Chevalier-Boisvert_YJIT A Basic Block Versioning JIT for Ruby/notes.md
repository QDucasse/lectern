<!-- Please prefix the notes with the date as in [22/12/2020] -->

CRuby, the official Ruby implementation includes a JIT compiler known as MJIT that works well on synthetic benchmarks but not with production workloads. Shopify and Github rely on the interpreter side only. Truffle Ruby, JRuby, PyPy and LuaJIT are implementation efforts that unfortunately contain a gap in terms of compatibility and support for the features of the latest reference implementation.

**Ruby:** Ruby has a broad set of features. Method calls perform **dynamic dispatch**. Methods can be **dynamically redefined** and the **method lookup order** can also be changed. Common operation such as integer arithmetic are not primitive and are calls that can be redefined at runtime. Ruby has support for first-class environments which allow local variable access from outside the local scope. Callees can redefine local variables in their callers.

**CRuby VM:** At its core lays a stack-based interpreter which executes **YARV** bytecode one at a time, with each instruction able to push and pop values of the temporary stack. Another stack is used to keep track of control frame objects corresponding to activation records for method calls. CRuby uses a system of **tags** to differentiate small immediate values as well as the constants `true`, `false` and `nil`. Ruby makes heavy use of method calls that are categorized in 11 different types (each with a slightly different implementation of `send`).

**MJIT:** MJIT compiles Ruby source by generating C source code, it then calls an external C compiler, then loads the output via dynamic linking. This limits optimizations and control.

**Lazy Basic Block Versioning (LBBV):** Code for methods is compiled incrementally one basic block at a time, as opposed to method-based compilers which treat whole methods as compilation units. Code generation proceeds for as long as the compiler can determine the direction of a branch. When it cannot anymore, branch stubs are installed and execution is resumed. Hitting a stub in turn interrupts execution to resume code generation. This helps bring more details to the runtime code generation such as types and values. Code that is not executed is never compiled. Machine code is appended to an array, and stubs are generated in a separate out-of-line memory region (so they do not impact caches). A fixed maximum number of block versions can be generated for each block. The last version must always be generic, meaning it accepts any incoming value types.

**YJIT:** 

1. **Integration with CRuby** by using the same direct-threaded interpreter as a baseline. A counter monitors how many times a method is called and triggers YJIT.
2. **Deoptimization** allows individual versions of a basic block to be invalidated if specific assumptions made at code generation do not hold at runtime. 
3. **Runtime value promotion** can be used to promote runtime values to compile-time constants (equivalent of Psyco's `unlift` operator), this is done by interrupting compilation and inserting a new stub which will then peek at the runtime value and resume compilation. This is used to create **Polymorphic Inline Caches** by detecting the runtime class so that it generates specialized machine code for reading the requested property on the class. If an object of another class is encountered, it causes a jump to a stub which will call back in to the JIT to generate a specialized instance variable read for the new class.
4. **Type Specialization** tracks and propagates type information that is then used to specialize machine code.



Validation over a list of benchmarks along with the number of instruction sequences compiled by YJIT.