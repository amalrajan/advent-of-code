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
    m = len(grid)
    n = len(grid[0])

    def dfs(x, y, num, path):
        if not 0 <= x < m or not 0 <= y < n:
            return 0

        if grid[x][y] == 9:
            return 1

        temp = grid[x][y]
        grid[x][y] = -1
        cnt = 0

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == num + 1:
                cnt += dfs(nx, ny, num + 1, path + [(nx, ny)])

        grid[x][y] = temp
        return cnt

    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                ans += dfs(i, j, 0, [(i, j)])

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
