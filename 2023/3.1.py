import sys


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def symbol_nearby(grid, x, y):
    symbols = "#$%&'()*+,-/:;<=>?@[\\]^_`{|}~"

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
            if grid[new_x][new_y] in symbols:
                return True

    return False


def extract_nums(grid):
    nums_arr = []
    nums_next_to_symbols = []

    for i in range(len(grid)):
        line = grid[i]

        j = 0
        temp = 0
        while j < len(line):
            num_encountered = False
            next_to_a_symbol = False
            while j < len(line) and line[j].isdigit():
                num_encountered = True

                if not next_to_a_symbol and symbol_nearby(grid, i, j):
                    next_to_a_symbol = True

                temp = temp * 10 + int(line[j])
                j += 1
            if num_encountered:
                if next_to_a_symbol:
                    nums_next_to_symbols.append(temp)
                nums_arr.append(temp)
            temp = 0
            j += 1

    # print(nums_arr)
    # print(nums_next_to_symbols)
    return sum(nums_next_to_symbols)


grid = []
while True:
    try:
        line = input()
    except EOFError:
        break

    grid.append(line)

ans = extract_nums(grid)
print(ans)
