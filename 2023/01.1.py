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
    ans = 0

    for text in inputs:
        first_digit = 0
        last_digit = 0

        for i in range(len(text)):
            if text[i].isdigit():
                first_digit = int(text[i])
                break

        for i in range(len(text) - 1, -1, -1):
            if text[i].isdigit():
                last_digit = int(text[i])
                break

        ans += first_digit * 10 + last_digit

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
