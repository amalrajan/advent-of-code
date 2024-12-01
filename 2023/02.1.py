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


def is_valid(game):
    elf_cubes = [12, 13, 14]

    for cubes in game:
        for cube_count, cube in cubes:
            if cube == "red" and cube_count > elf_cubes[0]:
                return False
            elif cube == "green" and cube_count > elf_cubes[1]:
                return False
            elif cube == "blue" and cube_count > elf_cubes[2]:
                return False

    return True


def solve(games):
    ans = 0
    for game_id, game in enumerate(games):
        if is_valid(game):
            ans += game_id + 1

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
