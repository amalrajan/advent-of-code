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
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)

    for match in matches:
        num1, num2 = match.replace("mul(", "").replace(")", "").split(",")
        ans += int(num1) * int(num2)

    return ans


if __name__ == "__main__":
    text = parse_input()
    print(solve(text))
