<!-- Please prefix the notes with the date as in [22/12/2020] -->



[04/10/2022]

**Threat model:** An attacker that has full control over the entire data memory of the executing program.

**Control-Flow Integrity  (CFI):** defines **security policies** that dictates how software execution must follow a given path. This path is defined in the **Control-Flow Graph (CFG)** determined ahead-of-time. The CFG is determined by analysis, either *source-code analysis*, *binary analysis* or *execution profiling*.  The enforcement is done using a combination of **lightweight static verification** and **machine-code rewriting that instruments software with runtime checks**. The runtime checks ensure that control flow remains within a given CFG. CFI enforcement protects a wide range of attacks, whther stack-based (buffer overflows) or heap-based (jump-to-libc). It will not however cover attacks within the vbounds of the CFG (*e.g.* incorrect string parsing).

**Related Works:** (1) *SFI and Inlined Reference Monitors (IRMs)* are a general technique for enforcing fine-grained security policies through inline checks. SFI is a special IRM that performs dynamic checks for the purposes of memory protection. They operate by adding code into the program that needs to be monitored. The performance is problematic because of the need for control-flow checks. (2) *Vulnerability Mitigation with Secrets* such as PointGuard that stores code addresses in an encrypted form in data memory. The reliability on a secret value remains uncertain.

**Solution:** CFI relies on dynamic checks implemented by machine-code rewriting (verified by static inspection). CFI requires that when a machine code instruction transfers control, it targets a valid destination determined by the CFG ahead of time. For static destinations, this is verified statically but control-flows whose destination is determined at runtime have to be dynamically checked. To determine if an address sane, multiple strategies are available. A check against a set of address ranges adds unacceptable overhead. Three instructions: `label ID` that has no effect, `call, ID, DST` that jumps to the address in `DST` if the `ID` is correct and the corresponding `ret ID` . The instrumentation modifies each source instruction and each possible destination instruction of computed control-flow transfer. It adds before each source a dynamic check (ID-check) that ensures the runtime destination has the ID of the proper equivalence class (that have to be defined in the CFG).

##### tags: cfi, security