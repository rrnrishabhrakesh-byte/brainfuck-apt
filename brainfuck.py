import sys

def run(code):
    cells = [0] * 30000
    pointer = 0
    pc = 0
    stack = []
    brackets = {}

    # Match [ and ]
    for i, char in enumerate(code):
        if char == "[":
            stack.append(i)
        elif char == "]":
            if not stack:
                raise SyntaxError("Unmatched ]")
            start = stack.pop()
            brackets[start] = i
            brackets[i] = start

    if stack:
        raise SyntaxError("Unmatched [")

    while pc < len(code):
        command = code[pc]

        if command == ">":
            pointer += 1

        elif command == "<":
            pointer -= 1

        elif command == "+":
            cells[pointer] = (cells[pointer] + 1) % 256

        elif command == "-":
            cells[pointer] = (cells[pointer] - 1) % 256

        elif command == ".":
            print(chr(cells[pointer]), end="", flush=True)

        elif command == ",":
            cells[pointer] = ord(sys.stdin.read(1) or "\0")

        elif command == "[":
            if cells[pointer] == 0:
                pc = brackets[pc]

        elif command == "]":
            if cells[pointer] != 0:
                pc = brackets[pc]

        pc += 1


if len(sys.argv) != 2:
    print("Usage: python3 brainfuck.py file.bf")
    sys.exit(1)

with open(sys.argv[1], "r") as f:
    run(f.read())
