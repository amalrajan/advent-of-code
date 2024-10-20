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

    for word in inputs:
        char_count = 0
        n = len(word)
        for i in range(n):
            if word[i] == '"' or word[i] == "\\":
                char_count += 2
            else:
                char_count += 1

        char_count += 2
        ans += char_count - len(word)

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
