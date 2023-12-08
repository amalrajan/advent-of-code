import sys


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def get_score(winning, yours):
    hset = set(yours)
    cnt = 0

    for card in winning:
        if card in yours:
            cnt += 1

    return int(2 ** (cnt - 1))


ans = 0

for line in sys.stdin:
    winning, yours = line.strip().split(":")[1].split("|")
    winning = winning.strip().split()
    yours = yours.strip().split()

    ans += get_score(winning, yours)

print(ans)
