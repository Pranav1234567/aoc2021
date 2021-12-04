with open('day1_input.txt') as f:
    lines = f.readlines()
    prev = None
    inc_count = 0
    dec_count = 0
    for i in range(len(lines) - 2):
        if prev:
            curr = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
            if curr - prev > 0:
                inc_count += 1
            else:
                dec_count += 1
            prev = curr
        else:
            prev = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    print(inc_count)
    print(dec_count)
