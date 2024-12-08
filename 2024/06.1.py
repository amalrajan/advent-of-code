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


def solve(grid):
    m = len(grid)
    n = len(grid[0])

    start_x, start_y = 0, 0
    for i in range(m):
        if "^" in grid[i]:
            start_x = i
            start_y = grid[i].index("^")
            break

    x, y, dx, dy = start_x, start_y, -1, 0
    grid[x][y] = "."

    ans = 0
    while grid[x][y] == "." or grid[x][y] == "X":
        if grid[x][y] != "X":
            grid[x][y] = "X"
            ans += 1
        nx, ny = x + dx, y + dy

        if not 0 <= nx < m or not 0 <= ny < n:
            break

        if grid[nx][ny] == "#":
            dx, dy = dy, -dx
        x += dx
        y += dy

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
