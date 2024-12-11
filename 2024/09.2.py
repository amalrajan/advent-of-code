import collections
import sys
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    disk_map = input().strip()
    return disk_map


def get_checksum(expanded_disk):
    checksum = 0
    for i in range(len(expanded_disk)):
        if expanded_disk[i] != ".":
            checksum += expanded_disk[i] * i

    return checksum


def solve(disk_map):
    disk_map = [int(x) for x in disk_map]
    files = []
    spaces = []

    pos = 0
    for i in range(len(disk_map)):
        if disk_map[i] == 0:
            continue

        if i & 1 == 0:
            files.append([pos, pos + disk_map[i], disk_map[i], i // 2])
        else:
            spaces.append([pos, pos + disk_map[i], disk_map[i], -1])
        pos += disk_map[i]

    i = len(files) - 1
    while i >= 0:
        j = 0
        while j < len(spaces):
            if spaces[j][0] > files[i][0]:
                j = len(spaces)
                break
            if spaces[j][2] < files[i][2]:
                j += 1
            else:
                break

        if j == len(spaces):
            i -= 1
            continue

        # Update the file position
        files[i][0] = spaces[j][0]
        files[i][1] = files[i][0] + files[i][2]

        # Update the space position
        spaces[j][0] = files[i][1]
        spaces[j][2] -= files[i][2]

        i -= 1

    files = [item for item in files if item[2] != 0]
    files.sort()
    res = []
    pos = 0
    for i in range(len(files)):
        spaces = files[i][0] - pos
        if spaces:
            res += ["."] * spaces
            pos += spaces

        res += [files[i][3]] * files[i][2]
        pos += files[i][2]

    # print("".join(list(map(str, res))))

    return get_checksum(res)


if __name__ == "__main__":
    disk_map = parse_input()
    print(solve(disk_map))
