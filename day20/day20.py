def convert_str(str_array):
    return "".join(["0" if c == "." else "1" for c in str_array])

def convert_binary(binary):
    num = 0
    multiplier = 1
    str = binary
    while len(str) > 0:
        num += multiplier * int(str[-1])
        str = str[:-1]
        multiplier *= 2
    return num


def enhance_image(img, enhancement_str):
    img_inside = []

    for i in range(len(img)-2):
        row = []
        for j in range(len(img[0])-2):
            binary = ""
            for x in range(i, i+3):
                binary += convert_str(img[x][j:j+3])
            position = convert_binary(binary)
            row.append(enhancement_str[position-1])
        img_inside.append(row)

    return img_inside

def reconstruct_image(img, img_inside):
    row_num = 0
    for i in range(1, len(img)-1):
        img_inside[row_num] = [img[i][0]] + img_inside[row_num] + [img[i][-1]]
        row_num += 1

    img_inside = [img[0]] + img_inside + [img[-1]]

    return img_inside

def expand_img(reconstructed_image, original_img, expansion_size):
    for i in range(1, expansion_size + 1):
        reconstructed_image = reconstruct_image([["." for i in range(len(original_img[0])+i)] for j in range(len(original_img) + i)],reconstructed_image)
    return reconstructed_image

def print_image(img):
    for row in img:
        print("".join(row))


with open('day20_input.txt') as f:
    lines = f.readlines()
    all_inputs = [line.rstrip() for line in lines]
    enhancement_str = all_inputs[0]
    img = [[c for c in str] for str in all_inputs[2:]]

    reconstructed_image = expand_img(img, img, 300)

    img_inside = enhance_image(reconstructed_image, enhancement_str)
    reconstructed_image = reconstruct_image(reconstructed_image, img_inside)

    img_inside = enhance_image(reconstructed_image, enhancement_str)
    reconstructed_image = reconstruct_image(reconstructed_image, img_inside)

    count = 0
    for i in range(len(reconstructed_image)):
        for j in range(len(reconstructed_image[0])):
            if reconstructed_image[i][j] == "#":
                count += 1

    print(count)
