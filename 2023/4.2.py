import collections
import sys


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    # sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def update_match_count(winning, yours):
    cnt = 0
    hset = set(winning)
    for card in yours:
        if card in hset:
            cnt += 1

    return cnt


match_count = collections.defaultdict(int)
stack = []

for line in sys.stdin:
    card, card_numbers = line.strip().split(":")
    card_id = card.split()[1]
    winning, yours = card_numbers.split("|")
    winning = winning.strip().split()
    yours = yours.strip().split()

    if card_id not in match_count:
        cards_won = update_match_count(winning, yours)
        match_count[int(card_id)] = cards_won
        stack.append(int(card_id))


ans = len(stack)
while stack:
    print(len(stack))
    card_id = stack.pop()
    cards_matched = match_count[card_id]
    stack.extend(list(range(card_id + 1, card_id + cards_matched + 1)))
    ans += cards_matched

# for x in match_count:
#     print(x, match_count[x])
print("Ans: ", ans)
