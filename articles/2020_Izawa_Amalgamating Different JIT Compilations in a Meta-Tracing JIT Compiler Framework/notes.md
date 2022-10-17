<!-- Please prefix the notes with the date as in [22/12/2020] -->

[12/02/2022]

JIT compilers mainly use two types of compilation: **trace-based** compilation and **method-based** compilation. **Method-based** compilation uses a method, or function, as its unit of compilation. It shares many optimisation techniques with traditional static compilers. On the other hand, **trace-based** compilation uses a trace of a program (a sequence of instructions during a particular run) as a compilation unit. It effectively executes **inlining, loop unrolling or type specialization**. **Method-based compilation** works well on average while the **trace-based** strategy exhibits a **gain in performance** for programs with many conditional branches and deeply nested function calls. However it can cause **severe overheads** when the path of an execution varies. Main related works that extend those are Facebook's HHVM that uses region-based compilation and Higgs Javascript VM that uses lazy basic block versioning.

Using both strategies needs to answer several questions: (1) how can we construct such a compilation engine without using two different compilers (2) how do the code fragments that are compiled by different strategies interact with each others and (3) how can we determine a compilation strategy to compile part of a program.


##### tags: jit