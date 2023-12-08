import sys


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_color_count(cubes):
    blue = 0
    red = 0
    green = 0

    cubes = cubes.split(",")

    for cube in cubes:
        if not cube or cube.isspace():
            break
        # print(cube)
        num, color = cube.split()
        if "blue" in color:
            blue = int(num)
        elif "green" in color:
            green = int(num)
        elif "red" in color:
            red = int(num)

    return (red, green, blue)


id_sum = 0

while True:
    try:
        game = input()
    except EOFError:
        break

    game_id, game = game.split(":")
    cube_lines = game.split(";")

    for cube_line in cube_lines:
        red, green, blue = parse_color_count(cube_line)
        # print(cube_line, red, green, blue)
        if red > 12 or green > 13 or blue > 14:
            # print(game_id, "invalid")
            break
    else:
        id_sum += int(game_id.split()[1])

print(id_sum)
