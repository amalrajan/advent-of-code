import re
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    text = ""

    for line in sys.stdin:
        text += line.strip()

    return text


def solve(text):
    ans = 0
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")

    multiply_flag = True
    operations = {
        "do()": True,
        "don't()": False,
    }

    for i in range(len(text)):
        for operation in operations:
            if text[i : i + len(operation)] == operation:
                multiply_flag = operations[operation]

        if multiply_flag:
            match = pattern.match(text, i)
            if match:
                num1, num2 = (
                    match.group().replace("mul(", "").replace(")", "").split(",")
                )
                ans += int(num1) * int(num2)

    return ans


if __name__ == "__main__":
    text = parse_input()
    print(solve(text))
