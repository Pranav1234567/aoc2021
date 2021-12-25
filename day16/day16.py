def convert_binary_to_decimal(s):
    multiplier = 1
    result = 0
    for c in s[::-1]:
        result += int(c) * multiplier
        multiplier *= 2
    return result

def parse_literal_value(s, num_start):
    num_digits = 0
    curr_num = ""
    while binary[num_start] == "1":
        curr_num += binary[num_start+1:num_start+5]
        num_digits += 1
        num_start += 5

    if binary[num_start] == "0":
        curr_num += binary[num_start+1:num_start+5]
        num_digits += 1
        num_start += 5

    total_valid_digits = num_digits * 5 + 6
    total_digits = total_valid_digits
    while total_digits % 4 != 0:
        total_digits += 1

    return total_digits

def parse_operator(binary, all_versions, length_type_id, start_length_type_id_bits):
    # operator packet
    length_type_id = binary[6 + start]
    start_length_type_id_bits = 7 + start

    if length_type_id == "1":
        # number of sub packets
        num_sub_packets = convert_binary_to_decimal(binary[start_length_type_id_bits: start_length_type_id_bits+11])
        start_sub_packets = start_length_type_id_bits+11

        parse_count_packets(binary, start_sub_packets, all_versions, num_sub_packets)

    else:
        # total length of sub packets
        length_sub_packets = convert_binary_to_decimal(binary[start_length_type_id_bits: start_length_type_id_bits+15])
        start_sub_packets = start_length_type_id_bits+15

        parse_measure_length(binary, start_sub_packets, all_versions, length_sub_packets)

        return length_sub_packets


def parse_count_packets():
    return None

def parse_measure_length():
    return None


def parse(binary, start, all_versions):

    while start < len(binary):
        version = binary[start:3+start]
        type_id = binary[start+3:6+start]

        if type_id == "100":
            # literal value
            num_start = 6 + start
            total_digits = parse_literal_value(binary, num_start)

            all_versions.append(version)
            # next packet
            start += total_digits

        else:
            # operator packet
            length_type_id = binary[6 + start]
            start_length_type_id_bits = 7 + start

            all_versions.append(version)

            total_digits = parse_operator(binary, all_versions, length_type_id, start_length_type_id_bits)

            start += total_digits

with open('day16_input.txt') as f:
    lines = f.readlines()
    input = lines[0].rstrip()
    m = dict()
    m['0'] = '0000'
    m['1'] = '0001'
    m['2'] = '0010'
    m['3'] = '0011'
    m['4'] = '0100'
    m['5'] = '0101'
    m['6'] = '0110'
    m['7'] = '0111'
    m['8'] = '1000'
    m['9'] = '1001'
    m['A'] = '1010'
    m['B'] = '1011'
    m['C'] = '1100'
    m['D'] = '1101'
    m['E'] = '1110'
    m['F'] = '1111'

    binary = ""

    for c in input:
        binary += m[c]

    binary = "110100101111111000101000"

    all_versions = []

    parse(binary, 0, all_versions)

    print(len(all_versions))
