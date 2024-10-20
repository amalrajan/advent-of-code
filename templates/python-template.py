import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(line.strip())

    return inputs


def solve(inputs):
    return


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
