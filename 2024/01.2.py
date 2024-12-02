import collections
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    list1 = []
    list2 = []
    for line in sys.stdin:
        num1, num2 = list(map(int, line.strip().split()))
        list1.append(num1)
        list2.append(num2)

    return list1, list2


def solve(inputs):
    list1, list2 = inputs
    list2_counter = collections.Counter(list2)

    ans = 0
    for num in list1:
        ans += num * list2_counter[num]

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
