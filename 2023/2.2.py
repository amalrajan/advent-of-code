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


ans = 0

while True:
    try:
        game = input()
    except EOFError:
        break

    game_id, game = game.split(":")
    cube_lines = game.split(";")

    max_red, max_green, max_blue = 0, 0, 0

    for cube_line in cube_lines:
        red, green, blue = parse_color_count(cube_line)
        max_red = max(max_red, red)
        max_green = max(max_green, green)
        max_blue = max(max_blue, blue)

    product = max_red * max_green * max_blue
    ans += product

print(ans)
