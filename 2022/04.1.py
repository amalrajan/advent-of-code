import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    pairs = []
    for line in sys.stdin:
        first, second = line.strip().split(",")
        first = tuple(int(x) for x in first.split("-"))
        second = tuple(int(x) for x in second.split("-"))
        pairs.append((first, second))

    return pairs


def count_valid_pairs(pairs):
    ans = 0

    for (x1, y1), (x2, y2) in pairs:
        if (x1 <= x2 and y2 <= y1) or (x2 <= x1 and y1 <= y2):
            ans += 1

    return ans


pairs = parse_input()
print("Ans:", count_valid_pairs(pairs))
