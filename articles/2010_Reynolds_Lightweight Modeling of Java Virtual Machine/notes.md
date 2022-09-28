<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[02/02/2021]*

Java Security is enforced in three ways:

- The **Java** **compiler** has a large number of **rules** that it enforces in order to ensure that the **syntax and semantics of the Java language are satisfied** but also to prohibit actions that are known to be malicious (e.g. uninitialized variables).
- The **Java** **class loader**, is used to port a classfile into the Java execution environment. When class loading is performed, the **Java Bytecode Verifier** is used to assert the bytecode are of correct form and types.
- The **Java Runtime** performs array bounds checking, type conversion checkings, etc. 



Almost all Java exploits use weaknesses in the **Bytecode Verifier**. The verifier uses a constraints-based approach to perform its analysis. The objective is to (1) provide an extensible framework for modeling security constraints and (2) provide a concrete model for meaningful, high value security constraints.