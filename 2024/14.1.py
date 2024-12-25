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
    for _ in range(k):
        for robot in robots:
            robot.px += robot.vx
            robot.px %= r
            robot.py += robot.vy
            robot.py %= c


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
    k = 100

    move(robots, k, r, c)
    return get_safety_factor(robots, r, c)


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
