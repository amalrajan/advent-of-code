import sys
import collections

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    cnt = 0
    inp = []
    temp = []
    for line in sys.stdin:
        if cnt > 0 and cnt % 3 == 0:
            inp.append(temp)
            temp = []
        temp.append(line.strip())
        cnt += 1

    return inp + [temp]


def get_common_badge(rucksacks):
    ans = 0

    for combo in rucksacks:
        # print(combo)
        part1, part2, part3 = combo[0], combo[1], combo[2]
        ch = set(part1).intersection(set(part2)).intersection(set(part3)).pop()
        if ch.islower():
            ans += ord(ch) - ord("a") + 1
        else:
            ans += ord(ch) - ord("A") + 27

    return ans


rucksacks = parse_input()
print("Ans:", get_common_badge(rucksacks))
