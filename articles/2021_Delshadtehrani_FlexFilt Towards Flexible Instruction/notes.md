<!-- Please prefix the notes with the date as in [22/12/2020] -->

[24/10/2022]

Moving the permission change from the OS level to the user-space (by changing the protection key right register PKRU using a dedicated `WRPKRU` instruction) makes it faster but an untrusted component can gain permission by writing into PKRU. Previous works were either insecure or too limiting in terms in terms of isolation.

**Watchpoints:** A hardware watchpoint is a debugging mechanism that allows the software developer to monitor a number of programmer-specified memory locations. They are usually limited in modern architectures and cannot be used as a fine-grained standalone solution to filter instructions at runtime. Even with an unlimited number of watchpoints, the developer has to scan the binary and instrument each call to the target instructions. 

**FlexFilt** goal is to generalize a solution to filter target instructions. The solution should (1) be flexible enough to be applicable to a variety of instructions, (2) be efficient enough to be applicable at runtime, and (3) be fine-grain to be able to filter various parts of the code. FlexFilt covers these requirements through two mechanisms: **instruction protection domains** and **flexible hardware-level filters**. 



##### tags: hardware, riscv, security, unread