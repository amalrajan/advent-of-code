import collections
import sys
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    galaxy = []
    for line in sys.stdin:
        galaxy.append(list(line.strip()))

    return galaxy


def expand_galaxy_rows(pos, k):
    # Expand rows
    expanded_rows = [pos[0][0] * k]
    for i in range(1, len(pos)):
        # print(expanded_rows)
        diff = pos[i][0] - pos[i - 1][0] - 1
        if diff < 0:
            expanded_rows.append(expanded_rows[-1])
        else:
            expanded_rows.append(expanded_rows[-1] + (diff * k) + 1)

    for i in range(len(pos)):
        pos[i] = (expanded_rows[i], pos[i][1])

    pos.sort(key=lambda x: x[1])

    # Expand cols
    expanded_cols = [pos[0][1] * k]
    for i in range(1, len(pos)):
        diff = pos[i][1] - pos[i - 1][1] - 1
        if diff < 0:
            expanded_cols.append(expanded_cols[-1])
        else:
            expanded_cols.append(expanded_cols[-1] + (diff * k) + 1)

    for i in range(len(pos)):
        pos[i] = (pos[i][0], expanded_cols[i])

    return pos


def get_all_positions(galaxy):
    positions = []

    for i in range(len(galaxy)):
        for j in range(len(galaxy[0])):
            if galaxy[i][j] == "#":
                positions.append((i, j))

    return positions


def calculate_total_distance(pos):
    dist = 0
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            dist += abs(pos[i][0] - pos[j][0]) + abs(pos[i][1] - pos[j][1])

    return dist


galaxy = parse_input()
positions = get_all_positions(galaxy)
positions = expand_galaxy_rows(positions, 2)
for pr in positions:
    print(pr)
total_dist = calculate_total_distance(positions)

print("Ans: ", total_dist)
