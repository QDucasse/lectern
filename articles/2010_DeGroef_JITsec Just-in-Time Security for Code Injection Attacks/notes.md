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