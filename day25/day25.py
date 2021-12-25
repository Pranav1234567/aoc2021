def move_right(grid):
    moves = 0
    for row in grid:
        i = 0
        first_filled = False
        while i < len(row):
            if i < len(row) - 1:
                if row[0] != '.':
                    first_filled = True

                if row[i] == '>' and row[i+1] == '.':
                    row[i] = '.'
                    row[i+1] = '>'
                    moves += 1
                    i += 1
            else:
                if row[i] == '>' and not first_filled:
                    row[0] = '>'
                    row[i] = '.'
                    moves += 1
            i += 1
    return moves
def move_down(grid):
    moves = 0
    for j in range(len(grid[0])):
        i = 0
        first_filled = False
        while i < len(grid):
            if i < len(grid) - 1:

                if grid[0][j] != '.':
                    first_filled = True

                if grid[i][j] == 'v' and grid[i+1][j] == '.':
                    grid[i][j] = '.'
                    grid[i+1][j] = 'v'
                    moves += 1
                    i += 1
            else:
                if grid[i][j] == 'v' and not first_filled:
                    grid[0][j] = 'v'
                    grid[i][j] = '.'
                    moves += 1
            i += 1
    return moves

def printGrid(grid):
    for row in grid:
        print("".join(row))

with open('day25_input.txt') as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        grid.append([c for c in line.rstrip()])

    # printGrid(grid)

    stop = False
    steps = 0
    while not stop:
        moves = 0
        steps += 1
        moves += move_right(grid)
        moves += move_down(grid)

        # print(moves)

        # if steps == 1:
        #     stop = True

        if moves == 0:
            stop = True

        # if steps == 1:
        #     print("***")
        #     printGrid(grid)
        #
        # if steps == 2:
        #     print("***")
        #     printGrid(grid)
        #
        # if steps == 3:
        #     print("***")
        #     printGrid(grid)
        #
        # if steps == 4:
        #     print("***")
        #     printGrid(grid)

        # if steps == 5:
        #     stop = True

    print(steps)
    # printGrid(grid)
