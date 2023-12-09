import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    # sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


times = list(map(int, input().strip().split(":")[1].split()))
dists = list(map(int, input().strip().split(":")[1].split()))

# Part 2 modification
times = [int("".join(map(str, times)))]
dists = [int("".join(map(str, dists)))]

print(times)
print(dists)


ans = 1
for i in range(len(times)):
    break
    time = times[i]
    dist = dists[i]

    cnt = 0
    for a in range(time + 1):
        print(a * 100 / time + 1)
        dist_covered = a * (time - a)
        if dist_covered > dist:
            cnt += 1

    ans *= cnt

print(ans)
