import collections
import sys
import bisect
from pprint import pprint
from multiprocessing import Pool

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    # sys.stdout = open(sys.path[0] + "/output.txt", "w")
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


def next_seed(next_map, seed, ends):
    pos = bisect.bisect_left(ends, seed)

    if pos == len(next_map) or next_map[pos][0] > seed:
        return seed
    seed = seed + next_map[pos][2]

    return seed


seed_range = list(map(int, input().strip().split(":")[1].split()))

all_maps = []
all_ends = []

for line in sys.stdin:
    if not line:
        continue

    next_map = get_input()
    all_maps.append(next_map)
    all_ends.append([x[1] for x in next_map])


def process_seed_range(seed_range):
    result = float("inf")

    for i in range(0, len(seed_range) - 1, 2):
        for s in range(seed_range[i], seed_range[i] + seed_range[i + 1]):
            curr = s
            for y in range(len(all_maps)):
                next_map = all_maps[y]
                ends = all_ends[y]
                curr = next_seed(next_map, curr, ends)

            result = min(result, curr)

    return result


seed_range_list = [
    list(map(int, seed_range[i : i + 2])) for i in range(0, len(seed_range), 2)
]

# Use multiprocessing Pool
with Pool() as pool:
    results = pool.map(process_seed_range, seed_range_list)

ans = min(results)

print("Ans:", ans)
