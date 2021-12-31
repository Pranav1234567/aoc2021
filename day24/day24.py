def monad(num, instructions):
    str_num = str(num)
    ptr = 0
    w = 0
    x = 0
    y = 0
    z = 0

    m = dict()
    m["w"] = w
    m["x"] = x
    m["y"] = y
    m["z"] = z

    for instruction in instructions:
        if instruction[0] == "inp":
            if instruction[1] == "w":
                w = int(str_num[ptr])
                ptr += 1
            elif instruction[1] == "x":
                x = int(str_num[ptr])
                ptr += 1
            elif instruction[1] == "y":
                y = int(str_num[ptr])
                ptr += 1
            elif instruction[1] == "z":
                z = int(str_num[ptr])
                ptr += 1
        else:
            instruction_2 = 0
            if instruction[2].isnumeric():
                instruction_2 = int(instruction[2])
            else:
                if instruction[2][0] == "-":
                    instruction_2 = int(instruction[2])
                else:
                    instruction_2 = m[instruction[2]]

            if instruction[1] == "w":
                if instruction[0] == "add":
                    w += instruction_2
                elif instruction[0] == "mul":
                    w *= instruction_2
                elif instruction[0] == "div":
                    w = w // instruction_2
                elif instruction[0] == "mod":
                    w = w % instruction_2
                elif instruction[0] == "eql":
                    w = int(w == instruction_2)
            elif instruction[1] == "x":
                if instruction[0] == "add":
                    x += instruction_2
                elif instruction[0] == "mul":
                    x *= instruction_2
                elif instruction[0] == "div":
                    x = x // instruction_2
                elif instruction[0] == "mod":
                    x = x % instruction_2
                elif instruction[0] == "eql":
                    x = int(x == instruction_2)
            elif instruction[1] == "y":
                if instruction[0] == "add":
                    y += instruction_2
                elif instruction[0] == "mul":
                    y *= instruction_2
                elif instruction[0] == "div":
                    y = y // instruction_2
                elif instruction[0] == "mod":
                    y = y % instruction_2
                elif instruction[0] == "eql":
                    y = int(y == instruction_2)
            elif instruction[1] == "z":
                if instruction[0] == "add":
                    z += instruction_2
                elif instruction[0] == "mul":
                    z *= instruction_2
                elif instruction[0] == "div":
                    z = z // instruction_2
                elif instruction[0] == "mod":
                    z = z % instruction_2
                elif instruction[0] == "eql":
                    z = int(z == instruction_2)
        print(w)
        print(x)
        print(y)
        print(z)
        print("***")

    if z == 0:
        print("passed");
with open('day24_input.txt') as f:
    lines = f.readlines()
    instructions = []
    for line in lines:
        instructions.append(tuple(line.rstrip().split(" ")))

    monad(99999999999999, instructions)
