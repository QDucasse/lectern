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

[1987 - Cointe, Metaclasses are First Class the ObjVlisp Model ](#1987---Cointe-Metaclasses-are-First-Class-the-ObjVlisp-Model-)

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

[2002 - Click, Fast Subtype Checking in the HotSpot JVM](#2002---Click-Fast-Subtype-Checking-in-the-HotSpot-JVM)

[2002 - Ertl, Vmgen a Generator of Efficient Virtual Machine Interpreters](#2002---Ertl-Vmgen-a-Generator-of-Efficient-Virtual-Machine-Interpreters)

[2003 - Dehnert, The Transmeta Code Morphing - Software Using Speculation recovery and Adaptive Retranslation to Address Real-Life Challenges](#2003---Dehnert-The-Transmeta-Code-Morphing---Software-Using-Speculation-recovery-and-Adaptive-Retranslation-to-Address-Real-Life-Challenges)

[2003 - Ertl, The Structure and Performance of Efficient Interpreters](#2003---Ertl-The-Structure-and-Performance-of-Efficient-Interpreters)

[2003 - Fink, Design Implementation and Evaluation of Adaptive Recompilation with On-Stack Replacement](#2003---Fink-Design-Implementation-and-Evaluation-of-Adaptive-Recompilation-with-On-Stack-Replacement)

[2003 - Govindavajhala, Using Memory Errors to Attack a Virtual Machine](#2003---Govindavajhala-Using-Memory-Errors-to-Attack-a-Virtual-Machine)

[2003 - Shaylor, A Java Virtual Machine Architecture for Very Small Devices](#2003---Shaylor-A-Java-Virtual-Machine-Architecture-for-Very-Small-Devices)

[2004 - Blackburn, Oil and Water High Performance Garbage Collection in Java with MMTk](#2004---Blackburn-Oil-and-Water-High-Performance-Garbage-Collection-in-Java-with-MMTk)

[2004 - Chambers, A Retrospective on Customization Optimizing Compiler Technology for SELF a Dynamically-Typed Object-Oriented Programming Language](#2004---Chambers-A-Retrospective-on-Customization-Optimizing-Compiler-Technology-for-SELF-a-Dynamically-Typed-Object-Oriented-Programming-Language)

[2004 - Ertl, Combining Stack Caching with Dynamic Superinstructions](#2004---Ertl-Combining-Stack-Caching-with-Dynamic-Superinstructions)

[2004 - Sachindran, MC2 High-Performance Garbage Collection for Memory-Constrained Environments](#2004---Sachindran-MC2-High-Performance-Garbage-Collection-for-Memory-Constrained-Environments)

[2005 - Click, The Pauseless GC Algorithm](#2005---Click-The-Pauseless-GC-Algorithm)

[2005 - Ertl, Advances in Interpreters Virtual Machines and Emulators](#2005---Ertl-Advances-in-Interpreters-Virtual-Machines-and-Emulators)

[2005 - Faes, FPGA-Aware Garbage Collection in Java](#2005---Faes-FPGA-Aware-Garbage-Collection-in-Java)

[2005 - Ierusalimschy, The Implementation of LUA5](#2005---Ierusalimschy-The-Implementation-of-LUA5)

[2005 - Ungar, Constructing a Metacircular Virtual Machine in an Exploratory Programming Environment](#2005---Ungar-Constructing-a-Metacircular-Virtual-Machine-in-an-Exploratory-Programming-Environment)

[2006 - Gal, HotpathVM An Effective JIT Compiler for Resource-Constrained Devices](#2006---Gal-HotpathVM-An-Effective-JIT-Compiler-for-Resource-Constrained-Devices)

[2006 - Leroy, Formal Certification of a Compiler Backend](#2006---Leroy-Formal-Certification-of-a-Compiler-Backend)

[2006 - Piumarta, Open extensible object models](#2006---Piumarta-Open-extensible-object-models)

[2006 - Rigo, PyPys Approach to Virtual Machine Construction](#2006---Rigo-PyPys-Approach-to-Virtual-Machine-Construction)

[2006 - Russell, Eliminating Synchronization-Related Atomic Operations with Biased Locking and Bulk Rebiasing](#2006---Russell-Eliminating-Synchronization-Related-Atomic-Operations-with-Biased-Locking-and-Bulk-Rebiasing)

[2008 - Fuess, An FPGA Implementation of Explicit-State Model Checking](#2008---Fuess-An-FPGA-Implementation-of-Explicit-State-Model-Checking)

[2008 - Kotzmann, Design of the Java HotSpot Client Compiler for Java 6](#2008---Kotzmann-Design-of-the-Java-HotSpot-Client-Compiler-for-Java-6)

[2009 - Bolz, Tracing the Meta-Level PyPys Tracing JIT Compiler](#2009---Bolz-Tracing-the-Meta-Level-PyPys-Tracing-JIT-Compiler)

[2009 - Frampton, Demystifying Magic High-Level Low-Level Programming](#2009---Frampton-Demystifying-Magic-High-Level-Low-Level-Programming)

[2010 - Agesen, The Evolution of an X86 Virtual Machine Monitor](#2010---Agesen-The-Evolution-of-an-X86-Virtual-Machine-Monitor)

[2010 - Blazakis, Interpreter Exploitation Pointer Inference and JIT Spraying](#2010---Blazakis-Interpreter-Exploitation-Pointer-Inference-and-JIT-Spraying)

[2010 - Ehringer, The Dalvik Virtual Machine Architecture](#2010---Ehringer-The-Dalvik-Virtual-Machine-Architecture)

[2010 - Onarlioglu, G-Free](#2010---Onarlioglu-G-Free)

[2010 - Reynolds, Lightweight Modeling of Java Virtual Machine](#2010---Reynolds-Lightweight-Modeling-of-Java-Virtual-Machine)

[2010 - Rizzo, Practical Padding Oracle Attacks](#2010---Rizzo-Practical-Padding-Oracle-Attacks)

[2010 - Siefers, Robusta Taming the Native Beast of the JVM](#2010---Siefers-Robusta-Taming-the-Native-Beast-of-the-JVM)

[2010 - Sintsov, Writing JIT Spray Shellcode for Fun and Profit](#2010---Sintsov-Writing-JIT-Spray-Shellcode-for-Fun-and-Profit)

[2011 - Bolz, Runtime Feedback in a Meta-Tracing JIT for Efficient Dynamic Languages](#2011---Bolz-Runtime-Feedback-in-a-Meta-Tracing-JIT-for-Efficient-Dynamic-Languages)

[2011 - Chen, JITDefender A Defense against JIT Spraying Attacks](#2011---Chen-JITDefender-A-Defense-against-JIT-Spraying-Attacks)

[2011 - Haupt, CSOMPL a virtual machine product line](#2011---Haupt-CSOMPL-a-virtual-machine-product-line)

[2012 - Barbu, Application-Replay Attack on Java Cards When the Garbage Collector Gets Confused](#2012---Barbu-Application-Replay-Attack-on-Java-Cards-When-the-Garbage-Collector-Gets-Confused)

[2012 - Rohou, Tiptop Hardware Performance Counters for the Masses](#2012---Rohou-Tiptop-Hardware-Performance-Counters-for-the-Masses)

[2012 - Wuerthinger, Self-optimizing AST interpreters](#2012---Wuerthinger-Self-optimizing-AST-interpreters)

[2013 - Chen, JITSafe a Framework Against Just-In-Time Spraying Attacks](#2013---Chen-JITSafe-a-Framework-Against-Just-In-Time-Spraying-Attacks)

[2013 - Eckert, Hardware Based Security Enhanced Direct Memory Access](#2013---Eckert-Hardware-Based-Security-Enhanced-Direct-Memory-Access)

[2013 - Fournet, Fully Abstract Compilation to Javascript](#2013---Fournet-Fully-Abstract-Compilation-to-Javascript)

[2013 - Kulkarni, Automatic Construction of Inlining Heuristics using Machine Learning](#2013---Kulkarni-Automatic-Construction-of-Inlining-Heuristics-using-Machine-Learning)

[2013 - Marr, Supporting Concurrency Abstractions in High-level Language Virtual Machines](#2013---Marr-Supporting-Concurrency-Abstractions-in-High-level-Language-Virtual-Machines)

[2013 - Snow, Just-In-Time Code Reuse On the Effectiveness of Fine-Grained Address Space Layout Randomization](#2013---Snow-Just-In-Time-Code-Reuse-On-the-Effectiveness-of-Fine-Grained-Address-Space-Layout-Randomization)

[2013 - Wimmer, Maxine an Approachable Virtual Machine for and in Java](#2013---Wimmer-Maxine-an-Approachable-Virtual-Machine-for-and-in-Java)

[2013 - Wuerthinger, One VM to Rule Them All](#2013---Wuerthinger-One-VM-to-Rule-Them-All)

[2014 - Backes, Oxymoron Making Fine-Grained Memory Randomization Practical by Allowing Code Sharing](#2014---Backes-Oxymoron-Making-Fine-Grained-Memory-Randomization-Practical-by-Allowing-Code-Sharing)

[2014 - Duboscq, Speculation Without Regret Reducing Deoptimization Meta-data in the Graal Compiler](#2014---Duboscq-Speculation-Without-Regret-Reducing-Deoptimization-Meta-data-in-the-Graal-Compiler)

[2014 - Eckert, FPGA-Based System Virtual Machines](#2014---Eckert-FPGA-Based-System-Virtual-Machines)

[2014 - Freundenberg, SqueakJS a Modern and Practical Smalltalk that Runs in any Browser](#2014---Freundenberg-SqueakJS-a-Modern-and-Practical-Smalltalk-that-Runs-in-any-Browser)

[2014 - Humer, A Domain-Specific Language for Building Self-Optimizing AST Interpreters](#2014---Humer-A-Domain-Specific-Language-for-Building-Self-Optimizing-AST-Interpreters)

[2014 - Jain, Sok Introspections on Trust and the Semantic Gap](#2014---Jain-Sok-Introspections-on-Trust-and-the-Semantic-Gap)

[2014 - Lin, A Security PaaS Container with a Customized JVM](#2014---Lin-A-Security-PaaS-Container-with-a-Customized-JVM)

[2014 - Niu, RockJIT Securing Just-In-Time Compilation Using Modular Control-Flow Integrity](#2014---Niu-RockJIT-Securing-Just-In-Time-Compilation-Using-Modular-Control-Flow-Integrity)

[2014 - Seaton, Debugging at Full Speed](#2014---Seaton-Debugging-at-Full-Speed)

[2014 - Stadler, Partial Escape Analysis and Scalar Replacement for Java](#2014---Stadler-Partial-Escape-Analysis-and-Scalar-Replacement-for-Java)

[2014 - Woss, An Object Storage Model for the Truffle Language Implementation Framework](#2014---Woss-An-Object-Storage-Model-for-the-Truffle-Language-Implementation-Framework)

[2015 - Athanasakis, The Devil is in the Constants Bypassing Defenses](#2015---Athanasakis-The-Devil-is-in-the-Constants-Bypassing-Defenses)

[2015 - Grimmer, Dynamically Composing Languages in a Modular Way Supporting C Extensions for Dynamic Languages](#2015---Grimmer-Dynamically-Composing-Languages-in-a-Modular-Way-Supporting-C-Extensions-for-Dynamic-Languages)

[2015 - Gunadi, Formal Certification of Android Bytecode](#2015---Gunadi-Formal-Certification-of-Android-Bytecode)

[2015 - Hussein, Impact of GC Design on Power and Performance for Android](#2015---Hussein-Impact-of-GC-Design-on-Power-and-Performance-for-Android)

[2015 - Lam, Numba](#2015---Lam-Numba)

[2015 - Lian, Too LeJIT to Quit Extending JIT Spraying to ARM](#2015---Lian-Too-LeJIT-to-Quit-Extending-JIT-Spraying-to-ARM)

[2015 - Rohou, Branch Prediction and the Performance of Interpreters Dont Trust Folklore](#2015---Rohou-Branch-Prediction-and-the-Performance-of-Interpreters-Dont-Trust-Folklore)

[2015 - Simon, Snippets Taking the High Road to a Low Level](#2015---Simon-Snippets-Taking-the-High-Road-to-a-Low-Level)

[2015 - Song, Exploiting and Protecting Dynamic Code Generation](#2015---Song-Exploiting-and-Protecting-Dynamic-Code-Generation)

[2015 - VanDeVanter, Building Debuggers and Other Tools We Can Have it All](#2015---VanDeVanter-Building-Debuggers-and-Other-Tools-We-Can-Have-it-All)

[2016 - Lin, Rust as a Language for High Performance GC Implementation](#2016---Lin-Rust-as-a-Language-for-High-Performance-GC-Implementation)

[2016 - Maas, Grail Quest A New Proposal for Hardware-assisted Garbage Collection](#2016---Maas-Grail-Quest-A-New-Proposal-for-Hardware-assisted-Garbage-Collection)

[2017 - Frassetto, JITGuard Hardening Just-in-time Compilers with SGX](#2017---Frassetto-JITGuard-Hardening-Just-in-time-Compilers-with-SGX)

[2017 - Izraelevitz, Reusability is FIRRTL Ground Hardware Construction Languages Compiler Frameworks and Transformations](#2017---Izraelevitz-Reusability-is-FIRRTL-Ground-Hardware-Construction-Languages-Compiler-Frameworks-and-Transformations)

[2017 - Kotselidis, Cross-ISA Debugging in Meta-circular VMs](#2017---Kotselidis-Cross-ISA-Debugging-in-Meta-circular-VMs)

[2017 - Pedersen, From Trash to Treasure Timing-Sensitive Garbage](#2017---Pedersen-From-Trash-to-Treasure-Timing-Sensitive-Garbage)

[2017 - Pridgen, Picking up the Trash Exploiting Generational GC for Memory Analysis](#2017---Pridgen-Picking-up-the-Trash-Exploiting-Generational-GC-for-Memory-Analysis)

[2018 - Belleville, Automated Software Protection for the Masses Against Side-Channels Attacks](#2018---Belleville-Automated-Software-Protection-for-the-Masses-Against-Side-Channels-Attacks)

[2018 - Cho, FPGASwarm High Throughput Model Checking on FPGAs](#2018---Cho-FPGASwarm-High-Throughput-Model-Checking-on-FPGAs)

[2018 - Gawlik, Make JIT Spray Great Again](#2018---Gawlik-Make-JIT-Spray-Great-Again)

[2018 - Lipp, Meltdown Reading Kernel Memory from User Space](#2018---Lipp-Meltdown-Reading-Kernel-Memory-from-User-Space)

[2018 - Wu, A Side-channel Attack on HotSpot Heap Management](#2018---Wu-A-Side-channel-Attack-on-HotSpot-Heap-Management)

[2019 - Du, XPC Architectural Support for Secure and Efficient Cross Process Call](#2019---Du-XPC-Architectural-Support-for-Secure-and-Efficient-Cross-Process-Call)

[2019 - Kermarrec, LiteX  an open-source SoC builder and library based on Migen Python DSL](#2019---Kermarrec-LiteX--an-open-source-SoC-builder-and-library-based-on-Migen-Python-DSL)

[2019 - Kocher, Spectre Attacks Exploiting Speculative Execution](#2019---Kocher-Spectre-Attacks-Exploiting-Speculative-Execution)

[2019 - Patel, Runtime-Programmable Pipelines for Model Checkers on FPGAs](#2019---Patel-Runtime-Programmable-Pipelines-for-Model-Checkers-on-FPGAs)

[2019 - Polito, GildaVM a Non-Blocking IO Architecture for the Cog](#2019---Polito-GildaVM-a-Non-Blocking-IO-Architecture-for-the-Cog)

[2019 - Schwarz, ZombieLoad Cross-Privilege-Boundary Data Sampling](#2019---Schwarz-ZombieLoad-Cross-Privilege-Boundary-Data-Sampling)

[2019 - Varoumas, High-level programming models for microcontrollers with scarce resources](#2019---Varoumas-High-level-programming-models-for-microcontrollers-with-scarce-resources)

[2020 - Agache, Firecracker Lightweight Virtualization for Serverless Applications](#2020---Agache-Firecracker-Lightweight-Virtualization-for-Serverless-Applications)

[2020 - Bruant, System Verilog to Chisel Translation for Faster](#2020---Bruant-System-Verilog-to-Chisel-Translation-for-Faster)

[2020 - Fournier, Menhir Generic High-Speed FPGA Model-Checker](#2020---Fournier-Menhir-Generic-High-Speed-FPGA-Model-Checker)

[2020 - Fumero, Running Parallel Bytecode Interpreters on Heterogeneous Hardware](#2020---Fumero-Running-Parallel-Bytecode-Interpreters-on-Heterogeneous-Hardware)

[2020 - Lee, Keystone An Open Framework for Architecting Trusted Execution Environments](#2020---Lee-Keystone-An-Open-Framework-for-Architecting-Trusted-Execution-Environments)

[2020 - Lima, Exposing Bugs in JavaScript Engines through Test Transplantation and Differential Testing](#2020---Lima-Exposing-Bugs-in-JavaScript-Engines-through-Test-Transplantation-and-Differential-Testing)

[2020 - Schrammel, Donky Domain Keys - Efficient In-Process Isolation for RISC-V and x86](#2020---Schrammel-Donky-Domain-Keys---Efficient-In-Process-Isolation-for-RISC-V-and-x86)

[2020 - Taemin, NoJITsu Locking Down Javascript](#2020---Taemin-NoJITsu-Locking-Down-Javascript)

[2020 - Valdiek, ERIM Secure Efficient In-process Isolation with Protection Keys MPK](#2020---Valdiek-ERIM-Secure-Efficient-In-process-Isolation-with-Protection-Keys-MPK)

[2020 - Zandberg, Minimal Virtual Machines on IoT Microcontrollers The Case of Berkeley Packet Filters with rBPF](#2020---Zandberg-Minimal-Virtual-Machines-on-IoT-Microcontrollers-The-Case-of-Berkeley-Packet-Filters-with-rBPF)

[2021 - Dobis, Open-Source Verification with Chisel and Scala](#2021---Dobis-Open-Source-Verification-with-Chisel-and-Scala)




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


### 1987 - Cointe, Metaclasses are First Class the ObjVlisp Model 
<!-- Please prefix the notes with the date as in [22/12/2020] -->

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


### 2003 - Govindavajhala, Using Memory Errors to Attack a Virtual Machine
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

[28/04/2021]

**Memory Management Toolkit (MMTk)** is written in and for Java. It addresses th tension between flexibility and performance with a combination of design features: 1) **Java** as a systems language 2) **Design patterns** 3) Clean **interface between the VM and MMTk** 4) Composition of **policies and mechanisms to define collectors**.

MMTk groups regions of memory into spaces and implements garbage collection algorithms with a policy that couples a space with an allocation and collection mechanism. *Whole heap* collectors use one policy for most objects while *generational collectors* use one or more. A *write barrier* remembers pointers into independently collected spaces. For every pointer store, the compiler inserts write-barrier code. At execution time, the write-barrier conditionally records pointers between independently collected spaces.

MMTk implements **allocation and collection mechanisms** (*Bump Pointer, Free-List, Tracing, Reference Counting*) and forms **policies** with the implementations (define *Copy Space MarkSweep Space,* etc.) in order to create collectors (*SemiSpace, MarkSweep, RefCount,* etc.).

MMTk design is based on *flexibility* and *performance* and uses for that:

**1) Java as a systems language:**

 MMTk uses the extension defined by and for Jikes RVM that defines special types for unsafe operations: `VM_Offset` (distance between two addresses), `VM_Word` (value returned by dereferencing an address) and `VM_Address`. These **unboxed types** (operations on them never result in allocation) help use pointer arithmetic, casts as well as memory reads and writes. Compiler **pragmas** are used to control *inlining* and *interruptibility*. Control over inlining helps improve efficiency for system-level code written in an object-oriented style. By executing in its own heap, the collector must not scavenge itself and *pre-copies* any GC-related  instances and 

**2) Design Patterns:**

MMTk uses patterns for efficiency and reuse (*TriColor, RootSet, Adapter, Facade, Iterator* and *Proxy*). They are here used for several reasons:

- **Hot and Cold Paths:** MMTk marks the *hot path* (used frequently and lightweight) with `PragmaInline` and the *cold path* (used rarely and heavyweight) with `PragmaNoInline`. This is the case of a copying nursery (copy pointers *-hot-* then acquire new memory *-cold-*).
- **Local and Global Scopes:** Multi-threaded memory manager performance and correctness depends on a scalable division of local and global context. This is done through the **use of classes in MMTk**, it uses an instance with each thread and uses the class to reflect the global state. Instance methods operate over heir data without syncronization and access shared state through synchronized global class methods. MMTk provides 'local' and 'global' variants of a class,  with N instances of the global class and N x P instances of the local class, each mapped to one global instance. 
- **Prepare and Release Phases:** MMTk uses a high level algorithm to perform the stop-the-world collectors (*prepare, process all work* and *release*). The phase are split in global and local steps: `prepareGlobal`,  `prepareLocal`,  **`processAllWork`** , `releaseLocal` and  `releaseGlobal`. The `processAllWork` is common to all collectors and consists of processing a collection work queue. Each new collector only implements a prepare and release phase.
- **Multiplexed Delegation:** When the memory manager allocates or traces an *object*, it invokes the corresponding method in the *plan*, which then delegates responsibility to the appropriate *policy*. 

**3) Interface VM/MMTk:**  The interface between the VM and the MMis bidirectional and each side contains ***requirements*** and *features*. The key requirements of the MM include *identifying source of pointers*, *providing access to per-object GC  state*, etc.  On the other side, the VM requires that the MM provide allocation, finalization write barrier implementations, soft/weak/phantom references and statistics such as heap size and GC count.

**4) Composition (Mechanisms, Policies, Plans):** Mechanisms are **collector-neutral**, **highly-tuned** mechanisms include *bump-pointer, free list, large object allocations*. Policies implements five policies: *immortal allocation, copying collection, mark-sweep collection, reference counting collection* and *treadmill collection*. MMTk maps policies to spaces which are contiguous regions of virtual memory managed by a single policy. Each policy follows a local/global pattern. A plan is MMTk's highest level of composition, defining the rules by which policies are composed (collection and allocation policy for each object for example).



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


### 2005 - Ierusalimschy, The Implementation of LUA5
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[22/04/2021]

Main objectives of Lua: *simplicity* (simple language for simple C code), efficiency (fast one-pass compiler and VM), *portability* (clean ANSI C implementation), *embeddability* (simple C API), *low embedding cost* (small Lua core and extension as user libraries).

Hand-written compiler (YACC too slow) with scanner and recursive descent parser. No intermediate representation, instructions for the VM emitted on the fly. Fastest language implementation of interpreted and dynamically-typed languages. 

**Values representation:** Eight basic types (*nil, boolean, number, string, table, function, userdata, thread*). Tables are associative arrays with index. Userdata consists of pointers to memory blocks (*heavy* allocated by Lua and GCd or *light* allocated and freed by the user). Values of **all types are first class values**, they can be stored in globals, locals and table fields, passed as arguments etc. Value types are stored as a C union:

```c
typedef union {
	GCObject *gc; // strings tables etc.
	void p*;      // light userdata
	lua_Number n; // double
	int b;        // integer
} Value;
```

This solution is expensive to copy values but ensures portability. Strings are immutable and internalized in a hash table



**Tables:** The only data structures in Lua are tables, or **associative arrays**. They can be indexed by any value and hold values of any type. They are dynamic because they grow or shrink accordingly. Only one set of operators is needed to perform operations on tables or arrays. Tables are implemented as **hybrid data structures** (**array part** with implicit integer index and **hash part** with other indexes). The load factor is balanced by testing both parts and choosing an n such as at least half the slots between 1 and n are used and that at least one is used between n/2+1 and n. The hash part uses a mix of  *chained scatter table with Brent's variation*.

**Functions and Closures:** **Upvalues** are used to implement closures. Any outer local variable is accessed indirectly through an upvalue. **The upvalue originally points to the stack slot wherein the variable lives. When it goes out of scope, the value migrates into a slot in the upvalue itself**. The migration is transparent to all the users. To ensure the uniqueness, a linked list of all open upvalues is kept. When a new closure is created, all outer local variables are gone through and if an open value is found, it uses this one, otherwise it creates and links it. **Flat closures** allows to pour outer variables into inner closures.

**Threads and Coroutines:** Asymmetric coroutines are supported by the functions `create`, `resume` and `yield`. Each coroutine has its own stack and are stackful (it can be suspended from inside any number of nested calls). Combination of stackfulness and first-class status makes coroutines equivalent to one-shot continuations.

**The VM itself:** For each function that Lua compiles it creates a prototype which contains an array with the opcodes for the function and an array of Lua values with all constants used by the function. Register-based VM allows for less instructions and a single fetch time because operands are inside the instruction. Instructions are 32 bits long divided into three or four fields: OP|A|B|C or OP|A|Bx or OP|A|sBx where A is the destination, B and C registers, Bx an unsigned value and sBx a signed value. Branch instructions are decoupled in a test and a jump instruction. If the test is not verified, the next instruction is skipped. Each function (and coroutine) holds two stacks, the activation records of the other functions and a large array of temporary values corresponding to a given function.





---


### 2005 - Ungar, Constructing a Metacircular Virtual Machine in an Exploratory Programming Environment
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2006 - Gal, HotpathVM An Effective JIT Compiler for Resource-Constrained Devices
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2006 - Leroy, Formal Certification of a Compiler Backend
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2006 - Piumarta, Open extensible object models
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2006 - Rigo, PyPys Approach to Virtual Machine Construction
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2006 - Russell, Eliminating Synchronization-Related Atomic Operations with Biased Locking and Bulk Rebiasing
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2008 - Fuess, An FPGA Implementation of Explicit-State Model Checking
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

[28/04/2021]

Programming at low-level using a high-level programming language is possible and brings into question the use of C as a rule rather than as an exception. To use a high-level language, there are several approaches: the language directly supports low-level coding, the language can be extended to support low-level features, low-level features could be described in another language or the language could be extended via an extensible framework.

Adding low-level features to high-level languages requires three characteristics. ***Extensibility*** as programmers need to be able to reach beyond the semantics of high-level languages. An **extensible framework** for introducing and structuring low-level primitives is necessary. ***Encapsulation*** as the containment of low-level code is essential to minimize the impact on high-level language. The use of **language annotations** helps enforcing specific policies. Coarse-grained approach when lowering semantics results in both performance and semantics. ***Fine-grained lowering*** can help  but needs the programmer to reason about the undergoing low-level application.

The main challenges when linking low-level and high-level programming are that the high-level language **does not allow data to be represented as required** or **does not allow behavior** that is required. In order to close the data representation gap, ***primitive types*, *compound types*** and ***unboxed types*** can help as well as the addition of references and values (pointers referencing/dereferencing) are needed. Additionally to extending the data representation, the semantics should be extended as well. This can be done through the use of **intrinsic functions** to directly reflect the required semantics or add **semantic regimes** within which certain language-imposed abstractions would be suspended.

**Implementation:** **Raw Storage** allows the user to associate an empty type with a raw chunk of backing data of a specified size. This helps to create non-compound unboxed types. This can be done through the use of `@RawStorage` and`@Unboxed`. An unboxed type is only syntactically distinguished from an object and the **runtime compiler** ensures that unboxed types are never used as objects.

 The framework is used by MMTk !

---


### 2010 - Agesen, The Evolution of an X86 Virtual Machine Monitor
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2010 - Blazakis, Interpreter Exploitation Pointer Inference and JIT Spraying
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2010 - Ehringer, The Dalvik Virtual Machine Architecture
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[22/04/2021]

Java aims at portability with the **Java Virtual Machine**. It consists of a supposedly stable ecosystem for desktop application through the **JSE platform** and **JEE server**. However the **mobile ecosystem JME** is more fragmented. Google abandonned both the JVM and JME with the **Dalvik virtual machine** along with **limited implementation of standard Java libraries**.

Android runtime must support: **limited processor speed, limited RAM, no swap space, battery powered, sandboxed application runtime, diverse set of devices**. In order to answer those requirements, each Android application runs in its own process with its own Dalvik VM (a register-based VM) that executes a Dalvik Executable file (`.dex`). The Dalvik VM relies on the Linux kernel for threading and low-memory management.

**DEX File Format:** For each class in Java source code, a `.class` file is generated (`javac`) with the corresponding bytecode. The corresponding `.dex` file is generated from those `.class` files (using `dx`). This file format uses specific constant pools for strings, type/class, fields or methods. These pools are shared among all classes. These memory optimizations brings more complexity to the GC because it is independent from applications. Mark bits are separated from other heap memory in order to keep the memory sharing.

**Zygote:** The Zygote enable fast startup time for new instances as well as sharing of code. It assumes a significant number of core libraries are used among multiple applications and often in read-only mode. The Zygote is a VM process that starts at system boot time, preloads core libraries and waits for socket request to fork a new VM.







---


### 2010 - Onarlioglu, G-Free
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2010 - Reynolds, Lightweight Modeling of Java Virtual Machine
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[02/02/2021]*

Java Security is enforced in three ways:

- The **Java** **compiler** has a large number of **rules** that it enforces in order to ensure that the **syntax and semantics of the Java language are satisfied** but also to prohibit actions that are known to be malicious (e.g. uninitialized variables).
- The **Java** **class loader**, is used to port a classfile into the Java execution environment. When class loading is performed, the **Java Bytecode Verifier** is used to assert the bytecode are of correct form and types.
- The **Java Runtime** performs array bounds checking, type conversion checkings, etc. 



Almost all Java exploits use weaknesses in the **Bytecode Verifier**. The verifier uses a constraints-based approach to perform its analysis. The objective is to (1) provide an extensible framework for modeling security constraints and (2) provide a concrete model for meaningful, high value security constraints.

---


### 2010 - Rizzo, Practical Padding Oracle Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2010 - Siefers, Robusta Taming the Native Beast of the JVM
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



---


### 2010 - Sintsov, Writing JIT Spray Shellcode for Fun and Profit
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2011 - Bolz, Runtime Feedback in a Meta-Tracing JIT for Efficient Dynamic Languages
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2011 - Chen, JITDefender A Defense against JIT Spraying Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[03/05/2021]

Code-reuse attacks can be used instead of injecting a malicious piece of code. The different techniques consist of **ROP** (*return-oriented programming*), **BCR** (*binary code extraction*) or **Inspector** (*automatic extraction of proprietary gadgets from malware binaries*). A new attack aimed at JIT-compiled code is called **JIT spraying** that reuses code on the Flash VM's heap to construct the attack. JIT spraying can prevent the usual counter-measures sucha s **data execution prevention (DEP)** or **address space layout randomization (ASLR)**. JIT spraying consists of coercing the JIT compiler to generate native code with the malicious code on the heap of the VM, then exploits bugs in the browser to execute it.

**Attack example:** By writing the objects using dynamic languages, the attacker coerces the JIT compiler to generate malicious code on the heap of the VM. It does so by writing several objects which contains many uniform statements with dedicated constructed integers. If the integer is correctly chosen, the native code may be transferred into the malicious code with one byte offset.

**JIT Compilation:** The dynamic translation of source code into native code on the heap needs to mark the page containing the JIT-code as executable and reuse the code repeatedly without recompiling or interpreting in order to boost the performance. The W+X protection is turned off.

**JIT Defender design:** When designing JITDefender, the two key points are the *cod compilation point* (native code generation) and the *code execution point* (native code execution by the VM). The idea is to mark the native code pages as non-executable at the first point, then executable right before the second point and finally non-executable again right after. Under this protection, if an attacker hijacks the control flow to the code snippet on the heap for JIT spraying attacks, the **access will be blocked because the pages are kept as non-executable**. **Different views of the compiled code are provided for the VM and attacker with the native code execution policy.**

**Flash engine:** The source code is actionscript language. It is translated into actionscript bytecode (ABC) or ShockWave File (SWF). This code can be JIT compiled or interpreted on the flash engine. JIT compiling is done through **Machine Code IR generation** the **Machine Code generation**. The native code is stored in the newly allocated heap memory. The JIT then provides a **Native Code Execution Controller** to control whether the compiled code is on the heap or not.

**Implementation in Flash engine:** The class `MethodInfo` holds the information needed of the functions that can be executed by the VM. The class `CodeMgr` is the one responsible to manage memory of compiled code. Adding a reference to this instance from the class `MethodInfo` allows to modify some attributes later on. The stored compiled function is defined as non-executable and before entering it through the function `coerceEnter` defined in the VM, it is set as executable then non-executable again when `endCoerce` is called.

**Implementation in Javascript engine:** In V8, Native code is stored as `SharedFunctionInfo`. At the end of `Compiler::Compile`, the page is set as non-executable. Before `Execution::call`, it is set as executable then non-executable again after the execution. In Safari's engine, the same idea is used: non-executable after `JIT::compile`, executable before `JITStubCall::call` then non-executable again.

 



---


### 2011 - Haupt, CSOMPL a virtual machine product line
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[27/04/2021]

Application of **MDSOC** (multi-dimensional separation of concerns) and **SPL** (software product line) principles to high-level language virtual machines. Modularisation of **CSOM** using **VMADL** (virtual machine architecture description language). VMs are intricate pieces of software, and modularisation can help dealing with their understanding and overall maintainability. The notion of **service module** helps untangling the complexity of VMs. It consists of a module with *bidirectional interface* that can receive requests and exhibit internal situations to the outside.

CSOM is a SmallTalk Virtual Machine written in C. It does not support images but rather SmallTalk code written in text files. Two threading possibilities are used: the system `pthreads` or threads from within the VM itself. The GC is a mark/sweep collector. a Threaded-interpreter, additional integral representation and snapshots have been developed as extension.

**VMADL**: system architectures need to be supported at source code level and uses **service modules** with signals linking each other called *exposed join points*. It provides a frame in which an **implementation language** and an **aspect language**. Here the implementation language is C and the aspect language is **AspectC++**. In **AspectC++**, the `services` are defined and can use `require` and `expose` to link them between each other. A construct used to implement module interactions is a `combiner`.

An extension of C called ClassDL is used to help with OOP mechanisms. The combination of all the different elements create a toolchain generating a modular VM on demand.

---


### 2012 - Barbu, Application-Replay Attack on Java Cards When the Garbage Collector Gets Confused
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2012 - Rohou, Tiptop Hardware Performance Counters for the Masses
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2012 - Wuerthinger, Self-optimizing AST interpreters
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2013 - Chen, JITSafe a Framework Against Just-In-Time Spraying Attacks
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


### 2013 - Fournet, Fully Abstract Compilation to Javascript
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2013 - Kulkarni, Automatic Construction of Inlining Heuristics using Machine Learning
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2013 - Marr, Supporting Concurrency Abstractions in High-level Language Virtual Machines
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2013 - Snow, Just-In-Time Code Reuse On the Effectiveness of Fine-Grained Address Space Layout Randomization
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[07/05/2021]

At first, the lack of proper bounds checking  was misused to overwrite information on the stack (eg a function's return address) and redirect the flow of a vulnerable application to arbitrary code (called *shellcode*) known as ***smashing the stack***. To mitigate stack-smashing, ***canary*** (random value) was introduced in the stack preceding the return value. Compilers added a verification routine to the end of functions that terminates if the canary is modified.  Attackers thought of new exploits such as ***structured exception handlers***. A ***no-execute*** bit was introduced to the x86 paging scheme that allows any memory to be marked as non-executable.  ***Code-reuse attacks*** utilize code already present in memory with the famous `return-to-libc`. The concept was then extended to chain instruction sequences ending in a `ret` instruction ***gadgets*** to implement arbitrary  program logic. This approach is called ***return-oriented programming***. To counter these attacks, ***address space layout randomization*** was used to randomize both the code and data memory regions.

**Code Reuse Attacks:** The logical program flow is redirected to instructions already present in memory, then use them to execute alternative program logic. ROP shown that attacks may combine short instructions sequences from within functions (gadgets). To orchestrate such an attack, the adversary writes a so-called ROP payload into the application's memory space. The payload consists of a number of pointers (the return addresses) and any other data needed for the attack. Then, the control-flow is hijacked from the intended one to the *stack pivot sequence*. Once the overwritten function pointer is used by the function, the control-flow is redirected. Stack-pivot sequences usually change the value of the stack counter `%esp` to a value stored in another register. The `ret` instruction in x86 simply loads the address pointed to by `%esp` into the instruction pointer and increments `%esp` by one word. A gadget represents an atomic operation (`LOAD`, `ADD`, `STORE`...) followed by `ret`. This succession of carefully crafted return addresses allows an attacker to introduce arbitrary program logic.

**Randomization for Exploit Mitigation:** The basic idea consists of a new stack memory allocator to add a random pad for stack objects larger than 16 bytes. For the most part, ASLR schemes randomize the base address of segments such as the stack, heap or the executable itself. The start address of an executable is therefore relocated between consecutive runs of the application and an attacker needs to guess the location of the functions and instruction sequences needed for successful deployment of a code-reuse attack. ASLR suffers from two problems: the ***entropy on 32-bits system is too low*** and can be bypassed by ***bruteforce*** and all ASLR implementations are vulnerable to ***memory disclosure attacks*** where the knowledge of a single runtime address re-enable code reuse. More fine-grained implementations exist but are based on the fact that the disclosure of a single address no longer allows an attacker to deploy a code-reuse attack.

The target platform uses the following mechanisms for mitigations: *non-executable memory* (NX or DEP), *JIT spraying mitigations*, *export address table filtering* (code outside a module's code segment cannot access shared libraries export tables), *base address randomization* and *fine-grained ASLR* on functions, basic blocks, etc.

**Memory Mapping:** The first action the attacker needs to do to perform his attack is to ***map code page memory*** to actual code without causing a crash. The knowledge of a single valid code pointer reveals that an entire 4 kilobyte-aligned page of memory is guaranteed to be mapped. The next step consists of applying static code analysis to identify both direct and indirect `call` and `jmp`. Direct control-flow instructions yield a hint to other code locations. Indirect control-flow instructions point to other modules and they can be processed by disclosing the address value in the Import Address Table. Iterating this process over each new page found allows an attacker to map a significant portion of the code layout.

**API Function Discovery:** As the payload will have to interact with the OS to be effective, and will prefer using API calls (as in `kernel32.dll`) rather than hardcoded system calls (e.g. `int 0x80` or `syscall`). These calls can be found by parsing the Process Environment Block, manually harvesting an application-specific function pointer. The approach consists of creating signatures based on opcode sequences for call sites of the API functions.

**Gadget Discovery:** A heuristic based on the observation that a single instruction type fulfills a gadget's semantic definitions simplifies the search down to a single table lookup to check if the first instruction type in the sequence meets one of the gadget semantic definitions. 

**JIT Compilation:** Since each instantiation of a vulnerable application may yield a completely different set of concrete gadgets, a dynamic compilation is required to ensure we can use a plethora of gadget types to build the final payload. The gadget compiler works like a traditional compiler except that compilation is embedded directly in an exploit script.

---


### 2013 - Wimmer, Maxine an Approachable Virtual Machine for and in Java
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2013 - Wuerthinger, One VM to Rule Them All
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2014 - Backes, Oxymoron Making Fine-Grained Memory Randomization Practical by Allowing Code Sharing
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


### 2014 - Jain, Sok Introspections on Trust and the Semantic Gap
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[27/04/2021]

The goals of **Virtual Machine Introspection (VMI)** is to identify if the guest OS has been compromised, if malicious applications are running on the system or if sensitive file have uncompromised secrecy or integrity. A *semantic gap* occurs when using a hypervisor to look into VM behavior as the abstractions used by the hypervisor policies are higher-level than what he can actually see (registers and cpu state). Most of VMI development goes into reconstructing high-level semantic from low-level sources.

To close this semantic gap, the **reconstruction** of data models is essential. A **learning phase** is used to extract information related to data structures (**signature**). A **search phase** can then look for instances of this data structure. Signatures are either handcrafted (`memparser`, `kntlist`  or `grepexec`), extracted from source analysis (`siggraph`, `kop` or `mas`)  and dynamic learning by studying a trusted OS behavior.

Other methods allow to bridge the gap , such as *code implanting* where the objective is to inject code into the guest OS that reports information back to the hypervisor, *process outgrafting*  that relocates the monitoring process from an untrusted VM to a second, trusted one or *kernel executable integrity* enforces the fact that the executable of the kernel has not been modified. This can be enforced by:  1) the W+X principle where a memory page can either be *writable* or *executable* but not both at the same time, 2) *whitelisting portions of code*.

- Current VMI systems face fundamental trade-offs between performance and risk, often making fragile assumptions about the guest OS

  

---


### 2014 - Lin, A Security PaaS Container with a Customized JVM
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2014 - Niu, RockJIT Securing Just-In-Time Compilation Using Modular Control-Flow Integrity
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[10/05/2021]

Enforcing the control-flow integrity (CFI) in a JIT compiler provides a better defense against code-reuse or code-injections. The generated control-flow graph (CFG) is updated as new code is generated.

**Architecture of JIT compilers:** Looking into several JIT engines (Google V8, Mozilla TraceMonkey, Facebook HHVM or LuaJIT),  they all consist of (1) a ***baseline executor*** that is either an interpreter that interprets (*e.g. Java bytecode*) or that compiles source code directly to unoptimized native code (*e.g. V8*). It also consists of an ***optimizing compiler*** that performs runtime profiling to identify hot code or types and generates optimized native code. Optimization can manifest as either *method-based* or *trace-based* and the corresponding blocks are optimized. Next, a ***garbage collector*** provides automatic memory management (allocation and collection).

**Modular Control-Flow Integrity:** CFI system with low performance overhead and modular support. A program is divided in modules and each module contains not only code and data but also auxiliary information used to generate a new CFG when linking with other modules. MCFI represents the CFG in tables during runtime. Thread-safe table transactions are used to access and update the tables.

**Security:** The JIT engine is modified to cooperate with RockJIT's compilation toolchain and generates an MCFI module. The module is loaded by RockJIT into a sandbox. After loading, RockJIT generates a control-flow graph. The sandbox around the compiler restricts their control flow according to the tables and also restricts the memory access to be inside the box. To rule out code-injection attacks, RockJIT uses W+X protections, however the code heap needs to be both writable and executable. RockJIT uses a *shadow code heap* (similar to what *NaCl-JIT* does), it is mapped to the same physical pages as the code heap in the sandbox but with different permissions. The shadow code heap is made readable and writable but not executable. Instead of directly modifying this shadow heap, the application invokes RockJIT services to install new or modify existing native code. RockJIT enforces CFI on both the JIT compiler and the JITed code but applies different levels of precision to them. For the compiler, it applies a C++ CFG strategy to produce a relatively fine-grained CFG offline while the CFG for the JITed code is coarse-grained.

**Verification:** The verifier maintains three sets of addresses that are code addresses in the code heap. **(1)** ***Pseudo-instruction start addresses (PSA)***, this set remembers the start addresses of all pseudo instructions (defined either as a checked indirect branch, a masked memory write or an instruction that is neither an indirect branch nor an indirect memory write). **(2)** ***Indirect branch targets (IBT)***  and **(3)** ***Direct branch targets***. It verifies several conditions on those sets. Those verifications are performed on native code emission, deletion or modification.

Technical implementations in C++ follow.

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


### 2015 - Athanasakis, The Devil is in the Constants Bypassing Defenses
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[12/05/2021]

ROP attacks consist of linking several *gadgets* (blocks of instructions ending with a `ret`). The threat model consists of a system with defenses present i most modern systems: DEP, W+X, ASLR, stack smashing protection (canaries or function cookies), EMET.

**Goal of the attack:** (1) The browser ***renders a malicious web page*** (2) The JavaScript code in this page, once compiled, ***produces a series of gadgets in the JIT buffer*** (3)  A memory-disclosure bug ***reveals the locations of the gadgets*** (4) A ROP chain ***is built with the just constructed gadgets*** and control is transferred to it (5) The ROP chain ***calls `VirtualProtect` (or `mprotect`) and makes the page where the shellcode is stored executable*** (6) Control is transferred to the shellcode and the ***browser is compromised***.

**Exploits:**

**Firefox:** The preparation is as follows, the idea is to produce a series of gadgets that eventually lead to a call to `mprotect`. To do so, the attacker needs to control four registers. First,  the corresponding system call number `0xb` is stored in `%eax`. Then, the address of the page the attacker wants to change is stored in `%ebx`. The length of the region is stored in `%ecx` and the desired access rights, `0x7` here are stored in `%edx`. To accomplish this, the attacker needs a ROP chain which will load the four registers with the required values and then a gadget will call `mprotect`. In Linux for x86 architectures, system calls are performed by using `int 0x80`. Loading a register with the required value can be done in two ways. Either place the required value on the stack and use `pop` or a `mov`-like command to copy the value to the register. For the JIT to work properly, the stack and `pop` are used for *large values* while *small values* are used with `mov` and registers. In the case a `mov` is used, it affects only part of the register and the attacker needs to zero the register before moving the value which is done by using a `xor` gadget.

In the end, the ROP chain involves seven gadgets:

```assembly
pop %ebx; ret;       // page address
pop %ecx; ret;       // region length
xor %eax; %eax; ret; // 0 before mov
mov 0x7d; %a1; ret;  // mprotect set
xor %edx; %edx; ret; // 0 before mov
mov 0x7; %d1; ret;   // permissions to WRX
int 0x80; ret;       // mprotect call
```

The gadgets need to be added to the JIT buffer and the attacker needs to: (1) trigger a JIT compilation (2) add the gadgets to memory. For (1), creating a "hot loop" will most likely trigger the JIT compilation and for (2), variable are initialized with specially crafted immediate values.

```javascript
var g1 = 0;
// ...
var g7 = 0;
for (var i=0; i<10000; ++i) {
    g1 = 50011;
    g2 = 50009;
    g3 = 12828721;
    g4 = 12811696;
    g5 = 12833329;
    g6 = 12781490;
    g7 = 12812493;
}
```

**Chakra:** function to change memory rights is `VirtualProtect` and needs 4 arguments. The attacker needs to adjust the real stack to the fake stack controlled by himself, this can be done by using ***stack pivoting***. It consists of exchanging a register the attacker controls with `%rsp` so the stack pointer points to an arbitrary value. This exchange can be done with `xchg` but unfortunately, it is 2 bytes long (3 with the `ret`) and these gadgets cannot be constructed trivially. 

Chakra uses several protections: (a) ***constant blinding*** where any value less than 2 bytes long is emitted XORed with a random value (and re-XORed when used), (b) ***long gadgets*** cannot be encapsulated in immediate values and have to be split in several parts, moreover Chakra places several checks when compiling such gadgets (c) ***code diversification*** where Chakra emits a random number of `nop` instructions hat change the layout of the JIT buffer and randomize the location of all important gadgets each time they are generated.

The gadgets have to be generated differently:

```javascript
function r8 (addr) {
    return addr + 0x5841;
}

function r9 (addr) {
    returnn addr + 0x5941;
}

function emit_gadgets() {
    for (i=0; i<10000; i++) {
        rax = 0xc358; // pop rax
        rcx = 0xc359; // pop rcx
        rdx = 0xc35a; // pop rdx
        r8(0);
        r9(0);
    }
    return 0;
}

emit_gadgets();
```

**Discovering the Gadgets:** This can be done using ***information leaks*** such as heap overwrites to obtain essential information to discover gadgets. Instead of revealing the code segment of a given object in a typical JS object layout, the attacker reveals the JIT buffer which contains the artificially constructed gadgets. The following code generates an object with a memory layout that can help access the JIT buffer. Accessing `O` then `foo` will give an access to the JIT buffer.

```javascript
O = new Object();
O.g1 = 0xc358;
O.g2 = 0xc359;
function foo(x) { return 0x 5841; }
O.func = foo;
```

**Defenses:** Enhance the JIT buffer with G-Free to remove all gadgets. The produced code is safe and gadget-free.

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


### 2015 - Lam, Numba
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Lian, Too LeJIT to Quit Extending JIT Spraying to ARM
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[12/05/2021]

JIT spraying has always be an x86-only attack thanks to its reliance on variable-length, unaligned instructions. ARM and RISC-like architectures work differently as presented.

**ARM Layout:** The ARM architecture has ***13 32-bit general purpose registers*** (`R0-R12`) and ***3 32-bit special-purpose registers*** (`R13-R15`). The usage convention is defined by the Procedure Call Standard (AAPCS). The ***stack pointer register*** (`SP/R13`) is used to hold a pointer to the top of the current execution stack. Special variants of `add` and `sub` are hardwired to `SP` to accelerate stack operations. The ***link register*** (`LR/R14`) is used to hold subroutine return addresses. The ARM analogs of x86 `call` instruction are the branch with link (`bl`) and the exchange (`blx`) instructions. The ***program counter register*** (`PC/R15`) holds the address of the currently-executing instruction plus 8. ARM is a ***bi-endian architecture***, meaning that it can interpret words and halfwords as either big or little endian. The `ENDIANSTATE` execution register stores a bit determining the endianness and the instruction `setend` can modify its value. The ARM architecture also supports the Thumb instruction set that contains mixed 16- and 32-bits instructions (Thumb-2 consists of two instructions close to each other). The choice of the current instruction set is determined by the instruction set state register (`ISETSTATE`). The ARM-Thumb interworking and variable-length instructions can be used as possible vectors for creating instruction confusion.

**JavaScriptCore:** JSC is a multi-tier JavaScript engine, source code is initially compiled to bytecode that is interpreted by an ***interpreter*** but once it has been executed several times (6 for functions, 100 for loops), the bytecode is compiled down to unoptimized native code by the ***baseline JIT***. Once the ***baseline JIT*** has been executed many times (60 for functions, 1000 for loops), the ***DFG JIT*** emits optimized Thumb-2. 

- The ***Low-Level Interpreter (LLInt)*** interprets bytecodes, 32-bit opcodes followed by as many operands as are required. The opcodes are pointers to pre-compiled code snippets in the interpreter's text section. During bytecode execution, a virtual program counter (vPC) register points to the currently-executing opcode in the bytecode while the real `PC` is in the code snippet pointed to by the opcode. The snippet accesses the opcode's operands via vPC-relative memory loads, performs the desired computation, advances the vPC and finally branches o the next opcode's snippet with a register-indirect jump through the vPC.
- The ***Baseline JIT*** generates native code. The instruction stream produced differs from the one executed by the ***LLInt*** since it does not need to manage the vPC. The code has clear boundaries where the execution of one bytecode instruction ends and the next begins, and it does not flow scratch values in registers across those boundaries. Instead, they are stored onto the JavaScript stack and read back by other bytecode operations.
- The ***Data Flow Graph JIT*** uses *dead code elimination analysis*, *function inlining* and a *basic register allocator* to optimize the JITed code better.



---


### 2015 - Rohou, Branch Prediction and the Performance of Interpreters Dont Trust Folklore
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Simon, Snippets Taking the High Road to a Low Level
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2015 - Song, Exploiting and Protecting Dynamic Code Generation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[10/05/2021]

The challenge posed by dynamic code generation is that the zone it generates code into needs to be both writable and executable, violating the usual W+X rule. A simple idea is to **keep the code cache as read-only and executable**, **switch to writable but not executable** when it needs to be modified and **switch back** when the write operation has finished. However, multi-threaded operations can exploit this idea. Other defense ideas consist of ***Software-based Fault Isolation*** , ***Memory Safety***, ***Control-Flow Integrity*** or ***Process Sandbox***.

**Overwriting the code cache**: The *Software Dynamic Translator (SDT)* translates the IR to native code and maintains a mapping between untranslated code and translated code. The ASLR needs to be bypassed to exploit primitives to overwrite the code cache with full `WRX` permission. 

**Exploiting Race Conditions to Bypass W+X Enforcement:** Memory pages are executable but not writable when allocated by default. The write permission is granted when *new code is installed* (native code is generated and copied to the location), *existing code is patched* (address or constant modifications), *runtime inline caching* (object type or properties cached) or *runtime garbage collection* (memory needs to be managed).

The poc runs as follows: 

- *Create worker*: A worker thread is created.
- *Initialize the worker*: The worker thread initializes its environment, making sure the code cache is created. It then notifies that it is ready.
- *Locate the worker's code cache*: The main JS thread locates the worker thread's code cache by exploiting an information disclosure vulnerability. It then notifies the worker thread that it is ready.
- *Make the code cache writable*: Upon receiving the main thread's message, the worker thread begins to execute another piece of code, forcing the SDT to update its code cache. It can either simply execute a function that is large enough to create a new chunk for the code fragment and set it as writable.
- *Monitor and Overwrite the code cache*:  At the same time, the main thread monitors the status of the code cache and tries to overwrite it once its status is updated.
- *Execute the shellcode*: When receiving the main thread's new message, the new worker calls the function whose content has already been overwritten. This way, the injected shellcode is executed.

The race condition needs to be validated and the method that notifies the update takes 23 microsec against the 43 needed by the W+X protection.

**System Design:** Three main challenges. ***Memory Map Synchronization*** as all memory regions allcated by the code cache are dynamically allocated and can grow and shrink freely, an effective way is needed to synchronize memories. A *reservation-based* strategy is chosen for the shared memory. When the process is initialized, a we reserve a large chunk of shared memory in both the untrusted process and the SDT. Once the memory is allocated, the synchronization can be performed with *Inter-Process Communication (IPC)*. ***Remote Procedure Call*** can be done via stubs but suffers from performance and argument passing. There is a choice to extend the shared memory to dynamic data the SDT depends on. ***Permission Enforcement*** comes by intercepting system calls related to virtual memory management. Specifically, some policies are enforced: (i) memory cannot be mapped as both writable and executable, (ii) when mapping a memory region as executable, the base address and the size must come from the SDT process, and the memory is always mapped as RX, (iii) The permission of non-writable memory cannot be changed.



---


### 2015 - VanDeVanter, Building Debuggers and Other Tools We Can Have it All
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2016 - Lin, Rust as a Language for High Performance GC Implementation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[30/04/2021]

The imperative of **performance and access to low-level programming** encourage use of C or C++ when dealing with memory manager. Rust promises *a systems programming language that runs blazingly fast, prevents segfaults, and guarantees thread safety*.

Rust presents several important aspects such as. **Ownership**, where variable binding grants a variable unique ownership of the value it is bound to. Unbound variables are not allowed and rebinding consists of transferring variables ownership. When a variable goes out of scope, the associated ownership expires and resources are reclaimed. **References** are borrowed in Rust and it allows one or more co-existing *immutable* references to an object and exactly one *mutable* reference with no immutable references. The ownership cannot be moved when the reference is borrowed. This eliminates data races altogether. **Data Guarantees (Wrapper Types)** are provided with different guarantees and tradeoffs. Plain references guarantee read-write lock for single-threaded code. `Box<T>` represents a pointer which uniquely owns a piece of heap-allocated data, `Arc<T>` provides an atomically-counted reference-counted shared pointer to data and guarantees it stays available until `Arc<T>` goes out of scope. **Unsafe** operations (raw pointers, sharing data across threads) are allowed in Rust but need to be declared within a marked block.

Building a GC in Rust brought up the following challenges:

- **Encapsulating address type:** a difference needs to be made between an *address* (arbitrary location in the memory space) and an *object reference* (language-level object that points to a memory piece with added meta-data). Object reference to address is always safe while the other way around is not. A single-field `tuple struct` is used for abstracting both other the word-width integer `usize`. The `Address`s can be created from raw pointers or derived from an existing `Address` but cannot be created from an arbitrary number (except 0 to avoid a `None` initialization overhead).
- **Ownership of memory blocks:** Thread-local allocation is an essential element of high performance memory management for multi-threaded languages. The usual approach is to maintain a global pool of raw memory regions from which thread-local allocators take memory as they need and to which thread-local collectors push memory as they recover it. `Blocks` objects are created to be in a coherent state among *usable*, *used* or *being allocated into by a unique thread*. The global memory owns the block and arranges them into a list of usable and used `Blocks` . The Rust's ownership model ensures that allocation will not happen unless the allocator *owns* the `Block`. Therefore every `Block` is either: owned by the global space as usable, owned by a single allocator and being allocated into or owned by the global space are used.
- **Globally accessible per-thread state:** A thread-local allocator avoids costly synchronization on the allocation fast path. However allocators might be told to yield by a collector and need to provide some access to their state. Every `Allocator` is broken up in two pieces, a *local* and a *global* one.

- **Library-supported parallelism:** The efficiency of the collector depends critically on the implementation of fast, correct, parallel work queues. Those are coming from `std::sync::mpsc` (multiple-producers single-consumer FIFO) and `crossbeam::sync::chase_lev` (lock-free Chase-Lev work stealing deque). 

Some **abuses** of Rust had to be performed to improve performance. To represent collections state, memory managers often use bit maps (or byte maps). Examples include **card tables** (remember modified memory regions) and **mark tables** (remember marked objects). Concurrent writing is needed in an array but forbidden by Rust. 



---


### 2016 - Maas, Grail Quest A New Proposal for Hardware-assisted Garbage Collection
<!-- Please prefix the notes with the date as in [22/12/2020] --> 

[10/05/2021]

Garbage collection can be made effectively pause-free at the cost of slowing down application threads and using a substantial amount of resources (both CPU time and energy consumption). Low pause times and energy efficiency can be reconciled using a proper algorithm. The two main GC strategies are ***tracing*** and ***reference counting***. *Tracing* performs a breadth-first search (BFS) to find all reachable objects and then recycle those that are not. *Reference counting* updates reachability data on the fly but requires a tracing backup collector to handle cycles. Next, there is a distinction between ***stop-the-world*** and ***concurrent*** collectors. *Stop-the-world* collectors require ***mutators*** and can only continue once GC has completed while a *concurrent* collector operates in parallel to the mutators. Finally, it is important to note whether or not the collector moves object in memory. Non-relocating collectors tend to fragment memory and end with poor memory locality. Relocation is important to obtain fast collectors but is very difficult to implement in concurrent collectors.

The objective is to design a ***pauseless GC algorithm*** that has to be performed by a ***concurrent, relocating mark-compact GC***. The algorithm has two key components: a *mark* and *relocation* phase. The mark phase regularly performs BFS passes over the heap to produce a fresh set of mark bits that tell if an object is reachable or not. The relocation phase uses the newest set of mark bits to pick pages in memory that are mostly garbage. The key idea is to try to perform these phases concurrently with respect to each other and the mutators. Write barriers are **"self-healing"** as they tag the reference in its original memory location such that next time it is encountered, it is known it has already communicated to the marker. This works by using the MSB of references to hold an NMT (not-marked-through) bit. This way the read barrier is only triggered once for each reference. The relocation phase uses the same mechanism, when an object is moved to another page, a self-healing barrier is used to remap the references to this object to the references to the new location. It maintains an **forwarding table** outside of the original page, which maps the old location to its location in the new page.

**Object Layout:** The object layout is modified from the usual language implementations. It usually starts with a header, then the parent classes' fields and finally the classes' fields. This facilitates casting an object to its parent class but reference are interspersed throughout the object. Using a ***bi-directional layout***, where the header is in the middle of the object, all non-reference fields to the left and reference fields to the right, the marker only needs to read and mark the header then read all references in a single unit-stride access.

The mark unit consists of three parts: the ***reader*** that polls the range until it has received all roots, the ***mark queue*** that is implemented as on-chip SRAM and the ***address range*** used to communicate with the between CPUs and the GC. Once the roots have been loaded, the ***marker*** and the ***tracer*** perform the mark phase. The marker is responsible for taking an object pointer from the mark queue, sending out an atomic fetch-and-or request to mark and read the object's header and, put it into a ***trace queue*** (if the object was unmarked and had at least one outgoing reference). This queue stores pairs of object pointers and number of references associated. The tracer then takes elements from this queue and issues read requests to load the references within the object into the mark queue as they return. This design decouples the different types of memory access necessary for the mark phase. The marker and tracer work together to maximize the memory bandwidth because if the tracer is busy copying one long object, the marker can run ahead and queue up additional objects . Similarly, if the marker is busy marking objects that have been marked before, the tracer can work through the remainder of the trace queue. This design is enabled by the object layout. The relocation unit **finds** pages that are mostly garbage, **builds** a side-table of forwarding pointers, **protects** the original page in the page table and **moves** objects over to the new page.

Changes to CPU consist of an added read barrier mechanism fully implemented in hardware than using a user-level trap. Three important cases are added ***NMT fault***, ***Relocation fault*** and ***Stale reference fault***

---


### 2017 - Frassetto, JITGuard Hardening Just-in-time Compilers with SGX
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[03/05/2021]

**SGX:** *Software Guard Extension (SGX)* is a hardware extension that enables isolated execution environments named **enclaves**. Enclaves are created within a user-mode process and cannot be accessed by any system entity. This is enforced by the CPU through access control. The memory of an enclave can only be accessed by the code executed within it/ This policy is enforced if the code is within a CPU cache. If it is outside however, it is encrypted and integrity-protected with an enclave-specific key.

**JIT:** JIT engines consist of an *interpreter*, a *JIT compiler* and a *garbage collector*. The *interpreter* executes unaltered bytecode (cold paths usually) while the *JIT compiler* outputs highly performant machine code from a succession of bytecodes. It first transforms the bytecodes in an IR which is then compiled to native code. The emitted JIT'd code is limited to basic instructions and cannot access arbitrary memory. While JIT'd code was initially placed in a read/write/execute memory space, it is now constrained to writable and non-executable when written. Finally, the *GC* is the memory manager and  takes care of allocations and collections.

**JIT Attacks:** Read-write-executable exploits are used against JITs. Payload into JIT memory (pwn2own Gong et al.) prevented later on by using W+X to JIT'd code as well. However the small time window during which the JIT code page is writable can be exploited. Code-reuse attacks chain existing pieces of code together to execute arbitrary malicious code. `call` and `return` are needed by exploits but forbidden by the JIT generator. However, it is possible to pass instructions through numerical constants and by forcing the control flow, execute arbitrary code. This can be mitigated by constant blinding, XORing  the constant at compile time with a random value then XORing it again before using it in the JIT compiler. Code randomization can also mitigate JIT spraying.

**DOJITA:** Data-Only JIT Attack manipulates the IR to trick the JIT compiler into generating arbitrary malicious payloads. The attacker **(1)** exploits a memory-corruption vulnerability to read and write arbitrary data memory **(2)** identifies a hot function which will be compiled to native code **(3)** during the compilation of F the JIT compiler will generate the corresponding IR, the attacker discloses the memory adress of the IR in memory which is commonly composed of C++ objects **(4)** injects crafted C++ objects into the IR **(5)** the JIT compiler uses the IR to generate native code and **(6)** the payload is now executed at each call of the initial function.

**Threat model:** The model excludes attacks on static code by supposing that ***static code is protected*** by either DEP, randomization-based solutions or (hardware-assisted) control-flow integrity, ***data randomization*** is in place through ASLR, a ***secure initialization*** can be performed, a ***memory-corruption vulnerability***  can be exploited and the access to a ***scripting engine*** is possible.

**JITGuard:** **(1)** SGX is used to isolate the JIT compiler and its data from the rest of the application. The attacker can no longer exploit memory-corruption vulnerabilities in the host process. **(2)** The JIT code and JIT stack memory addresses are randomized to protect against code-injection and code-reuse attacks. **(3)** An indirection layer is used through trampolines which contain `jump` instructions that obtain the address of the JIT code using an offset from a segmentation register. The compiler needs to be able to efficiently update the indirection layer without using read-write-executable permissions. A ***double mapping*** of the trampolines help prevent this issue. The same region in physical memory is mapped twice in the virtual address space of the process. The first part is executable but not writable while the second is writable but not executable, and its address is protected through randomization. The compiler uses the second mapping to update the trampolines (e.g. when a new function is compiled) and the indirection layer, while the (potentially vulnerable) static code uses the executable trampoline.

**Implementation:** Instead of using SGX to isolate the full JIT engine, it is used to isolate security-critical components (JIT Compiler) and securely store the randomization secret. It is done his way because a context switch is needed to execute code outside of the enclave and would add a consequent overhead. Initialization comes through a component that allocates two memory regions, the trampoline and the JITGuard Region, and then starts the enclave. The JITGuard Region is used to store the JIT code, the JIT stack and the writable mapping of the trampolines. (additional runtime modifications).

***Control Flow transfer:*** To cleanly isolate randomized JIT code from static code, a separate stack is provided which is hidden inside the randomized region. This way, it can be used safely during JIT execution and an adversary cannot recover a return pointer to the JIT code from the native stack. **To call JIT code**, **(1)** the static code initiates the switch by calling a trampoline. Each trampoline targets a single JIT code function. **(2)** The trampoline fetches the address of the function inside the randomized segment. A trampoline consists of a single `jump` instruction that retrieves the address using a constant offset in the segment. The jump table is located inside the randomized region. **(3)** The JIT code switches from the native stack to the randomized stack and starts executing its code. When the JIT-compiled function returns, the randomization code restores the old values for the registers so they point to the normal stack again and returns execution to the static code. **To call static code,** **(1)** the JIT code stores the return address to the JIT code in a jump table, switches the stack pointer to the native stack, save the offset between the two stacks in the randomized segment and set the return address on the native stack to point to the return trampoline. **(2)** the JIT code issues the static code function code until it returns. **(3)** It then retrieves the original return address using the segment register and an offset into the jimp table.

**Security analysis and performance evaluation: ...**

---


### 2017 - Izraelevitz, Reusability is FIRRTL Ground Hardware Construction Languages Compiler Frameworks and Transformations
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2017 - Kotselidis, Cross-ISA Debugging in Meta-circular VMs
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[30/04/2021]

Maxine VM is a meta-circular VM for Java written in Java. It adopts a modular approach in *schemes* that comprises the VM. The transition to a new ISA (x86_64 to ARMv7 32) brought several challenges.

Maxine VM offers three compilers: **T1X** (fast template compiler similar to an interpreter), **C1X** (JIT optimizing compiler based on statistics gathered by T1X) and **Graal** (aggressive JIT optimizing compiler). The fact that it is meta-circular makes the port to a new ISA complicated. The VM's bootimage is ahead-of-time compiled by one of its runtime compiler.  The 64 to 32-bits transition brings issues to the **object identification** (hashcode is 32-bits long and leaves no place for metadata) and **register allocation** (need for efficient 32 bits register allocations).

A **QEMU-based toolchain** is developed to be able to debug the whole flow of the Maxine VM port:

1. **`MaxineTester` Initialization:** Every unit test invokes the `MaxineTester` which resets all internal states and QEMU output files. Once the initialization is complete, a code buffer is returned to the unit tests which serves as placeholder for the generated assembly code.
2. **Unit Test Generation:** Depending on the nature of the unit test (assmbly instruction, T1X, C1X, ...) the code buffer is filled differently. When filled, it is passed to the `MaxineTester` for emulation.
3. **QEMU Binary Composition:** The `MaxineTester` assembles the binary that will be passed to QEMU for emulation. First, the assembly code of two helpers (`asm_startup.s` and `entry.s`) are linked together with the binary code of the unit test. The code buffer is inlined to a C file and a function pointer to its first entry is installed. Finally, the actual test that links the code buffer and the two assembly files is compiled and the binary is generated.
4. **QEMU Emulation:** The corresponding processor is simulated and the binary generated before is emulated. Upon completion, the register file is dumped to an output file defined in the `MaxineTester` class.
5. **Output Validation:** The dump file is validated against the expected values as set in the unit test definition.

Three kinds of unit tests can be ran into the toolchain: individual assembly instructions, T1X compiled methods and C1X compiled methods.

Then, tracking faulty methods at runtime is comple as bootstraping a meta-circular VM in a new ISA holds many parts that are untested. A unique identifier called `MethodID` was injected during compilation to keep track execution. Another approach would be to check the address of the faulty instructions through the PC, against the code cache to find the boundaries of the faulty method. Inlined methods would not be taken in consideration so a dedicated `MethodIDNode` is attached to the IR graph before the inlined code to overcome this issue.

---


### 2017 - Pedersen, From Trash to Treasure Timing-Sensitive Garbage
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[29/04/2021]

Timing garbage-collection can make internals of a program become clear outputs for an attacker. Authors bring the **first amplifiable covert channel via automatic memory management**. They observe that **garbage collection creates a bidirectional information channel** and design and demonstrate a **secure garbage collector using traditional information flow analysis**.

A garbage collector determines which parts of the heap contain objects that will not be accessed anymore and reclaims the memory occupied by these objects. The three GC strategies looked upon are ***mark-and-sweep*** (marking phase -cost = linear in reachable objects- and sweep phase -cost=linear in heap size-), ***copy collection*** (partition the heap in two pieces and copies only used objects) and ***generational collection*** (young and old generation with different GC frequencies).

To attack the JVM and V8, two amplifiable attacks are possible:

- **High dependency in low context:** During evacuation from *from-space* to *to-space*, the amount of bytes copied depends on the reachable nodes at the current point in the program. Creating a sufficiently large difference in reachable and unreachable nodes makes the time required to perform a minor/major GC observable. *(DETAILS OF THE ATTACK FIG.2)*

  Example:

- **Low modification in high context:** GC of public information in a sensitive context leads to a covert channel. Knowing whether or not a GC occurs leaks one bit of information. *(DETAILS OF THE ATTACK FIG.3)*

  Example:

The attack can be amplified to leak more bits (i.e. 32-bits `int` here).**First**, it is repeated sufficient (10/20) times where each trial is timed and stored if the duration is larger than some threshold. **Second**, instead of allocating one array when filling up the memory, K (<10) arrays are allocated. There is then a time/precision trade-off. **Third**, the average allocation time for each trial *that invoked the GC* is computed. If it is above some *DELTA* it is considered a `1`, else a `0`.

Example:

Semantics for secure garbage collection

---


### 2017 - Pridgen, Picking up the Trash Exploiting Generational GC for Memory Analysis
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2018 - Belleville, Automated Software Protection for the Masses Against Side-Channels Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2018 - Cho, FPGASwarm High Throughput Model Checking on FPGAs
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2018 - Gawlik, Make JIT Spray Great Again
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2018 - Lipp, Meltdown Reading Kernel Memory from User Space
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[13/01/2021]*

A central security feature of operating systems is **memory isolation**. It ensures programs cannot access each other's or kernel's memory. It allows running multiple operations at the same time. This isolation is usually performed by a **supervisor bit** of the processor that defines whether a memory page of the kernel can be accessed or not . This bit can only be set when entering kernel code and is cleared when switching to user processes. This hardware feature **allows operating system to map the kernel into the address space of every process** and have efficient transitions from user processes to the kernel.

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


### 2019 - Du, XPC Architectural Support for Secure and Efficient Cross Process Call
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2019 - Kermarrec, LiteX  an open-source SoC builder and library based on Migen Python DSL
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2019 - Kocher, Spectre Attacks Exploiting Speculative Execution
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2019 - Patel, Runtime-Programmable Pipelines for Model Checkers on FPGAs
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2019 - Polito, GildaVM a Non-Blocking IO Architecture for the Cog
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2019 - Schwarz, ZombieLoad Cross-Privilege-Boundary Data Sampling
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2019 - Varoumas, High-level programming models for microcontrollers with scarce resources
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2020 - Agache, Firecracker Lightweight Virtualization for Serverless Applications
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2020 - Bruant, System Verilog to Chisel Translation for Faster
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


### 2020 - Fumero, Running Parallel Bytecode Interpreters on Heterogeneous Hardware
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2020 - Lee, Keystone An Open Framework for Architecting Trusted Execution Environments
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2020 - Lima, Exposing Bugs in JavaScript Engines through Test Transplantation and Differential Testing
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


### 2020 - Schrammel, Donky Domain Keys - Efficient In-Process Isolation for RISC-V and x86
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[22/04/2021]

Need for memory isolation to secure any system. This can be applied to any layer of the software stack (e.g. process isolation, separate address spaces, etc.). Donky consists of a **hardware-software co-design providing strong in-process isolation guarantees based on memory protection keys**. It also offers **pure userspace policy management with negligible overhead and full backward-compatibility**.

RISC-V comprises the unprivileged ISA and privileged ISA. Control and Status Registers (CSR) allows configuring the CPU , access performance metrics and additional exception handling. They are prefixed with `m` (machine), `s` (supervisor) or `u` (user). To handle exceptions,  the CPU switches to machine mode and jumps to the address specified in the trap-vector base-address register (`mtvec`). RISC-V specifies a "Standard Extension for User-Level Interrupts" as **N extension**.

Modern CPUs support virtual address spaces for process isolation. For virtual-to-physical translation, address spaces are mapped in blocks of pages (4KiB). Their entries are cached in the translation-lookaside buffer (TLB). Page-table entries (PTE) help manage permissions per page such that the same physical page can be mapped in multiple virtual address spaces. Kernel level switches are required to update permissions, switch address space, etc.  An extension to page-based memory is enabled with memory protection keys. PTE are tagged with a protection key but the permissions are stored separately. Keys are associated with a protection domain and each memory region can have one associated key. Example: Intel MPK, ARM Memory Domains, IBM Power, etc.

JavaScript is **jitted** and sandboxed through browsers to enforce security. The source code is dynamically first compiled into an intermediate representation which is then interpreted and executed. Another component analyses the runtime and further optimizes the bytecode directly into machine code. This requires the code region to be both writable and executable. In V8, an ***Isolate*** is an independent copy of the entire JavaScript runtime environment (*code cache, gc and call stack*). As sandbox escapes are still possible, an additional security uses process isolation.

**Software design:** the Donky Monitor is the **trusted handler in charge of managing in-process access policies and securing domains from each other**. Any operation on domains or protection keys will invoke the Donky Monitor. Domain switches guarded with `dcalls`, tampering guarded with memory encapsulation in a separate domain, security enforced by a hardware call-gate mechanism that enforces the entry point. The Donky API expands the **POSIX** interface. It allows to manage domains, protection keys and associated memory, and share keys with other domains.

**Hardware design:** Memory protection keys are configured in the PTE of a process (upmost 10 bits). The userspace register (`DKRU`) can load **4 different protection keys simultaneously**. Each loaded key **enables the read/write of the corresponding PTE**. Additionally, each slot has a specific bit to enforce read-only mode. The monitor bit (upmost of `DKRU`) can be cleared to prevent unauthorized alteration of the protection key policy. A new exception is raised when a security violation is detected while the monitor bit in `DKRU` is cleared. The MMU is extended to verify that for any data access the protection key in the PTE matches at least one loaded in `DKRU`.

**Security Evaluation:** *Hardware call gates* prevent code-reuse attacks on Donky Monitor. *System calls and signals* are interposed by Donky by redirecting them to the Monitor. The *Donky Monitor* itself validates all inputs in the *Donky API*.



---


### 2020 - Taemin, NoJITsu Locking Down Javascript
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[04/05/2021]

Initially JIT compilers wrote all run-time generated code onto memory pages that were simultaneously writable and executable throughout the execution of the script. This led to **code-injection** attacks. Later JIT engines added support for **W+X policies** by doubly-mapping JIT pages instead. This meant that JIT code could no longer be found on memory pages that were simultaneously writable and executable. **JIT spraying** attacks still made their way through injecting instructions without writing directly to the pages. This led to the use of **constant blinding**, **constant elimination and code obfuscation**, **code randomization** or **control-flow integrity**. Successfully defending against **code-reuse** is more challenging since an attacker can traverse and disassemble ode pages to dynamically generate a **ROP chain** at run-time. **Randomization** and **execute-only memory** leverage this type of attacks. An attacker can still inject code with **data-only attacks**. Corrupting the intermediate representation without overwriting any code pointers can make the JIT generate malicious code. Defenses propose isolating the compilation from the execution of JIT code through **separate processes** or **hardware-based trusted execution environments**.

**Threat model:** Assume that the system has ***code-injection defense*** (W+X) set, ***code-reuse defense*** (ASLR, CFI) set, ***hardware-based memory protection features*** (Intel MPK) in place and a ***memory-corruption vulnerability*** (ability to arbitrarily corrupt any part of the program's address space).

**SpiderMonkey Implementation:** *Speculative optimization* makes the hypothesis of some type for example and checks that it holds at runtime otherwise it goes back to the standard path through the interpreter. *Native functions* are C++ functions that are registered as `JSNative` functions and are often not inlined and the control is transferred to an internal calling convention. Several regions play a crucial role in ensuring the correct and secure operation of the script engine: (1) bytecode region, (2) the JIT code cache (3) the JIT compiler data, (4) the JavaScript data objects and (5) the object tables.

**Interpreter Attack:** First, the attacker **locates** the **JavaScript context object** and the **JavaScript function objects** of a victim function (i.e. any function we can call from JavaScript). Once the two objects are located, the attacker **overwrites** the f**unction address** contained in the function object with the **address of a target function**. Finally, the attacker **invokes the victim function**. 

---

**NoJITsu design**

 A novel defense that provides fine-grained memory protection to lock down real-world scripting engines. As switching between interpreted and JIT'ed code happens frequently (on a per-function basis), an efficient implementation is key. The interpreter *cannot* be moved out-of-process as proposed for the JIT compiler. Automated dynamic and static analysis are used to restrict memory-access permissions within the scripting engine to the bare minimum. 

Current JIT engines do not distinguish between different kinds of data sections and have little to no security policies. Bytecodes, Objects table, Objects, JIT IR are usually stored in writable memory even though they are rarely overwritten. **This space can be used to manipulate the data structures.** JIT'ed code is usually protected as R/X memory only putting them to R/W when recompiling code. **A code-reuse attack is possible on this region.**

These threats can be countered by deploying **fine-grained security policies** to lock down access permissions for each of the main data regions we identified based on their lifetime and usage within the JIT engine. The data structures mentioned earlier are placed in different memory domains, enabling *write* when, where and as long it is needed before revoking it. Each new type of data is given a specific key. The different regions are:

**JIT Code:** The main goal of the approach is to implement ***execute-only support for JIT code***. The JIT code has to remain ***non-writable*** to prevent attackers to have direct access to the CPU, however this has to be leveraged when emitting a new compiled version of the code. It also needs to be ***non-readable*** to avoid JIT-ROP attacks that need to discover code-reuse gadgets at runtime. However, it needs to be readable because of constant values or target addresses in jump tables. The readable data needs to be separated into a dedicated read-only region.

**Static Code:** The static code regions include the code sections of the JavaScript engine itself and the dynamic libraries loaded into memory. Unlike the JIT code region, it cannot be subject to malicious code injection but can be used as a large code base for code-reuse gadgets. It has to be set to execute-only so the attacker cannot disclose executable memory regions to chain gadgets. **XOM-Switch** is used to enforce execute-only permissions.

**JIT IR:** The IR can be corrupted from another thread and the thread compiling the IR into machine code is the ***only one with write permission***.

**Bytecodes and Object Tables:** Similar to the JIT code, they should be writable only when they are generated during compilation. They then remain read-only throughout the execution. Write access is allowed only when the script parser generates them and immediately made non-writable afterwards.

**JavaScript Objects:** The JS objects can be written to frequently at any point of the program execution and several flags must be updated at run time (reference counter, GC flag). They are separated into two protection domains depending on the types they encapsulate: one for s**ensitive data objects** and the other for **primitive data objects**. An object is *sensitive* if it contains sensitive information such as *function pointers,* *object shape metadata*, *scope metadata* or *JIT code*. By separating the two types, those object classes are not writable at the same time, this way an attacker cannot setup an object type confusion to corrupt sensitive objects using primitive data types. Changing object permissions while the JIT code executes is too costly in terms of overhead so *all access restrictions to primitive data* are lifted during JIT code execution and set back again when the control is transferred back to the JS engine itself. Protections for *sensitive* objects are still enforced to prevent the attacker to manipulate frequently exploited objects (Shapes, Cells, Functions, etc.).

---

**Implementation**

**Intel's MPK (Memory Protection Key):** Allow user-space programs to manage access permissions for up to 16 memory domains. To change the access permissions for a domain, the program uses an unprivileged instruction to write to the thread-local PKRU register. While PKRU write is unprivileged, an attacker has to acquire arbitrary code execution to set its value.

**Compartmentalization:** 

- (1) *Jump table separation* to split jump target addresses from the rest of the jump table. This allows the jump addresses to be read-only and not executable.
- (2) *Permission change routine*: before writing to a protected region, we insert a call to `set_pkru` to change the value of the `PKRU` register to enable write access. The function first checks if the current `PKRU` value is already correct to avoid losing cycles by flushing the CPU pipeline.
- (3) *JS object protection*: In JS, the GC is responsible for allocating and reclaiming S objects on the heap. SpiderMonkey provides data isolation through *compartments* by keeping objects from the same origin within the same compartment with strict isolation. JS objects protected by NoJITsu include *shapes* which contain the object layout information, *script  objects* that point to bytecode. The unit of management is a *cell* that are classified on their allocation kind.

**Instrumenting Memory Accesses:**  

- (1) *Code Transformation and Signal handler*: Intentional traps when write accesses  to a protected region occur and catches the resulting segmentation faults in a custom signal handler.
- (2) *Dynamic Object-Flow Analysis*: Only read permissions are granted to JavaScript objects. At runtime, when a `segfault` is obtained, if it is caused by an MPK violation, it logs the faulting code to be processed later by the LLVM passes. Before entering the signal handler, the OS saves the register state of the interrupted process in memory and recovers the registers after the signal handler returns.
- (3) *Accessor Functions*: Only a limited number of functions can directly write to an object. Based on SpiderMonkey, any other function should invoke one of these accessor functions to modify a JS object. These functions can be decoupled in *Member Accessors* (private attributes), *Payload Accessors*, *Initialization Accessors* or *GC Accessors*.



---


### 2020 - Valdiek, ERIM Secure Efficient In-process Isolation with Protection Keys MPK
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


### 2021 - Dobis, Open-Source Verification with Chisel and Scala
<!-- Please prefix the notes with the date as in [22/12/2020] -->

---


