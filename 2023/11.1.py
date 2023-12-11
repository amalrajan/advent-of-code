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


def transpose_matrix(matrix):
    transpose_matrix = list(map(list, zip(*matrix)))

    return transpose_matrix


def expand_galaxy_rows(galaxy):
    expanded_galaxy = []
    for row in galaxy:
        expanded_galaxy.append(row)
        if "#" not in row:
            expanded_galaxy.append(row)

    return expanded_galaxy


def expand_galaxy(galaxy):
    expanded_galaxy = expand_galaxy_rows(galaxy)
    transposed = transpose_matrix(expanded_galaxy)
    expanded_galaxy = expand_galaxy_rows(transposed)

    return transpose_matrix(expanded_galaxy)


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
galaxy = expand_galaxy(galaxy)
positions = get_all_positions(galaxy)
total_dist = calculate_total_distance(positions)

print("Ans: ", total_dist)
