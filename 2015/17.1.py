import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(int(line.strip()))

    return inputs


def solve(containers):
    TOTAL_VOLUME = 150
    n = len(containers)
    ans = 0

    def backtrack(i, total):
        nonlocal ans

        if total == 0:
            ans += 1
            return

        if i >= n:
            return

        # Include curent container
        if total - containers[i] >= 0:
            backtrack(i + 1, total - containers[i])

        # Exclude current container
        backtrack(i + 1, total)

    backtrack(0, TOTAL_VOLUME)

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
