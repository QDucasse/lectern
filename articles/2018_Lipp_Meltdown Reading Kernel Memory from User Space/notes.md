<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[13/01/2021]*

A central security feature of operating systems is **memory isolation**. It ensures programs cannot access each other's or kernel's memory. It allows running multiple operations at the same time. This isolation is usually performed by a **supervisor bit** of the processor that defines whether a memory page of the kernel can be accessed or not . This bit can only be set when entering kernel code and is cleared when switching to user processes. This hardware feature **allows operating system to map the kernel into the address space of every process** and have efficient transitions from user processes to the kernel.