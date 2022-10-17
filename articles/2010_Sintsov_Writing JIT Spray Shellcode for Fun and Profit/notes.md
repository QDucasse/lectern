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