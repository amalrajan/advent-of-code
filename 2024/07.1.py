import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        res, nums = line.strip().split(":")
        inputs.append([int(res), [int(num) for num in nums.split()]])

    return inputs


def is_valid_equation(nums, expected_result):
    n = len(nums)
    cache = {}

    def dp(i, total):
        if i == n:
            return total == expected_result

        if total > expected_result:
            return False

        key = (i, total)

        if key not in cache:
            add = dp(i + 1, nums[i] + total)
            multiply = dp(i + 1, nums[i] * total)
            cache[key] = add or multiply

        return cache[key]

    return dp(1, nums[0])


def solve(equations):
    ans = 0
    for expected_result, nums in equations:
        if is_valid_equation(nums, expected_result):
            ans += expected_result

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
