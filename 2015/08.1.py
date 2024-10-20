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


def is_hex(s):
    try:
        int(s, 16)
        return True
    except ValueError:
        return False


def solve(santa_list):
    ans = 0

    for word in santa_list:
        char_count = 0
        n = len(word) - 1
        i = 1
        while i < n:
            if (
                i + 3 < n
                and word[i] == "\\"
                and word[i + 1] == "x"
                and is_hex(word[i + 2 : i + 4])
            ):
                char_count += 1
                i += 4
            elif i + 1 < n and word[i] == "\\" and word[i + 1] in ("\\", '"'):
                char_count += 1
                i += 2
            else:
                i += 1
                char_count += 1

        ans += len(word) - char_count

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
