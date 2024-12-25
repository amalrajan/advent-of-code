import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(list(line.strip()))

    return inputs


def dfs(grid, x, y, char, visited):
    if (
        not 0 <= x < len(grid)
        or not 0 <= y < len(grid[x])
        or grid[x][y] != char
        or (x, y) in visited
    ):
        return (0, 0)

    area = 1
    perimeter = count_perimeter(grid, x, y, char)
    visited.add((x, y))

    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[x]):
            a, p = dfs(grid, nx, ny, char, visited)
            area += a
            perimeter += p

    return (area, perimeter)


def count_perimeter(grid, r, c, char):
    perimeter = 0

    if r == 0 or grid[r - 1][c] != char:
        perimeter += 1
    if r == len(grid) - 1 or grid[r + 1][c] != char:
        perimeter += 1
    if c == 0 or grid[r][c - 1] != char:
        perimeter += 1
    if c == len(grid[0]) - 1 or grid[r][c + 1] != char:
        perimeter += 1

    return perimeter


def solve(grid):
    arr = []
    visited = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "#" and (i, j) not in visited:
                char = grid[i][j]
                area, perimeter = dfs(grid, i, j, char, visited)
                arr.append((char, area, perimeter))

                # for row in grid:
                #     print("".join(row))
                # print()

    ans = 0
    for char, area, perimeter in arr:
        # print(char, area, perimeter)
        ans += area * perimeter

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
