import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass

max_calories = 0
curr_calories = 0

for line in sys.stdin:
    if line.isspace() or not line:
        max_calories = max(max_calories, curr_calories)
        curr_calories = 0
    else:
        curr_calories += int(line.strip())

max_calories = max(max_calories, curr_calories)

print("Ans:", max_calories)
