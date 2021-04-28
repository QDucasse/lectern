<!-- Please prefix the notes with the date as in [22/12/2020] -->

[22/04/2021]

Main objectives of Lua: *simplicity* (simple language for simple C code), efficiency (fast one-pass compiler and VM), *portability* (clean ANSI C implementation), *embeddability* (simple C API), *low embedding cost* (small Lua core and extension as user libraries).

Hand-written compiler (YACC too slow) with scanner and recursive descent parser. No intermediate representation, instructions for the VM emitted on the fly. Fastest language implementation of interpreted and dynamically-typed languages. 

**Values representation:** Eight basic types (*nil, boolean, number, string, table, function, userdata, thread*). Tables are associative arrays with index. Userdata consists of pointers to memory blocks (*heavy* allocated by Lua and GCd or *light* allocated and freed by the user). Values of **all types are first class values**, they can be stored in globals, locals and table fields, passed as arguments etc. Value types are stored as a C union:

```c
typedef union {
	GCObject *gc; // strings tables etc.
	void p*;      // light userdata
	lua_Number n; // double
	int b;        // integer
} Value;
```

This solution is expensive to copy values but ensures portability. Strings are immutable and internalized in a hash table



**Tables:** The only data structures in Lua are tables, or **associative arrays**. They can be indexed by any value and hold values of any type. They are dynamic because they grow or shrink accordingly. Only one set of operators is needed to perform operations on tables or arrays. Tables are implemented as **hybrid data structures** (**array part** with implicit integer index and **hash part** with other indexes). The load factor is balanced by testing both parts and choosing an n such as at least half the slots between 1 and n are used and that at least one is used between n/2+1 and n. The hash part uses a mix of  *chained scatter table with Brent's variation*.

**Functions and Closures:** **Upvalues** are used to implement closures. Any outer local variable is accessed indirectly through an upvalue. **The upvalue originally points to the stack slot wherein the variable lives. When it goes out of scope, the value migrates into a slot in the upvalue itself**. The migration is transparent to all the users. To ensure the uniqueness, a linked list of all open upvalues is kept. When a new closure is created, all outer local variables are gone through and if an open value is found, it uses this one, otherwise it creates and links it. **Flat closures** allows to pour outer variables into inner closures.

**Threads and Coroutines:** Asymmetric coroutines are supported by the functions `create`, `resume` and `yield`. Each coroutine has its own stack and are stackful (it can be suspended from inside any number of nested calls). Combination of stackfulness and first-class status makes coroutines equivalent to one-shot continuations.

**The VM itself:** For each function that Lua compiles it creates a prototype which contains an array with the opcodes for the function and an array of Lua values with all constants used by the function. Register-based VM allows for less instructions and a single fetch time because operands are inside the instruction. Instructions are 32 bits long divided into three or four fields: OP|A|B|C or OP|A|Bx or OP|A|sBx where A is the destination, B and C registers, Bx an unsigned value and sBx a signed value. Branch instructions are decoupled in a test and a jump instruction. If the test is not verified, the next instruction is skipped. Each function (and coroutine) holds two stacks, the activation records of the other functions and a large array of temporary values corresponding to a given function.



