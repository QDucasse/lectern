### Attack Summary

***RISC-V gadget chaining*** is a code-reuse attack against the RISC-V ISA. It presents a new class of gadgets (using several Linear Code Sequences And Jumps, ***LCSAJ***) that were undetected by the Galileo tools. Chaining those gadgets allow the attacker to perform a privilege escalation attack from a C code injection.

### Attacker Threat Model

The target platform features a standard Linux operating system such as Debian or Fedora, with two levels of privilege (`user` and `root`). Standard protections are in place such as ASLR or DEP. Programs are compiled with stack smashing mitigation such as `gcc`'s `-fstack-protector-strong` (since `gcc`'s `-mmitigate-rop` or `clang`'s CFI are not available on RISC-V).

### Recipe

***Gadget Chaining:*** The hidden instruction are directly written in C code and feature one or two instructions followed by a jump to a relative offset.

```C
long long function15c() {
	dummy();
	dummy4((signed) 0x9932000,
		   0,
		   (signed) 0xa0212000,
		   (signed) 0x23371000);
	return 0;
}
```

