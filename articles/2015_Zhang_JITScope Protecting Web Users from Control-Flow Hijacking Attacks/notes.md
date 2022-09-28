<!-- Please prefix the notes with the date as in [22/12/2020] -->

[19/08/2022]

JITScope enforces **CFI ** on both statically compiled and JIT compiled code as well as W+X on JIT code.

**Threat model:** Attackers can (1) write to any writable memory and corrupt control data such as function pointers; (2) read arbitrary mapped memory and thus launch information leakage attacks and bypass ASLR; (3) cannot directly read or write to registers and can only do it using existing instructions that propagate data between registers and memory.

**Security risks:** Risks brought by scripting languages with (1) *heap spraying* where attackers are able to allocate a lot of memory indirectly and force objects to take an expected memory address defusing ASLR; (2) *information leakage* to read memory, retrieve a leaked value for further use (3) *shellcode generation* to build expected shellcode even without the help of ROP. Then JIT compilation brings its set of vulnerabilities (1) *jit code corruption and injection* as classical W+X is not applicable (2) *jit code reuse* to use the JIT compiler to build the shellcode itself.

**Implementation:** JITScope enforces a W+X on the JIT compiled code as well as a CFI policy on both the VM and a relaxed one on the JIT code. JITScope introduces **three delegates to enforce W+X:** `fwd-exec`, `bwd-exec` and `write`. All write operations are forced through the `write` delegate that enables the writable permission of the JIT code memory page and drops the executable permission at the same time and reverses it right after. All calls to the JIT code are enforced through the `fwd-exec` delegate that sets the target memory to read-only and executable before calling the JIT code. The reverse way is done through `bwd-exec` that only allows legitimate VM function calls and sets the target memory to read-only and executable before the VM functions return to the JIT compiled code. Another delegate is the `CodeGen` that enforces a CFI policy on the JIT code: it first randomly selects an ID at compile-time, when the JIT compiler is going to generate  a function, the delegate instruments the ID before this function. For an indirect call or jump instruction, the delegate invokes the delegate to instrument CFI checks before it (they validate the existence of the ID before the target function to ensure the transfer target is a valid JIT function entry). For the JIT code, the `CodeGen` delegate is used to instrument shadow stack related operations to runtime generated return instructions. The shadow stack is put in a separate memory region, indexed by a dedicated segment register (on x86). 



 