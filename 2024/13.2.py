import math
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = [[]]
    for line in sys.stdin:
        line = line.strip()
        if not line:
            inputs.append([])
            continue

        inputs[-1].append(line)

    return inputs


def clean_button_input(button):
    button = button.split(":")[1].strip().split(",")
    for i in range(len(button)):
        button[i] = int(button[i].strip().split("+")[1].strip())

    return button


def clean_prize_input(prize):
    prize = prize.split(":")[1].strip().split(",")
    for i in range(len(prize)):
        prize[i] = int(prize[i].strip().split("=")[1])
        prize[i] += 10000000000000

    return prize


def get_clean_input(inputs):
    machines = []
    for button_a, button_b, prize in inputs:
        machine = [
            clean_button_input(button_a),
            clean_button_input(button_b),
            clean_prize_input(prize),
        ]
        machines.append(machine)

    return machines


def solve(inputs):
    machines = get_clean_input(inputs)
    tokens = 0

    for button_a, button_b, prize in machines:
        ax, ay = button_a
        bx, by = button_b
        px, py = prize

        s = (px * by - py * bx) / (ax * by - bx * ay)
        t = (px - ax * s) / bx

        if s % 1 == 0 and t % 1 == 0:
            tokens += s * 3 + t

    return int(tokens)


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
