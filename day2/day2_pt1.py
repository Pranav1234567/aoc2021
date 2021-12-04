with open('day2_input.txt') as f:
    lines = f.readlines()
    d = dict()
    x = 0
    y = 0
    aim = 0
    for line in lines:
        line_split = line.split(' ')
        if line_split[0] == 'forward':
            x += int(line_split[1])
        elif line_split[0] == 'down':
            y += int(line_split[1])
        elif line_split[0] == 'up':
            y -= int(line_split[1])
    print(x * y)
