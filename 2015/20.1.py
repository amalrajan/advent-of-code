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
        while j <= n:
            dp[j] += 10 * i
            j += i

        if dp[i] >= inp:
            return i


if __name__ == "__main__":
    inp = 36000000
    print(solve(inp))
