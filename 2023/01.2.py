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


def find_first_digit(text, digit_list, inverted):
    first_digit = None

    for i in range(len(text)):
        if text[i].isdigit():
            first_digit = int(text[i])
            break

        for j in range(len(digit_list)):
            n = len(digit_list[j])

            sub = text[i : i + n]
            if inverted:
                sub = sub[::-1]

            if sub == digit_list[j]:
                first_digit = j
                break

        if first_digit is not None:
            break

    return first_digit


def solve(inputs):
    ans = 0
    digit_list = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]

    for text in inputs:
        first_digit = find_first_digit(text, digit_list, inverted=False)
        last_digit = find_first_digit(text[::-1], digit_list, inverted=True)

        ans += first_digit * 10 + last_digit

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
