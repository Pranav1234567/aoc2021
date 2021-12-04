def get_decimal(binary):
    s = binary
    multiplier = 1
    result = 0

    while len(s) > 0:
        result += multiplier * int(s[-1])
        multiplier *= 2
        s = s[:-1]

    return result

with open('day3_input.txt') as f:
    lines = f.readlines()
    #11 places
    arr_ones = [0 for i in range(12)]
    count = 0
    for line in lines:
        count += 1
        for j in range(len(line)):
            if line[j] == '1':
                arr_ones[j] += 1

    result1 = get_decimal("".join(list(map(lambda x: "1" if x >= 500 else "0", arr_ones))))
    result2 = get_decimal("".join(list(map(lambda x: "0" if x >= 500 else "1", arr_ones))))

    print(result1 * result2)
