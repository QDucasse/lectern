<!-- Please prefix the notes with the date as in [22/12/2020] --> 

[10/05/2021]

Garbage collection can be made effectively pause-free at the cost of slowing down application threads and using a substantial amount of resources (both CPU time and energy consumption). Low pause times and energy efficiency can be reconciled using a proper algorithm. The two main GC strategies are ***tracing*** and ***reference counting***. *Tracing* performs a breadth-first search (BFS) to find all reachable objects and then recycle those that are not. *Reference counting* updates reachability data on the fly but requires a tracing backup collector to handle cycles. Next, there is a distinction between ***stop-the-world*** and ***concurrent*** collectors. *Stop-the-world* collectors require ***mutators*** and can only continue once GC has completed while a *concurrent* collector operates in parallel to the mutators. Finally, it is important to note whether or not the collector moves object in memory. Non-relocating collectors tend to fragment memory and end with poor memory locality. Relocation is important to obtain fast collectors but is very difficult to implement in concurrent collectors.

The objective is to design a ***pauseless GC algorithm*** that has to be performed by a ***concurrent, relocating mark-compact GC***. The algorithm has two key components: a *mark* and *relocation* phase. The mark phase regularly performs BFS passes over the heap to produce a fresh set of mark bits that tell if an object is reachable or not. The relocation phase uses the newest set of mark bits to pick pages in memory that are mostly garbage. The key idea is to try to perform these phases concurrently with respect to each other and the mutators. Write barriers are **"self-healing"** as they tag the reference in its original memory location such that next time it is encountered, it is known it has already communicated to the marker. This works by using the MSB of references to hold an NMT (not-marked-through) bit. This way the read barrier is only triggered once for each reference. The relocation phase uses the same mechanism, when an object is moved to another page, a self-healing barrier is used to remap the references to this object to the references to the new location. It maintains an **forwarding table** outside of the original page, which maps the old location to its location in the new page.

**Object Layout:** The object layout is modified from the usual language implementations. It usually starts with a header, then the parent classes' fields and finally the classes' fields. This facilitates casting an object to its parent class but reference are interspersed throughout the object. Using a ***bi-directional layout***, where the header is in the middle of the object, all non-reference fields to the left and reference fields to the right, the marker only needs to read and mark the header then read all references in a single unit-stride access.

The mark unit consists of three parts: the ***reader*** that polls the range until it has received all roots, the ***mark queue*** that is implemented as on-chip SRAM and the ***address range*** used to communicate with the between CPUs and the GC. Once the roots have been loaded, the ***marker*** and the ***tracer*** perform the mark phase. The marker is responsible for taking an object pointer from the mark queue, sending out an atomic fetch-and-or request to mark and read the object's header and, put it into a ***trace queue*** (if the object was unmarked and had at least one outgoing reference). This queue stores pairs of object pointers and number of references associated. The tracer then takes elements from this queue and issues read requests to load the references within the object into the mark queue as they return. This design decouples the different types of memory access necessary for the mark phase. The marker and tracer work together to maximize the memory bandwidth because if the tracer is busy copying one long object, the marker can run ahead and queue up additional objects . Similarly, if the marker is busy marking objects that have been marked before, the tracer can work through the remainder of the trace queue. This design is enabled by the object layout. The relocation unit **finds** pages that are mostly garbage, **builds** a side-table of forwarding pointers, **protects** the original page in the page table and **moves** objects over to the new page.

Changes to CPU consist of an added read barrier mechanism fully implemented in hardware than using a user-level trap. Three important cases are added ***NMT fault***, ***Relocation fault*** and ***Stale reference fault***