<!-- Please prefix the notes with the date as in [22/12/2020] -->

[22/04/2021]

Java aims at portability with the **Java Virtual Machine**. It consists of a supposedly stable ecosystem for desktop application through the **JSE platform** and **JEE server**. However the **mobile ecosystem JME** is more fragmented. Google abandonned both the JVM and JME with the **Dalvik virtual machine** along with **limited implementation of standard Java libraries**.

Android runtime must support: **limited processor speed, limited RAM, no swap space, battery powered, sandboxed application runtime, diverse set of devices**. In order to answer those requirements, each Android application runs in its own process with its own Dalvik VM (a register-based VM) that executes a Dalvik Executable file (`.dex`). The Dalvik VM relies on the Linux kernel for threading and low-memory management.

**DEX File Format:** For each class in Java source code, a `.class` file is generated (`javac`) with the corresponding bytecode. The corresponding `.dex` file is generated from those `.class` files (using `dx`). This file format uses specific constant pools for strings, type/class, fields or methods. These pools are shared among all classes. These memory optimizations brings more complexity to the GC because it is independent from applications. Mark bits are separated from other heap memory in order to keep the memory sharing.

**Zygote:** The Zygote enable fast startup time for new instances as well as sharing of code. It assumes a significant number of core libraries are used among multiple applications and often in read-only mode. The Zygote is a VM process that starts at system boot time, preloads core libraries and waits for socket request to fork a new VM.





