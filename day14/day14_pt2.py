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

    pair_map = dict()

    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        if pair in pair_map:
            pair_map[pair] += 1
        else:
            pair_map[pair] = 1

    for step in range(40):
        dup_pair_map = dict(pair_map)
        new_map = dict()
        for pair in dup_pair_map.keys():
            if pair in insertion_map:
                c = insertion_map[pair]
                new_pair_1 = pair[0] + c
                new_pair_2 = c + pair[1]

                temp = dup_pair_map[pair]

                if new_pair_1 in new_map:
                    new_map[new_pair_1] += temp
                else:
                    new_map[new_pair_1] = temp

                if new_pair_2 in new_map:
                    new_map[new_pair_2] += temp
                else:
                    new_map[new_pair_2] = temp

        pair_map = new_map

    final_map = dict()

    for key in pair_map.keys():
        chars = [c for c in key]
        for ch in chars:
            if ch in final_map:
                final_map[ch] += pair_map[key]
            else:
                final_map[ch] = pair_map[key]

    temp = (final_map['K'] + 1) // 2
    temp2 = (final_map['F'] + 1) // 2

    final_map['K'] = temp
    final_map['F'] = temp2

    for key in final_map:
        if key != 'F' and key != 'K':
            final_map[key] //= 2

    print(dict(sorted(final_map.items(), key=lambda item: item[1])))

    # subtract smallest value from largest value to get the answer
