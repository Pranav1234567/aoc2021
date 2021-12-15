def convert_to_map(s):
    m = dict()
    for c in s:
        if c in m:
            m[c] += 1
        else:
            m[c] = 1
    return m

with open('day14_input.txt') as f:
    lines = f.readlines()
    insertion_rules = False
    insertion_map = dict()
    for line in lines:
        current_line = line.rstrip()

        if current_line == "":
            insertion_rules = True
        elif not insertion_rules:
            polymer = current_line
        else:
            key, value = current_line.split('->')
            insertion_map[key.rstrip()] = value.lstrip().rstrip()

    for step in range(10):
        arr_polymer = [c for c in polymer]
        ptr = 0

        while ptr < len(arr_polymer) - 1:
            first_char = arr_polymer[ptr]
            second_char = arr_polymer[ptr+1]

            s = first_char + second_char

            if s in insertion_map:
                arr_polymer = "".join(arr_polymer[:ptr+1]) + insertion_map[s] + "".join(arr_polymer[ptr+1:])
                ptr += 2
            else:
                ptr += 1

        polymer = "".join(arr_polymer)

    m = convert_to_map(polymer)

    for k in m.keys():
        print((k, m[k]))
