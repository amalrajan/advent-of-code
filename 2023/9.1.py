import collections
import sys
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def calculate_history(nums):
    history = [nums]

    while set(history[-1]) != {0}:
        next_row = []
        for i in range(1, len(history[-1])):
            next_row.append(history[-1][i] - history[-1][i - 1])

        history.append(next_row)

    history[-1].append(0)

    for i in range(len(history) - 2, -1, -1):
        history[i].append(history[i + 1][-1] + history[i][-1])

    return history[0][-1]


ans = 0
for line in sys.stdin:
    val = calculate_history(list(map(int, line.strip().split())))
    # print(val)
    ans += val

print(ans)
