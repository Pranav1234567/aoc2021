with open('day3_input.txt') as f:
    lines = f.readlines()

    # merge sort type of pattern

    # oxygen generator

    # starts with
    total = [line.rstrip() for line in lines]

    pos = 0
    while len(total) >= 2:
        ones = []
        zeros = []
        count_ones = 0
        count_zeros = 0
        for line in total:
            if line[pos] == '1':
                ones.append(line)
                count_ones += 1
            else:
                zeros.append(line)
                count_zeros += 1
        if count_ones >= count_zeros:
            total = ones
        else:
            total = zeros
        pos +=1

    print(total)

    # co2 scrubber

    total = [line.rstrip() for line in lines]

    pos = 0
    while len(total) >= 2:
        ones = []
        zeros = []
        count_ones = 0
        count_zeros = 0
        for line in total:
            if line[pos] == '1':
                ones.append(line)
                count_ones += 1
            else:
                zeros.append(line)
                count_zeros += 1
        if count_ones >= count_zeros:
            total = zeros
        else:
            total = ones
        pos +=1

    print(total)
