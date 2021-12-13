with open('day13_input.txt') as f:
    lines = f.readlines()
    instructions = False
    converted_instructions = []
    dots = dict()
    for line in lines:
        current_line = line.rstrip()
        if current_line == "":
            instructions = True

        if not instructions:
            x, y = current_line.split(',')
            if not (x,y) in dots:
                dots[(int(x),int(y))] = True

        else:
            if current_line:
                fold, along, equation = current_line.split(' ')
                direction, number = equation.split('=')
                converted_instructions.append((direction, int(number)))

    for instruction in converted_instructions:
        # part 1 - just first instruction & count points
        if instruction[0] == 'x':
            # reflect the points
            all_dots = dots.keys()
            new_dots = dict()
            for dot in all_dots:
                if dot[0] > instruction[1]:
                    new_x = instruction[1] - (dot[0] - instruction[1])

                    new_dots[(new_x, dot[1])] = True
                else:
                    new_dots[(dot[0], dot[1])] = True
            # count
            dots = new_dots
        else:
            # reflect the points
            all_dots = dots.keys()
            new_dots = dict()
            for dot in all_dots:
                if dot[1] > instruction[1]:
                    new_y = instruction[1] - (dot[1] - instruction[1])
                    new_dots[(dot[0], new_y)] = True
                else:
                    new_dots[(dot[0], dot[1])] = True
            # count
            dots = new_dots

    grid = [["" for i in range(6)] for j in range(81)]

    for dot in dots.keys():
        grid[dot[0]][dot[1]] = "*"

    for row in grid:
        print(row)

    # part 2 plot points from dots.keys() and see the 8 letters!
