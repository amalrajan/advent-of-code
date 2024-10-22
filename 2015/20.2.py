import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def solve(inp):
    n = 1200000
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        j = i
        cnt = 0
        while j <= n and cnt < 50:
            dp[j] += 11 * i
            j += i
            cnt += 1

        if dp[i] >= inp:
            return i


if __name__ == "__main__":
    inp = 36000000
    print(solve(inp))
