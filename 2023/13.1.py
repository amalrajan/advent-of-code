import sys
from pprint import pprint


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    patterns = []

    pattern = []
    for line in sys.stdin:
        line = line.strip()
        if line.isspace() or not line:
            patterns.append(pattern)
            pattern = []
        else:
            pattern.append(line)

    if pattern:
        patterns.append(pattern)

    return patterns


def check_for_horizontal_mirrors(pattern):
    point = 1
    mirror_point = -1
    while point < len(pattern):
        above = point - 1
        below = point

        mirror_exists = False
        if pattern[above] == pattern[below]:
            mirror_exists = True

        while above >= 0 and below < len(pattern) and pattern[above] == pattern[below]:
            above -= 1
            below += 1
        above += 1
        below -= 1

        if mirror_exists and (above == 0 or below == len(pattern) - 1):
            mirror_point = point
            break

        point += 1

    return mirror_point


def transpose_matrix(matrix):
    transpose_matrix = list(map(list, zip(*matrix)))
    return transpose_matrix


patterns = parse_input()

horizontals = 0
verticals = 0

for pattern in patterns:
    hor = check_for_horizontal_mirrors(pattern)
    if hor != -1:
        horizontals += hor
        continue

    ver = check_for_horizontal_mirrors(transpose_matrix(pattern))
    if ver != -1:
        verticals += ver

print("Ans: ", 100 * horizontals + verticals)
