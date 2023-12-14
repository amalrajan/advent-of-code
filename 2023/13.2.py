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

        one_smudge = False
        mirror_exists = False
        if (
            pattern[above] == pattern[below]
            or check_for_smudge(pattern[above], pattern[below]) == True
        ):
            mirror_exists = True

        while above >= 0 and below < len(pattern):
            if pattern[above] == pattern[below]:
                above -= 1
                below += 1
            elif (
                one_smudge == False
                and check_for_smudge(pattern[above], pattern[below]) == True
            ):
                one_smudge = True
                above -= 1
                below += 1
            else:
                break

        if mirror_exists and one_smudge and (above == -1 or below == len(pattern)):
            mirror_point = point
            break

        point += 1

    return mirror_point


def check_for_smudge(row1, row2):
    one_smudge = False
    for i in range(len(row1)):
        if row1[i] != row2[i]:
            if one_smudge == False:
                one_smudge = True
            else:
                return False

    return True


def transpose_matrix(matrix):
    transpose_matrix = list(map(list, zip(*matrix)))
    return ["".join(row) for row in transpose_matrix]


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
