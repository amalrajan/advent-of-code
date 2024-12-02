import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(list(map(int, line.strip().split())))

    return inputs


def is_safe_by_removing_one(nums):
    def left_to_right():
        prev = nums[0] - 1
        flag = False
        for num in nums:
            diff = num - prev
            if not 1 <= diff <= 3:
                if flag:
                    return False
                flag = True
            else:
                prev = num

        return True

    def right_to_left():
        prev = nums[-1] + 1
        flag = False
        for num in nums[::-1]:
            diff = num - prev
            if not -3 <= diff <= -1:
                if flag:
                    return False
                flag = True
            else:
                prev = num

        return True

    return left_to_right() or right_to_left()


def is_safe(nums):
    increasing = False
    decreasing = False

    is_valid = True

    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]

        if diff >= 0:
            increasing = True
        else:
            decreasing = True

        if increasing and decreasing:
            is_valid = False
            break

        if not 1 <= abs(diff) <= 3:
            is_valid = False
            break

    return is_valid


def solve(reports):
    ans = 0

    for report in reports:
        if is_safe(report):
            ans += 1
        else:
            if is_safe_by_removing_one(report) or is_safe_by_removing_one(report[::-1]):
                ans += 1

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
