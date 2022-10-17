<!-- Please prefix the notes with the date as in [22/12/2020] -->

[30/11/2021]

**RPython:**

RPython is a subset of Python that can run unmodified on the top of the Python interpreter. It forbids using values of incompatible types together. It is also not possible to dynamically change class definitions by adding or removing fields. It has specific built-in types `SomeInteger`, `SomeFloat`, `SomeBool`, `SomeChar` and `SomeString` along with some variants. Some built-in container types are defined as well: `SomeTuple`, `SomeList` and `SomeDict`. Lists and dictionaries need to be homogeneous in RPython. 

As for OO, fields (and their types) of custom classes are inferred based on the program. RPython only supports single inheritance but it supports ***mixin*** definitions (mixture of traits as it does not affect the inheritance hierarchy and traditional mixins as order is not important). **Classes and methods are first-order entities**, i.e.  they can be stored and passed around to be called/instantiated later. 

In Python, functions and classes are not defined by declarations but by executing the `def` and `class` statements, which have the side effect of creating a function or class object. When a module is imported into the interpreter, its top-level statements are executed and the resulting objects are collected into the namespace of the module. The translation of RPython does not start from the source files but rather from live Python objects that have been created and initialized by the standard Python interpreter. 

RPython defines three phases that structure the life cycle of a program: [1] ***initialization*** through construction and initialization of Python classes, functions and constants to be compiled [2] ***translation*** through analysis of the program as a whole, inferring types and producing an executable [3] ***run*** through the execution of the output produced by the previous step. The [1] and [2] steps can take full advantage of Python, without restrictions to get the most information out of the program.

**Architecture:**

RPython front-end consists of a [1] ***Flow Graph Generator*** that analyzes the source objects and creates a graph representing the control flow without type information. Then, the [2] ***Annotator*** adds annotations on the type. These annotations are lowered by the [3] ***RTyper*** to be more suitable for code generation. Finally, the chosen [4] ***Backend*** generates an executable.

[1] Creates a graph in an **untyped Static Single Information (SSI)** form with operations at very high level. It is derived from SSA with new names for each variable at each point where the analysis may obtain information on the value in the variable.

[2] Exploits the SSI graph to perform a static analysis and assigns to each variable a specific a specific RPython type which describes all of the possible values the variable may have at run-time. 

Both perform a global analysis of a program as a whole. The user has to supply a main function that serves as an entry point as well as a corresponding set of type annotations for their parameters. An integer list would become `SomeList(SomeInteger())`.

[3] Performs two main transformations: first, each annotation is translated from a high-level RPython type into an appropriate lower-level type ; second, high-level operations contained in a block are broken down into one or more lower-level operations. This level of indirection helps sharing a considerable amount of code between backends. The RTyper is customized by a specific type system which determines the exact lower-level types and operations needed.

Those type systems can be `lltype` which is intended for lower-level targets or `ootypes` intended for high-level, vm targets. The type `SomeList(SomeInteger())` would be mapped to the built-in type `ArrayList` for oo or the following code for ll:

```c
struct list {
	int length;
	int* items;
}
```


##### tags: general vm, pypy, python, rpython