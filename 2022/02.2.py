import sys


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass

score_map = {"R": 1, "P": 2, "S": 3}
opponent_map = {"A": "R", "B": "P", "C": "S"}
player_map = {"X": "R", "Y": "P", "Z": "S"}
winning_order = ["R", "S", "P"]
ans = 0

for line in sys.stdin:
    line = line.strip().split()
    opponent = opponent_map[line[0]]
    player = player_map[line[1]]

    opponent_index = winning_order.index(opponent)
    player_index = winning_order.index(player)

    # Additional code for part 2
    if player == "P":
        player = opponent
    elif player == "R":
        player = winning_order[(opponent_index + 1) % 3]
    else:
        player = winning_order[(opponent_index - 1) % 3]

    ans += score_map[player]

    # Opponent winning case
    if winning_order[(opponent_index + 1) % 3] == player:
        continue
    # Draw case
    elif opponent == player:
        ans += 3
    # Player winning case
    else:
        ans += 6

print("Ans: ", ans)
