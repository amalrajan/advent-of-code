import sys
import collections

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    compartments = []
    for line in sys.stdin:
        line = line.strip()
        compartments.append((line[: len(line) // 2], line[len(line) // 2 :]))

    return compartments


def get_common_chars(compartments):
    ans = 0

    for part1, part2 in compartments:
        ch = set(part1).intersection(set(part2)).pop()
        if ch.islower():
            ans += ord(ch) - ord("a") + 1
        else:
            ans += ord(ch) - ord("A") + 27

    return ans


compartments = parse_input()
print("Ans:", get_common_chars(compartments))
