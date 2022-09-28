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