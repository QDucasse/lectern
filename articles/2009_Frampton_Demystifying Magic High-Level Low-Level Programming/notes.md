<!-- Please prefix the notes with the date as in [22/12/2020] -->

[28/04/2021]

Programming at low-level using a high-level programming language is possible and brings into question the use of C as a rule rather than as an exception. To use a high-level language, there are several approaches: the language directly supports low-level coding, the language can be extended to support low-level features, low-level features could be described in another language or the language could be extended via an extensible framework.

Adding low-level features to high-level languages requires three characteristics. ***Extensibility*** as programmers need to be able to reach beyond the semantics of high-level languages. An **extensible framework** for introducing and structuring low-level primitives is necessary. ***Encapsulation*** as the containment of low-level code is essential to minimize the impact on high-level language. The use of **language annotations** helps enforcing specific policies. Coarse-grained approach when lowering semantics results in both performance and semantics. ***Fine-grained lowering*** can help  but needs the programmer to reason about the undergoing low-level application.

The main challenges when linking low-level and high-level programming are that the high-level language **does not allow data to be represented as required** or **does not allow behavior** that is required. In order to close the data representation gap, ***primitive types*, *compound types*** and ***unboxed types*** can help as well as the addition of references and values (pointers referencing/dereferencing) are needed. Additionally to extending the data representation, the semantics should be extended as well. This can be done through the use of **intrinsic functions** to directly reflect the required semantics or add **semantic regimes** within which certain language-imposed abstractions would be suspended.

**Implementation:** **Raw Storage** allows the user to associate an empty type with a raw chunk of backing data of a specified size. This helps to create non-compound unboxed types. This can be done through the use of `@RawStorage` and`@Unboxed`. An unboxed type is only syntactically distinguished from an object and the **runtime compiler** ensures that unboxed types are never used as objects.

 The framework is used by MMTk !

 ##### tags: garbage collection, intermediate representation