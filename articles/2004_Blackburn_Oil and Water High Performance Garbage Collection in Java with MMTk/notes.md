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

