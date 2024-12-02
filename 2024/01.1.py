import heapq
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
    heap1, heap2 = inputs
    heapq.heapify(heap1)
    heapq.heapify(heap2)

    ans = 0
    while heap1:
        num1 = heapq.heappop(heap1)
        num2 = heapq.heappop(heap2)

        ans += abs(num1 - num2)

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
