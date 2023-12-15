import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    return input().strip().split(",")


def calculate_hash(word):
    res = 0

    for ch in word:
        res += ord(ch)
        res = (res * 17) % 256

    return res


def find_sum_of_hashes(sequence):
    res = 0

    for word in sequence:
        res += calculate_hash(word)

    return res


sequence = parse_input()

# pprint(sequence)
print("Ans: ", find_sum_of_hashes(sequence))
