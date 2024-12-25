import sys
from functools import lru_cache

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass

cache = {}


def parse_input():
    return list(map(int, input().strip().split()))


def solve(stones):
    k = 75

    @lru_cache(maxsize=None)
    def dp(stone, blinks):
        if blinks == k:
            return 1

        if stone == 0:
            return dp(1, blinks + 1)

        stone = str(stone)
        mid = len(stone) // 2

        if not len(stone) & 1:
            return dp(int(stone[:mid]), blinks + 1) + dp(int(stone[mid:]), blinks + 1)

        return dp(int(stone) * 2024, blinks + 1)

    return sum(dp(stone, 0) for stone in stones)


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
