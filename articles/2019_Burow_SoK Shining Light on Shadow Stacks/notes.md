<!-- Please prefix the notes with the date as in [22/12/2020] -->

[01/04/2022]

**Attacker model:** Arbitrary read and write primitives to inject a payload and corrupt a code pointer to hijack program's execution. Only DEP and ASLR are up (stack canaries being too weak). Attacker is assumed to only target backward edges (*i.e.* return addresses of functions) as protection for forward edges is an orthogonal problem covered by protection such as CFI. **ROP** and **stack pivots** are the latest iteration of attacks on the stack. ROP is a code-reuse attack that overwrites return addresses on the stack to redirect control flow to a link of gadgets that perform arbitrary code (usually map a memory page as executable and writable then `memcpy` target shellcode before executing it). Stack pivots are an attack technique where the adversary controls the stack pointer and moves the stack frame to a controlled region. It is a payload delivery variant of ROP.

**Shadow Stack Design Space:** For a shadow stack to be adopted, it must be *highly performant*, *compatible with existing code* and provide *meaningful security*. Shadow stacks can be split into 5 categories, 3 as **compact** and 2 as **parallel**. They differ in the way they store the shadow stack pointer, either as a global variable, segment or register for the **compact** version or constant offset or register offset for the **parallel** version. The compact version use the location of the return address on the program stack to directly find the corresponding entry on the shadow stack. The parallel shadow stack is as large as the program stack and a simple offset maps from the program stack to the shadow stack. Direct mapping trades memory overhead for performance.
