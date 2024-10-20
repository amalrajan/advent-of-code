import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def expand(num):
    res = ""
    n = len(num)
    i = 0

    while i < n:
        cnt = 1
        digit = num[i]
        while i + 1 < n and num[i] == num[i + 1]:
            i += 1
            cnt += 1
        res += str(cnt) + digit
        i += 1

    return res


def solve(num):
    N = 50
    for _ in range(N):
        num = expand(num)

    return len(num)


if __name__ == "__main__":
    num = input().strip()
    print(solve(num))
