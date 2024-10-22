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


def iterate(grid):
    m, n = len(grid), len(grid[0])
    new_grid = [[grid[i][j] for j in range(n)] for i in range(m)]

    for x in range(m):
        for y in range(n):
            neighbor_count = 0
            for dx, dy in [
                (0, 1),
                (1, 0),
                (-1, 0),
                (0, -1),
                (-1, -1),
                (1, 1),
                (-1, 1),
                (1, -1),
            ]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "#":
                    neighbor_count += 1

            if grid[x][y] == "#":
                if neighbor_count not in (2, 3):
                    new_grid[x][y] = "."

            if grid[x][y] == ".":
                if neighbor_count == 3:
                    new_grid[x][y] = "#"

    return new_grid


def solve(grid):
    ITERATION_COUNT = 100
    for _ in range(ITERATION_COUNT):
        grid = iterate(grid)

    ans = 0
    for row in grid:
        ans += row.count("#")

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
