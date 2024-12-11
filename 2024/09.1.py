import sys

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
        if expanded_disk[i] == ".":
            break
        checksum += expanded_disk[i] * i

    return checksum


def solve(disk_map):
    disk_map = [int(x) for x in disk_map]

    expanded_disk = []
    file_id = 0

    for i in range(len(disk_map)):
        if i & 1 == 0:
            expanded_disk.extend([file_id] * disk_map[i])
            file_id += 1
        else:
            expanded_disk.extend(["."] * disk_map[i])

    i = 0
    j = len(expanded_disk) - 1

    while i < j:
        while i < j and expanded_disk[i] != ".":
            i += 1

        while i < j and expanded_disk[j] == ".":
            j -= 1

        expanded_disk[i], expanded_disk[j] = expanded_disk[j], expanded_disk[i]
        i += 1
        j -= 1

    return get_checksum(expanded_disk)


if __name__ == "__main__":
    disk_map = parse_input()
    print(solve(disk_map))
