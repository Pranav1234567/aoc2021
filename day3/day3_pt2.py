def helper(type, lines):
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
            if type == 'oxy_generator':
                total = ones
            elif type == 'co2_scrubber':
                total = zeros
        else:
            if type == 'oxy_generator':
                total = zeros
            elif type == 'co2_scrubber':
                total = ones
        pos += 1

    return total[0]

def get_oxy_generator(lines):
    return helper('oxy_generator', lines)

def get_co2_scrubber(lines):
    return helper('co2_scrubber', lines)

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

    oxy_generator = get_decimal(get_oxy_generator(lines))
    co2_scrubber = get_decimal(get_co2_scrubber(lines))

    print(oxy_generator * co2_scrubber)

