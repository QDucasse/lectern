<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[26/01/2021]*

Security for native code in Java applications. Based on **software-based fault isolation (SFI)**, Robusta isolates native code into a sandbox where **dynamic linking/loading of libraries** is supported and **unsafe system modification and confidentiality violations are prevented**.

The introduction of native functions in Java applications is done with the use of the **Java Native Interface (JNI)** along with the keyword `native`. Native code resides in the **same address space** as Java code but is not constrained by the **Java Security Model**. Native code can therefore **read/write any memory location** or cause **integrity and confidentiality violations** (e.g. *type-confusion attacks*).

Robusta defends with **SFI to isolate untrusted native code from the rest of the JVM** (done with Google's NaCl). Next, all JNI calls are redirected to **JNI trampolines** using "fake" interface pointers to untrusted native code. Those trampolines are the *only* way native code can escape the sandbox. They invoke trusted JNI wrappers outside of the sandbox to perform some safety checks. Robusta also prevents the JNI from using direct pointers to Java primitive arrays and native code from calling Java methods. Finally, Robusta connects to Java's Security Manager to mediate native system calls.

JVM **integrity** is ensured by the following definition: *Suppose one execution step in native code brings a state (s, h, w) (JVM stack, JVM heap, native world) to (s', h', w'). The integrity is respected if s is equal to s' and h is included in h'*. JVM **confidentiality** is respected if native code accesses **only objects reachable by the references set by the JVM** and if the **access-control modifiers** (e.g. `private`) **of fields and methods are respected**. Next, the system calls have to follow given policies.

Native code isolation:

- **Google's Native Client (NaCl)** and the use of **trampolines** (from untrusted to trusted) and **springboards** (reverse).
- **Secure Dynamic Linking/Loading:** the address space is separated into a code space (cs) and a data space (ds) and an address is interpreted differently whether it is used as a code or a data address. The usage of a dynamic library is guarded by a specific routine. 

**NaCl JVM integration:** When the JVM starts, Robusta constructs an NaCl sandbox, reserves a memory region for the NaCl address space and sets up a code and a data region. Page protection is configured so that the **code region is readable and executable** while the **data region is readable and writable**. **Trusted trampolines** are installed in the code region. Finally the dynamic linker/loader is loaded into the NaCl address space.

**Sandbox of JNI calls:** Native methods access JNI through an interface pointer. This pointer usually goes through the JNI methods however they are here outside of the sandbox. Robusta duplicates the function table with pointers to JNI trampolines so that the native function can access the outside of the sandbox if authorized. The JNI checks includes several safety checks (type, signature, etc.). JNI allows efficient access to primitive arrays however direct access to the heap is dangerous to provide to native functions. Robusta performs a copy-in/copy-out.

**Native Code Security:** The regulation of native system calls goes through the Java's Security Manager. It accepts or denies a system call based on a security policy. A security policy can grant two kinds of permissions: **mode permissions** and **system-access permissions**. **Mode permissions** specify whether a library can be loaded into the JVM and whether it should be sandboxed. The mode policy is enforced during library-loading. **System-access permissions** define what an application is allowed to perform (e.g. read or write files).

##### tags: attack, java, sandbox, security