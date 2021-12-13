
def check_string_has_chars(s, list_ch):
    for c in list_ch:
        if c not in s:
            return True
    return False

with open('day8_input.txt') as f:
    lines = f.readlines()
    count = 0
    total = 0
    for line in lines:
        signals, digits = line.split('|')
        # 10 numbers
        signals_split = signals.split()
        # 4 numbers
        digits_split = digits.split()

        # get 1
        one_digits = list(filter(lambda x: len(x) == 2, signals_split))[0]

        # get 7
        seven_digits = list(filter(lambda x: len(x) == 3, signals_split))[0]

        top = set(seven_digits) - set(one_digits)

        # get 4
        four_digits = list(filter(lambda x: len(x) == 4, signals_split))[0]

        # top_left & middle
        top_left_middle = set(four_digits) - set(one_digits)

        # get 6
        len_six_strings = set(list(filter(lambda x: len(x) == 6, signals_split)))

        six_digits_string = set(list(filter(lambda x: check_string_has_chars(x, one_digits), len_six_strings)))

        zero_nine_strings = len_six_strings - six_digits_string

        zero_nine_1, zero_nine_2 = list(zero_nine_strings)

        digit_1 = set(list(zero_nine_1)) - set(list(zero_nine_2))
        digit_2 = set(list(zero_nine_2)) - set(list(zero_nine_1))

        if list(digit_1)[0] not in top_left_middle:
            bottom_left = digit_1
            middle = digit_2
        else:
            bottom_left = digit_2
            middle = digit_1

        top_left = top_left_middle - middle

        six_digits_split = list(list(filter(lambda x: check_string_has_chars(x, one_digits),len_six_strings))[0])

        top_right = set(one_digits) - set(six_digits_split)
        bottom_right = set(one_digits) - set(top_right)

        eight_digits = list(filter(lambda x: len(x) == 7, signals_split))[0]

        top = list(top)[0]
        top_left = list(top_left)[0]
        top_right = list(top_right)[0]
        bottom_right = list(bottom_right)[0]
        bottom_left = list(bottom_left)[0]
        middle = list(middle)[0]
        bottom = list(set(list(eight_digits)) - {top, top_left, top_right, bottom_right, bottom_left, middle})[0]

        one = {top_right, bottom_right}
        four = {top_left, middle, top_right, bottom_right}
        seven = {top, top_right, bottom_right}
        eight = {top, top_left, top_right, bottom_right, bottom_left, middle, bottom}

        two = {top, top_right, middle, bottom_left, bottom}
        three = {top, top_right, middle, bottom_right, bottom}
        five = {top, top_left, middle, bottom_right, bottom}

        six = {top, top_left, middle, bottom_left, bottom_right, bottom}
        nine = {top, top_left, middle, top_right, bottom_right, bottom}
        zero = {top, bottom, bottom_left, bottom_right, top_left, top_right}

        result = []
        for d in digits_split:
            if len(d) == 2:
                result.append("1")
            elif len(d) == 3:
                result.append("7")
            elif len(d) == 4:
                result.append("4")
            elif len(d) == 7:
                result.append("8")
            elif len(d) == 5:
                if set(list(d)) == two:
                    result.append("2")
                elif set(list(d)) == three:
                    result.append("3")
                else:
                    result.append("5")
            else:
                if set(list(d)) == six:
                    result.append("6")
                elif set(list(d)) == nine:
                    result.append("9")
                else:
                    result.append("0")
        total += int("".join(result))

    print(total)

