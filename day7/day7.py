with open('day7_input.txt') as f:
    lines = f.readlines()
    input_list = list(map(lambda x: int(x), lines[0].rstrip().split(',')))

    # part 1
    mid_1 = sorted(input_list)[len(input_list) // 2]
    mid_2 = sorted(input_list)[len(input_list) // 2 - 1]
    mid_3 = sorted(input_list)[len(input_list) // 2 + 1]

    # part 1
    total_1 = 0
    total_2 = 0
    total_3 = 0
    for e in input_list:
        total_1 += abs(mid_1 - e)
        total_2 += abs(mid_2 - e)
        total_3 += abs(mid_3 - e)

    print(min(min(total_1, total_2), total_3))

    # part 2
    avg_1 = sum(input_list) // len(input_list)
    avg_2 = sum(input_list) // len(input_list) - 1
    avg_3 = sum(input_list) // len(input_list) + 1

    #part 2
    total_1 = 0
    total_2 = 0
    total_3 = 0
    for e in input_list:
        total_1 += abs(avg_1 - e) * (abs(avg_1 - e) + 1) // 2
        total_2 += abs(avg_2 - e) * (abs(avg_2 - e) + 1) // 2
        total_3 += abs(avg_3 - e) * (abs(avg_3 - e) + 1) // 2

    print(min(min(total_1, total_2), total_3))

