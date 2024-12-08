import collections
import sys
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(list(line.strip()))

    return inputs


def solve(grid):
    m = len(grid)
    n = len(grid[0])

    antennas = collections.defaultdict(list)
    antinodes = set()

    for i in range(m):
        for j in range(n):
            if grid[i][j].isalpha() or grid[i][j].isdigit():
                antennas[grid[i][j]].append((i, j))

    for _, positions in antennas.items():
        for i in range(len(positions)):
            x1, y1 = positions[i]
            for j in range(i + 1, len(positions)):
                x2, y2 = positions[j]

                dx1, dy1 = x1 - x2, y1 - y2
                px1, py1 = x1 + dx1, y1 + dy1

                if 0 <= px1 < m and 0 <= py1 < n:
                    antinodes.add((px1, py1))

                dx2, dy2 = x2 - x1, y2 - y1
                px2, py2 = x2 + dx2, y2 + dy2

                if 0 <= px2 < m and 0 <= py2 < n:
                    antinodes.add((px2, py2))

    return len(antinodes)


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
