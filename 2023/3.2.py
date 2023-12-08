import collections
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def gear_nearby(grid, x, y):
    gear = "*"

    for dx, dy in (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ):
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < len(grid) and 0 <= new_y < len(grid[new_x]):
            if grid[new_x][new_y] == gear:
                return (new_x, new_y)

    return (-1, -1)


def extract_nums(grid):
    gear_bucket = collections.defaultdict(list)

    for i in range(len(grid)):
        line = grid[i]

        j = 0
        temp = 0
        while j < len(line):
            gear_indices_list = []

            num_encountered = False
            next_to_a_gear = False
            while j < len(line) and line[j].isdigit():
                num_encountered = True

                gear_indices = (-1, -1)
                if not next_to_a_gear:
                    gear_indices = gear_nearby(grid, i, j)
                if gear_indices != (-1, -1):
                    gear_indices_list.append(gear_indices)
                    next_to_a_gear = True

                temp = temp * 10 + int(line[j])
                j += 1

            if num_encountered:
                for gear_indices in gear_indices_list:
                    gear_bucket[gear_indices].append(temp)

            temp = 0
            j += 1

    ans = 0
    for x in gear_bucket:
        # print(x, gear_bucket[x])
        if len(gear_bucket[x]) == 2:
            ans += gear_bucket[x][0] * gear_bucket[x][1]

    return ans


grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append(line)

ans = extract_nums(grid)
print(ans)
