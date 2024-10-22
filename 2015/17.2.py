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

    minimum_container_count = n
    number_of_minimum_ways = 0

    def backtrack(i, total, container_count):
        nonlocal minimum_container_count, number_of_minimum_ways

        if total == 0:
            if container_count < minimum_container_count:
                minimum_container_count = container_count
                number_of_minimum_ways = 1
            elif container_count == minimum_container_count:
                number_of_minimum_ways += 1
            return

        if i >= n:
            return

        # Include curent container
        if total - containers[i] >= 0:
            backtrack(i + 1, total - containers[i], container_count + 1)

        # Exclude current container
        backtrack(i + 1, total, container_count)

    backtrack(0, TOTAL_VOLUME, 0)

    return number_of_minimum_ways


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
