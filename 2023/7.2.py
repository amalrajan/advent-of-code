import sys
import collections
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def get_card_strengths():
    # Calculate strength
    strength = {}
    unique_cards = [
        "A",
        "K",
        "Q",
        "J",
        "T",
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
        "J",
    ]
    for ch in range(len(unique_cards)):
        strength[unique_cards[ch]] = len(unique_cards) - ch

    return strength


def get_char_freq(card):
    # Get character frequency of a card
    freq = collections.defaultdict(int)

    for ch in card:
        freq[ch] += 1

    return list(freq.values())


def absorb_joker(card, freq):
    j_count = card.count("J")
    idx = freq.index(j_count)

    if len(freq) > 1:
        del freq[idx]

    freq[-1] += j_count

    return freq


def categorize_cards(cards):
    # 7 categories
    # {
    #     "five-of-a-kind": [],
    #     "four-of-a-kind": [],
    #     "full-house": [],
    #     "three-of-a-kind": [],
    #     "two-pair": [],
    #     "one-pair": [],
    #     "high-card": [],
    # }
    card_category = [[] for _ in range(7)]

    for card in cards:
        freq = get_char_freq(card)
        freq.sort()

        if "J" in card:
            freq = absorb_joker(card, freq)

        if len(freq) == 1:
            card_category[0].append(card)
        elif freq == [1, 4]:
            card_category[1].append(card)
        elif freq == [2, 3]:
            card_category[2].append(card)
        elif freq == [1, 1, 3]:
            card_category[3].append(card)
        elif freq == [1, 2, 2]:
            card_category[4].append(card)
        elif freq == [1, 1, 1, 2]:
            card_category[5].append(card)
        elif freq == [1, 1, 1, 1, 1]:
            card_category[6].append(card)

    # for x in card_category:
    #     print(x)

    return card_category


def is_first_card_smaller(card1, card2):
    # Check if card1 is smaller
    for i in range(len(card1)):
        if strength[card1[i]] < strength[card2[i]]:
            return True
        elif strength[card1[i]] > strength[card2[i]]:
            return False

    return False


def selection_sort(cards):
    global rank, score

    if not cards:
        return

    for i in range(len(cards) - 1):
        mini = i
        for j in range(i + 1, len(cards)):
            # If cards[j] < cards[mini], swap
            if is_first_card_smaller(cards[j], cards[mini]) == True:
                mini = j

        if mini != i:
            cards[i], cards[mini] = cards[mini], cards[i]

    for i in range(len(cards)):
        # print(cards[i], bids[cards[i]], " * ", rank)
        score += bids[cards[i]] * rank
        rank += 1


bids = {}
for line in sys.stdin:
    card, bid = line.strip().split()
    bids[card] = int(bid)

cards = bids.keys()
strength = get_card_strengths()
card_category = categorize_cards(cards)

rank = 1
score = 0

for cards in card_category[::-1]:
    selection_sort(cards)

# for x in card_category[::-1]:
#     print(x)
# for x in bids:
#     print(x, bids[x])
print(score)
