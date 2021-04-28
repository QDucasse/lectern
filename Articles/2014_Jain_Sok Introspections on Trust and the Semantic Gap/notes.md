<!-- Please prefix the notes with the date as in [22/12/2020] -->

[27/04/2021]

The goals of **Virtual Machine Introspection (VMI)** is to identify if the guest OS has been compromised, if malicious applications are running on the system or if sensitive file have uncompromised secrecy or integrity. A *semantic gap* occurs when using a hypervisor to look into VM behavior as the abstractions used by the hypervisor policies are higher-level than what he can actually see (registers and cpu state). Most of VMI development goes into reconstructing high-level semantic from low-level sources.

To close this semantic gap, the **reconstruction** of data models is essential. A **learning phase** is used to extract information related to data structures (**signature**). A **search phase** can then look for instances of this data structure. Signatures are either handcrafted (`memparser`, `kntlist`  or `grepexec`), extracted from source analysis (`siggraph`, `kop` or `mas`)  and dynamic learning by studying a trusted OS behavior.

Other methods allow to bridge the gap , such as *code implanting* where the objective is to inject code into the guest OS that reports information back to the hypervisor, *process outgrafting*  that relocates the monitoring process from an untrusted VM to a second, trusted one or *kernel executable integrity* enforces the fact that the executable of the kernel has not been modified. This can be enforced by:  1) the W+X principle where a memory page can either be *writable* or *executable* but not both at the same time, 2) *whitelisting portions of code*.

- Current VMI systems face fundamental trade-offs between performance and risk, often making fragile assumptions about the guest OS

  