with open('day5_input.txt') as f:
    lines = f.readlines()
    m = dict()
    for line in lines:
        point1, point2 = line.split('->')
        x1, y1 = list(map(lambda x: int(x), point1.split(',')))
        x2, y2 = list(map(lambda x: int(x), point2.split(',')))
        # part 1
        if x1 == x2:
            end = max(y1, y2)
            start = min(y1, y2)
            for v in range(start, end + 1):
                if (x1, v) in m:
                    m[(x1, v)] += 1
                else:
                    m[(x1, v)] = 1
        elif y1 == y2:
            end = max(x1, x2)
            start = min(x1, x2)
            for v in range(start, end + 1):
                if (v, y1) in m:
                    m[(v, y1)] += 1
                else:
                    m[(v, y1)] = 1
        # part 2
        elif abs(y2 - y1) == abs(x2 - x1):
            slope = (y2 - y1) / (x2 - x1)
            start_x = x1
            start_y = y1
            if slope == 1:
                if y2 - y1 > 0:
                    while start_x < x2 + 1:
                        if (start_x, start_y) in m:
                            m[(start_x, start_y)] += 1
                        else:
                            m[(start_x, start_y)] = 1
                        start_x += 1
                        start_y += 1
                else:
                    while start_x > x2 - 1:
                        if (start_x, start_y) in m:
                            m[(start_x, start_y)] += 1
                        else:
                            m[(start_x, start_y)] = 1
                        start_x -= 1
                        start_y -= 1
            elif slope == -1:
                if x2 - x1 > 0:
                    while start_x < x2 + 1:
                        if (start_x, start_y) in m:
                            m[(start_x, start_y)] += 1
                        else:
                            m[(start_x, start_y)] = 1
                        start_x += 1
                        start_y -= 1
                else:
                    while start_x > x2 - 1:
                        if (start_x, start_y) in m:
                            m[(start_x, start_y)] += 1
                        else:
                            m[(start_x, start_y)] = 1
                        start_x -= 1
                        start_y += 1

    count = 0
    for key in m.keys():
        if m[key] >= 2:
            count += 1
    print(count)
