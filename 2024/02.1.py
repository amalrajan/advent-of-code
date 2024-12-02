import collections
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(list(map(int, line.strip().split())))

    return inputs


def solve(reports):
    ans = 0

    for report in reports:
        increasing = False
        decreasing = False

        is_valid = True

        for i in range(1, len(report)):
            diff = report[i] - report[i - 1]

            if diff >= 0:
                increasing = True
            else:
                decreasing = True

            if increasing and decreasing:
                is_valid = False
                break

            if not 1 <= abs(diff) <= 3:
                is_valid = False
                break

        # print(report, is_valid)
        if is_valid:
            ans += 1

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
