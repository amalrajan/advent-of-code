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


def check_for_loop(grid, x, y):
    m = len(grid)
    n = len(grid[0])

    seen = set()
    dx, dy = -1, 0

    while True:
        seen.add((x, y, dx, dy))

        if not 0 <= x + dx < m or not 0 <= y + dy < n:
            break
        elif grid[x + dx][y + dy] == "#":
            dx, dy = dy, -dx
        else:
            x, y = x + dx, y + dy
        if (x, y, dx, dy) in seen:
            return True

    return False


def solve(grid):
    m = len(grid)
    n = len(grid[0])
    ans = 0

    for start_x in range(m):
        for start_y in range(n):
            if grid[start_x][start_y] == "^":
                break
        else:
            continue
        break

    for i in range(m):
        for j in range(n):
            if grid[i][j] == ".":
                grid[i][j] = "#"
                if check_for_loop(grid, start_x, start_y):
                    ans += 1
                grid[i][j] = "."

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
