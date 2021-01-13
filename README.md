 ## VM-related Articles

This repository contains the different articles and the bibliography (in BibTeX format) related to the VM world (to a LARGE extent). The `VM.bib` file in `Bibliography` is best used with  [JabRef]. The notes in each of the folders, namely `notes.md` are integrated in the bibliography using a Python script in `utils.py`.  This script contains several useful helpers:

```bash
$ python utils.py --propagate  # Adds the contents of the notes.md files to their respective entry
$ python utils.py --nocomments # Generates a comment-free bibliography
$ python utils.py --process    # Creates a repository and empty notes.md file for each pdf in
							   # Articles/TO_PROCESS
$ python utils.py --genreadme  # Adds the notes to the present README.md file
```
[JabRef]: https://www.jabref.org/



## Article notes
### Summary
[1973 - Bell, Threaded Code](#1973---Bell-Threaded-Code)

[1974 - Popek, Formal Requirements for Virtualizable Third Generation Architectures](#1974---Popek-Formal-Requirements-for-Virtualizable-Third-Generation-Architectures)

[1975 - Dewar, Indirect Threaded Code](#1975---Dewar-Indirect-Threaded-Code)

[1983 - Krasner, Smalltalk-80 Bits of History Words of Advice](#1983---Krasner-Smalltalk-80-Bits-of-History-Words-of-Advice)

[1984 - Deutsch, Efficient Implementation of the SmallTalk-80 System](#1984---Deutsch-Efficient-Implementation-of-the-SmallTalk-80-System)

[1984 - Ungar, Generation Scavenging A non-disruptive High Performance Storage Reclamation Algorithm](#1984---Ungar-Generation-Scavenging-A-non-disruptive-High-Performance-Storage-Reclamation-Algorithm)

[1986 - Samples, SOAR Smalltalk Without Bytecodes](#1986---Samples-SOAR-Smalltalk-Without-Bytecodes)

[1986 - Ungar, The Design and Evaluation of a High Performance Smalltalk System](#1986---Ungar-The-Design-and-Evaluation-of-a-High-Performance-Smalltalk-System)

[1987 - Bush, Compiling Smalltalk-80 to a RISC](#1987---Bush-Compiling-Smalltalk-80-to-a-RISC)

[1987 - Ungar, What Price Smalltalk](#1987---Ungar-What-Price-Smalltalk)

[1989 - Chambers, Customization Optimizing Compiler Technology for SELF a Dynamically-Typed Object-Oriented Programming Language](#1989---Chambers-Customization-Optimizing-Compiler-Technology-for-SELF-a-Dynamically-Typed-Object-Oriented-Programming-Language)

[1991 - Hoelzle, Optimizing Dynamically-Typed Object-Oriented Languages with Polymorphic Inline Caches](#1991---Hoelzle-Optimizing-Dynamically-Typed-Object-Oriented-Languages-with-Polymorphic-Inline-Caches)

[1992 - Hoelzle, Debugging Optimized Code with Dynamic Deoptimization](#1992---Hoelzle-Debugging-Optimized-Code-with-Dynamic-Deoptimization)

[1994 - Hoelzle, Adaptive Optimization for SELF Reconciling High Performance with Exploratory Programming](#1994---Hoelzle-Adaptive-Optimization-for-SELF-Reconciling-High-Performance-with-Exploratory-Programming)

[1995 - Click, A Simple Graph-Based Intermediate Representation](#1995---Click-A-Simple-Graph-Based-Intermediate-Representation)

[1995 - Dean, Optimization of Object-Oriented Programs Using Static Class Hierarchy Analysis](#1995---Dean-Optimization-of-Object-Oriented-Programs-Using-Static-Class-Hierarchy-Analysis)

[1995 - Ertl, Stack Caching for Interpreters](#1995---Ertl-Stack-Caching-for-Interpreters)

[1995 - Gosling, Java Intermediate Bytecodes](#1995---Gosling-Java-Intermediate-Bytecodes)

[1996 - Bacon, Fast Static Analysis of C Virtual Function Calls](#1996---Bacon-Fast-Static-Analysis-of-C-Virtual-Function-Calls)

[1997 - Agesen, Design and Implementation of PEp a Java Just-In-Time Translator](#1997---Agesen-Design-and-Implementation-of-PEp-a-Java-Just-In-Time-Translator)

[1997 - Ingals, Back to the Future The Story of Squeak a Practical Smalltalk Written in Itself](#1997---Ingals-Back-to-the-Future-The-Story-of-Squeak-a-Practical-Smalltalk-Written-in-Itself)

[1997 - Kistler, Slim Binaries](#1997---Kistler-Slim-Binaries)

[1998 - Piumarta, Optimizing Direct Threaded Code by Selective Inlining](#1998---Piumarta-Optimizing-Direct-Threaded-Code-by-Selective-Inlining)

[1998 - Taivalsaari, Implementing a Java Virtual Machine in the Java Programming Language](#1998---Taivalsaari-Implementing-a-Java-Virtual-Machine-in-the-Java-Programming-Language)

[1999 - Burke, The Jalapeno Dynamic Optimizing Compiler for Java](#1999---Burke-The-Jalapeno-Dynamic-Optimizing-Compiler-for-Java)

[1999 - Wolczko, Self Includes Smalltalk](#1999---Wolczko-Self-Includes-Smalltalk)

[1999 - Yoshihiko, Partial Evaluation of Computation Process an Approach to a Compiler-Compiler](#1999---Yoshihiko-Partial-Evaluation-of-Computation-Process-an-Approach-to-a-Compiler-Compiler)

[2000 - Arnold, Adaptive Optimization in the Jalapeno JVM](#2000---Arnold-Adaptive-Optimization-in-the-Jalapeno-JVM)

[2000 - Bala, Dynamo a Transparent Dynamic Optimisation System](#2000---Bala-Dynamo-a-Transparent-Dynamic-Optimisation-System)

[2000 - Diehl, Abstract Machines for Programming Language Implementation](#2000---Diehl-Abstract-Machines-for-Programming-Language-Implementation)

[2001 - Cheng, A Parallel Real-Time Garbage Collector](#2001---Cheng-A-Parallel-Real-Time-Garbage-Collector)

[2001 - Paleczny, The Java HotSpot Server Compiler](#2001---Paleczny-The-Java-HotSpot-Server-Compiler)

[2002 - Barbu, Application-Replay Attack on Java Cards When the Garbage Collector Gets Confused](#2002---Barbu-Application-Replay-Attack-on-Java-Cards-When-the-Garbage-Collector-Gets-Confused)

[2002 - Click, Fast Subtype Checking in the HotSpot JVM](#2002---Click-Fast-Subtype-Checking-in-the-HotSpot-JVM)

[2002 - Ertl, Vmgen a Generator of Efficient Virtual Machine Interpreters](#2002---Ertl-Vmgen-a-Generator-of-Efficient-Virtual-Machine-Interpreters)

[2003 - Dehnert, The Transmeta Code Morphing - Software Using Speculation recovery and Adaptive Retranslation to Address Real-Life Challenges](#2003---Dehnert-The-Transmeta-Code-Morphing---Software-Using-Speculation-recovery-and-Adaptive-Retranslation-to-Address-Real-Life-Challenges)

[2003 - Ertl, The Structure and Performance of Efficient Interpreters](#2003---Ertl-The-Structure-and-Performance-of-Efficient-Interpreters)

[2003 - Fink, Design Implementation and Evaluation of Adaptive Recompilation with On-Stack Replacement](#2003---Fink-Design-Implementation-and-Evaluation-of-Adaptive-Recompilation-with-On-Stack-Replacement)

[2003 - Shaylor, A Java Virtual Machine Architecture for Very Small Devices](#2003---Shaylor-A-Java-Virtual-Machine-Architecture-for-Very-Small-Devices)

[2004 - Blackburn, Oil and Water High Performance Garbage Collection in Java with MMTk](#2004---Blackburn-Oil-and-Water-High-Performance-Garbage-Collection-in-Java-with-MMTk)

[2004 - Chambers, A Retrospective on Customization Optimizing Compiler Technology for SELF a Dynamically-Typed Object-Oriented Programming Language](#2004---Chambers-A-Retrospective-on-Customization-Optimizing-Compiler-Technology-for-SELF-a-Dynamically-Typed-Object-Oriented-Programming-Language)

[2004 - Ertl, Combining Stack Caching with Dynamic Superinstructions](#2004---Ertl-Combining-Stack-Caching-with-Dynamic-Superinstructions)

[2004 - Sachindran, MC2 High-Performance Garbage Collection for Memory-Constrained Environments](#2004---Sachindran-MC2-High-Performance-Garbage-Collection-for-Memory-Constrained-Environments)

[2005 - Click, The Pauseless GC Algorithm](#2005---Click-The-Pauseless-GC-Algorithm)

[2005 - Ertl, Advances in Interpreters Virtual Machines and Emulators](#2005---Ertl-Advances-in-Interpreters-Virtual-Machines-and-Emulators)

[2005 - Faes, FPGA-Aware Garbage Collection in Java](#2005---Faes-FPGA-Aware-Garbage-Collection-in-Java)

[2005 - Ungar, Constructing a Metacircular Virtual Machine in an Exploratory Programming Environment](#2005---Ungar-Constructing-a-Metacircular-Virtual-Machine-in-an-Exploratory-Programming-Environment)

[2006 - Gal, HotpathVM An Effective JIT Compiler for Resource-Constrained Devices](#2006---Gal-HotpathVM-An-Effective-JIT-Compiler-for-Resource-Constrained-Devices)

[2006 - Rigo, PyPys Approach to Virtual Machine Construction](#2006---Rigo-PyPys-Approach-to-Virtual-Machine-Construction)

[2006 - Russell, Eliminating Synchronization-Related Atomic Operations with Biased Locking and Bulk Rebiasing](#2006---Russell-Eliminating-Synchronization-Related-Atomic-Operations-with-Biased-Locking-and-Bulk-Rebiasing)

[2008 - Kotzmann, Design of the Java HotSpot Client Compiler for Java 6](#2008---Kotzmann-Design-of-the-Java-HotSpot-Client-Compiler-for-Java-6)

[2009 - Bolz, Tracing the Meta-Level PyPys Tracing JIT Compiler](#2009---Bolz-Tracing-the-Meta-Level-PyPys-Tracing-JIT-Compiler)

[2009 - Frampton, Demystifying Magic High-Level Low-Level Programming](#2009---Frampton-Demystifying-Magic-High-Level-Low-Level-Programming)

[2010 - Agesen, The Evolution of an X86 Virtual Machine Monitor](#2010---Agesen-The-Evolution-of-an-X86-Virtual-Machine-Monitor)

[2010 - Rizzo, Practical Padding Oracle Attacks](#2010---Rizzo-Practical-Padding-Oracle-Attacks)

[2011 - Bolz, Runtime Feedback in a Meta-Tracing JIT for Efficient Dynamic Languages](#2011---Bolz-Runtime-Feedback-in-a-Meta-Tracing-JIT-for-Efficient-Dynamic-Languages)

[2012 - Rohou, Tiptop Hardware Performance Counters for the Masses](#2012---Rohou-Tiptop-Hardware-Performance-Counters-for-the-Masses)

[2012 - Wuerthinger, Self-optimizing AST interpreters](#2012---Wuerthinger-Self-optimizing-AST-interpreters)

[2013 - Eckert, Hardware Based Security Enhanced Direct Memory Access](#2013---Eckert-Hardware-Based-Security-Enhanced-Direct-Memory-Access)

[2013 - Kulkarni, Automatic Construction of Inlining Heuristics using Machine Learning](#2013---Kulkarni-Automatic-Construction-of-Inlining-Heuristics-using-Machine-Learning)

[2013 - Wimmer, Maxine an Approachable Virtual Machine for and in Java](#2013---Wimmer-Maxine-an-Approachable-Virtual-Machine-for-and-in-Java)

[2013 - Wuerthinger, One VM to Rule Them All](#2013---Wuerthinger-One-VM-to-Rule-Them-All)

[2014 - Duboscq, Speculation Without Regret Reducing Deoptimization Meta-data in the Graal Compiler](#2014---Duboscq-Speculation-Without-Regret-Reducing-Deoptimization-Meta-data-in-the-Graal-Compiler)

[2014 - Eckert, FPGA-Based System Virtual Machines](#2014---Eckert-FPGA-Based-System-Virtual-Machines)

[2014 - Freundenberg, SqueakJS a Modern and Practical Smalltalk that Runs in any Browser](#2014---Freundenberg-SqueakJS-a-Modern-and-Practical-Smalltalk-that-Runs-in-any-Browser)

[2014 - Humer, A Domain-Specific Language for Building Self-Optimizing AST Interpreters](#2014---Humer-A-Domain-Specific-Language-for-Building-Self-Optimizing-AST-Interpreters)

[2014 - Seaton, Debugging at Full Speed](#2014---Seaton-Debugging-at-Full-Speed)

[2014 - Stadler, Partial Escape Analysis and Scalar Replacement for Java](#2014---Stadler-Partial-Escape-Analysis-and-Scalar-Replacement-for-Java)

[2014 - Woss, An Object Storage Model for the Truffle Language Implementation Framework](#2014---Woss-An-Object-Storage-Model-for-the-Truffle-Language-Implementation-Framework)

[2015 - Gosling, The Java 8 Language Specification](#2015---Gosling-The-Java-8-Language-Specification)

[2015 - Grimmer, Dynamically Composing Languages in a Modular Way Supporting C Extensions for Dynamic Languages](#2015---Grimmer-Dynamically-Composing-Languages-in-a-Modular-Way-Supporting-C-Extensions-for-Dynamic-Languages)

[2015 - Gunadi, Formal Certification of Android Bytecode](#2015---Gunadi-Formal-Certification-of-Android-Bytecode)

[2015 - Hussein, Impact of GC Design on Power and Performance for Android](#2015---Hussein-Impact-of-GC-Design-on-Power-and-Performance-for-Android)

[2015 - Lindholm, The JVM 8 Specification](#2015---Lindholm-The-JVM-8-Specification)

[2015 - Rohou, Branch Prediction and the Performance of Interpreters Dont Trust Folklore](#2015---Rohou-Branch-Prediction-and-the-Performance-of-Interpreters-Dont-Trust-Folklore)

[2015 - Simon, Snippets Taking the High Road to a Low Level](#2015---Simon-Snippets-Taking-the-High-Road-to-a-Low-Level)

[2015 - VanDeVanter, Building Debuggers and Other Tools We Can Have it All](#2015---VanDeVanter-Building-Debuggers-and-Other-Tools-We-Can-Have-it-All)

[2017 - Pedersen, From Trash to Treasure Timing-Sensitive Garbage](#2017---Pedersen-From-Trash-to-Treasure-Timing-Sensitive-Garbage)

[2018 - Lipp, Meltdown Reading Kernel Memory from User Space](#2018---Lipp-Meltdown-Reading-Kernel-Memory-from-User-Space)

[2018 - Wu, A Side-channel Attack on HotSpot Heap Management](#2018---Wu-A-Side-channel-Attack-on-HotSpot-Heap-Management)

[2019 - Kocher, Spectre Attacks Exploiting Speculative Execution](#2019---Kocher-Spectre-Attacks-Exploiting-Speculative-Execution)

[2019 - Patel, Runtime-Programmable Pipelines for Model Checkers on FPGAs](#2019---Patel-Runtime-Programmable-Pipelines-for-Model-Checkers-on-FPGAs)

[2019 - Schwarz, ZombieLoad Cross-Privilege-Boundary Data Sampling](#2019---Schwarz-ZombieLoad-Cross-Privilege-Boundary-Data-Sampling)

[2019 - Varoumas, High-level programming models for microcontrollers with scarce resources](#2019---Varoumas-High-level-programming-models-for-microcontrollers-with-scarce-resources)

[2020 - Fournier, Menhir Generic High-Speed FPGA Model-Checker](#2020---Fournier-Menhir-Generic-High-Speed-FPGA-Model-Checker)

[2020 - Lima, Exposing Bugs in JavaScript Engines through Test Transplantation and Differential Testing](#2020---Lima-Exposing-Bugs-in-JavaScript-Engines-through-Test-Transplantation-and-Differential-Testing)

[2020 - Zandberg, Minimal Virtual Machines on IoT Microcontrollers The Case of Berkeley Packet Filters with rBPF](#2020---Zandberg-Minimal-Virtual-Machines-on-IoT-Microcontrollers-The-Case-of-Berkeley-Packet-Filters-with-rBPF)




### 1973 - Bell, Threaded Code
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1974 - Popek, Formal Requirements for Virtualizable Third Generation Architectures
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1975 - Dewar, Indirect Threaded Code
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1983 - Krasner, Smalltalk-80 Bits of History Words of Advice
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1984 - Deutsch, Efficient Implementation of the SmallTalk-80 System
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1984 - Ungar, Generation Scavenging A non-disruptive High Performance Storage Reclamation Algorithm
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1986 - Samples, SOAR Smalltalk Without Bytecodes
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1986 - Ungar, The Design and Evaluation of a High Performance Smalltalk System
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1987 - Bush, Compiling Smalltalk-80 to a RISC
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[08/12/2020]:*

Goal of SOAR (Smalltalk On A RISC) is to produce a high-performance Smalltalk-80 execution language. It can attain high performance on a modified reduced instruction set architecture. The most important optimization is the removal of a layer of interpretation, compiling the bytecoded virtual machine instructions into low-level, register-based hardware instructions.

The Smalltalk-80 virtual machines executes *stack-based instructions* called **bytecodes**. An alternative is to compile **bytecodes** to native machine instructions directly. The SOAR approach consists of compiling all methods from *bytecodes* into **SOAR instructions**, therefor discarding the *bytecodes*. 

The basic task of the compiler is to translate *stack-oriented bytecodes* into **RISC-style loads, stores, and other register-based instructions**. It does this by *assigning Smalltalk variables and stack locations to registers and memory locations*, and then *simulating at compile time the bytecode stack operations on a symbolic stack*, converting the operations into SOAR instructions.

The RISC architecture presents a register file of overlapping register windows, each window corresponding to a procedure activation frame allocated in a stack discipline. The SOAR hardware uses a **window size of 16 registers with 8-register overlap**. Each window is divided into two identical sets of 8 registers, a **high set** (15-8) and a **low set** (7-0). Each set contains **6 general purpose registers and 2 dedicated registers** used for **return addresses** (15 and 7) and **return values** (14 and 6).

*FIGURE 2 PROVIDES A VERY GOOD INSIGHT*

When more registers are required than available, **spilling** is necessary. Spilling comes with two rules: (1) **Entire categories of variables are spilled if necessary** (arguments for example) (2) **A variable cannot be moved once it has been allocated a location**. These rules are not optimized in terms of register space usage but are simple and spilling is *minimized at reasonable cost*. Spills can either be *allocated from a common spill pool* or a separate *spill object can be allocated for each activation frame that spills*.

SOAR takes advantage of the fact that all simple arithmetic operations are performed only on integers. If incorrect, the hardware will **trap** and transfer to a handler that will **look-up** the correct method. The compiler also takes advantage of hardware that **maps registers to memory addresses** and allows **pointers to registers**.

---


### 1987 - Ungar, What Price Smalltalk
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1989 - Chambers, Customization Optimizing Compiler Technology for SELF a Dynamically-Typed Object-Oriented Programming Language
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1991 - Hoelzle, Optimizing Dynamically-Typed Object-Oriented Languages with Polymorphic Inline Caches
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[08/12/2020]:*

Historically, dynamically-typed object-oriented languages have run much slower than statically-typed languages. Techniques such as **type analysis**

[^1]: The compiler can "predict" the type of the receiver based on the message name and insert a runtime check before the message. It usually allows for later inlining based on the most frequent type. The type can be propagated through the control flow graph and can use type casing with several branches corresponding to the possible types and their version of the inlined method. 

, **customization**

[^2]: Extends dynamic compilation by exploiting the fact that many messages within a method are sent to `self`. The compiler creates a separate compiled version of a given source method for each receiver type. This duplication allows for customization. In particular, knowing the type of `self` at compile time allows all `self` sends to be inlined without any type tests. Customization can also be applied to global variable, instance variable for example.

, and **splitting** 

[^3]: Turns a polymorphic message into several separate monomorphic messages and avoids tests by copying parts of the control flow graph.

 have been shown to be very effective in reducing this disparity.

A new acceleration approach is presented: ***Polymorphic Inline Caches (PICs)*** that provide both an improvement of the efficiency of message sends and valuable type information that can be reused to conduct by the compiler to produce other optimizations.

Smalltalk code is dynamically compiled and machine code is cached. Method lookup is responsible for a substantial part of the execution time. **Lookup caches** reduce the overhead by mapping (Receiver types - Message name) pairs to methods and holding to the most recently used result. **Inline caches** use the fact that the type of the receiver at a given call site rarely varies and caches the looked-up method address at the call site, overwriting the call instruction.

Polymorphic sends have to be handled differently because using a simple inline cache would result in a permanent overwriting of the method address (due to the changing type) and therefore an additional call to the expensive lookup method. 

Sends are either:

- ***Monomorphic:*** one receiver type (1)
- ***Polymorphic:*** a few receiver types (2-10)
- ***Megamorphic:*** a lot of receiver types (10+)

A ***PIC*** will cache ALL lookup results for a given polymorphic call-site in a specially-generated stub routine that looks like the following after few calls of the method on different receiver types:

```pseudocode
if type = type1:						   |  Check receiver type
	jump to method     ___________________ | _______________________
										   | Code to apply on type 1
										   
if type = type2:                           | Check receiver type
	jump to method     ___________________ | _______________________
										   | Code to apply on type 2
	
call lookup            ___________________ | Fallback: call expensive lookup
```

A ***PIC*** is therefore an *extensible cache with no cache in which no cache item is ever displaced by another (newer) item*.

Remaining problems and possible solutions:

- **Megamorphic sends handling:** The inline cache miss handler should not extend the ***PIC*** beyond a certain number of type cases. It should mark the call-site as megamorphic and adopt a fallback strategy.
- **Linear search improvement:** If the dynamic usage frequency of each type were available, ***PICs*** could be reordered periodically to move the most frequently occurring types on top.
- **Short methods inlining:** Many methods are very small (*e.g*. output one of the receiver's instance variable). Such methods could be integrated into the ***PIC*** directly rather than being called by it.
- **Space efficiency improvement:** If the system runs on tight space, call sites with identical message names could share a common ***PIC*** to reduce the space overhead.

---


### 1992 - Hoelzle, Debugging Optimized Code with Dynamic Deoptimization
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1994 - Hoelzle, Adaptive Optimization for SELF Reconciling High Performance with Exploratory Programming
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1995 - Click, A Simple Graph-Based Intermediate Representation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1995 - Dean, Optimization of Object-Oriented Programs Using Static Class Hierarchy Analysis
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1995 - Ertl, Stack Caching for Interpreters
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[15/12/2020]*

While interpreters are used for their *simplicity* and *portability*, the question of *performance* rises and along it the question of the stack vs register architecture.

The **interpretation of a virtual machine instruction** consists of three parts: (1) **access the arguments** of the instruction, (2) **perform the function** of the instruction and (3) **dispatch (fetch, decode and start) the next instruction**. The *first* and *third* parts constitute the interpreter overhead.

The most efficient method for fetching, decoding and starting the next instruction is **direct threading**: instructions are represented by the *addresses of the routine* that implements them, and *instruction dispatch consists of fetching that address and jumping to the routine*. However, direct threading cannot be implemented in ANSI C but are replaced by either a **giant switch** or **calls**. The overhead induced by the two methods is due to the [range check/table lookup/jump] routine of the *switch method* and the fact that every virtual machine register (instruction and stack pointers) have to be kept in global or static variables for the *call method*. In the *switch method*, the virtual registers can be kept as local variables.

If the instructions are of constant length, the **dispatch of the next instruction can be performed in parallel with the processing of the current instruction**.  In addition, the overhead can also be reduced by **reducing the number of primitives executed**, i.e. by *increasing the semantic content of each instruction*. Combining often-used instruction sequences into one instruction or specializing an instruction for a frequent constant argument are well-known techniques.

While on the hardware side the contest between stack and registers is won by registers, the discussion is different for interpreters. **Data flow analysis** to perform the best register allocation is expensive and the **spill** are much more time consuming than in hardware. Moreover, in hardware the register numbers are decoded in parallel whereas a simple software implementation has to fetch and/or decode the register numbers using separate instructions.

**If there are enough registers, the number of operands fetches and stores can  be reduced by keeping n top-of-the-stack values in registers**.

Mapping a constant number of items in registers is simple but unnecessary. It would be better to keep a *varying number of items in registers*, on an on-demand basis (like a **cache**).

Every allowed mapping of stack items to machine registers constitutes a **cache state**. Many stack pointer updates can be optimized: the cache state can hold the information on how much the contents of the stack pointer vary from the actual value of the stack pointer (this difference can correspond to the number of stack items in the cache). This means the stack pointer does not need to be updated when an instruction can access all stack items in registers.

There should be one state for every number of stack items in registers. The bottom of the cached stack items should be in all states and the other stack items allocated similarly. This avoids the need to move stack items around the bottom of the cache when something on the top changes. 





---


### 1995 - Gosling, Java Intermediate Bytecodes
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[06/01/2021]*

Java emerged from its divergences with C++ by using a compiler to generate byte coded machine independent instructions. While this type of method is usually unsuitable for higher-level manipulation, some twists are used: unusual amount of **type information**, **restrictions on the use of the operand stack** and heavy reliance on **symbolic references** and **on-the-fly code rewriting**. 

Instruction definitions follow this inductive property: *Given only the type state before the execution of the instruction, the type state afterwards is determined*.  Smalltalk or PostScript stack-based codes do not have this property. The main idea behind this specification is **simplicity**.

In conjunction, instructions follow the property: *When there are two execution paths into the same point, they must arrive there with exactly the same type state*. This means that bytecode generators cannot write loops that iterate through arrays copying each element on the stack. Since all paths to a point are required to arrive with the same type state, then the type state from any incoming path can be used to do further manipulations.

These restrictions allow a number of important consequences:

- **Static checkability**: The last phase of the bytecode loader is the **verifier**, it traverses the bytecode, constructs type state information and verifies the type parameters of all opcodes. Once the **verifier** finishes, it is guaranteed that: there are no operand stack overflows or underflows, the types of the parameters of opcodes is correct, no illegal data conversions are done and object field accesses are legal. It helps the interpreter and provides a secure environment (no pointer can be forged, access restrictions are enforced, etc.).
- **Fragile Superclasses**: Java uses symbolic references to answer the issue. For example, the `getfield` opcode does not use an offset into the object but rather an index into the symbol table. Once the class is loaded, the offset into the object does not change. When the `getfield` opcode is executed, the interpreter looks up the symbol, finds its offset then rewrites the instruction to be a quick `getfield` with the exact offset.
- **Portability**: Compiled programs are portable given the end device has an interpreter.
- **Translation to machine code**: The static nature of the type states enable simple on-the-fly translation of bytecodes into machine code (no dynamic checks or inferences).



A deterministic stack type-state restriction and a bytecode IR allow the bytecoded program to be compact then directly interpreted or translated to machine code. The implementation of these manipulations can be simple, fast and small.

---


### 1996 - Bacon, Fast Static Analysis of C Virtual Function Calls
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1997 - Agesen, Design and Implementation of PEp a Java Just-In-Time Translator
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1997 - Ingals, Back to the Future The Story of Squeak a Practical Smalltalk Written in Itself
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1997 - Kistler, Slim Binaries
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1998 - Piumarta, Optimizing Direct Threaded Code by Selective Inlining
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1998 - Taivalsaari, Implementing a Java Virtual Machine in the Java Programming Language
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1999 - Burke, The Jalapeno Dynamic Optimizing Compiler for Java
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1999 - Wolczko, Self Includes Smalltalk
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 1999 - Yoshihiko, Partial Evaluation of Computation Process an Approach to a Compiler-Compiler
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2000 - Arnold, Adaptive Optimization in the Jalapeno JVM
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2000 - Bala, Dynamo a Transparent Dynamic Optimisation System
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2000 - Diehl, Abstract Machines for Programming Language Implementation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2001 - Cheng, A Parallel Real-Time Garbage Collector
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2001 - Paleczny, The Java HotSpot Server Compiler
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2002 - Barbu, Application-Replay Attack on Java Cards When the Garbage Collector Gets Confused
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2002 - Click, Fast Subtype Checking in the HotSpot JVM
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2002 - Ertl, Vmgen a Generator of Efficient Virtual Machine Interpreters
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2003 - Dehnert, The Transmeta Code Morphing - Software Using Speculation recovery and Adaptive Retranslation to Address Real-Life Challenges
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2003 - Ertl, The Structure and Performance of Efficient Interpreters
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2003 - Fink, Design Implementation and Evaluation of Adaptive Recompilation with On-Stack Replacement
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2003 - Shaylor, A Java Virtual Machine Architecture for Very Small Devices
<!-- Please prefix the notes with the date as in [22/12/2020] -->

**The size of Java classfiles** has long been recognized as an issue, especially for embedded devices. Several methods exist to reduce the size, both as a transmission format and as an execution format. Some methods try to perturb the Java execution engine as little as possible while the **Java Card Paradigm introduces a muscular transformer between classfiles and interpreter.**

The project’s main goal of building a CLDC-compliant system on a small device led to a few straightforward consequent goals, namely *minimizing the size of transmitted classfiles*, the *RAM needed for classfile loading*, the *size of loaded classfiles*, the *RAM required during execution*, and the *size of the interpreter and memory system*.

These goals are then translated in design choices:

- Standard CLDC classfiles are too large and complex. Using a **Java Card** technique, they are **preprocessed off-device** and packaged in a smaller representation (*suite*) that can be verified and loaded on-device.
- The **classfile preprocesor** identifies code snippets that are hard to verify or garbage collect and translates them into simpler versions
- Standard classfiles contain symbolic information for resolving references. **References are now resolved before execution**, either during off-device translation or during the installation of suites on the device.
- Standard construction and **object initialization is recasted** into an equivalent form that can be verified more efficiently
- Three memory spaces are available with different characteristics. A **region-aware memory manager** is therefore used.



Bytecode verification and exact garbage collection are complex on small devices, especially due to the fact that pointers are hard to find and track. While CLDC added a classfile attribute called a *stackmap*, it is too complex and memory intensive. Specific restrictions are added to the translator and applied when the conversion from classfiles to *suites* is performed:

- **A local variable can only hold one type**
- **The evaluation stack must be empty at the end of a basic block**
- **Bytecodes that can trigger a GC may only be executed when the evaluation stack contains only the operands for those bytecodes**



A compact bytecode set is used with **reduced operand field sizes** that can then be extended (8 bits by default but that can be extended to 12, 16 or 32). Local variables are explicitly typed so **no type-specific load and store are needed**. Symbolic references (through a name string rather than an index or pointer) are **resolved as much as possible** when they are written into the memory of the target device **during loading**. A **field access** can be resolved to an **absolute offset within an object**, a **method invocation** to an **offset in a vtable**. Simple two-pass verification process. First step reads the bytecode and verifies **type safety**, **class member references** and writes them in NVM. Second pass checks the **branch targets** are valid.

Standard Java object construction creates an *uninitialized* object and then fills it up. Squawk does not expose uninitialized object references to the bytecode. The **object method constructor creates the object and returns the address of the newly created object**. A *null* flag is used as the first parameter. A constructor will allocate an object and replace the first parameter only if that parameter is *null*.



**Memory:**

- Three memory spaces: *RAM*, *NVM* and *ROM*. Objects in less permanent memory are allowed to contain references to objets in more permanent memory but not the other way around.
- *Chunky stack* composed of chunks allocated in the *RAM heap*. Each chunk is a Java object and can be GC'd.
- Class definition information is divided into *immutable* and *mutable*. All objects have a one-word header pointing to the immutable class information for that object.
- *Object monitors* are used to implement synchronization. The monitors are placed in an LRU queue in RAM. All monitors keep a reference to their corresponding objects.

**Implementation:**

- *Methods* are *byte arrays*
- Every class contains a *reference to a byte array that contains an object pointer map* used by the GC
- A class state record is the mutable part of a class definition, it contains the object reference fields and the integer fields used to hold the static variables of the class. The class state records are kept in an LRU queue in the RAM.

Garbage collection is performed when the `interpret` method fails and outputs an `OutOfMemory` error. The `gc()` method is only called when it fails to allocate a stack chunk, when it fails to allocate an object or when it is explicitly called:

```java
for (;;) {
	interpret(result);
	result = gc();
}
```





---


### 2004 - Blackburn, Oil and Water High Performance Garbage Collection in Java with MMTk
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2004 - Chambers, A Retrospective on Customization Optimizing Compiler Technology for SELF a Dynamically-Typed Object-Oriented Programming Language
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2004 - Ertl, Combining Stack Caching with Dynamic Superinstructions
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2004 - Sachindran, MC2 High-Performance Garbage Collection for Memory-Constrained Environments
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2005 - Click, The Pauseless GC Algorithm
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2005 - Ertl, Advances in Interpreters Virtual Machines and Emulators
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2005 - Faes, FPGA-Aware Garbage Collection in Java
<!-- Please prefix the notes with the date as in "[22/12/2020]:" -->

*[08/12/2020]:*

This paper presents a virtual machine, based on the *Jikes Research Virtual Machine* (Jalapeno), that is able to bridge the gap by providing the same capabilities to hardware components as to software components. This integration is achieved by introducing an **architecture and protocol that allow reconfigurable hardware and software to communicate with each other in a transparent manner *i.e.* no component of the design needs to be aware whether other components are implemented in hardware or in software.** It also allows reconfigurable hardware to manage dynamically allocated memory.

Granting the same capabilities to HW as SW with regard to object references highlights three advantages:

- The number of HW registers can be limited. Instead of passing a large number of parameters, a reference to an object that contains the required data can be provided.
- Neither the HW or SW needs to know in what type of memory the object actually resides. The JVM runtime can implement heuristics that place data closer to the computing unit that is likely to use it in the near future.
- Calling a method, whether it is implemented in SW or HW is completely transparent. This allows a HW method to perform the same operations as a SW method, call methods of any of its arguments or pass them on to other methods.



**Architecture:** The reconfigurable computing device is modeled as a *shared memory machine.* *The address space of the HW is mapped into the address space of the JVM.* This way, the *JVM can access memory and control the registers of the HW* while the *HW can access the JVM's heap through Direct Memory Access.*

**Protocol:** A region is used for *garbage collection* and has a one-to-one mapping to the internal RAM for object references. *Method parameters* and *return values* are mapped arbitrarily onto addresses in the internal RAM for primitive datatypes or the internal RAM itself for object references. The rest of the addresses are *control registers* and are not mapped onto RAM but are either ignored or directly connected to HW registers.

*USE CASE FROM THE PAPER IS A GOOD SUMMARY*

***Garbage-Collector:*** The runtime system collects unused objects in the heap by conducting a liveness check (through an *object-reference graph*) and compacting the resulting memory to create a contiguous region of unused memory. This type of GC is called "stop-the-world". 

The GC in the HW/SW system needs to send a *pause* signal to each HW entity and then *resume* them once finished. This can be done because the GC has access to a list of all available HW entities (note that pausing is required so that no reference is changed, primitive computation can continue). The object references on the HW side can either be in the RAM (that is directly mapped to the garbage collector region) or hidden and fragmented in many different small RAMs or in registers. When a pause is requested, the HW needs to expose those regions by copying them into the GC region. 



***Results:*** Impact of GC is limited to an additional 2.32% execution time 

 



---


### 2005 - Ungar, Constructing a Metacircular Virtual Machine in an Exploratory Programming Environment
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2006 - Gal, HotpathVM An Effective JIT Compiler for Resource-Constrained Devices
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2006 - Rigo, PyPys Approach to Virtual Machine Construction
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2006 - Russell, Eliminating Synchronization-Related Atomic Operations with Biased Locking and Bulk Rebiasing
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2008 - Kotzmann, Design of the Java HotSpot Client Compiler for Java 6
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2009 - Bolz, Tracing the Meta-Level PyPys Tracing JIT Compiler
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2009 - Frampton, Demystifying Magic High-Level Low-Level Programming
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2010 - Agesen, The Evolution of an X86 Virtual Machine Monitor
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2010 - Rizzo, Practical Padding Oracle Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2011 - Bolz, Runtime Feedback in a Meta-Tracing JIT for Efficient Dynamic Languages
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2012 - Rohou, Tiptop Hardware Performance Counters for the Masses
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2012 - Wuerthinger, Self-optimizing AST interpreters
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2013 - Eckert, Hardware Based Security Enhanced Direct Memory Access
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[15/12/2020]*

Prevention against **Direct Memory Access (DMA)** attacks adding a **watchdog mechanism** that scans the data passing by and interrupts the processor after the detection of a malicious data or instruction sequence.

*REFERENCES TO OTHER ARTICLES IN THE FIELD OF PROCESSOR SECURITY*

[1] Chhabra et al., *An analysis of secure processor architectures*

[2] Wang et al., *Computer Architecture and Security: Fundamentals of Designing Secure Computer Systems*



DMA is a well-known technique to release processors from time consuming workload caused by simple data transfers. **Those transfers are performed without supervision**. Data and instruction are communicated between the memory as sink and source or between the memory and mass storage or interfaces. They reach their destination block-wise without completely before being checked by anti-malware agents. To complete the success of a DMA attack, **the attack pattern needs to launch the code before it has been checked** by the anti-malware agent. Another opportunity is to infect the **anti-malware** software directly.

The introduction of a **DMA-watchdog** can solve the issue. The watchdog resides between the *DMA-Controller* and the *Memory Controller*. It supervises the data part of the memory-bus with a number of sensors that provide a pattern matching functionality to identify malware. If one of the sensors is matching, it signals the watchdog that will, in turn, block the current DMA-transfer. The pattern matching is performed in parallel.

*PRHS (Partially Reconfigurable Heterogeneous System)* framework used to deploy the project on FPGA. 

*DESCRIPTION AND FIGURE*

**Proof-of-concept**: A DMA Simulator is added to the secondary data bus of the system and to the RAM via an SD-Arbiter. Its task is to *copy the content of internal Block-RAM (8KiB) to a given RAM address*. It does not take additional CPU time as it is completely independent.



---


### 2013 - Kulkarni, Automatic Construction of Inlining Heuristics using Machine Learning
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2013 - Wimmer, Maxine an Approachable Virtual Machine for and in Java
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2013 - Wuerthinger, One VM to Rule Them All
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2014 - Duboscq, Speculation Without Regret Reducing Deoptimization Meta-data in the Graal Compiler
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2014 - Eckert, FPGA-Based System Virtual Machines
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2014 - Freundenberg, SqueakJS a Modern and Practical Smalltalk that Runs in any Browser
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2014 - Humer, A Domain-Specific Language for Building Self-Optimizing AST Interpreters
<!-- Please prefix the notes with the date as in [22/12/2020] -->



*[15/12/2020]*

Presentation of **Truffle DSL**, where a *guest VM* runs on top of a *host VM*. The *guest language* is the language we want to implement an application in while the *host language* is the language the *guest VM* is written in. 

The *guest language*  implementation is written as an abstract tree interpreter. The ability to replace one AST node with another is a key aspect of **Truffle**. The executed AST is improved at runtime by replacing nodes by more specialized ones based on profiling feedback. This specialized node makes *assumptions* about its operands for future executions. The implementation of the execution semantics *checks that all assumptions still hold then performs the operation*. If the assumptions do not hold, it replaces itself with a more generic version of the same node.

A dynamic compiler speculates the AST is stable (no node rewriting) and it compiles the interpreter `execute` method of the root node then recursively inlines the `execute` methods of all children. Speculation failures are handled using *deoptimization*, the compiled code is discarded and execution continues in the AST interpreter.

**Node Rewriting:** If a node cannot handle an operation, it replaces itself and lets the new node handle the input. The node replacement depends on (1) **Completeness**, it must provide rewrites for *all* cases that it does not handle itself and (2) **Finiteness**, after a finite number of node replacements, the operation must end up in a state that handles the full semantics without further rewrites. Before a node is executed, its state is *uninitialized*. If no specialization is found its state is *generic*.

**Express Specializations:** Separate the full semantics of an operation into multiple specializations helps encapsulating behavior and allows the compiler to write small and fast machine code. The implementation of a specialization consists of two parts: (1) **Checks that all inputs are as expected** and performs **node rewriting if not** (2) **Performs the actual operation**. If an operation works for a given specialization on all occurrences, it is a *monomorphic call*. If it varies between different inputs, we cannot change the node every now and then since it would violate the *finiteness principle*. A *Polymorphic node* is needed. This polymorphic call is represented by a node containing all encountered types.

*EXAMPLES RUN THROUGH THE TRUFFLE SYNTAX AND PRESENT ITS ANNOTATIONS*

**Truffle DSL** designed following three principles: (1) Declarative (2) Facilitate Optimizations (3) Interoperability. The DSL elements are Java annotations on classes and methods. The classes are used for two different kinds of DSL root elements. The specialization mechanism is used through *guards*. Guards can be applied as *type guards* that assume the type of a child value, *method guards* that assume the return value of a user-defined to be `true` or *event guards* in case an exception is thrown in the specialization body.

Several optimizations are enabled: 

- **Type check Elimination:** A node may ask a child node to return its data with a specific type by assigning a static type to the return value. This way, either the type is correct or an exception containing the resulting type is produced if the type is not correct.
- **Specialization Reduction:** As soon as an operation gets polymorphic, it is worthwhile to evaluate if a single more generic specialization leads to better code than a chain of monomorphic specializations. The `cost` option of specializations can be used to choose to replace with a more generic option. It is obtained from the sum of all specializations' `costs`.
- **Guard Reduction:** Types and method guards are executed while the polymorphic chain of specializations is traversed. These guards are represented with constant boolean values and an `@Implies` annotation is used to prove that a Java guard method implies another.



---


### 2014 - Seaton, Debugging at Full Speed
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2014 - Stadler, Partial Escape Analysis and Scalar Replacement for Java
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2014 - Woss, An Object Storage Model for the Truffle Language Implementation Framework
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Gosling, The Java 8 Language Specification
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Grimmer, Dynamically Composing Languages in a Modular Way Supporting C Extensions for Dynamic Languages
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Gunadi, Formal Certification of Android Bytecode
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Hussein, Impact of GC Design on Power and Performance for Android
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Lindholm, The JVM 8 Specification
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Rohou, Branch Prediction and the Performance of Interpreters Dont Trust Folklore
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Simon, Snippets Taking the High Road to a Low Level
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - VanDeVanter, Building Debuggers and Other Tools We Can Have it All
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2017 - Pedersen, From Trash to Treasure Timing-Sensitive Garbage
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2018 - Lipp, Meltdown Reading Kernel Memory from User Space
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2018 - Wu, A Side-channel Attack on HotSpot Heap Management
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[13/01/2021]*

**CPU time-multiplexing** is a common practice in multitenant systems to improve system utilization. However, the sharing of CPU and a single system clock makes it difficult for programs to accurately measure the length of an operation. **Applications employing time-based resource management face a potential security threat of time manipulation** (through dilation). 

HotSpot (JVM) relies on timing **garbage-collections to infer a heap size**. A side-channel attack exploits time dilation to break the heap sizing algorithm and causes any program to raise an out-of-memory error. It can be configured with an initial `-Xms` and maximal `-Xmx` heap size. during runtime, the JVM adjusts the size based on statistics from GC. In general, the heap is **shrunk** if each individual GC takes too long and **violates a user-defined pause-time target**. It is also **expanded** if GC is frequently performed and the total GC time constitutes a significant portion of the total execution time (**violates throughput target**). If **both targets** are met, the JVM **gradually shrinks the heap to save memory**. Most Java heap sizing algorithm use measured GC time, which is based on **wall-clock time**.

**Adaptive-sizing in Parallel-Scavenge (PS):** Stop-the-world throughput-oriented algorithm that uses multiple GC threads to scan the heap and is expected to meet two goals, **pause-time** and **throughput** that are both user-defined. PS divides the heap into multiple generations: *young, old* and *metaspace*. The *young* space is divided into one *eden* and two survivor spaces, the *from-space* and the *to-space*. New objects are put in the *eden* which, once filled, will perform a minor GC where referenced objects from the *eden* and *from-space* are moved to the *to-space*. The *eden* and *from-space* are then cleared and object in the *to-space* get their age increased. After surviving several generations, the objects in the *to-space* are moved in the *old* generation. 

**An Out-of-Memory (OOM)** error occurs when the JVM does not have space to allocate a new object in the heap. The PS algorithm tries to allocate an object in 5 tries before raising the error: (1) minor GC on young generation, (2) major GC in old and move mature objects from young to old, (3) allocate directly in the old generation, (4) major GC with soft references in the young generation and (5) another try to allocate directly in the old generation.

The GC cost is a metric used in adaptive heap sizing. The cost of a particular GC (major or minor) corresponds to the *time of the GC* / *(time since last GC + time of the GC)*. Note that it might include the time spent in another GC. All time measurement are based on wall-clock time (`gettimeofday`). Several adjustment mechanisms exist for each of the different spaces and given a main goal (pause-time or throughput).

**Time Dilation in Multi-tenant Systems:** The *Time-stamp Counter* is commonly used for timekeeping as it is an **auto-incremented register on CPU at the clock rate**. Timing utilities such as `gettimeofday` use this register to keep track of time. Leaving the control of time keeping utilities to an external tool can allow other programs to run between the meantime and dilate the time spent performing an action.



---


### 2019 - Kocher, Spectre Attacks Exploiting Speculative Execution
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2019 - Patel, Runtime-Programmable Pipelines for Model Checkers on FPGAs
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[08/12/2020]*

Design of an efficient *instruction-driven runtime-programmable pipeline for model checkers*. This pipeline replaces the model-specific pipeline found in prior works that hardwire the target model in FPGA logic. High-throughput model checking without requiring synthesis and place-and-route on every model change.

*FIGURE 1 PRESENTS THE EXPLICIT STATE MODEL CHECKING PROCESSING FLOW*

The model checker needs to be (1) Fast in execution time (2) Fast in preparation time. In order to answer (1), the**FPGASwarm Verification Methodology**  has been chosen. To answer (2), an **instruction-driven runtime-programmable pipeline for the successor state generator and the state validator, which support checking different models without RTL changes.**

To obtain high throughput, each **pipeline must have access to its own BRAMs containing a copy of the instructions**. The throughput of the Swarm-based FPGA model is **bound by the BRAM capacity**, a key consideration is to **minimize the footprint of the instruction memory**.



***Pipeline for the Successor State Generator:*** Each stage takes a different slice of the instruction as its control bits.

- **Instruction Fetch**: On each cycle, a state vector (along with a PID and ND value) is pushed on the pipeline to generate one successor state. The PID is used to get the PC out of the state vector. The address of instruction is obtained out of the concatenation of the PID, ND and PC values.

- **Variable Selection and Constants**: The first slice of the instruction bits is used to load values from the state vector with the address encoded in the instruction, constants are obtained as immediate values.

- **Pipeline Registers**: The pipeline registers between the variable selection stage and the final store stage have a specific arrangement. For the first one there are M registers (number of value selection units), followed by N registers (immediate values from the instruction), then several registers for storing temporary values between the multiple execution stages.

- **Execute Stages**: Computation is performed by a series of execute stages, each having several parallel ALUs. The number of ALUs should be correctly sized to accommodate the target model

  Each ALU has two operands and one output. The first one is fixed and the second is freely selected from the preceding state registers and four read-only constants: *PID, NUMPROC, value 1 and value 0*. Each ALU output is restricted to be stored in one of two possible locations. Not all ALUs need to load and two types of ALUs are developed: *Normal ALU* and *Load ALU*. A 4-bit OP field corresponds to one of the 16 operations available.

- **Permutation Stage**: The permutation stage sets up appropriate registers for the store unit by moving the calculated values from the execute stages to the correct location for the store unit to use.

- **Store Stage and PC Updating**: the store stage comprises several store units to update variables in the state vector. Each store unit has three inputs from the previous stage: *condition, value and index*. If the *condition* is non-0, the variable in the state vector with position *base + index* becomes *value*.

**Pipeline for the State Validator**: All state vectors require the same validation checks. No need for separate instructions for each PID-ND-PC combination. The final output of the validator pipeline is a single value, selected from a register in the last execution stage, which indicates whether or not the input state is a **model violation**. Note that the **validator DOES NOT consume BRAMs** as it has no instruction memory footprint.



---


### 2019 - Schwarz, ZombieLoad Cross-Privilege-Boundary Data Sampling
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2019 - Varoumas, High-level programming models for microcontrollers with scarce resources
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2020 - Fournier, Menhir Generic High-Speed FPGA Model-Checker
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[08/12/2020]*

Menhir is a modular hardware model-checker. Menhir decouples the verification core from the modeling language semantics by introducing a generic language-agnostic verification interface (**GLI**). Menhir provides a *polymorphic verification core*. It offers a **pure hardware configuration** (VHDL-based GLI-specific modeling language) as well as a **system-on-chip (SoC) configuration** (existing software implementation of the modeling language). Two system specification are handled, **DVE** as well as **EMI** and six verification algorithms.

**Explicit state online model checking for regular safety specifications.**

The verification algorithm is built upon a model. The model is represented as follows:

```pseudocode
structure M (C: Type) :=
	(initial : set C)
	(next    : C -> set C)
	(is_safe : C -> bool)
```

where `M` is the model over an arbitrary configuration `C`. `initial` is the set of the initial configurations, `next` outputs a set of configurations given a specific one and `is_safe` checks that a given configuration is safe. 



The verification algorithm itself is presented as follows:

``` pseudocode
def safety_checker (m: M) : bool :=
	K <- {}
	F <- {}
	N <- m.initial
	do
		if there is n in N such as not(m.is_safe(n)) 
			then return false
		K, F <- KuN, N\K
	while not(F is empty)
	return true
```

where `K` is the known set and `F` the frontier. `K` stores the states encountered while `F` only stores the configurations discovered recently that HAVE NOT yet been processed. The algorithm starts by populating the `N` set with the initial states. The states in the `N` set are checked for safety and the next states are added to `F` and `K`.  If an unsafe configuration is found, the algorithm stops.

*LOOK AT FIGURE 1 FOR ARCHITECTURE OVERVIEW*

Model-checker organized in two parametric layers: ***Model Frontend*** containing *Next State Generator* and *Invariant Checker* and ***Storage Backend*** that contains the *Frontier FIFO* and *Known Set*. Between the two parts is the **GLI** which mediates the dialogue from the *Frontend* to the *Controller*. The *Controller* itself is composed of the *Next Controller* (access to the **GLI**),  the *Scheduler* (forwards the newly discovered configurations) and the *Termination Checker* (monitors the progression). 

The call to `is_safe` is inlined into the `next` instruction to reduce the call cost. 

*LOOK AT FIGURE 2 FOR GLI SPECS*

*LOOK AT FIGURE 3 FOR ALGORITHM POSSIBILITIES*



---


### 2020 - Lima, Exposing Bugs in JavaScript Engines through Test Transplantation and Differential Testing
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2020 - Zandberg, Minimal Virtual Machines on IoT Microcontrollers The Case of Berkeley Packet Filters with rBPF
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[15/12/2020]*

Enhancing the security of low-power low-memory devices can take the form of **process isolation**. This isolation can be conducted either:

	- By isolating **high-level business** logic, updatable on-demand remotely over the low-power network *(long-lived, non-real-time timing requirements)*
	- By isolating **debug/monitoring** code snippets at low-level, inserted and removed on-demand, remotely over the network *(short-lived, strict timing requirements)*

Concretely performing the isolation can be performed through a *modification of the hardware architecture* to add mechanisms to guarantee process isolation. This is the path taken by the **TrustZone on Arm Cortex-M**, **Sanctum on RISC-V** or **Sancus2.0 on MSP430**.

On the other hand, software-only equivalent can be achieved to perform process isolation:

-  **Small VMs:** *Darjeeling*, a subset of the JVM using a 16-bit architectures. *Wasm*, a VM specification designed for process isolation in web browsers. *JavaCard*, a small JVM running on smart cards. *eBPF* small VM hosting and isolating debug and inspection code in the Linux kernel at runtime.
- **Scripted Logic Interpreters:** *Small JavaScript run-time container* hosting business logic interpreted aboard a microcontroller, glued atop a real-time OS (*RIOT*).
- **OS-Level Mechanisms:** *Tock* is an OS written in Rust that offers strong isolation between its kernel and application logic processes. However it requires a memory protection unit (MPU).



Comparison of two VMs:

- **WebAssembly (Wasm):** Stack-based VM that uses a heap and memory allocations in chunks of 64KiB (pages). Wasm uses the LLVM compiler and once  binary is created, it is transferred to the IoT device on which it is interpreted and executed. Several interpreters exist and WASM3, for example, transpiles the loaded application to an optimized executable that can then be executed in the interpreter.
- **Extended Berkeley Packet Filters (eBPF):** Small in-kernel VM available on Unix-like OS. Original purpose was packet filtering but got rebranded to other purposes. 64-bit register-based VM with a fixed 512B stack. No heap is presented in the specification but an interface to key-value maps is used as an alternative for persistent storage between invocations.



Design of **rBPF**, a variant of the eBPF VM designed to be ISA-compatible. It extends the bindings to be able to access the OS facilities and events. The VM is integrated in the **RIOT OS** and scheduled as a regular thread. The VM can interact with multiple OS event sources. Tehe VM is based on an iterative loop design over the application instructions. Depending on the instruction, **different protection mechanisms are activated**. (1) Host address space isolated from the sandbox by policies loaded in the VM. (2) Protections on the code executed ensure the VM does not start executing code outside the supplied application. Note that the eBPF ISA *does not support indirect jump instructions and no pc register is available*. This means the virtual program counter can only be modified via the guarded direct branch and jump instructions.



VM adds overhead that has an impact on execution time and a measurable additional size. While the Wasm VM requires too much RAM and ROM, rBPF looks like a good compromise between security through process isolation and memory and time overhead.

---


