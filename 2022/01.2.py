import sys
import heapq


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass

heap = []
heapq.heapify(heap)

curr_calories = 0
for line in sys.stdin:
    if not line or line.isspace():
        heapq.heappush(heap, curr_calories)
        if len(heap) > 3:
            heapq.heappop(heap)
        curr_calories = 0
    else:
        curr_calories += int(line.strip())

print("Ans: ", sum(heap))
