with open('day1_input.txt') as f:
    lines = f.readlines()
    prev = None
    inc_count = 0
    dec_count = 0
    for line in lines:
        if prev:
            curr = int(line)
            if curr - prev > 0:
                inc_count += 1
            else:
                dec_count += 1
            prev = curr
        else:
            prev = int(line)
    print(inc_count)
    print(dec_count)
