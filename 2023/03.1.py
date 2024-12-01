import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(line.strip())

    return inputs


def solve(grid):
    m = len(grid)
    n = len(grid[0])

    ans = 0
    for i in range(m):
        j = 0
        while j < n:
            k = j
            symbol_nearby = False

            while k < n and grid[i][k].isdigit():
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
                    nx, ny = i + dx, k + dy
                    if (
                        0 <= nx < m
                        and 0 <= ny < n
                        and grid[nx][ny] in "#$%&'()*+,-/:;<=>?@[\\]^_`{|}~"
                    ):
                        symbol_nearby = True
                        break

                k += 1

            if k != j and symbol_nearby:
                number = int(grid[i][j:k])
                ans += number

            j = k + 1

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
