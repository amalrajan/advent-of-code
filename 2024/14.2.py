import sys
from dataclasses import dataclass

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


@dataclass
class Robot:
    px: int
    py: int
    vx: int
    vy: int


def parse_input():
    inputs = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        p, v = line.split()
        py, px = p.split("=")[1].strip().split(",")
        vy, vx = v.split("=")[1].strip().split(",")
        inputs.append(
            Robot(
                int(px),
                int(py),
                int(vx),
                int(vy),
            )
        )

    return inputs


def move(robots, k, r, c):
    max_neis = 0

    for day in range(k):
        pos = set()
        neis = 0

        for robot in robots:
            robot.px += robot.vx
            robot.px %= r
            robot.py += robot.vy
            robot.py %= c

            x, y = robot.px, robot.py
            for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                if (nx, ny) in pos:
                    neis += 1
                    break
            pos.add((x, y))

        if neis > max_neis:
            max_neis = neis

            grid = [[0] * c for _ in range(r)]
            for robot in robots:
                grid[robot.px][robot.py] += 1

            print(day + 1)
            for row in grid:
                print("".join([str(x) for x in row]))
            print("\n")


def get_safety_factor(robots, r, c):
    res = [0, 0, 0, 0]

    for robot in robots:
        if robot.px == r // 2 or robot.py == c // 2:
            continue

        if robot.px <= r // 2:
            if robot.py <= c // 2:
                res[0] += 1
            else:
                res[1] += 1
        else:
            if robot.py <= c // 2:
                res[2] += 1
            else:
                res[3] += 1

    return res[0] * res[1] * res[2] * res[3]


def solve(robots):
    r = 103
    c = 101
    k = 10000

    move(robots, k, r, c)
    return get_safety_factor(robots, r, c)


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
