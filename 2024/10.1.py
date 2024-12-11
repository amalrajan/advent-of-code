import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(list(map(int, line.strip())))

    return inputs


def solve(grid):
    # Important thing to notice is that score is counted as how many "9"s you
    # can reach from each 0. Not every path count.
    m = len(grid)
    n = len(grid[0])

    reached = set()

    def dfs(x, y, num, path):
        if not 0 <= x < m or not 0 <= y < n:
            return

        if grid[x][y] == 9:
            reached.add((x, y))
            return

        temp = grid[x][y]
        grid[x][y] = -1

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == num + 1:
                dfs(nx, ny, num + 1, path + [(nx, ny)])

        grid[x][y] = temp

    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                reached.clear()
                dfs(i, j, 0, [(i, j)])
                ans += len(reached)

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
