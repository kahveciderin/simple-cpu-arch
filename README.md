# Very Simple CPU Architecture

This is a simple RISC architecture built just to spin a penguin. It is a 8-bit architecture with 8 registers. The CPU uses the
Harvard architecture, meaning that the instruction memory and data memory are separate. The CPU has 15 instructions, each 16 bits long.

The CPU is written in [dhdl](https://github.com/kahveciderin/dhdl), my own hardware description language for a logic circuit simulator called [Digital](https://github.com/hneemann/Digital).

## Registers

The CPU has 8 registers, each 8 bits long. The registers are as follows:

- r0
- r1
- r2
- r3
- r4
- r5
- r6
- r7

The program counter register is 16 bits, but isn't directly accessible by the programmer.

## Instruction Set

The CPU has 15 instructions, each 16 bits long. The instructions are as follows:

| Instruction | Opcode | Description                                                                             |
| ----------- | ------ | --------------------------------------------------------------------------------------- |
| ADD         | 0x0    | Add two registers and store in a register                                               |
| LDI         | 0x1    | Load immediate value into register                                                      |
| SUB         | 0x2    | Subtract two registers and store in a register                                          |
| JIOZ        | 0x3    | Jump to a relative (immediate) address if a register is zero                            |
| NOT         | 0x4    | Bitwise NOT of a register                                                               |
| STO         | 0x5    | Store a register in memory, address denoted by two registers                            |
| AND         | 0x6    | Bitwise AND of two registers                                                            |
| LOD         | 0x7    | Load a value from ram with the address denoted by two registers into a register         |
| OR          | 0x8    | Bitwise OR of two registers                                                             |
| JROZ        | 0x9    | Jump to an absolute address denoted by two registers if a register is zero              |
| XOR         | 0xa    | Bitwise XOR of two registers                                                            |
| LOR         | 0xb    | Load a value from rom with the address denoted by two registers into a register         |
| SHL         | 0xc    | Bitwise left shift of a register                                                        |
| LPC         | 0xd    | Load the program counter (either upper or lower \| determined by the msb) to a register |
| SHR         | 0xe    | Bitwise right shift of a register                                                       |

A terribly written example assembler with no label support is provided in the `assembler.py` file.

The `penguin.s` file contains a simple program that spins a penguin on the screen. The program is written in assembly and can be assembled using the provided assembler. The generated code can then be loaded into the CPU by changing the `Data` parameter of the `ROM` component.
