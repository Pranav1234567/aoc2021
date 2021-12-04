def check_rows(grid):
    for line in grid:
        if all(line):
            return True
    return False

def check_cols(grid):
    for j in range(len(grid[0])):
        result = True
        for i in range(len(grid)):
            result = (grid[i][j] and result)
        if result:
            return True
    return False

# converts each grid into a dictionary of grid_element : (row, col)
def convert_inputs(lines):
    count = 0
    all_grid_locations = []
    grid_location = dict()
    row = 0
    for line in lines:
        if count == 0:
            moves = line.split(',')
        else:
            if line == '\n':
                row = 0
                all_grid_locations.append(grid_location)
                grid_location = dict()
            else:
                grid_line = line.rstrip().split()
                for i in range(len(grid_line)):
                    grid_location[grid_line[i]] = (row, i)
                row += 1
        count += 1

    all_grid_locations = all_grid_locations[1:]

    return (moves, all_grid_locations)

def get_first_win(moves, all_grid_locations):

    min_moves = len(moves)
    min_index = -1

    for k, grid_locations in enumerate(all_grid_locations):
        boolean_grid = [[False for i in range(5)] for j in range(5)]
        for move_num, move in enumerate(moves):
            if move in grid_locations:
                row, col = grid_locations[move]
                boolean_grid[row][col] = True

                if check_rows(boolean_grid) or check_cols(boolean_grid):
                    if move_num + 1 < min_moves:
                        min_moves = move_num + 1
                        min_index = k

    return (min_index, min_moves)

def get_last_win(moves, all_grid_locations):

    all_win_num_moves = []

    for k, grid_locations in enumerate(all_grid_locations):
        boolean_grid = [[False for i in range(5)] for j in range(5)]
        won = False
        for move_num, move in enumerate(moves):
            if move in grid_locations:
                row, col = grid_locations[move]
                boolean_grid[row][col] = True

                if check_rows(boolean_grid) or check_cols(boolean_grid):
                    all_win_num_moves.append((k, move_num + 1))
                    won = True

            if won:
                break
    # last win
    return sorted(all_win_num_moves, key=lambda tup: tup[1])[-1]

def compute_result(winning_grid, move_num, moves):

    grid_elements = winning_grid.keys()
    unmarked = grid_elements - moves[:move_num]
    winning_move = moves[move_num-1]
    unmarked_sum = sum(list(map(lambda x : int(x), unmarked)))

    return unmarked_sum * int(winning_move)

with open('day4_input.txt') as f:
    lines = f.readlines()

    moves, all_grid_locations = convert_inputs(lines)

    # part 1
    (min_index, min_moves) = get_first_win(moves, all_grid_locations)
    first_winning_grid = all_grid_locations[min_index]
    print(compute_result(first_winning_grid, min_moves, moves))

    # part 2
    (grid_num, move_num) = get_last_win(moves, all_grid_locations)
    last_winning_grid = all_grid_locations[grid_num]
    print(compute_result(last_winning_grid, move_num, moves))

