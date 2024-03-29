<!-- Please prefix the notes with the date as in [22/12/2020] -->

[12/10/2022]

Using a generalization of non-control-data attacks called **Control-Flow Bending (CFB)**, the authors present a way to achieve a Turing-complete computation on memory using calls to the standard library.  A **non-control-data attack** is an attack where a memory corruption is used to corrupt data but no code pointer (*i.e.* pointer to a return address, function pointer). These attacks can still allow an attacker to execute arbitrary code through a victim's program.

**Control-Flow Bending (CFB)**  allows an attacker to bend the control-flow of the application while still adhering to the imposed security policy (CFI). A "data-only attack" is a non-control-data attack where the entire execution trace is identical to some feasible non-exploit execution trace. CFB is more general as each control-flow transfer is *in* the valid CFG but the execution trace is not necessarily required to match a valid non-exploit trace. To clarify:

- An attacker who overwrites arguments to `exec()` is performing a **data-only attack**
- An attacker who overwrites an `is_admin` flag half-way through processing a request is performing a **non-control-data attack**
- An attacker who modifies a function pointer to point to a different (valid) call target is mounting a **control-flow bending attack**

**Fully-precise CFI** where a CFG is the most restrictive that still allows all feasible non-malicious execution does not exist in practice. Practical implementations of CFI are always limited by the precision of the CFG that can be obtained. Most CFI mechanisms over-approximate allowed targets for individual indirect control-flow transfers. While a CFI solution can be decoupled in: (1) restricting indirect control transfers to the CFG and (2) restricting the return instructions, some modern CFI schemes deactivate shadow stacks (answer to the second point) due to its performance overhead. 

Evaluating CFI solutions is possible using the **AIR and gadget reduction metrics**. The **AIR metric** measures the relative reduction in the average number of valid targets for all indirect branch instructions that a CFI scheme provides (without CFI, an indirect branch can target any instruction in the program). The **gadget reduction metric** measures the relative reduction in the number of gadgets that can be found at locations that are valid targets for an indirect branch instruction. The authors propose **Basic Exploitation Test (BET)** that involves selecting a minimal program that contains a realistic vulnerability and determining if attacks are still possible under protection of the CFI scheme. The minimal program should be chosen to use a subset of common run-time libraries normally found in real applications, and constructed so it contains a vulnerability that allows hijacking control-flow in a way that is seen in real-life attacks. The evaluator applies the CFI scheme to the program, chooses an attacker goal (arbitrary code execution, partial code execution or information leakage) and checks whether it is achievable under the CFI scheme.

To return to a different location than it was called from, a function must be able to **overwrite the return address on the stack after it is called and before it returns**. This is easy when the memory corruption vulnerability happens in that specific function. An attacker can use a **dispatcher function** to perform this task. It is a function that can overwrite its own return address when given arguments supplied by an attacker. Any function that contains a "write-what-where" primitive when the arguments are under the attacker's control can be used as a dispatcher function. The `libc` presents different dispatcher functions such as:

- `memcpy()` - pointing the source buffer to an attacker-controlled location and the target buffer to `memcpy()`'s return address .
- `printf()` - using `%n` to write an arbitrary value to an arbitrary location and rewrite its own return address.
- `strcat()` - similar to `memcpy()` but only usable if the address to return to does not contain null bytes.
- `fputs()` - characters are temporarily buffered to a location as specified in the `FILE` argument that the attacker can supply, placing the temporary buffer on top of the return address.

It is also possible to perform a **loop injection** using two following calls to the same dispatcher function where the attacker controls the input to the second one. It is common for programs to perform successive calls to `printf()` for example. When the second call to `printf()` is reached, the attacker can modify the return address to point to the instruction right after the first `printf()` and re-trigger the second call! This just created a **loop**!

##### tags: attack, cfi, security