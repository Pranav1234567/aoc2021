def is_low_point(x, y, length, width, lines):
    neighbor_vectors = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    neighbors = []
    for vector in neighbor_vectors:
        if x + vector[0] < length and x + vector[0] >= 0 and y + vector[1] < width and y + vector[1] >= 0:
            if int(lines[x + vector[0]][y + vector[1]]) <= int(lines[x][y]):
                return False
    return True

def dfs(x, y, length, width, lines, visited):
    if x < length and x >= 0 and y < width and y >= 0:
        if not visited[x][y] and int(lines[x][y]) != 9:
            visited[x][y] = True
            dfs(x+1, y, length, width, lines, visited)
            dfs(x, y+1, length, width, lines, visited)
            dfs(x-1, y, length, width, lines, visited)
            dfs(x, y-1, length, width, lines, visited)

with open('day9_input.txt') as f:
    lines = f.readlines()
    risk_sum = 0
    width = len(lines)
    all_counts = []
    for i in range(len(lines)):
        row = lines[i].rstrip()
        for j in range(len(row)):
            if is_low_point(i, j, len(row), width, lines):
                risk_sum += (int(row[j]) + 1)
                # find basin here with depth first search
                visited = [[False for i in range(len(row))] for j in range(len(lines))]
                dfs(i, j, len(row), width, lines, visited)
                count = 0
                for r in visited:
                    for element in r:
                        if element:
                            count += 1
                all_counts.append(count)
    print(risk_sum)
    print(sorted(all_counts)[::-1][:3])

