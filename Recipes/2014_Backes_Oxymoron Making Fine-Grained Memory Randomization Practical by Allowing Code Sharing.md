### Defense Summary

***Oxymoron*** is an extension of the traditional ASLR with a per-process randomization to allow for code sharing. Executables and libraries are built using ***memory-layout agnostic code***.

### Attacker Threat Model

Linux operating system that runs a user mode process which contains a memory corruption vulnerability. The goal of the attacker is to exploit this vulnerability to execute arbitrary code. The attacker knows the process' binary executable and can pre-compute gadget chains in advance. The attacker can control the input of all communication channels to the process (file content, network traffic, user input for example). The process has at least one memory disclosure vulnerability which makes the process read from an arbitrary location in memory. The process itself performs the read attempt.

### Recipe

The procedure goes through 3 main steps. First, ***code transformation*** that transforms an executable *E* to ***Position-and-Layout-Agnostic-Code (PALACE)*** *Pe*. The same applies to shared libraries. Next, ***splitting*** that transforms *Pe* into the smallest possible piece that can be shared among processes: ***a memory page***. *Pe* bcomes *p1 | p2 |...| pn*. Finally, ***randomization*** takes place at load time where the different pieces *p1 | p2 | ... | pn* are shuffled by the ASLR part of the OS loader. Their order is completely random and the pieces may have empty gaps of arbitrary size between them. **RaTTle** is the mechanism that hold the code segments locations through offset kept in the ***Global Descriptor Table*** using specific instructions.

<img src="../Articles/2014_Backes_Oxymoron Making Fine-Grained Memory Randomization Practical by Allowing Code Sharing/oxymoron.png" style="zoom: 67%;" />

<img src="../Articles/2014_Backes_Oxymoron Making Fine-Grained Memory Randomization Practical by Allowing Code Sharing/rattle.png" style="zoom: 67%;" />

