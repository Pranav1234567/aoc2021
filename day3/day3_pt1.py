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

    result1 = ""
    result2 = ""
    for a in arr_ones:
        if a >= 500:
            result1 += "1"
            result2 += "0"
        else:
            result1 += "0"
            result2 += "1"
    print(result1)
    print(result2)
