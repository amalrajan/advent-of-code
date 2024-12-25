import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    return list(map(int, input().strip().split()))


def solve(stones):
    k = 25
    for _ in range(k):
        new_stones = []

        for stone in stones:
            if stone == 0:
                new_stones.append(1)
            elif not len(str(stone)) & 1:
                stone = str(stone)
                midpoint = len(stone) // 2
                new_stones.extend([int(stone[:midpoint]), int(stone[midpoint:])])
            else:
                new_stones.append(stone * 2024)

        stones = new_stones

    return len(stones)


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
