import math
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    coordinates = [(0, 0, None)]

    for line in sys.stdin:
        direction, distance, _ = line.strip().split()
        distance = int(distance)
        dx, dy = direction_map[direction]
        x, y, _ = coordinates[-1]
        coordinates.append((x + dx * distance, y + dy * distance, direction))

    return coordinates


def create_grid(coordinates):
    min_row = math.inf
    min_col = math.inf

    for x, y, _ in coordinates:
        min_row = min(min_row, x)
        min_col = min(min_col, y)

    rows = -math.inf
    cols = -math.inf
    for i in range(len(coordinates)):
        coordinates[i] = (
            coordinates[i][0] - min_row,
            coordinates[i][1] - min_col,
            coordinates[i][2],
        )
        rows = max(rows, coordinates[i][0])
        cols = max(cols, coordinates[i][1])
    rows += 1
    cols += 1

    grid = [["."] * cols for _ in range(rows)]
    boundary = 0

    x, y, _ = coordinates[0]
    for i in range(1, len(coordinates)):
        cx, cy, direction = coordinates[i]
        px, py, _ = coordinates[i - 1]
        dx, dy = direction_map[direction]

        for _ in range(abs(cx - px)):
            x += dx
            y += dy
            grid[x][y] = "#"
            boundary += 1
        for _ in range(abs(cy - py)):
            x += dx
            y += dy
            grid[x][y] = "#"
            boundary += 1

    return grid, boundary


def display(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                print(grid[i][j], end="")
            else:
                print(".", end="")
        print()


def flood_fill_util(grid, x, y):
    m = len(grid)
    n = len(grid[0])

    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        grid[x][y] = "#"

        for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == ".":
                stack.append((nx, ny))


def flood_fill(grid):
    m = len(grid)
    n = len(grid[0])

    # Handle the top and bottom borders
    for j in range(n):
        if grid[0][j] == ".":
            flood_fill_util(grid, 0, j)
        if grid[m - 1][j] == ".":
            flood_fill_util(grid, m - 1, j)

    # Handle the left and right borders
    for i in range(m):
        if grid[i][0] == ".":
            flood_fill_util(grid, i, 0)
        if grid[i][n - 1] == ".":
            flood_fill_util(grid, i, n - 1)

    # Count the interior region
    interior_area = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == ".":
                interior_area += 1

    return interior_area


direction_map = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}

coordinates = parse_input()
grid, boundary = create_grid(coordinates)
interior_area = flood_fill(grid)

print("Ans:", boundary + interior_area)
