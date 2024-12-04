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

    ans = 0
    word = "MAS"

    for i in range(1, m - 1):
        for j in range(1, n - 1):
            left_diag = "".join(
                [
                    grid[i - 1][j - 1],
                    grid[i][j],
                    grid[i + 1][j + 1],
                ]
            )
            right_diag = "".join(
                [
                    grid[i - 1][j + 1],
                    grid[i][j],
                    grid[i + 1][j - 1],
                ]
            )

            if {left_diag, left_diag[::-1]} & {word} and {
                right_diag,
                right_diag[::-1],
            } & {word}:
                ans += 1

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
