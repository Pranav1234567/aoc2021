with open('day6_input.txt') as f:
    lines = f.readlines()

    all_fish = list(map(lambda x: int(x), lines[0].rstrip().split(',')))

    m = dict()
    for fish in all_fish:
        if fish in m:
            m[fish] += 1
        else:
            m[fish] = 1

    for i in range(9):
        if i not in m:
            m[i] = 0

    for day in range(256):
        for i in range(9):
            if i == 0:
                temp = m[0]
                m[0] = 0
            else:
                m[i-1] += m[i]
                m[i] = 0
        m[6] += temp
        m[8] += temp

    print(sum([m[i] for i in range(9)]))

