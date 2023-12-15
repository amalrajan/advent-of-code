import sys
from pprint import pprint


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    patterns = []

    for line in sys.stdin:
        pattern, nums = line.strip().split()
        pattern = "?".join([pattern] * 5)
        nums = ",".join([nums] * 5)

        nums = tuple(map(int, nums.strip().split(",")))

        patterns.append((pattern, nums))

    return patterns


def dp(pattern, nums, cache):
    # Base case 1: pattern is empty
    if pattern == "":
        if nums == ():
            return 1
        else:
            return 0

    # Base case 2: nums is empty
    if nums == ():
        # If there are more #, then that would mean we need
        # more nums, but we don't have any nums
        if "#" in pattern:
            return 0
        else:
            return 1

    key = (pattern, nums)

    if key not in cache:
        res = 0

        # Option 1: Treat '?' as a '.'
        # That is, ignore it
        if pattern[0] in ".?":
            res += dp(pattern[1:], nums, cache)

        # Option 2: Treat '?' as a '#'
        # That is, consider it
        if pattern[0] in "#?":
            # Try to put a block of ### of length nums[0]
            if (
                nums[0] <= len(pattern)
                and "." not in pattern[: nums[0]]
                and (nums[0] == len(pattern) or pattern[nums[0]] != "#")
            ):
                # nums[0] + 1 because the next character is pointless
                res += dp(pattern[nums[0] + 1 :], nums[1:], cache)

        cache[key] = res

    return cache[key]


patterns = parse_input()
cache = {}

ans = 0
for pattern, nums in patterns:
    ans += dp(pattern, nums, cache)

print("Ans: ", ans)
