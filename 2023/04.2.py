import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        winning, yours = line.strip().split(":")[1].strip().split("|")

        winning = list(map(int, winning.strip().split()))
        yours = list(map(int, yours.strip().split()))

        inputs.append([set(winning), yours])

    return inputs


def count_copies(winning_set, yours):
    cnt = 0
    for card in yours:
        if card in winning_set:
            cnt += 1

    return cnt


def solve(table):
    dp = [0] * 10**6

    for i in range(len(table)):
        dp[i] += 1

        winning_set, yours = table[i]
        cnt = count_copies(winning_set, yours)

        for j in range(i + 1, i + cnt + 1):
            dp[j] += dp[i]

    return sum(dp)


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
