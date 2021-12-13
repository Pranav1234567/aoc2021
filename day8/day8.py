with open('day8_input.txt') as f:
    lines = f.readlines()
    count = 0
    for line in lines:
        digits = line.split('|')[1].split()
        for d in digits:
            if len(d) == 7 or len(d) == 4 or len(d) == 3 or len(d) == 2:
                count += 1
    print(count)

