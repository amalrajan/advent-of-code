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


def scan_for_number(row, y):
    left = y
    right = y

    while left >= 0 and row[left].isdigit():
        left -= 1
    while right < len(row) and row[right].isdigit():
        right += 1
    left += 1
    right -= 1

    return (left, right)


def solve(grid):
    m = len(grid)
    n = len(grid[0])

    ans = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "*":
                numbers = set()

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
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny].isdigit():
                        left, right = scan_for_number(grid[nx], ny)
                        numbers.add((nx, left, right))

                if len(numbers) == 2:
                    prod = 1
                    for r, left, right in numbers:
                        prod *= int(grid[r][left : right + 1])
                    ans += prod

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
