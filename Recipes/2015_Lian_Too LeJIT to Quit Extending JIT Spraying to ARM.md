### Attack Summary

Classic JIT Spraying is unfeasible on ARM as instruction size is fixed and aligned. Switching ISA (ARM to Thumb-2) mid execution does not provide enough gadgets to get a Turing-complete program. ***Gadget chaining*** is the only option and needs to call pieces of code already available in memory in the correct order to execute arbitrary code.

### Attacker Threat Model

The attacker lures the victim's browser into loading and executing attacker-provided JavaScript. The attacker code induces the client to repeatedly JIT-compile a JavaScript function containing a memory store gadget in RWX memory. The attacker is assumed to have corrupted a function whose execution can be induced on demand and accepts two attacker-controlled 32-bit arguments.

### Recipe

First, the attacker ***pinpoints*** the gadgets in memory by guessing an address where they hope a store gadget has been sprayed. They then have to ***prepare registers and branching to gadgets from JavaScript***. The memory store gadget's unintended `str` instruction expects two inputs, a register containing the word to write and a register containing a base address. The `HTMLInputElement` in the WebKit DOM exposes the virtual method `void setRangeText(replacement, start, end, selectionMode)` to JavaScript. This function makes a good candidate as it takes two arguments that are 32-bit integer (`start` and `end`). Next, the exploit has to ***return from gadgets without crashing***. The `setRangeText` function is compiled ahead-of-time then exposed to JavaScript for calling through Web IDL. Host functions operate on the native call stack rather than the JavaScript stack and they do not follow the same register-preservation rules as JS functions. JavaScript uses ***prototype functions*** to wrap the calls to host functions. They are responsible for storing callee-saved registers onto the native stack, passing arguments, etc. They marshall the return value into a JavaScript value and return to the JS code. The call to the store gadget must overwrite its own return sequence with a `bx lr` instruction which will cause execution to return to the prototype function.

