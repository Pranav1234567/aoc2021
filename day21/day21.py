p1_position = 8
p2_position = 6

p1_score = 0
p2_score = 0

dice = range(1, 101)
i = 0
dice_rolls = 0

while p1_score < 999 and p2_score < 999:

    # p1 moves
    roll1 = dice[i % 100]
    roll2 = dice[(i+1) % 100]
    roll3 = dice[(i+2) % 100]

    p1_position = (roll1 + roll2 + roll3 + p1_position) % 10

    if p1_position == 0:
        p1_position = 10

    # p1 update score
    p1_score += p1_position

    i += 3
    dice_rolls += 3

    if p1_score == 1000:
        print(p2_score)
        print(dice_rolls)

    # p2 moves
    roll1 = dice[i % 100]
    roll2 = dice[(i+1) % 100]
    roll3 = dice[(i+2) % 100]
    p2_position = (roll1 + roll2 + roll3 + p2_position) % 10

    if p2_position == 0:
        p2_position = 10

    # p2 update score
    p2_score += p2_position

    i += 3
    dice_rolls += 3

# print(p1_score)
# print(p2_score)
# print(dice_rolls)
