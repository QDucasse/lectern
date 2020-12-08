<!-- Please prefix the notes with the date as in [22/12/2020] -->

*[08/12/2020]*

Design of an efficient *instruction-driven runtime-programmable pipeline for model checkers*. This pipeline replaces the model-specific pipeline found in prior works that hardwire the target model in FPGA logic. High-throughput model checking without requiring synthesis and place-and-route on every model change.

*FIGURE 1 PRESENTS THE EXPLICIT STATE MODEL CHECKING PROCESSING FLOW*

The model checker needs to be (1) Fast in execution time (2) Fast in preparation time. In order to answer (1), the**FPGASwarm Verification Methodology**  has been chosen. To answer (2), an **instruction-driven runtime-programmable pipeline for the successor state generator and the state validator, which support checking different models without RTL changes.**

To obtain high throughput, each **pipeline must have access to its own BRAMs containing a copy of the instructions**. The throughput of the Swarm-based FPGA model is **bound by the BRAM capacity**, a key consideration is to **minimize the footprint of the instruction memory**.



***Pipeline for the Successor State Generator:*** Each stage takes a different slice of the instruction as its control bits.

- **Instruction Fetch**: On each cycle, a state vector (along with a PID and ND value) is pushed on the pipeline to generate one successor state. The PID is used to get the PC out of the state vector. The address of instruction is obtained out of the concatenation of the PID, ND and PC values.

- **Variable Selection and Constants**: The first slice of the instruction bits is used to load values from the state vector with the address encoded in the instruction, constants are obtained as immediate values.

- **Pipeline Registers**: The pipeline registers between the variable selection stage and the final store stage have a specific arrangement. For the first one there are M registers (number of value selection units), followed by N registers (immediate values from the instruction), then several registers for storing temporary values between the multiple execution stages.

- **Execute Stages**: Computation is performed by a series of execute stages, each having several parallel ALUs. The number of ALUs should be correctly sized to accommodate the target model

  Each ALU has two operands and one output. The first one is fixed and the second is freely selected from the preceding state registers and four read-only constants: *PID, NUMPROC, value 1 and value 0*. Each ALU output is restricted to be stored in one of two possible locations. Not all ALUs need to load and two types of ALUs are developed: *Normal ALU* and *Load ALU*. A 4-bit OP field corresponds to one of the 16 operations available.

- **Permutation Stage**: The permutation stage sets up appropriate registers for the store unit by moving the calculated values from the execute stages to the correct location for the store unit to use.

- **Store Stage and PC Updating**: the store stage comprises several store units to update variables in the state vector. Each store unit has three inputs from the previous stage: *condition, value and index*. If the *condition* is non-0, the variable in the state vector with position *base + index* becomes *value*.

**Pipeline for the State Validator**: All state vectors require the same validation checks. No need for separate instructions for each PID-ND-PC combination. The final output of the validator pipeline is a single value, selected from a register in the last execution stage, which indicates whether or not the input state is a **model violation**. Note that the **validator DOES NOT consume BRAMs** as it has no instruction memory footprint.

