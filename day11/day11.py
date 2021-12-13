def increment_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] += 1

def check_for_flashes(grid):
    flashes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9:
                flashes.append((i, j))
    return flashes

def set_zeros(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] > 9:
                count += 1
                grid[i][j] = 0
    return count

def dfs(x, y, grid, has_flashed):
    if x < len(grid) and x >= 0 and y < len(grid[0]) and y >= 0 and not has_flashed[x][y]:
        grid[x][y] += 1
        if grid[x][y] > 9:
            has_flashed[x][y] = True
            dfs(x+1, y, grid, has_flashed)
            dfs(x, y+1, grid, has_flashed)
            dfs(x+1, y+1, grid, has_flashed)
            dfs(x-1, y, grid, has_flashed)
            dfs(x, y-1, grid, has_flashed)
            dfs(x-1, y-1, grid, has_flashed)
            dfs(x+1, y-1, grid, has_flashed)
            dfs(x-1, y+1, grid, has_flashed)

with open('day11_input.txt') as f:
    lines = f.readlines()
    grid = []
    for line in lines:
        grid.append([int(c) for c in line.rstrip()])
    total_count = 0
    step = 0
    while True:
        step += 1
        # increase level by 1
        increment_grid(grid)
        # check for flashing & dfs to increase 1 in all directions
        has_flashed = [[False for i in range(len(grid[0]))] for row in range(len(grid))]
        flashes = check_for_flashes(grid)
        for flash in flashes:
            dfs(flash[0], flash[1], grid, has_flashed)
        count = set_zeros(grid)
        total_count += count
        if count == 100:
            print(step)
            break

    # part 1
    # print(total_count)
