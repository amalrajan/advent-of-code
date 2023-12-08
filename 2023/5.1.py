import collections
import sys
import bisect
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def get_input():
    inp = []

    for line in sys.stdin:
        if not line or line.isspace():
            break
        elif "map" in line:
            continue
        dest, source, steps = list(map(int, line.strip().split()))

        # Append the other way for convenience
        # If the val is between [0] and [1], increment by [2]
        inp.append([source, source + steps - 1, dest - source])

    inp.sort(key=lambda x: x[0])

    return inp


def update_seeds(next_map):
    ends = [x[1] for x in next_map]
    # print("Map: ", next_map)

    for i in range(len(seeds)):
        seed = seeds[i]
        pos = bisect.bisect_left(ends, seed)
        # print(seed, pos)

        if pos == len(next_map) or next_map[pos][0] > seeds[i]:
            continue
        seeds[i] = seeds[i] + next_map[pos][2]


seeds = list(map(int, input().strip().split(":")[1].split()))
# print(seeds)

for line in sys.stdin:
    if not line:
        continue

    next_map = get_input()

    update_seeds(next_map)
    # print(seeds)

print(min(seeds))
