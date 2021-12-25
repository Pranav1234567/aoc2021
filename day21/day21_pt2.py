p1_position = 8
p2_position = 6

p1_score = 0
p2_score = 0

queue = []
queue.append((p1_position, p1_score, p2_position, p2_score))

p1_wins = 0
p2_wins = 0

while queue != []:
    element = queue[0]
    queue = queue[1:]

    p1_score = 0
    # update the queue for each element
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                p1_position = (i + j + k + element[0]) % 10
                if p1_position == 0:
                    p1_position = 10
                p1_score += p1_position

                if p1_score > 20:
                    p1_wins += 1
                else:
                    p2_score = 0
                    for i in range(1, 4):
                        for j in range(1, 4):
                            for k in range(1, 4):
                                p2_position = (i + j + k + element[2]) % 10
                                if p2_position == 0:
                                    p2_position = 10
                                p2_score += p2_position

                                if p2_score > 20:
                                    p2_wins += 1
                                else:
                                    queue.append((p1_position, p1_score, p2_position, p2_score))

    print(len(queue))
    # print(p1_wins)
    # print(p2_wins)
