<!-- Please prefix the notes with the date as in [22/12/2020] -->

[27/04/2021]

Application of **MDSOC** (multi-dimensional separation of concerns) and **SPL** (software product line) principles to high-level language virtual machines. Modularisation of **CSOM** using **VMADL** (virtual machine architecture description language). VMs are intricate pieces of software, and modularisation can help dealing with their understanding and overall maintainability. The notion of **service module** helps untangling the complexity of VMs. It consists of a module with *bidirectional interface* that can receive requests and exhibit internal situations to the outside.

CSOM is a SmallTalk Virtual Machine written in C. It does not support images but rather SmallTalk code written in text files. Two threading possibilities are used: the system `pthreads` or threads from within the VM itself. The GC is a mark/sweep collector. a Threaded-interpreter, additional integral representation and snapshots have been developed as extension.

**VMADL**: system architectures need to be supported at source code level and uses **service modules** with signals linking each other called *exposed join points*. It provides a frame in which an **implementation language** and an **aspect language**. Here the implementation language is C and the aspect language is **AspectC++**. In **AspectC++**, the `services` are defined and can use `require` and `expose` to link them between each other. A construct used to implement module interactions is a `combiner`.

An extension of C called ClassDL is used to help with OOP mechanisms. The combination of all the different elements create a toolchain generating a modular VM on demand.

##### tags: general vm