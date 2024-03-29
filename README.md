 ## VM-related articles

This repository contains the different articles and the bibliography (in BibTeX format) related to the VM world (to a LARGE extent). The notes in each of the folders, namely `notes.md` are integrated in the bibliography using a Python script in `utils.py`.  This script contains several useful helpers:

```bash
$ python lectern.py --process
# or -p. Creates a repository and empty notes.md file for each pdf in

$ python lectern.py --genreadme
# or -g. Adds the notes to the present README.md file

$ python lectern.py --bibgui
# or -b. Opens the GUI to generate a bibgen.bib file with selected articles.

$ python lectern.py --missbib
# or -m. Checks for missing or empty biblio files.
```

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

[1991 - Holzle, Optimizing Dynamically-Typed Object-Oriented Languages with Polymorphic Inline Caches](#1991---Holzle-Optimizing-Dynamically-Typed-Object-Oriented-Languages-with-Polymorphic-Inline-Caches)

[1992 - Holzle, Debugging Optimized Code with Dynamic Deoptimization](#1992---Holzle-Debugging-Optimized-Code-with-Dynamic-Deoptimization)

[1993 - Wahbe, Efficient Software-Based Fault Isolation](#1993---Wahbe-Efficient-Software-Based-Fault-Isolation)

[1994 - Holzle, A Third-Generation SELF Implementation Reconciling Responsiveness with Performance](#1994---Holzle-A-Third-Generation-SELF-Implementation-Reconciling-Responsiveness-with-Performance)

[1995 - Click, A Simple Graph-Based Intermediate Representation](#1995---Click-A-Simple-Graph-Based-Intermediate-Representation)

[1995 - Dean, Optimization of Object-Oriented Programs Using Static Class Hierarchy Analysis](#1995---Dean-Optimization-of-Object-Oriented-Programs-Using-Static-Class-Hierarchy-Analysis)

[1995 - Ertl, Stack Caching for Interpreters](#1995---Ertl-Stack-Caching-for-Interpreters)

[1995 - Gosling, Java Intermediate Bytecodes](#1995---Gosling-Java-Intermediate-Bytecodes)

[1995 - Yellin, Low-Level Security in Java](#1995---Yellin-Low-Level-Security-in-Java)

[1996 - Bacon, Fast Static Analysis of C Virtual Function Calls](#1996---Bacon-Fast-Static-Analysis-of-C-Virtual-Function-Calls)

[1997 - Agesen, Design and Implementation of PEp a Java Just-In-Time Translator](#1997---Agesen-Design-and-Implementation-of-PEp-a-Java-Just-In-Time-Translator)

[1997 - Forrest, Building Diverse Computer Systems](#1997---Forrest-Building-Diverse-Computer-Systems)

[1997 - Franz, Slim Binaries](#1997---Franz-Slim-Binaries)

[1997 - Ingals, Back to the Future The Story of Squeak a Practical Smalltalk Written in Itself](#1997---Ingals-Back-to-the-Future-The-Story-of-Squeak-a-Practical-Smalltalk-Written-in-Itself)

[1998 - Piumarta, Optimizing Direct Threaded Code by Selective Inlining](#1998---Piumarta-Optimizing-Direct-Threaded-Code-by-Selective-Inlining)

[1998 - Taivalsaari, Implementing a Java Virtual Machine in the Java Programming Language](#1998---Taivalsaari-Implementing-a-Java-Virtual-Machine-in-the-Java-Programming-Language)

[1999 - Burke, The Jalapeno Dynamic Optimizing Compiler for Java](#1999---Burke-The-Jalapeno-Dynamic-Optimizing-Compiler-for-Java)

[1999 - Futamara, Partial Evaluation of Computation Process an Approach to a Compiler-Compiler](#1999---Futamara-Partial-Evaluation-of-Computation-Process-an-Approach-to-a-Compiler-Compiler)

[1999 - Wolczko, Self Includes Smalltalk](#1999---Wolczko-Self-Includes-Smalltalk)

[2000 - Alpern, The Jalapeno Virtual Machine](#2000---Alpern-The-Jalapeno-Virtual-Machine)

[2000 - Arnold, Adaptive Optimization in the Jalapeno JVM](#2000---Arnold-Adaptive-Optimization-in-the-Jalapeno-JVM)

[2000 - Bala, Dynamo a Transparent Dynamic Optimisation System](#2000---Bala-Dynamo-a-Transparent-Dynamic-Optimisation-System)

[2000 - Diehl, Abstract Machines for Programming Language Implementation](#2000---Diehl-Abstract-Machines-for-Programming-Language-Implementation)

[2001 - Cheng, A Parallel Real-Time Garbage Collector](#2001---Cheng-A-Parallel-Real-Time-Garbage-Collector)

[2001 - Paleczny, The Java HotSpot Server Compiler](#2001---Paleczny-The-Java-HotSpot-Server-Compiler)

[2002 - Click, Fast Subtype Checking in the HotSpot JVM](#2002---Click-Fast-Subtype-Checking-in-the-HotSpot-JVM)

[2002 - Ertl, Vmgen a Generator of Efficient Virtual Machine Interpreters](#2002---Ertl-Vmgen-a-Generator-of-Efficient-Virtual-Machine-Interpreters)

[2002 - Lattner, The LLVM Instruction Set and Compilation Strategy](#2002---Lattner-The-LLVM-Instruction-Set-and-Compilation-Strategy)

[2002 - Ozdoganoglu, SmashGuard A Hardware Solution To Prevent Attacks on the Function Return Address](#2002---Ozdoganoglu-SmashGuard-A-Hardware-Solution-To-Prevent-Attacks-on-the-Function-Return-Address)

[2003 - Asokan, Man-in-the-Middle in Tunneled Authentication Protocols](#2003---Asokan-Man-in-the-Middle-in-Tunneled-Authentication-Protocols)

[2003 - Dehnert, The Transmeta Code Morphing - Software Using Speculation recovery and Adaptive Retranslation to Address Real-Life Challenges](#2003---Dehnert-The-Transmeta-Code-Morphing---Software-Using-Speculation-recovery-and-Adaptive-Retranslation-to-Address-Real-Life-Challenges)

[2003 - Ertl, The Structure and Performance of Efficient Interpreters](#2003---Ertl-The-Structure-and-Performance-of-Efficient-Interpreters)

[2003 - Fink, Design Implementation and Evaluation of Adaptive Recompilation with On-Stack Replacement](#2003---Fink-Design-Implementation-and-Evaluation-of-Adaptive-Recompilation-with-On-Stack-Replacement)

[2003 - Govindavajhala, Using Memory Errors to Attack a Virtual Machine](#2003---Govindavajhala-Using-Memory-Errors-to-Attack-a-Virtual-Machine)

[2003 - Merrill, GENERIC and GIMPLE A New Tree Representation for Entire Functions](#2003---Merrill-GENERIC-and-GIMPLE-A-New-Tree-Representation-for-Entire-Functions)

[2003 - Ogel, Towards Active Applications the Virtual Virtual Machine Project](#2003---Ogel-Towards-Active-Applications-the-Virtual-Virtual-Machine-Project)

[2003 - Pax, Pax Team NOEXEC](#2003---Pax-Pax-Team-NOEXEC)

[2003 - Shaylor, A Java Virtual Machine Architecture for Very Small Devices](#2003---Shaylor-A-Java-Virtual-Machine-Architecture-for-Very-Small-Devices)

[2004 - Blackburn, Oil and Water High Performance Garbage Collection in Java with MMTk](#2004---Blackburn-Oil-and-Water-High-Performance-Garbage-Collection-in-Java-with-MMTk)

[2004 - Chambers, A Retrospective on Customization Optimizing Compiler Technology for SELF a Dynamically-Typed Object-Oriented Programming Language](#2004---Chambers-A-Retrospective-on-Customization-Optimizing-Compiler-Technology-for-SELF-a-Dynamically-Typed-Object-Oriented-Programming-Language)

[2004 - Ertl, Combining Stack Caching with Dynamic Superinstructions](#2004---Ertl-Combining-Stack-Caching-with-Dynamic-Superinstructions)

[2004 - Garfinkel, Ostia A Delegating Architecture for Secure System Call Interposition](#2004---Garfinkel-Ostia-A-Delegating-Architecture-for-Secure-System-Call-Interposition)

[2004 - Ravi, Security in Embedded Systems Design Challenges](#2004---Ravi-Security-in-Embedded-Systems-Design-Challenges)

[2004 - Sachindran, MC2 High-Performance Garbage Collection for Memory-Constrained Environments](#2004---Sachindran-MC2-High-Performance-Garbage-Collection-for-Memory-Constrained-Environments)

[2004 - VanDeVen, New Security Enhancements in Red Hat Enterprise Linux](#2004---VanDeVen-New-Security-Enhancements-in-Red-Hat-Enterprise-Linux)

[2005 - Chen, Non Control Data Attacks Are Realistic Threats](#2005---Chen-Non-Control-Data-Attacks-Are-Realistic-Threats)

[2005 - Click, The Pauseless GC Algorithm](#2005---Click-The-Pauseless-GC-Algorithm)

[2005 - Faes, FPGA-Aware Garbage Collection in Java](#2005---Faes-FPGA-Aware-Garbage-Collection-in-Java)

[2005 - Ierusalimschy, The Implementation of LUA5](#2005---Ierusalimschy-The-Implementation-of-LUA5)

[2005 - Krall, Advances in Interpreters Virtual Machines and Emulators](#2005---Krall-Advances-in-Interpreters-Virtual-Machines-and-Emulators)

[2005 - Sheridan, Practical Testing of a C99 Compiler using Output Comparison](#2005---Sheridan-Practical-Testing-of-a-C99-Compiler-using-Output-Comparison)

[2005 - Spett, Cross-Site Scripting](#2005---Spett-Cross-Site-Scripting)

[2005 - Ungar, Constructing a Metacircular Virtual Machine in an Exploratory Programming Environment](#2005---Ungar-Constructing-a-Metacircular-Virtual-Machine-in-an-Exploratory-Programming-Environment)

[2006 - Gal, HotpathVM An Effective JIT Compiler for Resource-Constrained Devices](#2006---Gal-HotpathVM-An-Effective-JIT-Compiler-for-Resource-Constrained-Devices)

[2006 - Leroy, Formal Certification of a Compiler Backend](#2006---Leroy-Formal-Certification-of-a-Compiler-Backend)

[2006 - Piumarta, Open extensible object models](#2006---Piumarta-Open-extensible-object-models)

[2006 - Rigo, PyPys Approach to Virtual Machine Construction](#2006---Rigo-PyPys-Approach-to-Virtual-Machine-Construction)

[2006 - Russell, Eliminating Synchronization-Related Atomic Operations with Biased Locking and Bulk Rebiasing](#2006---Russell-Eliminating-Synchronization-Related-Atomic-Operations-with-Biased-Locking-and-Bulk-Rebiasing)

[2007 - Bolz, How to not write Virtual Machines for Dynamic Languages](#2007---Bolz-How-to-not-write-Virtual-Machines-for-Dynamic-Languages)

[2007 - Shacham, The Geometry of Innocent Flesh on the Bone Return-into-libc without Function Calls on the x86](#2007---Shacham-The-Geometry-of-Innocent-Flesh-on-the-Bone-Return-into-libc-without-Function-Calls-on-the-x86)

[2007 - Sotirov, Heap Feng Shui Javascript](#2007---Sotirov-Heap-Feng-Shui-Javascript)

[2008 - Ancona, RPython a Step Towards Reconciling Dynamically and Statically Typed OO Languages](#2008---Ancona-RPython-a-Step-Towards-Reconciling-Dynamically-and-Statically-Typed-OO-Languages)

[2008 - Barth, Robust Defenses for Cross Site Request Forgery](#2008---Barth-Robust-Defenses-for-Cross-Site-Request-Forgery)

[2008 - Fuess, An FPGA Implementation of Explicit-State Model Checking](#2008---Fuess-An-FPGA-Implementation-of-Explicit-State-Model-Checking)

[2008 - Heiser, The Role Of Virtualization in Embedded Systems](#2008---Heiser-The-Role-Of-Virtualization-in-Embedded-Systems)

[2008 - Kotzmann, Design of the Java HotSpot Client Compiler for Java 6](#2008---Kotzmann-Design-of-the-Java-HotSpot-Client-Compiler-for-Java-6)

[2008 - One, Smashing the Stack for Fun and Profit](#2008---One-Smashing-the-Stack-for-Fun-and-Profit)

[2009 - Abadi, Control-Flow Integrity Principles Implementations and Applications](#2009---Abadi-Control-Flow-Integrity-Principles-Implementations-and-Applications)

[2009 - Bolz, Tracing the Meta-Level PyPys Tracing JIT Compiler](#2009---Bolz-Tracing-the-Meta-Level-PyPys-Tracing-JIT-Compiler)

[2009 - Callegati, Man-in-the-Middle Attack to the HTTPS Protocol](#2009---Callegati-Man-in-the-Middle-Attack-to-the-HTTPS-Protocol)

[2009 - Frampton, Demystifying Magic High-Level Low-Level Programming](#2009---Frampton-Demystifying-Magic-High-Level-Low-Level-Programming)

[2009 - Gal, Trace-based Just-in-Time Type Specialization for Dynamic Languages](#2009---Gal-Trace-based-Just-in-Time-Type-Specialization-for-Dynamic-Languages)

[2010 - Agesen, The Evolution of an X86 Virtual Machine Monitor](#2010---Agesen-The-Evolution-of-an-X86-Virtual-Machine-Monitor)

[2010 - Bania, JIT Spraying and Mitigations](#2010---Bania-JIT-Spraying-and-Mitigations)

[2010 - Blazakis, Interpreter Exploitation Pointer Inference and JIT Spraying](#2010---Blazakis-Interpreter-Exploitation-Pointer-Inference-and-JIT-Spraying)

[2010 - Brunthaler, Inline Caching Meets Quickening](#2010---Brunthaler-Inline-Caching-Meets-Quickening)

[2010 - Checkoway, Return-Oriented Programming without Returns](#2010---Checkoway-Return-Oriented-Programming-without-Returns)

[2010 - DeGroef, JITsec Just-in-Time Security for Code Injection Attacks](#2010---DeGroef-JITsec-Just-in-Time-Security-for-Code-Injection-Attacks)

[2010 - Ehringer, The Dalvik Virtual Machine Architecture](#2010---Ehringer-The-Dalvik-Virtual-Machine-Architecture)

[2010 - Erlingsson, Low-Level Software Security by Example](#2010---Erlingsson-Low-Level-Software-Security-by-Example)

[2010 - Onarlioglu, G-Free](#2010---Onarlioglu-G-Free)

[2010 - Reynolds, Lightweight Modeling of Java Virtual Machine](#2010---Reynolds-Lightweight-Modeling-of-Java-Virtual-Machine)

[2010 - Rizzo, Practical Padding Oracle Attacks](#2010---Rizzo-Practical-Padding-Oracle-Attacks)

[2010 - Siefers, Robusta Taming the Native Beast of the JVM](#2010---Siefers-Robusta-Taming-the-Native-Beast-of-the-JVM)

[2010 - Sintsov, Writing JIT Spray Shellcode for Fun and Profit](#2010---Sintsov-Writing-JIT-Spray-Shellcode-for-Fun-and-Profit)

[2010 - Swaine, Back to the futures Incremental Parallelization of Existing Sequential Runtime Systems](#2010---Swaine-Back-to-the-futures-Incremental-Parallelization-of-Existing-Sequential-Runtime-Systems)

[2010 - Wei, Secure Dynamic Code Generation Against Spraying](#2010---Wei-Secure-Dynamic-Code-Generation-Against-Spraying)

[2010 - Yee, Native Client A Sandbox for Portable, Untrusted x86 Native Code](#2010---Yee-Native-Client-A-Sandbox-for-Portable,-Untrusted-x86-Native-Code)

[2011 - Ansel, Language-Independent Sandboxing of Just-In-Time Compilation and Self-Modifying Code](#2011---Ansel-Language-Independent-Sandboxing-of-Just-In-Time-Compilation-and-Self-Modifying-Code)

[2011 - Bletsch, Jump-Oriented Programming A New Class of Code-Reuse Attack](#2011---Bletsch-Jump-Oriented-Programming-A-New-Class-of-Code-Reuse-Attack)

[2011 - Bolz, Runtime Feedback in a Meta-Tracing JIT for Efficient Dynamic Languages](#2011---Bolz-Runtime-Feedback-in-a-Meta-Tracing-JIT-for-Efficient-Dynamic-Languages)

[2011 - Cai, JVM virtual method invoking optimization based on CAM table](#2011---Cai-JVM-virtual-method-invoking-optimization-based-on-CAM-table)

[2011 - Chen, JITDefender A Defense against JIT Spraying Attacks](#2011---Chen-JITDefender-A-Defense-against-JIT-Spraying-Attacks)

[2011 - Davi, ROPdefender A Detection Tool to Defend Against Return-Oriented Programming Attacks](#2011---Davi-ROPdefender-A-Detection-Tool-to-Defend-Against-Return-Oriented-Programming-Attacks)

[2011 - Haupt, CSOMPL a virtual machine product line](#2011---Haupt-CSOMPL-a-virtual-machine-product-line)

[2011 - Miranda, The Cog Smalltalk Virtual Machine Writing a JIT in a High-Level Language](#2011---Miranda-The-Cog-Smalltalk-Virtual-Machine-Writing-a-JIT-in-a-High-Level-Language)

[2011 - Rohlf, The Security Challenges of Client-Side Just-in-Time Engines](#2011---Rohlf-The-Security-Challenges-of-Client-Side-Just-in-Time-Engines)

[2012 - Barbu, Application-Replay Attack on Java Cards When the Garbage Collector Gets Confused](#2012---Barbu-Application-Replay-Attack-on-Java-Cards-When-the-Garbage-Collector-Gets-Confused)

[2012 - Pappas, Smashing the Gadgets: Hindering Return-Oriented Programming Using In-Place Code Randomization](#2012---Pappas-Smashing-the-Gadgets:-Hindering-Return-Oriented-Programming-Using-In-Place-Code-Randomization)

[2012 - Rohou, Tiptop Hardware Performance Counters for the Masses](#2012---Rohou-Tiptop-Hardware-Performance-Counters-for-the-Masses)

[2012 - Wu, RIM An Architecture for JIT Spraying Mitigation](#2012---Wu-RIM-An-Architecture-for-JIT-Spraying-Mitigation)

[2012 - Wuerthinger, Self-optimizing AST interpreters](#2012---Wuerthinger-Self-optimizing-AST-interpreters)

[2013 - Chen, JITSafe a Framework Against Just-In-Time Spraying Attacks](#2013---Chen-JITSafe-a-Framework-Against-Just-In-Time-Spraying-Attacks)

[2013 - Duboscq, Graal IR An Extensible Declarative Intermediate Representation](#2013---Duboscq-Graal-IR-An-Extensible-Declarative-Intermediate-Representation)

[2013 - Eckert, Hardware Based Security Enhanced Direct Memory Access](#2013---Eckert-Hardware-Based-Security-Enhanced-Direct-Memory-Access)

[2013 - Fournet, Fully Abstract Compilation to Javascript](#2013---Fournet-Fully-Abstract-Compilation-to-Javascript)

[2013 - Homescu, Librando Transparent Code Randomization for JIT Compilers](#2013---Homescu-Librando-Transparent-Code-Randomization-for-JIT-Compilers)

[2013 - Kulkarni, Automatic Construction of Inlining Heuristics using Machine Learning](#2013---Kulkarni-Automatic-Construction-of-Inlining-Heuristics-using-Machine-Learning)

[2013 - Marr, Supporting Concurrency Abstractions in High-level Language Virtual Machines](#2013---Marr-Supporting-Concurrency-Abstractions-in-High-level-Language-Virtual-Machines)

[2013 - Papadogiannakis, ASIST Architectural Support for Instruction Set Randomization](#2013---Papadogiannakis-ASIST-Architectural-Support-for-Instruction-Set-Randomization)

[2013 - Snow, Just-In-Time Code Reuse On the Effectiveness of Fine-Grained Address Space Layout Randomization](#2013---Snow-Just-In-Time-Code-Reuse-On-the-Effectiveness-of-Fine-Grained-Address-Space-Layout-Randomization)

[2013 - Wimmer, Maxine an Approachable Virtual Machine for and in Java](#2013---Wimmer-Maxine-an-Approachable-Virtual-Machine-for-and-in-Java)

[2013 - Wuerthinger, One VM to Rule Them All](#2013---Wuerthinger-One-VM-to-Rule-Them-All)

[2014 - Backes, Oxymoron Making Fine-Grained Memory Randomization Practical by Allowing Code Sharing](#2014---Backes-Oxymoron-Making-Fine-Grained-Memory-Randomization-Practical-by-Allowing-Code-Sharing)

[2014 - Bittau, Hacking Blind](#2014---Bittau-Hacking-Blind)

[2014 - Bosman, Framing Signals A Return to Portable Shellcode](#2014---Bosman-Framing-Signals-A-Return-to-Portable-Shellcode)

[2014 - Carlini, ROP is Still Dangerous Breaking Modern Defenses](#2014---Carlini-ROP-is-Still-Dangerous-Breaking-Modern-Defenses)

[2014 - Davi, Stitching the Gadgets On the Ineffectiveness of Coarse-Grained Control-Flow Integrity Protection](#2014---Davi-Stitching-the-Gadgets-On-the-Ineffectiveness-of-Coarse-Grained-Control-Flow-Integrity-Protection)

[2014 - Duboscq, Speculation Without Regret Reducing Deoptimization Meta-data in the Graal Compiler](#2014---Duboscq-Speculation-Without-Regret-Reducing-Deoptimization-Meta-data-in-the-Graal-Compiler)

[2014 - Eckert, FPGA-Based System Virtual Machines](#2014---Eckert-FPGA-Based-System-Virtual-Machines)

[2014 - Freundenberg, SqueakJS a Modern and Practical Smalltalk that Runs in any Browser](#2014---Freundenberg-SqueakJS-a-Modern-and-Practical-Smalltalk-that-Runs-in-any-Browser)

[2014 - Goktas, Out Of Control Overcoming Control-Flow Integrity](#2014---Goktas-Out-Of-Control-Overcoming-Control-Flow-Integrity)

[2014 - Humer, A Domain-Specific Language for Building Self-Optimizing AST Interpreters](#2014---Humer-A-Domain-Specific-Language-for-Building-Self-Optimizing-AST-Interpreters)

[2014 - Jain, Sok Introspections on Trust and the Semantic Gap](#2014---Jain-Sok-Introspections-on-Trust-and-the-Semantic-Gap)

[2014 - Jauernig, Lobotomy An Architecture for JIT Spraying Mitigation](#2014---Jauernig-Lobotomy-An-Architecture-for-JIT-Spraying-Mitigation)

[2014 - Kuznetsov, Code Pointer Integrity](#2014---Kuznetsov-Code-Pointer-Integrity)

[2014 - Lin, A Security PaaS Container with a Customized JVM](#2014---Lin-A-Security-PaaS-Container-with-a-Customized-JVM)

[2014 - Niu, RockJIT Securing Just-In-Time Compilation Using Modular Control-Flow Integrity](#2014---Niu-RockJIT-Securing-Just-In-Time-Compilation-Using-Modular-Control-Flow-Integrity)

[2014 - Seaton, Debugging at Full Speed](#2014---Seaton-Debugging-at-Full-Speed)

[2014 - Stadler, Partial Escape Analysis and Scalar Replacement for Java](#2014---Stadler-Partial-Escape-Analysis-and-Scalar-Replacement-for-Java)

[2014 - Woss, An Object Storage Model for the Truffle Language Implementation Framework](#2014---Woss-An-Object-Storage-Model-for-the-Truffle-Language-Implementation-Framework)

[2015 - Asanovic, The Berkeley Out-of-Order Machine BOOM An Industry Competitive Synthesizable Parameterized RISC-V](#2015---Asanovic-The-Berkeley-Out-of-Order-Machine-BOOM-An-Industry-Competitive-Synthesizable-Parameterized-RISC-V)

[2015 - Athanasakis, The Devil is in the Constants Bypassing Defenses](#2015---Athanasakis-The-Devil-is-in-the-Constants-Bypassing-Defenses)

[2015 - Carlini, Control-Flow Bending: On the Effectiveness of Control-Flow Integrity](#2015---Carlini-Control-Flow-Bending:-On-the-Effectiveness-of-Control-Flow-Integrity)

[2015 - Evans, Missing the Pointer on the Effectiveness of Code Pointer Integrity](#2015---Evans-Missing-the-Pointer-on-the-Effectiveness-of-Code-Pointer-Integrity)

[2015 - Grimmer, Dynamically Composing Languages in a Modular Way Supporting C Extensions for Dynamic Languages](#2015---Grimmer-Dynamically-Composing-Languages-in-a-Modular-Way-Supporting-C-Extensions-for-Dynamic-Languages)

[2015 - Gunadi, Formal Certification of Android Bytecode](#2015---Gunadi-Formal-Certification-of-Android-Bytecode)

[2015 - Hussein, Impact of GC Design on Power and Performance for Android](#2015---Hussein-Impact-of-GC-Design-on-Power-and-Performance-for-Android)

[2015 - Jangda, Adaptive Just-in-time Code Diversification](#2015---Jangda-Adaptive-Just-in-time-Code-Diversification)

[2015 - Lam, Numba](#2015---Lam-Numba)

[2015 - Lian, Too LeJIT to Quit Extending JIT Spraying to ARM](#2015---Lian-Too-LeJIT-to-Quit-Extending-JIT-Spraying-to-ARM)

[2015 - Lockhart, Pydgin Generating Fast Instruction Set Simulators from Simple Architecture Descriptions with Meta-Tracing JIT Compilers](#2015---Lockhart-Pydgin-Generating-Fast-Instruction-Set-Simulators-from-Simple-Architecture-Descriptions-with-Meta-Tracing-JIT-Compilers)

[2015 - McGillion, Open-TEE An Open Virtual Trusted Execution Environment](#2015---McGillion-Open-TEE-An-Open-Virtual-Trusted-Execution-Environment)

[2015 - Prakash, Defeating ROP Through Denial of Stack Pivot](#2015---Prakash-Defeating-ROP-Through-Denial-of-Stack-Pivot)

[2015 - Rohou, Branch Prediction and the Performance of Interpreters Dont Trust Folklore](#2015---Rohou-Branch-Prediction-and-the-Performance-of-Interpreters-Dont-Trust-Folklore)

[2015 - Sartor, The Impact of Virtual Machines on Embedded Systems](#2015---Sartor-The-Impact-of-Virtual-Machines-on-Embedded-Systems)

[2015 - Simon, Snippets Taking the High Road to a Low Level](#2015---Simon-Snippets-Taking-the-High-Road-to-a-Low-Level)

[2015 - Song, Exploiting and Protecting Dynamic Code Generation](#2015---Song-Exploiting-and-Protecting-Dynamic-Code-Generation)

[2015 - VanDeVanter, Building Debuggers and Other Tools We Can Have it All](#2015---VanDeVanter-Building-Debuggers-and-Other-Tools-We-Can-Have-it-All)

[2015 - Zhang, JITScope Protecting Web Users from Control-Flow Hijacking Attacks](#2015---Zhang-JITScope-Protecting-Web-Users-from-Control-Flow-Hijacking-Attacks)

[2016 - Asanovic, The Rocket Chip Generator](#2016---Asanovic-The-Rocket-Chip-Generator)

[2016 - Constan, Intel SGX Explained](#2016---Constan-Intel-SGX-Explained)

[2016 - Conti, A Survey of Man In The Middle Attack](#2016---Conti-A-Survey-of-Man-In-The-Middle-Attack)

[2016 - Gruss, Rowhammer js A Remote Software-Induced Fault Attack in JavaScript](#2016---Gruss-Rowhammer-js-A-Remote-Software-Induced-Fault-Attack-in-JavaScript)

[2016 - Hu, Data-Oriented Programming On the Expressiveness of Non-Control Data Attacks](#2016---Hu-Data-Oriented-Programming-On-the-Expressiveness-of-Non-Control-Data-Attacks)

[2016 - Ilbeyi, Pydgin for RISC-V A Fast and Productive Instruction-Set Simulator](#2016---Ilbeyi-Pydgin-for-RISC-V-A-Fast-and-Productive-Instruction-Set-Simulator)

[2016 - Lin, Rust as a Language for High Performance GC Implementation](#2016---Lin-Rust-as-a-Language-for-High-Performance-GC-Implementation)

[2016 - Lopriore, Memory Protection in Embedded Systems](#2016---Lopriore-Memory-Protection-in-Embedded-Systems)

[2016 - Maas, Grail Quest A New Proposal for Hardware-assisted Garbage Collection](#2016---Maas-Grail-Quest-A-New-Proposal-for-Hardware-assisted-Garbage-Collection)

[2016 - Maisuradze, What Cannot Be Read Cannot Be Leveraged Revisiting Assumptions of JIT-ROP Defenses](#2016---Maisuradze-What-Cannot-Be-Read-Cannot-Be-Leveraged-Revisiting-Assumptions-of-JIT-ROP-Defenses)

[2016 - Shoshitaishvili, (State of) The Art of War Offensive Techniques in Binary Analysis](#2016---Shoshitaishvili-(State-of)-The-Art-of-War-Offensive-Techniques-in-Binary-Analysis)

[2017 - Burow, Control-Flow Integrity Precision Security and Performance](#2017---Burow-Control-Flow-Integrity-Precision-Security-and-Performance)

[2017 - Delshadtehrani, Nile A Programmable Monitoring Coprocessor](#2017---Delshadtehrani-Nile-A-Programmable-Monitoring-Coprocessor)

[2017 - Frassetto, JITGuard Hardening Just-in-time Compilers with SGX](#2017---Frassetto-JITGuard-Hardening-Just-in-time-Compilers-with-SGX)

[2017 - Izraelevitz, Reusability is FIRRTL Ground Hardware Construction Languages Compiler Frameworks and Transformations](#2017---Izraelevitz-Reusability-is-FIRRTL-Ground-Hardware-Construction-Languages-Compiler-Frameworks-and-Transformations)

[2017 - Jangda, RandHeap Heap Randomization for mitigating Heap Spray Attacks in Virtual Machines](#2017---Jangda-RandHeap-Heap-Randomization-for-mitigating-Heap-Spray-Attacks-in-Virtual-Machines)

[2017 - Kotselidis, Cross-ISA Debugging in Meta-circular VMs](#2017---Kotselidis-Cross-ISA-Debugging-in-Meta-circular-VMs)

[2017 - Lian, A Call to ARMs Understanding the Costs and Benefits of JIT Spraying Mitigations](#2017---Lian-A-Call-to-ARMs-Understanding-the-Costs-and-Benefits-of-JIT-Spraying-Mitigations)

[2017 - Maas, Full System Simulation of Java Workloads with RISC-V and the Jikes Research Virtual Machine](#2017---Maas-Full-System-Simulation-of-Java-Workloads-with-RISC-V-and-the-Jikes-Research-Virtual-Machine)

[2017 - Maisuradze, Dachshund: Digging for and Securing Against Non-Blinded Constants in JIT Code](#2017---Maisuradze-Dachshund:-Digging-for-and-Securing-Against-Non-Blinded-Constants-in-JIT-Code)

[2017 - Pedersen, From Trash to Treasure Timing-Sensitive Garbage](#2017---Pedersen-From-Trash-to-Treasure-Timing-Sensitive-Garbage)

[2017 - Pridgen, Picking up the Trash Exploiting Generational GC for Memory Analysis](#2017---Pridgen-Picking-up-the-Trash-Exploiting-Generational-GC-for-Memory-Analysis)

[2017 - Reshetova, Randomization cannot stop BPF JIT spray](#2017---Reshetova-Randomization-cannot-stop-BPF-JIT-spray)

[2017 - Sinha, Reviving Instruction Set Randomization](#2017---Sinha-Reviving-Instruction-Set-Randomization)

[2018 - Belleville, Automated Software Protection for the Masses Against Side-Channels Attacks](#2018---Belleville-Automated-Software-Protection-for-the-Masses-Against-Side-Channels-Attacks)

[2018 - Biondo, The Guard’s Dilemma Efficient Code-Reuse Attacks Against Intel SGX](#2018---Biondo-The-Guard’s-Dilemma-Efficient-Code-Reuse-Attacks-Against-Intel-SGX)

[2018 - Cho, FPGASwarm High Throughput Model Checking on FPGAs](#2018---Cho-FPGASwarm-High-Throughput-Model-Checking-on-FPGAs)

[2018 - Fratric, Bypassing Mitigations by Attacking JIT Server in Microsoft Edge](#2018---Fratric-Bypassing-Mitigations-by-Attacking-JIT-Server-in-Microsoft-Edge)

[2018 - Gawlik, Make JIT Spray Great Again](#2018---Gawlik-Make-JIT-Spray-Great-Again)

[2018 - Lipp, Meltdown Reading Kernel Memory from User Space](#2018---Lipp-Meltdown-Reading-Kernel-Memory-from-User-Space)

[2018 - Miranda, Two Decades of Smalltalk VM Development Live VM Development through Simulation Tools](#2018---Miranda-Two-Decades-of-Smalltalk-VM-Development-Live-VM-Development-through-Simulation-Tools)

[2018 - Park, Bytecode Corruption Attacks are Real and How to Defend Against Them](#2018---Park-Bytecode-Corruption-Attacks-are-Real-and-How-to-Defend-Against-Them)

[2018 - Wu, A Side-channel Attack on HotSpot Heap Management](#2018---Wu-A-Side-channel-Attack-on-HotSpot-Heap-Management)

[2019 - Burow, SoK Shining Light on Shadow Stacks](#2019---Burow-SoK-Shining-Light-on-Shadow-Stacks)

[2019 - Choi, Reusable Inline Caching for JavaScript Performance](#2019---Choi-Reusable-Inline-Caching-for-JavaScript-Performance)

[2019 - De, FIXER Flow Integrity Extensions for Embedded RISC-V](#2019---De-FIXER-Flow-Integrity-Extensions-for-Embedded-RISC-V)

[2019 - Du, XPC Architectural Support for Secure and Efficient Cross Process Call](#2019---Du-XPC-Architectural-Support-for-Secure-and-Efficient-Cross-Process-Call)

[2019 - Fumero, Dynamic Application Reconfiguration on Heterogeneous Hardware](#2019---Fumero-Dynamic-Application-Reconfiguration-on-Heterogeneous-Hardware)

[2019 - Hedayati, Hodor Intra-Process Isolation for High-Throughput Data Plane Libraries](#2019---Hedayati-Hodor-Intra-Process-Isolation-for-High-Throughput-Data-Plane-Libraries)

[2019 - Kermarrec, LiteX  an open-source SoC builder and library based on Migen Python DSL](#2019---Kermarrec-LiteX--an-open-source-SoC-builder-and-library-based-on-Migen-Python-DSL)

[2019 - Kocher, Spectre Attacks Exploiting Speculative Execution](#2019---Kocher-Spectre-Attacks-Exploiting-Speculative-Execution)

[2019 - Kwon, uXOM Efficient eXecute-Only Memory on ARM Cortex-M](#2019---Kwon-uXOM-Efficient-eXecute-Only-Memory-on-ARM-Cortex-M)

[2019 - Malenko, Hardware Software Co-designed Security Extensions for Embedded Devices](#2019---Malenko-Hardware-Software-Co-designed-Security-Extensions-for-Embedded-Devices)

[2019 - Park, libmpk Software Abstraction for Intel Memory Protection Keys](#2019---Park-libmpk-Software-Abstraction-for-Intel-Memory-Protection-Keys)

[2019 - Patel, Runtime-Programmable Pipelines for Model Checkers on FPGAs](#2019---Patel-Runtime-Programmable-Pipelines-for-Model-Checkers-on-FPGAs)

[2019 - Polito, GildaVM a Non-Blocking IO Architecture for the Cog](#2019---Polito-GildaVM-a-Non-Blocking-IO-Architecture-for-the-Cog)

[2019 - Pullini, Mr Wolf An Energy-Precision Scalable Parallel Ultra Low Power SoC for IoT Edge Processing](#2019---Pullini-Mr-Wolf-An-Energy-Precision-Scalable-Parallel-Ultra-Low-Power-SoC-for-IoT-Edge-Processing)

[2019 - Schwarz, ZombieLoad Cross-Privilege-Boundary Data Sampling](#2019---Schwarz-ZombieLoad-Cross-Privilege-Boundary-Data-Sampling)

[2019 - Vahldiek, ERIM Secure Efficient In-process Isolation with Protection Keys MPK](#2019---Vahldiek-ERIM-Secure-Efficient-In-process-Isolation-with-Protection-Keys-MPK)

[2019 - Weiser, TIMBER-V Tag-Isolated Memory Bringing Fine-grained Enclaves to RISC-V](#2019---Weiser-TIMBER-V-Tag-Isolated-Memory-Bringing-Fine-grained-Enclaves-to-RISC-V)

[2020 - Agache, Firecracker Lightweight Virtualization for Serverless Applications](#2020---Agache-Firecracker-Lightweight-Virtualization-for-Serverless-Applications)

[2020 - Ahmed, Methodologies for Quantifying Re-randomization Security and Timing under JIT-ROP](#2020---Ahmed-Methodologies-for-Quantifying-Re-randomization-Security-and-Timing-under-JIT-ROP)

[2020 - Araujo, Improving Cybersecurity Hygiene through JIT Patching](#2020---Araujo-Improving-Cybersecurity-Hygiene-through-JIT-Patching)

[2020 - Brennan, JIT Leaks Inducing Timing Side Channels through Just-in-Time Compilation](#2020---Brennan-JIT-Leaks-Inducing-Timing-Side-Channels-through-Just-in-Time-Compilation)

[2020 - Bruant, System Verilog to Chisel Translation for Faster Hardware Design](#2020---Bruant-System-Verilog-to-Chisel-Translation-for-Faster-Hardware-Design)

[2020 - Canacki, Efficient Context-Sensitive CFI Enforcement Through a Hardware Monitor](#2020---Canacki-Efficient-Context-Sensitive-CFI-Enforcement-Through-a-Hardware-Monitor)

[2020 - Christou, On Architectural Support for Instruction Set Randomization](#2020---Christou-On-Architectural-Support-for-Instruction-Set-Randomization)

[2020 - Delshadtehrani, PHMon A Programmable Hardware Monitor and Its Security Use Cases](#2020---Delshadtehrani-PHMon-A-Programmable-Hardware-Monitor-and-Its-Security-Use-Cases)

[2020 - Fournier, Menhir Generic High-Speed FPGA Model-Checker](#2020---Fournier-Menhir-Generic-High-Speed-FPGA-Model-Checker)

[2020 - Fumero, Running Parallel Bytecode Interpreters on Heterogeneous Hardware](#2020---Fumero-Running-Parallel-Bytecode-Interpreters-on-Heterogeneous-Hardware)

[2020 - Garlati, A Clean Slate Approach to Linux Security RISC-V Enclaves](#2020---Garlati-A-Clean-Slate-Approach-to-Linux-Security-RISC-V-Enclaves)

[2020 - Geffen, Synthesizing JIT Compilers for In-Kernel DSLs](#2020---Geffen-Synthesizing-JIT-Compilers-for-In-Kernel-DSLs)

[2020 - Izawa, Amalgamating Different JIT Compilations in a Meta-Tracing JIT Compiler Framework](#2020---Izawa-Amalgamating-Different-JIT-Compilations-in-a-Meta-Tracing-JIT-Compiler-Framework)

[2020 - Jaloyan, Return-Oriented Programming on RISC-V](#2020---Jaloyan-Return-Oriented-Programming-on-RISC-V)

[2020 - Kim, RIMI Instruction-level Memory Isolation for Embedded Systems on RISC-V](#2020---Kim-RIMI-Instruction-level-Memory-Isolation-for-Embedded-Systems-on-RISC-V)

[2020 - Lee, Keystone An Open Framework for Architecting Trusted Execution Environments](#2020---Lee-Keystone-An-Open-Framework-for-Architecting-Trusted-Execution-Environments)

[2020 - Lehmann, Everything Old is New Again Binary Security of WebAssembly](#2020---Lehmann-Everything-Old-is-New-Again-Binary-Security-of-WebAssembly)

[2020 - Lima, Exposing Bugs in JavaScript Engines through Test Transplantation and Differential Testing](#2020---Lima-Exposing-Bugs-in-JavaScript-Engines-through-Test-Transplantation-and-Differential-Testing)

[2020 - Papadimitriou, Transparent Compiler and Runtime Specializations for Accelerating Managed Languages on FPGAs](#2020---Papadimitriou-Transparent-Compiler-and-Runtime-Specializations-for-Accelerating-Managed-Languages-on-FPGAs)

[2020 - Park, NoJITsu Locking Down Javascript](#2020---Park-NoJITsu-Locking-Down-Javascript)

[2020 - Proskurin, xMP Selective Memory Protection for Kernel and User Space](#2020---Proskurin-xMP-Selective-Memory-Protection-for-Kernel-and-User-Space)

[2020 - Schrammel, Donky Domain Keys - Efficient In-Process Isolation for RISC-V and x86](#2020---Schrammel-Donky-Domain-Keys---Efficient-In-Process-Isolation-for-RISC-V-and-x86)

[2020 - Sung, Intra-Unikernel Isolation with Intel Memory Protection Keys](#2020---Sung-Intra-Unikernel-Isolation-with-Intel-Memory-Protection-Keys)

[2020 - Varoumas, High-level programming models for microcontrollers with scarce resources](#2020---Varoumas-High-level-programming-models-for-microcontrollers-with-scarce-resources)

[2020 - Xu, Hardware-Based Domain Virtualization for Intra-Process Isolation of Persistent Memory Objects](#2020---Xu-Hardware-Based-Domain-Virtualization-for-Intra-Process-Isolation-of-Persistent-Memory-Objects)

[2020 - Zandberg, Minimal Virtual Machines on IoT Microcontrollers The Case of Berkeley Packet Filters with rBPF](#2020---Zandberg-Minimal-Virtual-Machines-on-IoT-Microcontrollers-The-Case-of-Berkeley-Packet-Filters-with-rBPF)

[2021 - Chevalier-Boisvert, YJIT A Basic Block Versioning JIT for Ruby](#2021---Chevalier-Boisvert-YJIT-A-Basic-Block-Versioning-JIT-for-Ruby)

[2021 - Cui, SmashEx Smashing SGX Enclaves Using Exceptions](#2021---Cui-SmashEx-Smashing-SGX-Enclaves-Using-Exceptions)

[2021 - Delshadtehrani, FlexFilt Towards Flexible Instruction](#2021---Delshadtehrani-FlexFilt-Towards-Flexible-Instruction)

[2021 - Dobis, Open-Source Verification with Chisel and Scala](#2021---Dobis-Open-Source-Verification-with-Chisel-and-Scala)

[2021 - Dorflinger, A Comparative Survey of Open-Source Application-Class RISC-V Processor Implementations](#2021---Dorflinger-A-Comparative-Survey-of-Open-Source-Application-Class-RISC-V-Processor-Implementations)

[2021 - Harris, Morpheus II a RISC-V Security Extension for Protecting Vulnerable Software and Hardware](#2021---Harris-Morpheus-II-a-RISC-V-Security-Extension-for-Protecting-Vulnerable-Software-and-Hardware)

[2021 - Herdt, Adaptive Simulation with Virtual Prototypes in an open-source RISC-V evaluation platform](#2021---Herdt-Adaptive-Simulation-with-Virtual-Prototypes-in-an-open-source-RISC-V-evaluation-platform)

[2021 - Izawa, Threaded Code Generation with a Meta-Tracing JIT Compiler](#2021---Izawa-Threaded-Code-Generation-with-a-Meta-Tracing-JIT-Compiler)

[2021 - Kang, A Framework for Automatic Exploit Generation for JIT Compilers](#2021---Kang-A-Framework-for-Automatic-Exploit-Generation-for-JIT-Compilers)

[2021 - Kim, Refining Indirect Call Targets at the Binary Level](#2021---Kim-Refining-Indirect-Call-Targets-at-the-Binary-Level)

[2021 - Kwon, A Hardware Platform for Ensuring OS Kernel Integrity on RISC-V](#2021---Kwon-A-Hardware-Platform-for-Ensuring-OS-Kernel-Integrity-on-RISC-V)

[2021 - Lu, A Survey on RISC-V Security Hardware and Architecture](#2021---Lu-A-Survey-on-RISC-V-Security-Hardware-and-Architecture)

[2021 - Polito, Cross-ISA Testing of the Pharo VM Lessons Learned While Porting to ARMv8](#2021---Polito-Cross-ISA-Testing-of-the-Pharo-VM-Lessons-Learned-While-Porting-to-ARMv8)

[2021 - Suzaki, TS-Perf General Performance Measurement of Trusted Execution Environment and Rich Execution Environment on Intel SGX Arm TrustZone and RISC-V Keystone](#2021---Suzaki-TS-Perf-General-Performance-Measurement-of-Trusted-Execution-Environment-and-Rich-Execution-Environment-on-Intel-SGX-Arm-TrustZone-and-RISC-V-Keystone)

[2022 - Cloosters, RiscyROP Automated Return-Oriented Programming Attacks on RISC-V and ARM64](#2022---Cloosters-RiscyROP-Automated-Return-Oriented-Programming-Attacks-on-RISC-V-and-ARM64)

[2022 - Izawa, Two-level Just-in-Time Compilation with One Interpreter and One Engine](#2022---Izawa-Two-level-Just-in-Time-Compilation-with-One-Interpreter-and-One-Engine)

[2022 - Jentzch, 2022](#2022---Jentzch-2022)

[2022 - Jeong, Exploiting Metaobjects to Reinforce Data Leakage Attacks](#2022---Jeong-Exploiting-Metaobjects-to-Reinforce-Data-Leakage-Attacks)

[2022 - Jiang, On the Challenges of Detecting Side-Channel Attacks in SGX](#2022---Jiang-On-the-Challenges-of-Detecting-Side-Channel-Attacks-in-SGX)

[2022 - Park, Bratter An Instruction Set Extension for Forward Control-Flow Integrity in RISC-V](#2022---Park-Bratter-An-Instruction-Set-Extension-for-Forward-Control-Flow-Integrity-in-RISC-V)

[2022 - Qin, DeJITLeak Eliminating JIT-Induced Timing Side-Channel Leaks](#2022---Qin-DeJITLeak-Eliminating-JIT-Induced-Timing-Side-Channel-Leaks)

[2022 - Saileshwar, HeapCheck Low-cost Hardware Support for Memory Safety](#2022---Saileshwar-HeapCheck-Low-cost-Hardware-Support-for-Memory-Safety)

[2022 - Schneider, SoK Hardware-supported Trusted Execution Environments](#2022---Schneider-SoK-Hardware-supported-Trusted-Execution-Environments)




### 1973 - Bell, Threaded Code
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 1974 - Popek, Formal Requirements for Virtualizable Third Generation Architectures
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 1975 - Dewar, Indirect Threaded Code
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 1983 - Krasner, Smalltalk-80 Bits of History Words of Advice
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, smalltalk, unread

---


### 1984 - Deutsch, Efficient Implementation of the SmallTalk-80 System
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, smalltalk, unread

---


### 1984 - Ungar, Generation Scavenging A non-disruptive High Performance Storage Reclamation Algorithm
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: garbage collection, unread

---


### 1986 - Samples, SOAR Smalltalk Without Bytecodes
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, smalltalk, unread

---


### 1986 - Ungar, The Design and Evaluation of a High Performance Smalltalk System
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, smalltalk, unread

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

##### tags: smalltalk

---


### 1987 - Cointe, Metaclasses are First Class the ObjVlisp Model 
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: lisp, oop, unread

---


### 1987 - Ungar, What Price Smalltalk
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, smalltalk, unread

---


### 1989 - Chambers, Customization Optimizing Compiler Technology for SELF a Dynamically-Typed Object-Oriented Programming Language
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, self, smalltalk, unread

---


### 1991 - Holzle, Optimizing Dynamically-Typed Object-Oriented Languages with Polymorphic Inline Caches
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

##### tags: cache, pic, smalltalk, general vm

---


### 1992 - Holzle, Debugging Optimized Code with Dynamic Deoptimization
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: debug, deoptimization, general vm, smalltalk, unread

---


### 1993 - Wahbe, Efficient Software-Based Fault Isolation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 1994 - Holzle, A Third-Generation SELF Implementation Reconciling Responsiveness with Performance
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, self, smalltalk, unread

---


### 1995 - Click, A Simple Graph-Based Intermediate Representation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: intermediate representation, unread

---


### 1995 - Dean, Optimization of Object-Oriented Programs Using Static Class Hierarchy Analysis
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

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

##### tags: cache, general vm, interpreter



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

##### tags: general vm, intermediate representation, java

---


### 1995 - Yellin, Low-Level Security in Java
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: java, security, unread

---


### 1996 - Bacon, Fast Static Analysis of C Virtual Function Calls
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 1997 - Agesen, Design and Implementation of PEp a Java Just-In-Time Translator
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: java, unread

---


### 1997 - Forrest, Building Diverse Computer Systems
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: aslr, general security, unread

---


### 1997 - Franz, Slim Binaries
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 1997 - Ingals, Back to the Future The Story of Squeak a Practical Smalltalk Written in Itself
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, smalltalk, squeak, unread

---


### 1998 - Piumarta, Optimizing Direct Threaded Code by Selective Inlining
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 1998 - Taivalsaari, Implementing a Java Virtual Machine in the Java Programming Language
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 1999 - Burke, The Jalapeno Dynamic Optimizing Compiler for Java
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 1999 - Futamara, Partial Evaluation of Computation Process an Approach to a Compiler-Compiler
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 1999 - Wolczko, Self Includes Smalltalk
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, self, smalltalk, unread

---


### 2000 - Alpern, The Jalapeno Virtual Machine
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, jalapeno, java, unread

---


### 2000 - Arnold, Adaptive Optimization in the Jalapeno JVM
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, jalapeno, java, unread

---


### 2000 - Bala, Dynamo a Transparent Dynamic Optimisation System
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: dynamo, general vm, unread

---


### 2000 - Diehl, Abstract Machines for Programming Language Implementation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 2001 - Cheng, A Parallel Real-Time Garbage Collector
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: garbage collection, unread

---


### 2001 - Paleczny, The Java HotSpot Server Compiler
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, java, hotspot, unread

---


### 2002 - Click, Fast Subtype Checking in the HotSpot JVM
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, hotspot, java, unread

---


### 2002 - Ertl, Vmgen a Generator of Efficient Virtual Machine Interpreters
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, interpreter, unread

---


### 2002 - Lattner, The LLVM Instruction Set and Compilation Strategy
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: intermediate representation, llvm, unread

---


### 2002 - Ozdoganoglu, SmashGuard A Hardware Solution To Prevent Attacks on the Function Return Address
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: cfi, hardware, unread

---


### 2003 - Asokan, Man-in-the-Middle in Tunneled Authentication Protocols
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2003 - Dehnert, The Transmeta Code Morphing - Software Using Speculation recovery and Adaptive Retranslation to Address Real-Life Challenges
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: translation, unread

---


### 2003 - Ertl, The Structure and Performance of Efficient Interpreters
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, interpreter, unread

---


### 2003 - Fink, Design Implementation and Evaluation of Adaptive Recompilation with On-Stack Replacement
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 2003 - Govindavajhala, Using Memory Errors to Attack a Virtual Machine
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, general vm, security

---


### 2003 - Merrill, GENERIC and GIMPLE A New Tree Representation for Entire Functions
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: intermediate representation, unread

---


### 2003 - Ogel, Towards Active Applications the Virtual Virtual Machine Project
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 2003 - Pax, Pax Team NOEXEC
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: permissions, security

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

##### tags: java, hardware



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

##### tags: garbage collection, java, mmtk

---


### 2004 - Chambers, A Retrospective on Customization Optimizing Compiler Technology for SELF a Dynamically-Typed Object-Oriented Programming Language
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, self, unread

---


### 2004 - Ertl, Combining Stack Caching with Dynamic Superinstructions
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: cache, general vm, interpreter, unread

---


### 2004 - Garfinkel, Ostia A Delegating Architecture for Secure System Call Interposition
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: sandbox, unread

---


### 2004 - Ravi, Security in Embedded Systems Design Challenges
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: embedded systems, security, unread

---


### 2004 - Sachindran, MC2 High-Performance Garbage Collection for Memory-Constrained Environments
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: garbage collection, unread

---


### 2004 - VanDeVen, New Security Enhancements in Red Hat Enterprise Linux
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: aslr, linux, unread

---


### 2005 - Chen, Non Control Data Attacks Are Realistic Threats
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, non-control data attack, security, unread

---


### 2005 - Click, The Pauseless GC Algorithm
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: garbage collection, unread

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

 

##### tags: fpga, garbage collection, hardware, java

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


##### tags: general vm, lua

---


### 2005 - Krall, Advances in Interpreters Virtual Machines and Emulators
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 2005 - Sheridan, Practical Testing of a C99 Compiler using Output Comparison
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: fuzzing, unread

---


### 2005 - Spett, Cross-Site Scripting
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2005 - Ungar, Constructing a Metacircular Virtual Machine in an Exploratory Programming Environment
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 2006 - Gal, HotpathVM An Effective JIT Compiler for Resource-Constrained Devices
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: embedded systems, unread

---


### 2006 - Leroy, Formal Certification of a Compiler Backend
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: formal, unread

---


### 2006 - Piumarta, Open extensible object models
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: oop, unread

---


### 2006 - Rigo, PyPys Approach to Virtual Machine Construction
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, pypy, unread

---


### 2006 - Russell, Eliminating Synchronization-Related Atomic Operations with Biased Locking and Bulk Rebiasing
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2007 - Bolz, How to not write Virtual Machines for Dynamic Languages
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[30/11/2021]

Dynamic languages are traditionally implemented by writing a virtual machine (VM ) for them in a low-level language like C or in a language that can relatively easily be turned into C. The VM implements an object model supporting the high-level dynamic language's object. It provides features such as automatic garbage collection. The effort required to build a new VM is important and especially for complicated languages in evolution. **Writing a new VM from C** means having to deal with garbage collection and threading which are complicated topics on their own. Implementing a VM on top of a general-purpose object-oriented virtual machine (OOVM) such as the **JVM** or the **CLR**. However, as a language gains in popularity, it will be wanted by the community for it to run on C-level environments as well as on top on high-level VMs. The crux of the argument is that **VMs for dynamic languages should not be written by hand**. The authors argue that it is possible to benefit from OOVMs while keeping the dynamic language implemented as a single simple source code base. The idea is to write an **interpreter for that language in another sufficiently high-level but less dynamic language**. It will play the role of a **specification** for the dynamic language.

**Implementing a language on top of OOVMs** has several advantages such as *better interoperability*, *better performance*, *ease of implementation* or *cross-platform portability*. However, all these points are debatable due to some elements (GC or JIT) that need to be tuned depending on the language/architecture or the fact that the enforced IR might not be the best representation. However, there will definitely be better tools and better GCs.

The main idea PyPy defends is that VMs for dynamic languages should be generated automatically around an interpreter playing the role of a high-level description of a language. PyPy uses a very expressive *object language* **RPython** as the language in which the complete python  interpreter is written with its built-in types. A very expressive metalanguage (Python itself) is used to perform the analysis of RPython code (control and data flow, type inference, etc.). This **translation framework** adds aspects and specializes the interpreter to fit a selectable virtual or hardware runtime environment. 

The benefits are: *single source to maintain*, *writing the interpreter is easier*, *separation of concerns*. And the effort of writing a translation toolchain is still lower than writing the VM from scratch. It is also possible to add a dynamic compilation (JIT) pass in the toolchain so that a dynamic compiler can be automatically generated.


##### tags: general vm, pypy, python, rpython

---


### 2007 - Shacham, The Geometry of Innocent Flesh on the Bone Return-into-libc without Function Calls on the x86
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, rop, security

---


### 2007 - Sotirov, Heap Feng Shui Javascript
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, heap feng shui, javascript, security

---


### 2008 - Ancona, RPython a Step Towards Reconciling Dynamically and Statically Typed OO Languages
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

---


### 2008 - Barth, Robust Defenses for Cross Site Request Forgery
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2008 - Fuess, An FPGA Implementation of Explicit-State Model Checking
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: fpga, hardware, model checking

---


### 2008 - Heiser, The Role Of Virtualization in Embedded Systems
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: embedded systems, general vm, unread

---


### 2008 - Kotzmann, Design of the Java HotSpot Client Compiler for Java 6
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hotspot, java, unread

---


### 2008 - One, Smashing the Stack for Fun and Profit
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, buffer overflow, unread

---


### 2009 - Abadi, Control-Flow Integrity Principles Implementations and Applications
<!-- Please prefix the notes with the date as in [22/12/2020] -->



[04/10/2022]

**Threat model:** An attacker that has full control over the entire data memory of the executing program.

**Control-Flow Integrity  (CFI):** defines **security policies** that dictates how software execution must follow a given path. This path is defined in the **Control-Flow Graph (CFG)** determined ahead-of-time. The CFG is determined by analysis, either *source-code analysis*, *binary analysis* or *execution profiling*.  The enforcement is done using a combination of **lightweight static verification** and **machine-code rewriting that instruments software with runtime checks**. The runtime checks ensure that control flow remains within a given CFG. CFI enforcement protects a wide range of attacks, whther stack-based (buffer overflows) or heap-based (jump-to-libc). It will not however cover attacks within the vbounds of the CFG (*e.g.* incorrect string parsing).

**Related Works:** (1) *SFI and Inlined Reference Monitors (IRMs)* are a general technique for enforcing fine-grained security policies through inline checks. SFI is a special IRM that performs dynamic checks for the purposes of memory protection. They operate by adding code into the program that needs to be monitored. The performance is problematic because of the need for control-flow checks. (2) *Vulnerability Mitigation with Secrets* such as PointGuard that stores code addresses in an encrypted form in data memory. The reliability on a secret value remains uncertain.

**Solution:** CFI relies on dynamic checks implemented by machine-code rewriting (verified by static inspection). CFI requires that when a machine code instruction transfers control, it targets a valid destination determined by the CFG ahead of time. For static destinations, this is verified statically but control-flows whose destination is determined at runtime have to be dynamically checked. To determine if an address sane, multiple strategies are available. A check against a set of address ranges adds unacceptable overhead. Three instructions: `label ID` that has no effect, `call, ID, DST` that jumps to the address in `DST` if the `ID` is correct and the corresponding `ret ID` . The instrumentation modifies each source instruction and each possible destination instruction of computed control-flow transfer. It adds before each source a dynamic check (ID-check) that ensures the runtime destination has the ID of the proper equivalence class (that have to be defined in the CFG).

##### tags: cfi, security

---


### 2009 - Bolz, Tracing the Meta-Level PyPys Tracing JIT Compiler
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general, pypy, python, unread

---


### 2009 - Callegati, Man-in-the-Middle Attack to the HTTPS Protocol
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2009 - Frampton, Demystifying Magic High-Level Low-Level Programming
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[28/04/2021]

Programming at low-level using a high-level programming language is possible and brings into question the use of C as a rule rather than as an exception. To use a high-level language, there are several approaches: the language directly supports low-level coding, the language can be extended to support low-level features, low-level features could be described in another language or the language could be extended via an extensible framework.

Adding low-level features to high-level languages requires three characteristics. ***Extensibility*** as programmers need to be able to reach beyond the semantics of high-level languages. An **extensible framework** for introducing and structuring low-level primitives is necessary. ***Encapsulation*** as the containment of low-level code is essential to minimize the impact on high-level language. The use of **language annotations** helps enforcing specific policies. Coarse-grained approach when lowering semantics results in both performance and semantics. ***Fine-grained lowering*** can help  but needs the programmer to reason about the undergoing low-level application.

The main challenges when linking low-level and high-level programming are that the high-level language **does not allow data to be represented as required** or **does not allow behavior** that is required. In order to close the data representation gap, ***primitive types*, *compound types*** and ***unboxed types*** can help as well as the addition of references and values (pointers referencing/dereferencing) are needed. Additionally to extending the data representation, the semantics should be extended as well. This can be done through the use of **intrinsic functions** to directly reflect the required semantics or add **semantic regimes** within which certain language-imposed abstractions would be suspended.

**Implementation:** **Raw Storage** allows the user to associate an empty type with a raw chunk of backing data of a specified size. This helps to create non-compound unboxed types. This can be done through the use of `@RawStorage` and`@Unboxed`. An unboxed type is only syntactically distinguished from an object and the **runtime compiler** ensures that unboxed types are never used as objects.

 The framework is used by MMTk !

 ##### tags: garbage collection, intermediate representation

---


### 2009 - Gal, Trace-based Just-in-Time Type Specialization for Dynamic Languages
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, jit, unread

---


### 2010 - Agesen, The Evolution of an X86 Virtual Machine Monitor
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2010 - Bania, JIT Spraying and Mitigations
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, jit, jit spraying, security, unread

---


### 2010 - Blazakis, Interpreter Exploitation Pointer Inference and JIT Spraying
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[19/05/2021]

To overcome DEP and ASLR, to techniques are presented: ***pointer inference*** and ***JIT spraying***.

In ActionScript, small primitive objects (integer/boolean) are stored by value and objects such as doubles, strings or class instances are stored by reference (the interpreter will allocate a buffer to hold the object and store a pointer to this value). In dynamically typed languages, types are not assigned to values at compile time. The interpreter will simply check if the operands are valid for the given operation at run time. To handle this, the interpreter represents internal objects using tagged pointers (***atoms***). Tagged pointers are a common implementation technique to differentiate between those objects stored by value and those stored by reference using the same word sized memory cell. In ActionScript, a tagged pointer stores type information in 3 bits and the value in 29 bits. ***Both values and references are used as atoms by the interpreter***. 

The built-in ActionScript Dictionary class exposes an associative map data structure, it provides an interface to associate any ActionScript object with any other ActionScript object. Internally, it is implemented as a hashtable that derives the hash from the key atom and stores the key and value atom together in the table. 



**Pointer Inference:** EIP is the ***stack pointer register***, it holds the address of next instruction to be executed. Scripting environments are a perfect target for pointer inference as the objects live on the heap and are dynamically typed. The goal is to find a way to determine the memory address of a script object in the interpreter/virtual machine. Since integers are placed into the hashtable using their value as the key, we can determine the atom value of some ActionScript object by measuring where the new objec is found when iterating over the hashtable. By recording the integers that fall before and after the newly inserted object, the attacker can derive a bound on the atom of the new object. Since object atoms are just pointers (with the first three bits modified), we can disclose as many bits of a pointer as we can grow the hashtable. To avoid the problem of hash collision, the test is performed twice, ***once for the odd integers, once with the even integers, up to a power of two*** (the larger the better). ***The victim object is inserted in both dictionaries*** and an iterative search using the `for-in` construct recording the last key visited and breaking when the current key is the victim key. The attacker now has two integer values that should differ by 17. The attacker now has the integer that, when turned into an atom is 8 smaller than the victim atom.  

```javascript
// First, create the Dictionaries
var even = new Dictionary();
var odd = new Dictionary();
// Now, fill the Dictionary objects with the integer atoms
var index;
for (index = 0; index < 8; index += 1) {
    even[index * 2] = true;
    odd[index * 2 + 1] = true;
}

var victim = “AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA”;
even[victim] = true;
odd[victim] = true;

var curr, evenPrev, oddPrev;
for (curr in even) {
    if (curr == victim) { break; }
    evenPrev = curr;
}
for (curr in odd) {
    if (curr == obj) { break; }
    oddPrev = curr;
}
```

**JIT Spraying:** DEP makes executing delivered shell-code difficult as the stack and default heaps are marked as non-executable. The key insight is that the JIT is predictable and must copy some constants to the executable page. Given a uniform statement (such as a long sum or any repeating pattern), those constants can encode small instructions and then control flow to the next constant location. A long XOR expression (`a ^ b ^ c ^ d ...`) would be compiled down to a very compact set of XOR instructions.

```javascript
var y = (0x3c54d0d9 ^ 0x3c909058 ^ 0x3c59f46a ^ 0x3c90c801 ^ ...);
```

is compiled to

```assembly
03470069 B8 D9D0543C     MOV EAX,3C54D0D9
0347006E 35 5890903C     XOR EAX,3C909058
03470073 35 6AF4593C     XOR EAX,3C59F46A
03470078 35 01C8903C     XOR EAX,3C90C801
0347007D 35 D930903C     XOR EAX,3C9030D9
03470082 35 5B53533C     XOR EAX,3C53535B
```

which if execution begins at `0x0347006A` will become the `GetPC()` method:

```assembly
0347006A  D9 D0          FNOP
0347006C  54             PUSH ESP
0347006D  3C 35          CMP AL,35
0347006F  58             POP EAX
03470070  90             NOP
03470071  90             NOP
03470072  3C 35          CMP AL,35
03470074  6A F4          PUSH -0C
03470076  59             POP ECX
03470077  3C 35          CMP AL,35
03470079  01 C8          ADD EAX,ECX
0347007B  90             NOP
0347007C  3C 35          CMP AL,35
0347007E  D9 30          FSTENV DS:[EAX]     
```

Flash objects are allocated using a custom allocator which boils down to `VirtualAlloc`. It will map pages at a 64kB granularity and does so with a linear scan finding the first hole that matches the size requested. 

##### tags: attack, jit, jit spraying, rop, security

---


### 2010 - Brunthaler, Inline Caching Meets Quickening
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: cache, general vm, unread

---


### 2010 - Checkoway, Return-Oriented Programming without Returns
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, rop, security, unread

---


### 2010 - DeGroef, JITsec Just-in-Time Security for Code Injection Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[28/05/2021]

**System calls:** system calls are the interface between user programs and the operating system. This separation allows the OS to enforce security policies and conform processes to their permissions. When a program wants to communicate with the kernel through a system call on x86/Linux , it places the number of the system call in the `eax` register and the arguments in `ebx`, `ecx`, `edx`, `edi` and `esi`. The program then issues a system call interrupt (`int 0x80`) which informs the operating system that the caller program wants to perform a system call. Execution flow is returned once the call is performed.

**Threat model:** It is assumed a vulnerability exists so that an attacker can change at least one memory location in the user-space of the process (return addresses, function pointers, etc.). One attacker-controlled variable exists which the attacker can use to inject the code of its choice.

**Design:** A monitor checks the callsite of a system call interrupt to guarantee correct behavior of the interrupting process. When it lies on the stack or the heap, the request is modified to terminate the application. In all other cases, the system call will not be changed. the monitor is placed between user processes and the system call handler by hijacking the `IDT` register (Interrupt Descriptor Table, a data structure that is used to determine the correct function to handle interrupts and exceptions). The trampoline function stores the content of registers on the stack, calls the policy-enforcing function then popped from the stack. The policy-enforcing function accesses the return address where the control flow is supposed to return to. It is checked against the range of the stack and heap memory sections. If it is one in one of them, the contents of the `eax` register is overwritten with the number for the `exit()` system call.

```C
void asmlinkage jitsec_trampoline (void) 
{
	__asm__ __volatile__ (
    	"push %edi               \n"
    	"push %esi               \n"
        "push %edx               \n"
        "push %ecx               \n"
        "push %ebx               \n"
        "push %eax               \n"
        "call jitsec_monitor     \n"
        // discard original eax value
        "pop %ebx                \n"
        "pop %ebx                \n"
        "pop %ecx                \n"
        "pop %edx                \n"
        "pop %esi                \n"
        "pop %edi                \n"
        "pushl orig_sc_routine   \n"
    );
}
```

```c
#define K_EXIT 0 x1     // exit system call number
#define IS_BETWEEN_ADDR ( start , log2size , addr )
	((( start ^ addr ) >> log2size ) == 0)

int jitsec_monitor ( unsigned int orig_eax )
{
    /* general structures provided by the kernel */
    struct task_struct * task = current_thread_info () -> task ;
    struct mm_struct * mm = task - > mm ;
    struct pt_regs *r ;
    /* contains the ( possibly ) new eax value */
    unsigned int new_eax = orig_eax ;
    
    /* Size of stack is given in memory pages
       log_2 ( stack_size * page_size ) =
       log_2 ( stack_size ) + ( log_2 (4096) = 12) */
    unsigned long l = log_2 ( mm - > stack_vm ) + 12;
    
    /* accessing registers for the current process thread */
    r = (( struct pt_regs *) task - > thread . sp0 - 1) ;
    
    /* 1. Check if callsite on stack */
    if ( IS_BETWEEN_ADDR ( mm - > start_stack , l , r - > ip ) ) {
    	/* callsite on stack -> exit ! */
    	new_eax = K_EXIT ;
    }
    else {
    	/* subtracting start and end gives size of heap */
    	l = log_2 ( mm - > brk - mm - > start_brk ) ;
    	/* 2. Check if callsite on heap */
    	if ( IS_BETWEEN_ADDR ( mm - > start_brk , l , r - > ip ) ) {
    		/* callsite on heap -> exit ! */
    		new_eax = K_EXIT ;
    	}
    }
    
    return new_eax ;
}
```

##### tags: defense, jit

---


### 2010 - Ehringer, The Dalvik Virtual Machine Architecture
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[22/04/2021]

Java aims at portability with the **Java Virtual Machine**. It consists of a supposedly stable ecosystem for desktop application through the **JSE platform** and **JEE server**. However the **mobile ecosystem JME** is more fragmented. Google abandonned both the JVM and JME with the **Dalvik virtual machine** along with **limited implementation of standard Java libraries**.

Android runtime must support: **limited processor speed, limited RAM, no swap space, battery powered, sandboxed application runtime, diverse set of devices**. In order to answer those requirements, each Android application runs in its own process with its own Dalvik VM (a register-based VM) that executes a Dalvik Executable file (`.dex`). The Dalvik VM relies on the Linux kernel for threading and low-memory management.

**DEX File Format:** For each class in Java source code, a `.class` file is generated (`javac`) with the corresponding bytecode. The corresponding `.dex` file is generated from those `.class` files (using `dx`). This file format uses specific constant pools for strings, type/class, fields or methods. These pools are shared among all classes. These memory optimizations brings more complexity to the GC because it is independent from applications. Mark bits are separated from other heap memory in order to keep the memory sharing.

**Zygote:** The Zygote enable fast startup time for new instances as well as sharing of code. It assumes a significant number of core libraries are used among multiple applications and often in read-only mode. The Zygote is a VM process that starts at system boot time, preloads core libraries and waits for socket request to fork a new VM.

##### tags: general vm, java

---


### 2010 - Erlingsson, Low-Level Software Security by Example
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: security, unread

---


### 2010 - Onarlioglu, G-Free
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: security, unread

---


### 2010 - Reynolds, Lightweight Modeling of Java Virtual Machine
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[02/02/2021]*

Java Security is enforced in three ways:

- The **Java** **compiler** has a large number of **rules** that it enforces in order to ensure that the **syntax and semantics of the Java language are satisfied** but also to prohibit actions that are known to be malicious (e.g. uninitialized variables).
- The **Java** **class loader**, is used to port a classfile into the Java execution environment. When class loading is performed, the **Java Bytecode Verifier** is used to assert the bytecode are of correct form and types.
- The **Java Runtime** performs array bounds checking, type conversion checkings, etc. 



Almost all Java exploits use weaknesses in the **Bytecode Verifier**. The verifier uses a constraints-based approach to perform its analysis. The objective is to (1) provide an extensible framework for modeling security constraints and (2) provide a concrete model for meaningful, h

##### tags: java, formal, unread

---


### 2010 - Rizzo, Practical Padding Oracle Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, security, unread

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

##### tags: attack, java, sandbox, security

---


### 2010 - Sintsov, Writing JIT Spray Shellcode for Fun and Profit
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[19/05/2021]

Browsers are getting protected by permanent DEP that is deployed on IE8 and FF3.5. On the other side, OSes implement ASLR. The idea of JIT spraying is to use many XOR operators with payload as integers in the script itself. The following example needs the memory with evil XORs to be executable and the presence of a

```javascript
var y = (0x11223344 ^ 0x44332211 ^ ...);
```

will be transformed into

```assembly
...
0x909090:35  44332211    XOR EAX, 11223344
0x909095:35  44332211    XOR EAX, 11223344
0x90909A:35  44332211    XOR EAX, 11223344
...
```

If an attacker can control the return address, they can switch it on the XOR with one byte offset:

```assembly
...
0x909091:44                INC ESP
0x909092:3322              XOR ESP, [EDX]
0x909095:1135  44332211    ADC [11223344], ESI
0x90909A:35    44332211    XOR EAX, 11223344
...
```

The author uses the `as3compiler.exe` from SWFTOOLS as the ActionScript compiler. To perform the spray, he creates an SWF file that tries to load another one (with XORs) many times. It is important to control the size of the second SWF bytecode as the offsets between allocated memory blocks grow alongside this file. We cannot know exactly where the XOR instructions are, we simply know the first 0x0CD ~ 0x100 bytes are Flash intro code then executable and non-executable blocks of 0x01000 bytes are interleaved. Loading enough blocks will fill the memory map.

To write shell-code, the high byte must be <0x7F (for XOR) otherwise the compiler breaks the XOR instruction with some others. To use JNE or JE, the Z flag needs to be safe but it is modified by the masking of the XOR instruction. The shell-code cannot deal with 4-byte data directly so it has to combine several PUSH/CALL or MOV.

(Description of the attack)

##### tags: attack, jit, jit spraying, security

---


### 2010 - Swaine, Back to the futures Incremental Parallelization of Existing Sequential Runtime Systems
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 2010 - Wei, Secure Dynamic Code Generation Against Spraying
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: jit, jit spraying, defense, diversification, security, unread

---


### 2010 - Yee, Native Client A Sandbox for Portable, Untrusted x86 Native Code
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: sandbox, unread

---


### 2011 - Ansel, Language-Independent Sandboxing of Just-In-Time Compilation and Self-Modifying Code
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: jit, defense, sandbox, security, unread

---


### 2011 - Bletsch, Jump-Oriented Programming A New Class of Code-Reuse Attack
<!-- Please prefix the notes with the date as in [22/12/2020] -->


##### tags: attack, jop, rop, security, unread

---


### 2011 - Bolz, Runtime Feedback in a Meta-Tracing JIT for Efficient Dynamic Languages
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, jit, unread

---


### 2011 - Cai, JVM virtual method invoking optimization based on CAM table
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: java, unread

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

 
##### tags: defense, jit, w xor x, 

---


### 2011 - Davi, ROPdefender A Detection Tool to Defend Against Return-Oriented Programming Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2011 - Haupt, CSOMPL a virtual machine product line
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[27/04/2021]

Application of **MDSOC** (multi-dimensional separation of concerns) and **SPL** (software product line) principles to high-level language virtual machines. Modularisation of **CSOM** using **VMADL** (virtual machine architecture description language). VMs are intricate pieces of software, and modularisation can help dealing with their understanding and overall maintainability. The notion of **service module** helps untangling the complexity of VMs. It consists of a module with *bidirectional interface* that can receive requests and exhibit internal situations to the outside.

CSOM is a SmallTalk Virtual Machine written in C. It does not support images but rather SmallTalk code written in text files. Two threading possibilities are used: the system `pthreads` or threads from within the VM itself. The GC is a mark/sweep collector. a Threaded-interpreter, additional integral representation and snapshots have been developed as extension.

**VMADL**: system architectures need to be supported at source code level and uses **service modules** with signals linking each other called *exposed join points*. It provides a frame in which an **implementation language** and an **aspect language**. Here the implementation language is C and the aspect language is **AspectC++**. In **AspectC++**, the `services` are defined and can use `require` and `expose` to link them between each other. A construct used to implement module interactions is a `combiner`.

An extension of C called ClassDL is used to help with OOP mechanisms. The combination of all the different elements create a toolchain generating a modular VM on demand.

##### tags: general vm

---


### 2011 - Miranda, The Cog Smalltalk Virtual Machine Writing a JIT in a High-Level Language
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: cog, jit, smalltalk, unread

---


### 2011 - Rohlf, The Security Challenges of Client-Side Just-in-Time Engines
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: jit, security, unread

---


### 2012 - Barbu, Application-Replay Attack on Java Cards When the Garbage Collector Gets Confused
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, garbage collection, java, unread

---


### 2012 - Pappas, Smashing the Gadgets: Hindering Return-Oriented Programming Using In-Place Code Randomization
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2012 - Rohou, Tiptop Hardware Performance Counters for the Masses
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, performance, unread

---


### 2012 - Wu, RIM An Architecture for JIT Spraying Mitigation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: jit, jit spraying, defense, diversification, unread

---


### 2012 - Wuerthinger, Self-optimizing AST interpreters
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: ast, interpreter, unread

---


### 2013 - Chen, JITSafe a Framework Against Just-In-Time Spraying Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[19/05/2021]

Modern OS adopted ***data execution prevention (DEP)*** or ***writable XOR executable (W+X)*** policies to overcome code-injection attacks. Along with code-injection attacks, code-reuse techniques such as `return-to-libc` or ***return-oriented programming (ROP)*** have been proposed to overcome DEP or W+X. ***Address Space Layout Randomization*** was proposed to mitigate this type of attacks. However, JIT spraying attacks demonstrate that it is possible to overcome the defense mechanisms. 

**JITSafe presentation:** JIT compilation needs to store the JITed code as writable *and* executable, breaking the W+X policy and opening the door to JIT spraying attacks. The objective of JITSafe is to ***enforce the W+X protection within the VM***, ***eliminate the immediate values*** and ***obfuscate the JITed code***. 

**Immediate value  elimination:** To eliminate immediate values, when the machine code generator comes across a XOR instruction, it first allocates the memory on the heap to pre-store the immediate value. Then it inserts the instruction that obtains the value from the memory to one register and replaces the original instruction with the new one that uses the register instead of the immediate value.

**Code Obfuscation:** To add more complexity, code obfuscation randomly selects the register that obtains the immediate value and inserts the padding between the instructions. The new XOR operation will use the randomly chosen register as an operand. Moreover, NOP instructions are added in between compiled instructions. 

**W+X:** Two important points during the execution of JIT compiled code  have to be noted: (1) the code compilation point where the JIT compiler generates the native code and (2) the code execution point when the VM executes the native code. When entering (1), the memory pages are marked as writable and non-executable. Shortly before (2), memory pages are marked as executable, and afterwards, non-executable again.

##### tags: defense, diversification, jit, jit spraying, w xor x, security

---


### 2013 - Duboscq, Graal IR An Extensible Declarative Intermediate Representation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, graal, intermediate representation, unread

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

##### tags: defense, fpga, hardware, security

---


### 2013 - Fournet, Fully Abstract Compilation to Javascript
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: javascript, unread

---


### 2013 - Homescu, Librando Transparent Code Randomization for JIT Compilers
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[15/09/2021]

**Background:** JIT compilers are extremely useful in the speedup of languages runtime such as Java or JavaScript. However, from a security point of view, they have an important characteristic: predictability. As they optimize code for performance, there are only a few optimal translation of HLL code to native code, and a JIT compiler emits one of these. Attackers can use this predictability to their advantage with attacks such as code injection or code reuse. JIT spraying is an example of the sooner while ROP is of the latter. Note that ROP attacks can even be designed at runtime in JIT compilers because an attacker can submit the gadget they want to compile down to machine code.

**Librando:** The objective of librando is to diversify the code generated by the compiler. It can do so following *black-box* or *white-box* diversification. On one hand, *black-box* diversification treats the compiler as a black box and the library has no knowledge of compiler internals. The library attaches to the compiler and intercepts all branches into and out of dynamically-generated code, without requiring any changes to compiler internals. On the other hand, *white-box* diversification works with some assistance from the compiler. The code emitter notifies librando through an API when it starts running undiversified code. The library locates this code, diversifies it and provides the diversified code address back to the compiler. 

It sets up several  security measures. The first one is the prevention of dynamically-generated code execution. Instead, the library disassembles the code in a cfg, diversifies every basic block then writes the blocks to a separate executable area. The library intercepts all memory allocation functions that return executable memory, then removes the executable flag on all intercepted allocation requests. In *black-box* diversification, the library catches segmentation fault signals (page faults in the MMU) and redirects execution of undiversified code to their diversified version.

Several assumptions are made to simplify the implementation effort. *No stack-pointer reuse*, *no self-modifying code* and *all calls are paired with returns*. Moreover, librando has to maintain several pieces of program state such as: *processor register contents*, *native stack contents* and *POSIX signals*.

Two rewriting techniques are used: **NOP insertion** and **constant blinding**. Moreover, the randomization goes through **`mmap` address randomization**, **basic block reordering**, **equivalent instruction substitution** and **register reallocation**. The implementation is presented on x86.

##### tags: defense, diversification, jit, security

---


### 2013 - Kulkarni, Automatic Construction of Inlining Heuristics using Machine Learning
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: inlining, machine learning, unread

---


### 2013 - Marr, Supporting Concurrency Abstractions in High-level Language Virtual Machines
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 2013 - Papadogiannakis, ASIST Architectural Support for Instruction Set Randomization
<!-- Please prefix the notes with the date as in [22/12/2020] -->

**Instruction Set Randomization (ISR)** has been proposed to defend against any type of code injection attack. It randomizes the instruction set of a processor so that an attacker is not able to inject meaningful code. ISR techniques encrypt the instructions of a possibly vulnerable program with a program-specific key. Instructions are decrypted at runtime. 

**ASIST** is a hardware/software scheme that supports ISR on top of an unmodified ISA. It uses distinct per-process keys and another system kernel's key. Two registers, `oskey` and `usrkey` are added to processor, which contains the kernel's key and the user-level key of the running process. These registers are only accessible by the operating system via privileged instructions.

The solution is built on top of a **SPARC** architecture. The decryption unit is added at the instruction fetch pipeline stage. It implements two (weak) encryption algorithms: XOR and transposition. The encryption comes with two different techniques: **statically** by adding a new section in the ELF that contains the key and encrypting code section using it and **dynamically** by generating a random key at load time and encrypting with this key.

##### tags: defense, isr, security

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

##### tags: aslr, attack, jit, rop, security

---


### 2013 - Wimmer, Maxine an Approachable Virtual Machine for and in Java
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, java, maxine, unread

---


### 2013 - Wuerthinger, One VM to Rule Them All
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 2014 - Backes, Oxymoron Making Fine-Grained Memory Randomization Practical by Allowing Code Sharing
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[20/05/2021]

Oxymoron aims to provide fine-grained memory randomization. It features ***memory-layout-agnostic code*** which works on a per-process level and does not interfere with code sharing. This way, the memory is secure without having to throw away shared libraries.

While ASLR has become widespread, it has also been shown to be ineffective by using large chunks of memory. Using finer grain randomization techniques aim at randomizing functions, basic blocks or even instructions. To be effective, it has to prevent an attacker from using information about the memory layout of one process to infer the layout of another process. This is a particular threat when looking at shared code originating from shared libraries. Most fine-grained techniques also randomize shared libraries for every single process. As a result, there is no identical in any two processes which makes sharing impossible and increases the overall memory footprint.

Oxymoron uses a new x86 calling convention: ***Position-and-Layout-Agnostic Code (PALACE)***. This code uses no instructions that reference other code or data directly. It cuts program code into the smallest sharable piece, a memory page. Those pages are randomized and shared among processes. An index is given to each process and it would appear different to each of them, organized in a translation table.

**Oxymoron Design:** The main objective of Oxymoron is to benefit from both worlds (code sharing AND fine-grained randomization). Four challenges come along this objective: (1) ***small translation table*** ; (2) ***efficient layer of indirection*** ; (3) ***translation inaccessible for adversaries*** ; (4) ***ability to run on a commodity Linux***. The overall procedure consists of:

- **Code Transformation:** The executable *E* is transformed to a PALACE-code executable *Pe*. The same applies to shared libraries, which can be treated like executables. To enable layout-agnostic code, all references to code and data are replaced with a unique label, an assigned index into a translation table. This ***randomization-agnostic translation table (rattle)*** in turn refers to the actual target.
- **Splitting:** The code is split into the smallest possible piece that can be shared: a memory page. The code of *Pe* now consists of code pieces: *p1 | p2 | ... | pn*. The PALACE code is split into page-sized pieces, as those pieces are shuffled, it must be assured that the original semantics of the program are kept intact. Explicit control flow needs to be inserted between consecutive code pieces that might be moved away in a alter stage of randomization. These links are inserted as the last instruction of a piece to ensure the successor is correct.
- **Randomization:** At program load time, the pieces are shuffled by the ASLR part of the OS loader. In memory, their order is completely random and the pieces may have empty gaps of arbitrary size between them. Modern OSes already support ASLR, loading code, data and stack segments at random base addresses. Every memory page is put in its own loadable segment of the executable file or of the shared library. Each process can have its own permutation of the randomization. Only the ***rattle*** needs to be kept up to date with a per-process randomization.

**RATTLE:** This translation table is needed because other methods have drawbacks. Storing the rattle at a **fixed** address in memory allows for its address to be hard-coded in the instructions themselves. Unfortunately, this can be exploited by an attacker. Ut can use a **Global Offset Table (GOT)** but this is realized using relative addresses and forfeits sharing. A dynamic address that is randomly chosen for every process could be stored in a dedicated **machine register**. However, this sacrifices the usage of that register. Rattle chose to use the x86 feature of ***memory segmentation*** to address and at the same time hide it from adversaries. It allows for different *segment descriptors* to be created, each with their own *base address* and *limit* (start and length).

##### tags: aslr, diversification, defense, security

---


### 2014 - Bittau, Hacking Blind
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, security, unread

---


### 2014 - Bosman, Framing Signals A Return to Portable Shellcode
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, rop, security, unread

---


### 2014 - Carlini, ROP is Still Dangerous Breaking Modern Defenses
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, rop, security, unread

---


### 2014 - Davi, Stitching the Gadgets On the Ineffectiveness of Coarse-Grained Control-Flow Integrity Protection
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, cfi, rop, security, unread

---


### 2014 - Duboscq, Speculation Without Regret Reducing Deoptimization Meta-data in the Graal Compiler
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: deoptimization, general vm, graal, unread

---


### 2014 - Eckert, FPGA-Based System Virtual Machines
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: fpga, general vm, unread

---


### 2014 - Freundenberg, SqueakJS a Modern and Practical Smalltalk that Runs in any Browser
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, javascript, smalltalk, squeak, unread

---


### 2014 - Goktas, Out Of Control Overcoming Control-Flow Integrity
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: cfi, unread

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

##### tags: ast, general vm, intermediate representation, interpreter

---


### 2014 - Jain, Sok Introspections on Trust and the Semantic Gap
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[27/04/2021]

The goals of **Virtual Machine Introspection (VMI)** is to identify if the guest OS has been compromised, if malicious applications are running on the system or if sensitive file have uncompromised secrecy or integrity. A *semantic gap* occurs when using a hypervisor to look into VM behavior as the abstractions used by the hypervisor policies are higher-level than what he can actually see (registers and cpu state). Most of VMI development goes into reconstructing high-level semantic from low-level sources.

To close this semantic gap, the **reconstruction** of data models is essential. A **learning phase** is used to extract information related to data structures (**signature**). A **search phase** can then look for instances of this data structure. Signatures are either handcrafted (`memparser`, `kntlist`  or `grepexec`), extracted from source analysis (`siggraph`, `kop` or `mas`)  and dynamic learning by studying a trusted OS behavior.

Other methods allow to bridge the gap , such as *code implanting* where the objective is to inject code into the guest OS that reports information back to the hypervisor, *process outgrafting*  that relocates the monitoring process from an untrusted VM to a second, trusted one or *kernel executable integrity* enforces the fact that the executable of the kernel has not been modified. This can be enforced by:  1) the W+X principle where a memory page can either be *writable* or *executable* but not both at the same time, 2) *whitelisting portions of code*.

- Current VMI systems face fundamental trade-offs between performance and risk, often making fragile assumptions about the guest OS

  ##### tags: formal, sok

---


### 2014 - Jauernig, Lobotomy An Architecture for JIT Spraying Mitigation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: defense, jit, security, unread

---


### 2014 - Kuznetsov, Code Pointer Integrity
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: code pointer integrity, defense, security, unread

---


### 2014 - Lin, A Security PaaS Container with a Customized JVM
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: java, unread

---


### 2014 - Niu, RockJIT Securing Just-In-Time Compilation Using Modular Control-Flow Integrity
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[10/05/2021]

Enforcing the control-flow integrity (CFI) in a JIT compiler provides a better defense against code-reuse or code-injections. The generated control-flow graph (CFG) is updated as new code is generated.

**Architecture of JIT compilers:** Looking into several JIT engines (Google V8, Mozilla TraceMonkey, Facebook HHVM or LuaJIT),  they all consist of (1) a ***baseline executor*** that is either an interpreter that interprets (*e.g. Java bytecode*) or that compiles source code directly to unoptimized native code (*e.g. V8*). It also consists of an ***optimizing compiler*** that performs runtime profiling to identify hot code or types and generates optimized native code. Optimization can manifest as either *method-based* or *trace-based* and the corresponding blocks are optimized. Next, a ***garbage collector*** provides automatic memory management (allocation and collection).

**Modular Control-Flow Integrity:** CFI system with low performance overhead and modular support. A program is divided in modules and each module contains not only code and data but also auxiliary information used to generate a new CFG when linking with other modules. MCFI represents the CFG in tables during runtime. Thread-safe table transactions are used to access and update the tables.

**Security:** The JIT engine is modified to cooperate with RockJIT's compilation toolchain and generates an MCFI module. The module is loaded by RockJIT into a sandbox. After loading, RockJIT generates a control-flow graph. The sandbox around the compiler restricts their control flow according to the tables and also restricts the memory access to be inside the box. To rule out code-injection attacks, RockJIT uses W+X protections, however the code heap needs to be both writable and executable. RockJIT uses a *shadow code heap* (similar to what *NaCl-JIT* does), it is mapped to the same physical pages as the code heap in the sandbox but with different permissions. The shadow code heap is made readable and writable but not executable. Instead of directly modifying this shadow heap, the application invokes RockJIT services to install new or modify existing native code. RockJIT enforces CFI on both the JIT compiler and the JITed code but applies different levels of precision to them. For the compiler, it applies a C++ CFG strategy to produce a relatively fine-grained CFG offline while the CFG for the JITed code is coarse-grained.

**Verification:** The verifier maintains three sets of addresses that are code addresses in the code heap. **(1)** ***Pseudo-instruction start addresses (PSA)***, this set remembers the start addresses of all pseudo instructions (defined either as a checked indirect branch, a masked memory write or an instruction that is neither an indirect branch nor an indirect memory write). **(2)** ***Indirect branch targets (IBT)***  and **(3)** ***Direct branch targets***. It verifies several conditions on those sets.

[05/10/2022]

Those verifications are performed on native code emission, deletion or modification. The three address sets presented earlier are constructed at code installation. The verifier performs address-set updates and constraint checking in one phase: (1) **code installation** checks code and updates address sets, copies the code to the shadow heap and MCFI updates is tables, (2) **code deletion** checks that direct branches outside the code region do not target any instruction within, remove related entries in the MCDI table and checks that there are no threads in the code region (3) **code modification** boils down to a code deletion followed by a code installation.

##### tags: cfi, defense, jit, security

---


### 2014 - Seaton, Debugging at Full Speed
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: debug, general vm, unread

---


### 2014 - Stadler, Partial Escape Analysis and Scalar Replacement for Java
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: java, unread

---


### 2014 - Woss, An Object Storage Model for the Truffle Language Implementation Framework
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: truffle, unread

---


### 2015 - Asanovic, The Berkeley Out-of-Order Machine BOOM An Industry Competitive Synthesizable Parameterized RISC-V
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, processor, risc-v, unread

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

##### tags: attack, jit, rop, security

---


### 2015 - Carlini, Control-Flow Bending: On the Effectiveness of Control-Flow Integrity
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

---


### 2015 - Evans, Missing the Pointer on the Effectiveness of Code Pointer Integrity
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: code pointer integrity, unread

---


### 2015 - Grimmer, Dynamically Composing Languages in a Modular Way Supporting C Extensions for Dynamic Languages
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, unread

---


### 2015 - Gunadi, Formal Certification of Android Bytecode
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: android, formal, general vm, unread

---


### 2015 - Hussein, Impact of GC Design on Power and Performance for Android
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: android, garbage collection, unread

---


### 2015 - Jangda, Adaptive Just-in-time Code Diversification
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: diversification, unread

---


### 2015 - Lam, Numba
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: general vm, llvm, numba, python, unread

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

On x86, the attacker uses back-to-back sequences of one non-attacker controlled byte (opcode) followed by four bytes of attacker controlled data (an immediate operand). ARM and Thumb need to split a 32-bit immediate value into halfwords and loaded into registers one value at a time. An attacker can control the immediate bits in arithmetic operations (up to 16 bits) or in a PC-relative branch (up to 25 for ARM, 24 for Thumb). Aside from immediate, an attacker can control the choice of operand and destination registers used in instructions by carefully crafting an input.

An attacker can control the content of 8 different registers along with different operations between them:

```javascript
function (R0, R2, R8, R10) {
	var R1  = R0  ^ 0x1234;
	var R4  = R2  ^ 0x2345;
	var R9  = R8  ^ 0x3456;
	var R11 = R10 ^ 0x4567;
    // The values of all 8 registers are known 
	return (R1 ^ R2) | (R4 ^ R8) | (R10 ^ R9) | (R11 ^ R0);
}
```

```assembly
4051       eors   r1 , r2
ea84 0408  eor.w  r4 , r4 , r8
4321       orrs   r1 , r4
ea8a 0a09  eor.w  r10, r10, r9
ea41 010a  orr.w  r1 , r1 , r10
ea8b 0b00  eor.w  r11, r11, r0
ea41 010b  orr.w  r1 , r1 , r11
```



Three JIT spraying attacks are presented: first the ***original attack shown to be unfeasible***, then the attack with the ***`ISETSTATE` register*** and finally an attack using ***gadget chaining***. 

The original attack is unfeasible because ARM expects instruction to be 4-byte aligned and shifting it by a byte (the opcode) as it was done in the original attack is not possible here. However, while it is necessary to fetch and decode two-bytes aligned instructions, the mixing of 16- and 32-bits Thumb-2 instructions allows for the second halfword of a 32-bit Thumb-2 instruction to be interpreted as the first halfword of an (unintended) instruction. This way, all ***unintended instructions*** must be ***32-bit Thumb-2 instructions*** and the ***intended instructions encoding them*** as well. **The attack consists of a chain of intended 32-bits Thumb-2 instructions executed one halfword out of phase.** Inducing the JIT to compile correct second halfwords of intended instructions mean that they have to be a valid first word as well. Using a chain of Thumb-2 only instructions makes it impossible to generate a payload because the second halfwords cannot be used as first and vice-versa.

 However, using the switch between ARM and Thumb-2 can be exploited: the attacker needs to induce the JIT to produce Thumb-2 instructions whose bytes in instruction memory decode to a useful stream of ARM instructions and execute it in ARM mode via an inter-working branch instruction. The two ARM instruction fields that make it difficult to encode ARM instructions in a Thumb instruction stream are the ***condition code*** and ***ALU result destination register***. The condition code is expected before most ARM instructions and consists of a 4-bits flag that predicates the runtime execution of the instruction on the status of condition flags (e.g. ***negative, zero, carry, overflow, etc.***). The `1111` code is illegal as a condition but can be used by specific instructions (SIMD, hint or unconditional PC-relative branch with a forced instruction set change to Thumb) that are not useful to an attacker. However, with this technique it is still complex to generate and construct a Turing-complete ARM shellcode.

***Gadget chaining*** consists of using the already available sequences of instructions called ***gadgets*** to generate a full program. The major components are (1) ***pinpointing gadgets in memory***, (2) ***preparing registers and branching to gadgets from JavaScript*** (3) ***returning from gadgets without crashing***. 

##### tags: attack, jit, jit spraying, rop, security

---


### 2015 - Lockhart, Pydgin Generating Fast Instruction Set Simulators from Simple Architecture Descriptions with Meta-Tracing JIT Compilers
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: pydgin, instruction set simulator, unread

---


### 2015 - McGillion, Open-TEE An Open Virtual Trusted Execution Environment
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: tee, unread

---


### 2015 - Prakash, Defeating ROP Through Denial of Stack Pivot
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: rop, security, unread

---


### 2015 - Rohou, Branch Prediction and the Performance of Interpreters Dont Trust Folklore
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: interpreter, performance, unread

---


### 2015 - Sartor, The Impact of Virtual Machines on Embedded Systems
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: embedded systems, general vm, unread

---


### 2015 - Simon, Snippets Taking the High Road to a Low Level
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

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
- *Make the code cache writable*: Upon receiving the main thread's message, the worker thread begins to execute another piece of code, forcing the SDT to update its code cache. It can  simply execute a function that is large enough to create a new chunk for the code fragment and set it as writable.
- *Monitor and Overwrite the code cache*:  At the same time, the main thread monitors the status of the code cache and tries to overwrite it once its status is updated.
- *Execute the shellcode*: When receiving the main thread's new message, the new worker calls the function whose content has already been overwritten. This way, the injected shellcode is executed.

The race condition needs to be validated and the method that notifies the update takes 23 microsec against the 43 needed by the W+X protection.

**System Design:** Three main challenges. ***Memory Map Synchronization*** as all memory regions allocated by the code cache are dynamically allocated and can grow and shrink freely, an effective way is needed to synchronize memories. A *reservation-based* strategy is chosen for the shared memory. When the process is initialized, a we reserve a large chunk of shared memory in both the untrusted process and the SDT. Once the memory is allocated, the synchronization can be performed with *Inter-Process Communication (IPC)*. ***Remote Procedure Call*** can be done via stubs but suffers from performance and argument passing. There is a choice to extend the shared memory to dynamic data the SDT depends on. ***Permission Enforcement*** comes by intercepting system calls related to virtual memory management. Specifically, some policies are enforced: (i) memory cannot be mapped as both writable and executable, (ii) when mapping a memory region as executable, the base address and the size must come from the SDT process, and the memory is always mapped as RX, (iii) The permission of non-writable memory cannot be changed.


##### tags: permissions, unread, w xor x

---


### 2015 - VanDeVanter, Building Debuggers and Other Tools We Can Have it All
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: debug, unread

---


### 2015 - Zhang, JITScope Protecting Web Users from Control-Flow Hijacking Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[19/08/2022]

JITScope enforces **CFI ** on both statically compiled and JIT compiled code as well as W+X on JIT code.

**Threat model:** Attackers can (1) write to any writable memory and corrupt control data such as function pointers; (2) read arbitrary mapped memory and thus launch information leakage attacks and bypass ASLR; (3) cannot directly read or write to registers and can only do it using existing instructions that propagate data between registers and memory.

**Security risks:** Risks brought by scripting languages with (1) *heap spraying* where attackers are able to allocate a lot of memory indirectly and force objects to take an expected memory address defusing ASLR; (2) *information leakage* to read memory, retrieve a leaked value for further use (3) *shellcode generation* to build expected shellcode even without the help of ROP. Then JIT compilation brings its set of vulnerabilities (1) *jit code corruption and injection* as classical W+X is not applicable (2) *jit code reuse* to use the JIT compiler to build the shellcode itself.

**Implementation:** JITScope enforces a W+X on the JIT compiled code as well as a CFI policy on both the VM and a relaxed one on the JIT code. JITScope introduces **three delegates to enforce W+X:** `fwd-exec`, `bwd-exec` and `write`. All write operations are forced through the `write` delegate that enables the writable permission of the JIT code memory page and drops the executable permission at the same time and reverses it right after. All calls to the JIT code are enforced through the `fwd-exec` delegate that sets the target memory to read-only and executable before calling the JIT code. The reverse way is done through `bwd-exec` that only allows legitimate VM function calls and sets the target memory to read-only and executable before the VM functions return to the JIT compiled code. Another delegate is the `CodeGen` that enforces a CFI policy on the JIT code: it first randomly selects an ID at compile-time, when the JIT compiler is going to generate  a function, the delegate instruments the ID before this function. For an indirect call or jump instruction, the delegate invokes the delegate to instrument CFI checks before it (they validate the existence of the ID before the target function to ensure the transfer target is a valid JIT function entry). For the JIT code, the `CodeGen` delegate is used to instrument shadow stack related operations to runtime generated return instructions. The shadow stack is put in a separate memory region, indexed by a dedicated segment register (on x86). 

##### tags: cfi, defense, jit, w xor x

---


### 2016 - Asanovic, The Rocket Chip Generator
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, processor, risc-v

---


### 2016 - Constan, Intel SGX Explained
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: tee, sgx, unread

---


### 2016 - Conti, A Survey of Man In The Middle Attack
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2016 - Gruss, Rowhammer js A Remote Software-Induced Fault Attack in JavaScript
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, security, side-channel, unread

---


### 2016 - Hu, Data-Oriented Programming On the Expressiveness of Non-Control Data Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[12/10/2022]

Authors present and qualify **non-control data attacks** that tamper with or leak security-sensitive memory that is not directly used in control transfer instructions. Data-oriented programming can offer rich exploits from common vulnerabilities. Corrupting simple local variables (through a buffer overflow for example) can allow an attacker to take control of simple operations (condition, dereference, assignment, addition, etc.) and extract these micro-operations as **data-oriented gadgets**. Executing them on attacker-controlled inputs chained in a sequence makes it possible to perform an expressive computation. A loop that allows to chain gadgets in an infinite sequence (*e.g.:* `while` on a local variable) are called **gadget dispatchers** and help attackers chaining the gadgets.

| **Semantics**      | Instructions in C | Data-Oriented gadgets in DOP |
| ------------------ | ----------------- | ---------------------------- |
| arithmetic/logical | `a op b`          | `*p op *q`                   |
| assignment         | `a = b`           | `*p = *q`                    |
| load               | `a = *b`          | `*p = **q`                   |
| store              | `*a = b`          | `**p = *q`                   |
| jump               | `goto L`          | `vpc = &input`               |
| conditional jump   | `if a goto L`     | `vpc = &input if *p`         |

The authors define **MinDOP**, a small language that uses a virtual instruction set and virtual register operands in which the attacker's payload can be specified. The 6 kind of virtual instructions are presented in the above table and allow to perform arithmetic/logical calculations, load and stores as well as conditional and unconditional jumps . Note that `vpc` is the virtual input pointer that is modified to simulate jumps. Each virtual operation is simulated by real x86 instruction sequences available in the vulnerable program. **None of the gadgets or dispatchers modify any code-pointers or violate CFI in the real-program execution**. To avoid tampering with the CFG, virtual registers are implemented with carefully-chosen memory locations (**not** hardware registers) used only through gadget operations.

A **data-oriented gadget** simulates three logical micro-operations: (**1**) loading the micro-operation, (**2**) the intended virtual operation's semantics (**3**) final store micro-operation. (1) simulates the read of the virtual register operand(s) from memory and (3) writes the result back to memory. The main differences with ROP/JOP gadgets is that: data-oriented gadgets require to write the operation result back in memory and they must execute in at least one legitimate control flow without the requirement of executing immediately one after the other. The **gadget dispatcher** is simulated by a loop which iterates over computation that simulates gadgets and has a selector in it. Each iteration executes a subset of gadgets using outputs from gadgets in the previous iteration. 

An **interactive attack** rewrites local variables at each iteration so that the desired gadget works as required. Given *Mj* the memory state for executing gadget *j*, the attacker can corrupt local variables to configure *Mj* to execute a *j* in a round, provide multiple rounds of malicious inputs to perform an expressive computation the corrupt the loop condition variable to stop. A **non-interactive attack** consists of the attacker providing the entire malicious input as a single data transmission, *i.e.* all the memory setup and conditions for deciding loop termination and selective gadget activation. MinDOP adds two virtual operations that enable conditional chaining of operations, or virtual jumps. It keeps a pointer called **virtual PC** that points to the desired configuration *Mj*. 

##### tags: attack, cfi, non-control data attack, security

---


### 2016 - Ilbeyi, Pydgin for RISC-V A Fast and Productive Instruction-Set Simulator
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: instruction set simulator, pydgin, risc-v, unread

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

##### tags: garbage collection, mmtk

---


### 2016 - Lopriore, Memory Protection in Embedded Systems
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: embedded system, security, unread

---


### 2016 - Maas, Grail Quest A New Proposal for Hardware-assisted Garbage Collection
<!-- Please prefix the notes with the date as in [22/12/2020] --> 

[10/05/2021]

Garbage collection can be made effectively pause-free at the cost of slowing down application threads and using a substantial amount of resources (both CPU time and energy consumption). Low pause times and energy efficiency can be reconciled using a proper algorithm. The two main GC strategies are ***tracing*** and ***reference counting***. *Tracing* performs a breadth-first search (BFS) to find all reachable objects and then recycle those that are not. *Reference counting* updates reachability data on the fly but requires a tracing backup collector to handle cycles. Next, there is a distinction between ***stop-the-world*** and ***concurrent*** collectors. *Stop-the-world* collectors require ***mutators*** and can only continue once GC has completed while a *concurrent* collector operates in parallel to the mutators. Finally, it is important to note whether or not the collector moves object in memory. Non-relocating collectors tend to fragment memory and end with poor memory locality. Relocation is important to obtain fast collectors but is very difficult to implement in concurrent collectors.

The objective is to design a ***pauseless GC algorithm*** that has to be performed by a ***concurrent, relocating mark-compact GC***. The algorithm has two key components: a *mark* and *relocation* phase. The mark phase regularly performs BFS passes over the heap to produce a fresh set of mark bits that tell if an object is reachable or not. The relocation phase uses the newest set of mark bits to pick pages in memory that are mostly garbage. The key idea is to try to perform these phases concurrently with respect to each other and the mutators. Write barriers are **"self-healing"** as they tag the reference in its original memory location such that next time it is encountered, it is known it has already communicated to the marker. This works by using the MSB of references to hold an NMT (not-marked-through) bit. This way the read barrier is only triggered once for each reference. The relocation phase uses the same mechanism, when an object is moved to another page, a self-healing barrier is used to remap the references to this object to the references to the new location. It maintains an **forwarding table** outside of the original page, which maps the old location to its location in the new page.

**Object Layout:** The object layout is modified from the usual language implementations. It usually starts with a header, then the parent classes' fields and finally the classes' fields. This facilitates casting an object to its parent class but reference are interspersed throughout the object. Using a ***bi-directional layout***, where the header is in the middle of the object, all non-reference fields to the left and reference fields to the right, the marker only needs to read and mark the header then read all references in a single unit-stride access.

The mark unit consists of three parts: the ***reader*** that polls the range until it has received all roots, the ***mark queue*** that is implemented as on-chip SRAM and the ***address range*** used to communicate with the between CPUs and the GC. Once the roots have been loaded, the ***marker*** and the ***tracer*** perform the mark phase. The marker is responsible for taking an object pointer from the mark queue, sending out an atomic fetch-and-or request to mark and read the object's header and, put it into a ***trace queue*** (if the object was unmarked and had at least one outgoing reference). This queue stores pairs of object pointers and number of references associated. The tracer then takes elements from this queue and issues read requests to load the references within the object into the mark queue as they return. This design decouples the different types of memory access necessary for the mark phase. The marker and tracer work together to maximize the memory bandwidth because if the tracer is busy copying one long object, the marker can run ahead and queue up additional objects . Similarly, if the marker is busy marking objects that have been marked before, the tracer can work through the remainder of the trace queue. This design is enabled by the object layout. The relocation unit **finds** pages that are mostly garbage, **builds** a side-table of forwarding pointers, **protects** the original page in the page table and **moves** objects over to the new page.

Changes to CPU consist of an added read barrier mechanism fully implemented in hardware than using a user-level trap. Three important cases are added ***NMT fault***, ***Relocation fault*** and ***Stale reference fault***

##### tags: fpga, garbage collection, hardware

---


### 2016 - Maisuradze, What Cannot Be Read Cannot Be Leveraged Revisiting Assumptions of JIT-ROP Defenses
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, jit, rop, security

---


### 2016 - Shoshitaishvili, (State of) The Art of War Offensive Techniques in Binary Analysis
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2017 - Burow, Control-Flow Integrity Precision Security and Performance
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: cfi, security, unread

---


### 2017 - Delshadtehrani, Nile A Programmable Monitoring Coprocessor
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

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

##### tags: attack, non-control data attack, defense jit, sgx, tee, security



---


### 2017 - Izraelevitz, Reusability is FIRRTL Ground Hardware Construction Languages Compiler Frameworks and Transformations
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: firrtl, hardware, unread

---


### 2017 - Jangda, RandHeap Heap Randomization for mitigating Heap Spray Attacks in Virtual Machines
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: defense, diversification, security, unread

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

##### tags: vm development

---


### 2017 - Lian, A Call to ARMs Understanding the Costs and Benefits of JIT Spraying Mitigations
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, defense, jit, jit spraying, sok, unread

---


### 2017 - Maas, Full System Simulation of Java Workloads with RISC-V and the Jikes Research Virtual Machine
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, java, jikes, risc-v, unread

---


### 2017 - Maisuradze, Dachshund: Digging for and Securing Against Non-Blinded Constants in JIT Code
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: jit, security, unread

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

##### tags: garbage collection, security, side-channel attack

---


### 2017 - Pridgen, Picking up the Trash Exploiting Generational GC for Memory Analysis
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: garbage collection, side-channel attack, unread

---


### 2017 - Reshetova, Randomization cannot stop BPF JIT spray
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, jit, jit spraying, unread

---


### 2017 - Sinha, Reviving Instruction Set Randomization
<!-- Please prefix the notes with the date as in [22/12/2020] -->

**Instruction Set Randomization (ISR)** is ineffective against code-reuse attacks which are the cornerstone of modern attacks. Previous solutions propose **(1)** unfavorable performance-security trade-offs, **(2)** no self-protection, **(3)** no support for shared libraries and page sharing, and **(4)** archaic threat models.

**Polyglot** is a hardware-based ISR schemes that uses strong encryption (AES and ECC). It removes decryption from the critical path in the processor to improve performance. The encryption is performed at the page granularity and enables page sharing between applications. It comes with strong encryption and a low overhead. Instructions are encrypted right from system boot.

##### tags: defense, isr, security

---


### 2018 - Belleville, Automated Software Protection for the Masses Against Side-Channels Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2018 - Biondo, The Guard’s Dilemma Efficient Code-Reuse Attacks Against Intel SGX
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2018 - Cho, FPGASwarm High Throughput Model Checking on FPGAs
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: fpga, hardware, model-checking

---


### 2018 - Fratric, Bypassing Mitigations by Attacking JIT Server in Microsoft Edge
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, jit, security, unread

---


### 2018 - Gawlik, Make JIT Spray Great Again
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[26/08/2022]

Existing defenses in Edge are *Microsoft's Control Flow Guard* (**MS-CFG**), a CFI implementation. *Arbitrary Code Guard* (**ACG**) prevents aking code pages writable and writable pages executable. As this is an issue for the JIT compiler, Edge provides an out-of-process JIT server which maps dynamic code into a memory region shared with the browser process. 

JIT-Spray specific protections: *constant folding*, *constant blinding*, *NOP insertion*.

##### tags: jit, jit spraying, security, sok

---


### 2018 - Lipp, Meltdown Reading Kernel Memory from User Space
<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[13/01/2021]*

A central security feature of operating systems is **memory isolation**. It ensures programs cannot access each other's or kernel's memory. It allows running multiple operations at the same time. This isolation is usually performed by a **supervisor bit** of the processor that defines whether a memory page of the kernel can be accessed or not . This bit can only be set when entering kernel code and is cleared when switching to user processes. This hardware feature **allows operating system to map the kernel into the address space of every process** and have efficient transitions from user processes to the kernel.

##### tags: security, side-channel attack

---


### 2018 - Miranda, Two Decades of Smalltalk VM Development Live VM Development through Simulation Tools
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: smalltalk, vm development, unread 

---


### 2018 - Park, Bytecode Corruption Attacks are Real and How to Defend Against Them
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: non-control data attack, security, unread

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

##### tags: hotspot, security, side-channel attack

---


### 2019 - Burow, SoK Shining Light on Shadow Stacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[01/04/2022]

**Attacker model:** Arbitrary read and write primitives to inject a payload and corrupt a code pointer to hijack program's execution. Only DEP and ASLR are up (stack canaries being too weak). Attacker is assumed to only target backward edges (*i.e.* return addresses of functions) as protection for forward edges is an orthogonal problem covered by protection such as CFI. **ROP** and **stack pivots** are the latest iteration of attacks on the stack. ROP is a code-reuse attack that overwrites return addresses on the stack to redirect control flow to a link of gadgets that perform arbitrary code (usually map a memory page as executable and writable then `memcpy` target shellcode before executing it). Stack pivots are an attack technique where the adversary controls the stack pointer and moves the stack frame to a controlled region. It is a payload delivery variant of ROP.

**Shadow Stack Design Space:** For a shadow stack to be adopted, it must be *highly performant*, *compatible with existing code* and provide *meaningful security*. Shadow stacks can be split into 5 categories, 3 as **compact** and 2 as **parallel**. They differ in the way they store the shadow stack pointer, either as a global variable, segment or register for the **compact** version or constant offset or register offset for the **parallel** version. The compact version use the location of the return address on the program stack to directly find the corresponding entry on the shadow stack. The parallel shadow stack is as large as the program stack and a simple offset maps from the program stack to the shadow stack. Direct mapping trades memory overhead for performance.

##### tags: cfi, security, sok

---


### 2019 - Choi, Reusable Inline Caching for JavaScript Performance
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: cache, javascript, unread

---


### 2019 - De, FIXER Flow Integrity Extensions for Embedded RISC-V
<!-- Please prefix the notes with the date as in [22/12/2020] -->

**Flow Integrity eXtension for Embedded RISC-V (FIXER)**  is a low energy, low overhead solution that ensures integrity of backward and forward edge control flow of programs running on a RISC-V core. The unmodified RISC-V core is a hard IP, while the dynamically reconfigurable FIXER coprocessor is implemented on an on-chip FPGA.

**RoCC:**  The architecture is based on the Rocket chip using the RocketChip generator to generate a Rocket Tile (scalar 64-bit RISC-V core, L1 instruction and data caches and the Rocket Custom Coprocessor **RoCC**). The communication between the core and RoCC goes through the **RoCCIO** interface. RoCC instructions extend the RISC-V ISA with 4 custom instructions. These instructions take the usual register/register fields:`opcode`, `rd`, `rs1`, `rs2` and `funct7`. The `funct3` is used by the RoCC interface and split in `xs1`, `xs2` and `xd` controlling the read and write of the core registers by the RoCC instruction. If `xs1` is 1, then the 64-bit value in the integer register specified by `rs1` is passed to the RoCC (and it is not if `xs1` is clear). The same idea applies to `xs2`, controlling the read of register specified by `rs2`. If the `xd` bit is 1 and `rd` is not 0, the core will wait for a value returned by the co-processor over RoCCIO after issuing the instruction to it. While the `funct7` field can be used to select user-defined functions on top of the already present 4 custom instructions, RoCC already defines 4 opcodes:

| RoCC Instruction | Opcode  |
| ---------------- | ------- |
| custom0          | 0001011 |
| custom1          | 0101011 |
| custom2          | 1011011 |
| custom3          | 1111011 |

**CFI:** For backward-edge CFI, FIXER implements a **shadow stack** in a hardware memory on the RoCC. When a function call occurs, the return address is both set on the stack and simultaneously passed to the RoCC. When returning it retrieves the return address from the RoCC and compares it to the actual one, raising a CFI error in the case of a mismatch. The forward-edge protection uses a **control-flow graph (CFG)** represented as a **policy matrix** that indicates the valid call targets for each function call. The policy matrix is loaded in memory at runtimeand is queried to validate the call target for every indirect function call.

**Software design:** Any program that wants to be backward-edge protected needs to go through three steps: (1) **source code annotation** to add `CFI_CALL` tags before function calls and a corresponding `CFI_RET` before a return from the called function (presented in the code snippet) (2) **tag expansion** to translate the tags to actual RISC-V assembly instructions (expansion presented in the code snippet below), and (3) **compilation** to assemble, link and generate the final executable (**no change to the compiler since it is passed as a word!**). For forward-edge integrity, a matrix is derived from a CFG. A RoCC instruction `cfi_matld` is used to load the policy from the policy matrix (64x64 - callee/caller addresses -, where a set/unset bit indicates a valid/invalid call). Another RoCC instruction `cfi_fwd` is inserted before every indirect function call in the source code. 

```
void main() {                   void myFunc()) {
	...                             ...
	CFI_CALL                        CFI_RET
	myFunc();                       return;
}

# CFI_CALL                      # CFI_RET
auipc  t0,0                     .word   0x0200428b
add    t0,0,14                  bne     t0,ra,_cfi_error  
.word  0x0002a00b               jr      ra
call   myFunc
```

> `CFI_CALL` extends to: retrieve the current value of the pc, add 14 bytes of offset to calculate the return address, then a custom instruction is used - custom0 is used, `funct7` is set to `0000000` for `CFI_CALL` , `rs1` is set to use `t0` (X5 or `00101`) and `xs1` is set to 1 to transfer the computed value to the RoCC. The resulting instruction is `0x0002a00b`!
>
> `CFI_RET` extends to: compare the actual return value to the stored one where `funct7` is set to `0000001` for `CFI_RET` , `rd` is set to use `t0` (X5 or `00101`) and `xd` is set to 1 to transfer the computed value back to the core. The resulting instruction is `0x0200428b`! It should then be coupled with a `bne` to check equality between the actual `ra` and the one retrieved from the shadow stack.

**Hardware design:** The program binary runs on the Rocket Core and sends RoCC instruction over the RoCCIO whenever a security validation is required. The RoCC instruction is passed to through the command decoder which extracts the individual fields of the RoCC instruction. The `funct7` decodes a `cfi_call` or `cfi_ret`. for a `cfi_call`, the contents of `t0` is sent through and stored in the shadow stack memory (in SRAM, that can store up to 1000 addresses but is parameterizable). It is accessed through a top-of-stack register. For a `cfi_ret`, the address pointed by the top-of-stack register is returned to the core. No presentation of the forward-edge implementation...

##### tags: cfi, fpga, hardware, riscv, security

---


### 2019 - Du, XPC Architectural Support for Secure and Efficient Cross Process Call
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2019 - Fumero, Dynamic Application Reconfiguration on Heterogeneous Hardware
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, unread

---


### 2019 - Hedayati, Hodor Intra-Process Isolation for High-Throughput Data Plane Libraries
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2019 - Kermarrec, LiteX  an open-source SoC builder and library based on Migen Python DSL
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, fpga, unread

---


### 2019 - Kocher, Spectre Attacks Exploiting Speculative Execution
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: security, side-channel attack, unread

---


### 2019 - Kwon, uXOM Efficient eXecute-Only Memory on ARM Cortex-M
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, unread

---


### 2019 - Malenko, Hardware Software Co-designed Security Extensions for Embedded Devices
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[14/03/2022]

The work focuses on IoT security and especially **low-cost microcontrollers (MCUs)** which operate in a **single physical address space**. The need for isolation at a very low cost is extremely important since some of those MCUs perform security and safety critical operations. 

**Experimental Setup:** The architecture of the solution is based on a RISC-V **`vscale`** implementation on which a minimal microkernel (***SmartOS***) is running. The **`vscale`** processor is a single-issue, three stage pipeline implementation of the RISC-V ISA. It is simple, minimal and has room for extensions. The MCU includes several peripherals which are mapped into a single address space with the memories, and if no memory protection is available, are available to everyone. ***SmartOS*** is a small, modular, real-time operating system suitable for low-cost embedded devices. It uses two operational modes: the kernel runs in privileged machine mode while tasks and libraries run in user mode. The kernel uses its own stack and is responsible for priority-aware scheduling, system call execution, interrupt handling, dynamic resource management and inter-task synchronization with events. The kernel code and data can only be accessed using system calls which are atomic and executed in machine mode. Due to the ***single physical address space*** constraint, the system has to be properly designed and isolated. Task communicate with events which can be invoked by tasks or interrupt service routines (ISRs).

**Implementation Details:** The MPU is configured with four Control and Status Registers (CSRs), which hold the address range of the API functions, called libraries and are not reprogrammed on every context switch. **Basic memory protection** is performed at task creation by specifying the priority, the amount of stack to be used as well as the entry function. When a task is loaded, the kernel assigns unique code and data (including stack) memory regions which are stored in the Task Control Block (TCB). The two privileges proposed by **`vscale`** are used to separate MPU configuration from being modified in user mode. **Peripheral protection** implies that shared peripherals are declared as resources. Tasks request access to a resource and wait for hardware checks to complete to give them access. One CSR is used to protect up to 32 peripherals. **Inter-task communication protection** is implemented using a shared memory approach. The memory region is divided into pages of configurable but mutually equal sizes. The MPU bitfield register has a '1' only if the communication is requested and acknowledged by both sending and receiving tasks. The authentication is performed in machine mode before switching to user mode to send data in a dedicated register and avoid expensive system calls. In hardware, every time a data memory operation is performed in the designated shared memory area for communication, the MPU calculates the page index, checks the `comm_reg` register and raises a data memory access exception if the executing task has no privileges to use the indexed page.


##### tags: embedded system, hardware

---


### 2019 - Park, libmpk Software Abstraction for Intel Memory Protection Keys
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: mpk, unread

---


### 2019 - Patel, Runtime-Programmable Pipelines for Model Checkers on FPGAs
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: fpga, hardware, model checking, unread

---


### 2019 - Polito, GildaVM a Non-Blocking IO Architecture for the Cog
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: cog, smalltalk, unread

---


### 2019 - Pullini, Mr Wolf An Energy-Precision Scalable Parallel Ultra Low Power SoC for IoT Edge Processing
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, unread

---


### 2019 - Schwarz, ZombieLoad Cross-Privilege-Boundary Data Sampling
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, security, side-channel attack, unread

---


### 2019 - Vahldiek, ERIM Secure Efficient In-process Isolation with Protection Keys MPK
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: mpk, security, unread

---


### 2019 - Weiser, TIMBER-V Tag-Isolated Memory Bringing Fine-grained Enclaves to RISC-V
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, risc-v, security, unread

---


### 2020 - Agache, Firecracker Lightweight Virtualization for Serverless Applications
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: serverless, unread

---


### 2020 - Ahmed, Methodologies for Quantifying Re-randomization Security and Timing under JIT-ROP
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: diversification, jit, rop, security, unread

---


### 2020 - Araujo, Improving Cybersecurity Hygiene through JIT Patching
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: defense, jit, security, unread

---


### 2020 - Brennan, JIT Leaks Inducing Timing Side Channels through Just-in-Time Compilation
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: attack, jit, side-channel attack, security, unread

---


### 2020 - Bruant, System Verilog to Chisel Translation for Faster Hardware Design
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, fpga, unread

---


### 2020 - Canacki, Efficient Context-Sensitive CFI Enforcement Through a Hardware Monitor
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2020 - Christou, On Architectural Support for Instruction Set Randomization
<!-- Please prefix the notes with the date as in [22/12/2020] -->

**ASIST** extension is able to protect both user- and kernel-level processes transparently without any program modifications. It utilizes a combination of techniques to increase security and performance. It uses highly secure cryptographic algorithms that can provide resilience against several attacks. It takes advantage of efficient caching strategies, as well as the spatial locality of the code to decrease the execution overheads. This way, the number of decrypt operations needed decreases and the overall performance is improved. It adds less than 1.5% overhead for XOR or transposition and around 10% for AES.

##### tags: defense, isr, security

---


### 2020 - Delshadtehrani, PHMon A Programmable Hardware Monitor and Its Security Use Cases
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

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

##### tags: hardware, fpga, model checking

---


### 2020 - Fumero, Running Parallel Bytecode Interpreters on Heterogeneous Hardware
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, interpreter, unread

---


### 2020 - Garlati, A Clean Slate Approach to Linux Security RISC-V Enclaves
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, linux, risc-v, tee, unread

---


### 2020 - Geffen, Synthesizing JIT Compilers for In-Kernel DSLs
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, jit, unread

---


### 2020 - Izawa, Amalgamating Different JIT Compilations in a Meta-Tracing JIT Compiler Framework
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[12/02/2022]

JIT compilers mainly use two types of compilation: **trace-based** compilation and **method-based** compilation. **Method-based** compilation uses a method, or function, as its unit of compilation. It shares many optimisation techniques with traditional static compilers. On the other hand, **trace-based** compilation uses a trace of a program (a sequence of instructions during a particular run) as a compilation unit. It effectively executes **inlining, loop unrolling or type specialization**. **Method-based compilation** works well on average while the **trace-based** strategy exhibits a **gain in performance** for programs with many conditional branches and deeply nested function calls. However it can cause **severe overheads** when the path of an execution varies. Main related works that extend those are Facebook's HHVM that uses region-based compilation and Higgs Javascript VM that uses lazy basic block versioning.

Using both strategies needs to answer several questions: (1) how can we construct such a compilation engine without using two different compilers (2) how do the code fragments that are compiled by different strategies interact with each others and (3) how can we determine a compilation strategy to compile part of a program.


##### tags: jit

---


### 2020 - Jaloyan, Return-Oriented Programming on RISC-V
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[18/05/2021]

Preventing the introduction of malicious code is not enough to prevent the execution of malicious computations. ***Return-oriented  programming*** thinks of reusing the code already present from intended operations to perform an attack. Several mitigations have been developed such as `gcc`'s `-mmitigate-rop`, G-Free or even Control-Flow Integrity. 

Return-object Programming consists of injecting a succession of call frames in the stack. Each call frame on the stack will result in the execution of a ***gadget***, a small snippet of legitimate code containing a a small number of instructions ended by a `ret`. When the `ret` instruction is reached, the address of the next gadget is popped from the stack into the program counter. Arbitrary code may be executed providing that enough gadgets are available. Two categories of gadgets can be distinguished: ***Main Execution Path (MEP)*** from legitimate code written by the programmer and ***Hidden Execution Path (HEP)*** that uses overlapping code such as sections that have another interpretation depending on its internal status (32- or 64-bits, Thumb mode, offset of the execution, etc.). ***HEP*** has the advantage that it bypasses traditional compiler stack protections.

The ***Galileo*** algorithm allows the detection of gadgets in any executable memory region. It is based ona backward disassembly method, starting from every return instruction and then trying to bruteforce the length of the previous instruction. The payload is then designed based on the discovered gadgets and the injection method.

The base RISC-V ISA can be extended with several extensions: **M** for integer multiplication and division, **A** for atomic operations, **F, D and Q** for single-, double- and quad-precision floating-point operations, **L** for decimal floating-point operations, **C** for compressed instructions, **J** for just-in-time instructions, **T** for transactional memory, **P** for packed-SIMD instructions, **V** for vector operations and **N** for user-level interrupts. The general extension (**G**) includes **IMAFD** and the one agreed on by Debian and Fedora for Unix platforms is the RV64GC ISA. The RISC-V architecture consists of 32 floating-point registers (`f0-f31`), a program counter (`pc`), 31 general purpose 64-bit registers (`x1-x31`) whose usage is shown in the table below as well as various control and status registers. 

![](./table.png)

RV64GC features 32- and 16-bit instructions, aligned on 16 bits. Instruction length is encoded in the LSB (lowest-address as RISC-V is little endian). 16-bit instructions require the last two bits to be different from 11 whereas 32-bit instructions have their last two bits equal to 11 and the three previous different from 11. This means that there is a possibility for overlapping instructions that can be obtained by either using two 32-bit instructions 2 bytes apart or by using a 32-bit instruction whose last 2 bytes are also a valid 16-bit compressed instruction.

![](overlapping.png)

**Threat model:** The system consists of RISC-V systems with ROP mitigations deployed such as DEP, ASLR as well as `gcc`'s `-fstack-protector-strong` (since `gcc`'s `-mmitigate-rop` or `clang`'s CFI are not available on RISC-V).

**Backdoor:** Adding a backdoor that consists of a ***trigger*** and a ***payload*** to access a privileged state.  leading to a ROP attack. This often consists of exploiting an SUID program to perform *privilege escalation*. The attacker can then create a concealed persistent backdoor on a compromised system to ensure they have access to the exploit at any time in the future.

**Gadget Chaining:** Hidden gadgets are inserted in the code using one function per gadget, each ending with a C `return` function. Note that for each function, the compiler may add assembly code at the beginning and the end whose purpose is to *insert (save)* or *remove (restore)* the call frame from the stack. Those *restore* are essential in ROP attacks as they tamper with the return address register. The hidden instructions are written directly in C code, and feature one or two instructions followed by a jump to a relative offset. 


##### tags: attack, risc-v, rop, security

---


### 2020 - Kim, RIMI Instruction-level Memory Isolation for Embedded Systems on RISC-V
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[23/08/2021]

**Previous techniques:** Usual isolation techniques such as *hardware virtualization extension*, *enclaves* and *tagged memory architectures* are not suitable for low-end embedded systems due to hardware costs or power consumption. Memory isolation ensures data can only be accessed by authorized code. Two types of isolation coexist, software- and hardware-based solutions. The first ones instrument program code by inserting instruction sequences to assign different memory permissions or sensitive data to legitimate code. These solutions often come with a significant overhead and scalability issues. Hardware-based solutions enable legitimate code to have another memory view from other code without the need for code instrumentation. These solutions are not scalable due to the limited number of memory regions that can be defined.

**RISC-V native options:** RISC-V defines three privilege modes from least to most privileged: user (U), supervisor (S) and machine (M). The supervisor mode is the one the operating system runs on. Each of these mode use *control and status registers* to configure the system operation and status. RISC-V also provides *physical memory protection (PMP)* that divides memory space into up to 16 regions and assigns specific memory permissions to each region. Two CSRs `pmpcfg` (permissions) and `pmpaddr` (regions) configure the PMP.

**Threat model:** Memory vulnerabilities exist in the software of the embedded system. The goal of the attacker would be to modify or leak sensitive data in the embedded system. A trusted privileged software is present in the system as *trusted computing base (TCB)*. This component guarantees the integrity of critical resources such as W+X policy on PMP regions.

**RIMI: ** RIMI is a technique for instruction-level memory isolation. It introduces two domains, `domain0` and `domain1`. Each domain consists of PMP regions and dedicated instructions to access its PMP regions. The access permission is bound to the dedicated instructions for each domain and the domain switch is only allowed by the dedicated control transfer instructions. To decide which PMP regions are included in each domain, a special CSR is added.

All existing instructions for memory access and control transfer are duplicated and the PMP is adjusted to check the permission according to the instructions. The control signal for added instructions is processed at the same time as the original instructions after the decoding stage. It does not affect the internal states of the core and the method can be applied to various RISC-V cores at a very small cost.

For *memory instructions*, RIMI uses replicated instructions for `domain1` and existing memory instructions for `domain0`. To distinguish which domains those instructions belong to, a small logic is added at the decode stage of the processor. The signal is then passed to PMP to check memory access. For *control transfer instructions*, RIMI defines the existing `branch`, `jal` and `jalr` instructions as the ones allowed to branch to the same domain and `jalx` and `jalrx` the ones to switch domains. Control transfer instructions do not access memory directly but access in the fetch state of the pipeline. The memory access is verified in the next pipeline state and information on the executed instruction is kept until the next fetch cycle.

**Domain Memory Protection (DMP):** DMP adjusts the memory permission so that only dedicated instructions can access isolated memory. It is implemented by bit-masking the PMP permission for the memory region and errors in the PMP always take precedence on the DMP ones. DMP defines an additional control status register `dmpcfg` to state from which domain the memory is accessible. 

**Evaluation:** Bristol/Embescom Embedded Benchmark Suite (BEEBS) shows that RIMI presents a 0.88% overhead against the 7.74% reached by other software solutions.

##### tags: hardware, risc-v, security

---


### 2020 - Lee, Keystone An Open Framework for Architecting Trusted Execution Environments
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, risc-v, security, tee, unread

---


### 2020 - Lehmann, Everything Old is New Again Binary Security of WebAssembly
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: security, unread, webassembly

---


### 2020 - Lima, Exposing Bugs in JavaScript Engines through Test Transplantation and Differential Testing
<!-- Please prefix the notes with the date as in [22/12/2020] -->

 ##### tags: fuzzing, javascript, unread

---


### 2020 - Papadimitriou, Transparent Compiler and Runtime Specializations for Accelerating Managed Languages on FPGAs
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2020 - Park, NoJITsu Locking Down Javascript
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

##### tags: jit, mpk, non-control data attack, security 

---


### 2020 - Proskurin, xMP Selective Memory Protection for Kernel and User Space
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

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

##### tags: hardware, mpk, risc-v, security

---


### 2020 - Sung, Intra-Unikernel Isolation with Intel Memory Protection Keys
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: mpk, security, unread

---


### 2020 - Varoumas, High-level programming models for microcontrollers with scarce resources
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: embedded systems, unread

---


### 2020 - Xu, Hardware-Based Domain Virtualization for Intra-Process Isolation of Persistent Memory Objects
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

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

##### tags: embedded systems

---


### 2021 - Chevalier-Boisvert, YJIT A Basic Block Versioning JIT for Ruby
<!-- Please prefix the notes with the date as in [22/12/2020] -->

CRuby, the official Ruby implementation includes a JIT compiler known as MJIT that works well on synthetic benchmarks but not with production workloads. Shopify and Github rely on the interpreter side only. Truffle Ruby, JRuby, PyPy and LuaJIT are implementation efforts that unfortunately contain a gap in terms of compatibility and support for the features of the latest reference implementation.

**Ruby:** Ruby has a broad set of features. Method calls perform **dynamic dispatch**. Methods can be **dynamically redefined** and the **method lookup order** can also be changed. Common operation such as integer arithmetic are not primitive and are calls that can be redefined at runtime. Ruby has support for first-class environments which allow local variable access from outside the local scope. Callees can redefine local variables in their callers.

**CRuby VM:** At its core lays a stack-based interpreter which executes **YARV** bytecode one at a time, with each instruction able to push and pop values of the temporary stack. Another stack is used to keep track of control frame objects corresponding to activation records for method calls. CRuby uses a system of **tags** to differentiate small immediate values as well as the constants `true`, `false` and `nil`. Ruby makes heavy use of method calls that are categorized in 11 different types (each with a slightly different implementation of `send`).

**MJIT:** MJIT compiles Ruby source by generating C source code, it then calls an external C compiler, then loads the output via dynamic linking. This limits optimizations and control.

**Lazy Basic Block Versioning (LBBV):** Code for methods is compiled incrementally one basic block at a time, as opposed to method-based compilers which treat whole methods as compilation units. Code generation proceeds for as long as the compiler can determine the direction of a branch. When it cannot anymore, branch stubs are installed and execution is resumed. Hitting a stub in turn interrupts execution to resume code generation. This helps bring more details to the runtime code generation such as types and values. Code that is not executed is never compiled. Machine code is appended to an array, and stubs are generated in a separate out-of-line memory region (so they do not impact caches). A fixed maximum number of block versions can be generated for each block. The last version must always be generic, meaning it accepts any incoming value types.

**YJIT:** 

1. **Integration with CRuby** by using the same direct-threaded interpreter as a baseline. A counter monitors how many times a method is called and triggers YJIT.
2. **Deoptimization** allows individual versions of a basic block to be invalidated if specific assumptions made at code generation do not hold at runtime. 
3. **Runtime value promotion** can be used to promote runtime values to compile-time constants (equivalent of Psyco's `unlift` operator), this is done by interrupting compilation and inserting a new stub which will then peek at the runtime value and resume compilation. This is used to create **Polymorphic Inline Caches** by detecting the runtime class so that it generates specialized machine code for reading the requested property on the class. If an object of another class is encountered, it causes a jump to a stub which will call back in to the JIT to generate a specialized instance variable read for the new class.
4. **Type Specialization** tracks and propagates type information that is then used to specialize machine code.



Validation over a list of benchmarks along with the number of instruction sequences compiled by YJIT.

##### tags: general vm, jit

---


### 2021 - Cui, SmashEx Smashing SGX Enclaves Using Exceptions
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2021 - Delshadtehrani, FlexFilt Towards Flexible Instruction
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[24/10/2022]

Moving the permission change from the OS level to the user-space (by changing the protection key right register PKRU using a dedicated `WRPKRU` instruction) makes it faster but an untrusted component can gain permission by writing into PKRU. Previous works were either insecure or too limiting in terms in terms of isolation.

**Watchpoints:** A hardware watchpoint is a **debugging mechanism** that allows the software developer to **monitor a number of programmer-specified memory locations**. They are usually limited in modern architectures and cannot be used as a fine-grained standalone solution to filter instructions at runtime. Even with an unlimited number of watchpoints, the developer has to scan the binary and instrument each call to the target instructions. 

**FlexFilt** goal is to generalize a solution to filter target instructions. The solution should (1) be flexible enough to be applicable to a variety of instructions, (2) be efficient enough to be applicable at runtime, and (3) be fine-grain to be able to filter various parts of the code. FlexFilt covers these requirements through two mechanisms: **instruction protection domains** and **flexible hardware-level filters**. 



##### tags: hardware, riscv, security, unread

---


### 2021 - Dobis, Open-Source Verification with Chisel and Scala
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, fpga, unread

---


### 2021 - Dorflinger, A Comparative Survey of Open-Source Application-Class RISC-V Processor Implementations
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, processor, risc-v, unread

---


### 2021 - Harris, Morpheus II a RISC-V Security Extension for Protecting Vulnerable Software and Hardware
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, risc-v, security, unread

---


### 2021 - Herdt, Adaptive Simulation with Virtual Prototypes in an open-source RISC-V evaluation platform
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, risc-v, unread

---


### 2021 - Izawa, Threaded Code Generation with a Meta-Tracing JIT Compiler
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: jit, unread

---


### 2021 - Kang, A Framework for Automatic Exploit Generation for JIT Compilers
<!-- Please prefix the notes with the date as in [22/12/2020] -->

**Overview:** authors present a framework for **automatic exploit generation** for JIT compilers. It consists of two components: (1) an **analyzer of existing exploits** to extract exploitation primitives, which are abstractions of low-level behaviors useful for constructing exploits and (2) a **primitive composer** to construct an exploit for a new bug given a proof-of-concept input that triggers the bug.

**Analyzer:** the analyzer determines **exploitation primitives**, high-level abstractions of lower-level behaviors represented in terms of one sequence of operations. Four kinds of primitives are extracted:

| Primitive Name | Arguments        | Ability              | Description                                                  |
| -------------- | ---------------- | -------------------- | ------------------------------------------------------------ |
| Read           | `addr`           | `addrs`              | reads the value at address `addr` and its ability is described by the addresses `addrs` it can read from |
| Write          | `addr`, `val`    | `addrs`              | writes an attacker-controlled value `val` to an attacker-control address `addr`, its ability is described by the `addrs` it can write to |
| IP Hijack      | `addr`           | `n`                  | overwrites the instruction pointer register with an attacker-controlled address `addr`, its ability describes the number `n` of lowest bytes it is able to control (*i.e.* the range it can reach) |
| Type Confusion | `obj`, `DstType` | `SrcType`, `DstType` | converts the type of an object `obj` into `DstType`, its ability is defined by its capability to convert from an `SrcType` to a `DstType` |

Each of these primitives is represented by a sequence of operations defined by:

| Operation Name | Arguments              | Description                                                  |
| -------------- | ---------------------- | ------------------------------------------------------------ |
| ReadData       | `obj`, `field`         | reads the value of an object at a specific field             |
| WriteData      | `obj`, `field`, `data` | writes attacker-specified data to the attacker-specified field of an attacker-specified object |
| CreateObj      | `specification`        | creates an object that is the same as the given specification |

An **exploitation plan**, a mixture of real code and descriptions of wanted primitives. Descriptions correspond to the ones described by exploitation primitives where the address is represented by `(base, index, offset)`. An **exploit** derives from **exploitation primitives** and **exploit plans**.

**Preprocessing:** The preprocessing phase relies on inspecting the data flow between different objects. It uses an instruction-level execution trace for a given exploit and **extracts operation sequences** on objects in a **dedicated algorithm**. Then, extracted operation sequences are stored in a **primitive database** as `(sequence, usage, ability)`. They are then sorted by ability for each category.

**Exploit Creation:** A **memory analyzer** keeps track of values, permissions and objects (location and fields) in memory. A **bug analyzer** randomly modifies a PoC file to collect its optimization action sequence and extract the longest common subsequence that keeps optimizations unchanged and therefore leave a potential bug in place. Both these analyzers output their results to the **primitive application** where the primitive is built. It uses an algorithm that takes a sequence from the database, tries to implement each operation in the sequence. It checks pre- and post-conditions for each primitive.

Still a prototype! (only preprocessing phase available)

##### tags: jit, security, unread

---


### 2021 - Kim, Refining Indirect Call Targets at the Binary Level
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2021 - Kwon, A Hardware Platform for Ensuring OS Kernel Integrity on RISC-V
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: hardware, risc-v, security

---


### 2021 - Lu, A Survey on RISC-V Security Hardware and Architecture
<!-- Please prefix the notes with the date as in [22/12/2020] -->

 ##### tags: hardware, risc-v, security, survey, unread

---


### 2021 - Polito, Cross-ISA Testing of the Pharo VM Lessons Learned While Porting to ARMv8
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[30/06/2021]

**Pharo VM:** At its core, the Pharo VM contains a threaded bytecode interpreter, a linear non-optimising JIT compiler named **Cogit** and a generational scavenger garbage collector (copy collector for young objects and mark-compact collector for older objects). The VM itself contains **255 bytecodes (in 77 families)**, **340 primitive methods** with some duplicated in the interpreter and the JIT compiler as well as **150 IR instructions**.

**Slang:** Smalltalk-to-C VM-specific transpiler. It transpiles a group of classes into a single C file. Methods are translated into functions, message sends to function calls and polymorphism is forbidden. It helps introducing interpreter optimizations (localisation of critical variables, inlining of bytecode cases, threaded code) and helps simulating the Pharo VM by executing it as normal code.

**Cogit:** The JIT compiler is a **method-based non-optimising linear** JIT compiler. It uses a linear **2-address-code** immediate representation. Compiling a method includes three phases: (1) *bytecode scan phase* extracts meta-data (i.e. need for frame) (2) *bytecode parse phase* does an abstract interpretation through a stack-bytecode to register-IR transformation (3) *code generation phase* computes the IR instruction offsets and assembles the machine code for the platform.

**CogRTL IR:** The intermediate representation uses a fixed number of virtual registers (such as `ReceiverRegister` or `ClassRegister`). These registers are needed by the compilation and are mapped to the real registers ahead of time as a compiler configuration for each supported backend/platform. CogRTL aims to be as machine-independent as possible, there is a clear separation between the compiler's frontend that parses bytecode and generates an IR and the compiler's backend that generates machine code from the IR.

**Code Patching and PICs:** Apart from method compilation, Cogit performs code patching as implemented in the compiler's backend. This does not use any of the support from CogRTL and is used in two scenarios: mono/poly/mega-morphic inline caches and updating object references when moved by the garbage collector.



 ##### tags: cog, smalltalk, vm development

---


### 2021 - Suzaki, TS-Perf General Performance Measurement of Trusted Execution Environment and Rich Execution Environment on Intel SGX Arm TrustZone and RISC-V Keystone
<!-- Please prefix the notes with the date as in [22/12/2020] -->

 ##### tags: hardware, performance, tee, unread

---


### 2022 - Cloosters, RiscyROP Automated Return-Oriented Programming Attacks on RISC-V and ARM64
<!-- Please prefix the notes with the date as in [22/12/2020] -->

Due to the lack of a **stack-based return instruction** and **strict instruction alignment**, it is significantly harder to perform ROP attacks on RISC-V or ARM64. Existing tools to automate ROP attacks utilize implementations based on the **Galileo algorithm**. It searches for byte sequences reassembling a return instruction and analyzes the preceding bytes got valid and useful instructions. Some hidden instructions (overlapping, compressed) can still be missed by the algorithm. Several novelties with the architectures make it significantly harder to find ROP gadgets: (1) the program counter (`pc`) is **not a general purpose register**, (2) there is **no stack-based return instruction**, (3) arguments to function are passed via **dedicated registers instead of the stack**, (4) **memory alignment requirements** prevent execution of unintended sequences, and (5) function epilogue sequences introduce side effects by executing several instructions between loading a return address from the stack and actually using it. 

|                                        | x86   | x86_64 | ARM32 | RISC-V | ARM64 |
| -------------------------------------- | ----- | ------ | ----- | ------ | ----- |
| (1) Writable PC                        | **X** | **X**  | **O** | **X**  | **X** |
| (2) Available stack return instruction | **O** | **O**  | **O** | **X**  | **X** |
| (3) Maximum arguments in registers     | 0     | 4-6    | 4     | 8      | 8     |
| (3) Mixed-purpose registers            | **O** | **O**  | **O** | **X**  | **X** |
| (4) Instruction alignment              | 1     | 1      | 4/2   | 4/2    | 4     |
| (5) Short function epilogue            | **O** | **O**  | **O** | **X**  | **X** |

**Challenges:** ***(1: stack-based returns)*** RISC architectures use a dedicated register to store the return address (`ra/lr`), but fr non-leaf functions (nested calls), the return addresses are still stored on the stack. On RISC-V and ARM64, the program counter is protected and can only be modified by jump instructions. RISC-V use a load instruction (`ld ra, 0x10(sp)`) to restore `ra` at the beginning of the epilogue and ARM64 use load pair to restore `lr` and `fp` in the same instruction before jumping/returning to the caller (`ldp fp, lr, [sp], #0x30; ret`).  Between the loading of the return address from the stack and the actual jump to the intended gadget, callee-saved registers are restored (`s0-s11` on RISC-V). ***(2: memory alignment)*** RISC-V should be aligned to 4 bytes (or 2 for compressed instructions), few hidden instructions are available, ARM64 is 4-bytes aligned only which prevents it. ***(3: function calls)*** arguments have to be loaded in dedicated registers that are not set by function epilogue. ***(4: system calls)*** the system call instruction is very unlikely to be included unintentionally and simply does not exist in applications that use the `libc` as a system-call wrapper.

**RiscyROP:** the gadget finding tool operates through 4 steps to construct a ROP chain to perform arbitrary function calls: (1) **scan** of every aligned address (2) **evaluation** of gadgets using **symbolic execution** and storage in a **database with their constraints** (preconditions and effects) (3) stitching of compatible gadgets and verification that they do not contain breaking side effects (4) **exploit generation** using attacker-supplied argument values.

**Gadget finding:** Does not rely on Galileo and specific byte sequence/pattern but uses **symbolic execution** without known instruction patterns. It allows the tool to discover gadgets based on their effects rather than specific instructions, allowing the use of different types of jumps. Every aligned address is analyzed independently by: (1) symbolically **initializing** registers and stack (2) **executing** the instructions until the control-flow changes to a symbolically unconstrained target (return or jump to an unset reg) and (3) **analyzing** the reached state and **summarizing** the effects of the gadget. The **effects** are summarized determining which registers: are overwritten with data from the stack, depend on one different register, are set to a constant, are changed in more complex ways. **Preconditions** are the return type of the gadget and the path constraints.

**Gadget chaining:** Using attacker-supplied target registers (argument registers for example) as input and aiming for a chain to control them all, the tool provide a gadget chain. Gadgets are processed using priorities - (1) gadgets that load a value from the *stack* over another *register* (2) gadgets that return to a *stack-read* address over *register-based* return (3) gadgets that use the least amount of registers to reduce complexity. Once it is selected, the target registers are updated for the next iteration to include remaining registers and new dependencies. This procedure is done recursively until no registers remain.

 ##### tags: attack, risc-v, rop, security, unread



---


### 2022 - Izawa, Two-level Just-in-Time Compilation with One Interpreter and One Engine
<!-- Please prefix the notes with the date as in [22/12/2020] -->

 ##### tags: jit, unread

---


### 2022 - Jentzch, 2022
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2022 - Jeong, Exploiting Metaobjects to Reinforce Data Leakage Attacks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2022 - Jiang, On the Challenges of Detecting Side-Channel Attacks in SGX
<!-- Please prefix the notes with the date as in [22/12/2020] -->

##### tags: unread

---


### 2022 - Park, Bratter An Instruction Set Extension for Forward Control-Flow Integrity in RISC-V
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[28/09/2022]

**Introduction to CFI:**

**Control-flow Integrity (CFI)** is considered as an effective way to prevent a number of control hijacking attacks such as **return-oriented programming (ROP)**.

CFI checks if the **control transfer instruction** (CTI) is legitimate before executing the instruction. The solutions can be categorized in **forward CFI** for **indirect call/jump** and **backward CFI** for **return addresses**. Backward CFI is usually performed using a **shadow stack** but various methods are available for forward CFI: using a **control flow graph (CFG)** or making use of the **function type**.

**Background:**

There are two types of CTIs: **direct** and **indirect**. In RISC-V `beq`, `blt`, `j` and `jal` correspond to direct CTIs whereas `jalr` and `jr` are indirect. In direct CTIs, the target address is **obtained from the offset** (12 bits sign-extended for branches and 22 bits sign-extended for jumps). In indirect CTIs, it is **processed by adding a 12-bits sign-extended offset to an address in a general purpose register**. This register is a target of choice for attackers! Indirect CTIs are categorized according to their expression in the CFG: indirect branches and indirect calls are called **forward-edges** while return instructions are called **backward-edges**.

The RISC-V ISA provides **hint instructions**, instructions that do not require processing under particular circumstances. They are treated as `nop` instructions when the behavior is not implemented. The *constraints* are the conditions for the instruction to be detected as a hint.

| Instructions | Constraints | Code Points | Purpose             |
| ------------ | ----------- | ----------- | ------------------- |
| LUI          | rd = x0     | 2^20        | Future standard use |
| AND          | rd = x0     | 2^10        | -                   |
| SLLI         | rd = x0     | 2^10        | Custom use          |
| SRLI         | rd = x0     | 2^10        | -                   |

**Issues with existing solutions:**

Software-based techniques insert additional instructions to every CTI. They consist of a couple of arithmetic/logic instructions and are applicable to any processor/software but add considerable performance overhead. Manufacturers added dedicated instruction extensions (ARM BTI and Intel CETS). While these provide a good basis, they cannot be used to implement finer-grain CFI solutions that enforce different rules for every indirect CTI.

For example, ARM BTI and Intel CETS expects every indirect branch to land on a specific **landing pad instruction (`bti` for ARM, `endbranch`)** with the corresponding operand (`c` for a call, `j` for a jump). While this prevent jumping to attacker controlled data, function reuse attack are still possible by jumping to an attacker-controlled function with the correct operand. 

An extension of it provides a value for each function and stores it in a dedicated register and the entry point of a function is compared against this register. This approach needs to duplicate most of the functions to have different signatures and be sure that the access to one function is restricted to another given one.

**Bratter:**

The authors present **Bratter, an instruction set extension for forward CFI on RISC-V**. Bratter introduces a **branch tag register** and **special instructions** to allow developers to set and verify the value of the register. This register supports **multiple 8-bit long branch tags** and can effectively support various CFI policies.

Bratter is composed of the following:

1. **Branch tag register (BTR)**, a control status register (CSR) that holds branch tag values.

2. **Dedicated instructions**, `sbtag` (set branch tag register to BTR) and `cbtag` (check branch tag register in BTR is legitimate)

3. **Dedicated exception**, that triggers when a check of branch tag fails.

(1) The branch tag register has four fields to hold up to four 8-bits tag values. It is a CSR that can only be accessed through dedicated instructions. The solution can be extended to have multiple BTR.

(2) Setting and checking branch tags is performed through `sbtag` and `cbtag`. They both take two operands, a 2-bit `id` and an 8-bit `value`. `sbtag` assigns a value to the `id`-th branch tag and `cbtag` checks whether the assigned value is the same. The instructions are implemented by extending `slli` and `srli` hint instructions, and therefore provides backwards compatibility with systems that do not use Bratter.

(3) To ensure CFI, the processor needs to guarantee `cbtag` instruction after the control transfer. This means that after the control transfer, when the next instruction is not `cbtag`, the processor should halt the process and an exception occurs. The exception raised is for now an *illegal instruction*.

The two CFI solutions presented are **function signature check**, check at the granularity of a function and **branch regulation**, check at the granularity of a basic block. 

**Evaluation:**

The solution is presented on top of the Spike RISC-V simulator ans as an LLVM pass. The code size overhead usually is lower than 1% for the function signature solution and around 2% for the other (up to 11% in worst-case scenario!). Execution time overhead is less than 6%!

 ##### tags: cfi, hardware, risc-v, security

---


### 2022 - Qin, DeJITLeak Eliminating JIT-Induced Timing Side-Channel Leaks
<!-- Please prefix the notes with the date as in [22/12/2020] -->

 ##### tags: defense, jit, security, side-channel attack, unread

---


### 2022 - Saileshwar, HeapCheck Low-cost Hardware Support for Memory Safety
<!-- Please prefix the notes with the date as in [22/12/2020] -->

 ##### tags: unread

---


### 2022 - Schneider, SoK Hardware-supported Trusted Execution Environments
<!-- Please prefix the notes with the date as in [22/12/2020] -->

[01/06/2022]

**Trusted Execution Environments (TEE)** are an increasingly popular solution to the problem of protecting sensitive computations and data against co-located attackers. While they differ in their implementation, they aim to provide **four high level security protections**:

1. ***Verifiable launch of the execution environment*** for the sensitive code and data so that a remote entity can ensure it was set up correctly.
2. ***Run-time isolation*** to protect the confidentiality and integrity of sensitive code and data.
3. ***Trusted IO*** to enable secure access to peripherals and accelerators.
4. ***Secure storage for TEE data*** that must be stored persistently and made available only to authorized entities at a later point in time.

A comparison of the solutions considering those four points is presented. Its methodology consists of different characteristics for each point:

(1) refers to the proof regarding the correctness of the initial state of the TEE. It establishes a *Root of Trust for Measurement (RTM)*, uses it to measure the state of the code/data within the TEE and makes it available for verification.

(2) is qualified using two dimensions, *resource partitioning* and *isolation enforcement*. Those dimensions are used to discuss their resource advantages and suitability for isolating CPU and memory against different adversaries. The corresponding components are then compared.

(3) involves two components: a *trusted path to the device* and a *trusted device architecture to protect security sensitive data just like the CPU*. The trusted paths are either *logical* or *cryptographic* and the same taxonomy as (2) is used to qualify the trusted device architecture.

(4) ensures that any sensitive data that is persistent is only available

 ##### tags: hardware, security, sok, tee

---


