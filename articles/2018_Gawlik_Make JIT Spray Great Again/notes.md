<!-- Please prefix the notes with the date as in [22/12/2020] -->

[26/08/2022]

Existing defenses in Edge are *Microsoft's Control Flow Guard* (**MS-CFG**), a CFI implementation. *Arbitrary Code Guard* (**ACG**) prevents aking code pages writable and writable pages executable. As this is an issue for the JIT compiler, Edge provides an out-of-process JIT server which maps dynamic code into a memory region shared with the browser process. 

JIT-Spray specific protections: *constant folding*, *constant blinding*, *NOP insertion*.

##### tags: jit, jit spraying, security, sok