import math
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        _, cubes = line.strip().split(":")
        cubes = [x.strip().split(",") for x in cubes.split(";")]

        for i in range(len(cubes)):
            for j in range(len(cubes[i])):
                cubes[i][j] = cubes[i][j].strip().split()
                cubes[i][j][0] = int(cubes[i][j][0])

        inputs.append(cubes)

    return inputs


def calculate_power(game):
    min_cubes = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    for cubes in game:
        for cube_count, cube in cubes:
            min_cubes[cube] = max(min_cubes[cube], cube_count)

    return math.prod(min_cubes.values())


def solve(games):
    ans = 0
    for game in games:
        ans += calculate_power(game)

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
