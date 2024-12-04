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

    word = "XMAS"
    ans = 0

    for i in range(m):
        for j in range(n):
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue

                    x, y = i, j
                    pos = 0
                    while (
                        0 <= x < m
                        and 0 <= y < n
                        and pos < len(word)
                        and word[pos] == grid[x][y]
                    ):
                        x += dx
                        y += dy
                        pos += 1

                    if pos == len(word):
                        ans += 1

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
