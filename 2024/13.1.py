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


def min_cost(button_a, button_b, prize):
    ax, ay = button_a
    bx, by = button_b
    px, py = prize

    cost = math.inf
    MAX_PRESSES = 100

    for a in range(MAX_PRESSES + 1):
        for b in range(MAX_PRESSES + 1):
            val1 = a * ax + b * bx
            val2 = a * ay + b * by

            if val1 == px and val2 == py:
                cost = min(cost, a * 3 + b * 1)

    return cost


def solve(inputs):
    machines = get_clean_input(inputs)
    tokens = 0

    for button_a, button_b, prize in machines:
        cost = min_cost(button_a, button_b, prize)
        if cost != math.inf:
            tokens += cost

    return tokens


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
