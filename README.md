# brainfuck-compiler
A brainfuck compiler written in python. Requires g++ and python 3

Simply create a brainfuck file (*.txt) and compile it with bfc.py

Eg

```bash
python bfc.py multiplier.bf
```

This will generate a binary called multiplier.

Standard input and output is used by the ',' and '.' operators respectively
'+' will increment the current cell

'-' will decrement the current cell

'>' will move the cell pointer 1 position right

'<' will move the cell pointer 1 position left

'[' and ']' begin and end a while loop respectively which continues while the current cell is not 0
