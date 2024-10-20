import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    words = []
    for line in sys.stdin:
        words.append(line.strip())

    return words


def solve(words):
    ans = 0
    vowels = set("aeiou")

    for word in words:
        n = len(word)
        position = {}

        condition_1 = False
        condition_2 = False

        for i in range(n):
            if condition_1 == False and i + 1 < n:
                pair = word[i : i + 2]
                if pair not in position:
                    position[pair] = i
                else:
                    previous_pos = position[pair]
                    if previous_pos + 1 < i:
                        condition_1 = True

            if condition_2 == False and i + 2 < n:
                if word[i] == word[i + 2]:
                    condition_2 = True

            if condition_1 and condition_2:
                break

        if condition_1 and condition_2:
            ans += 1

    return ans


if __name__ == "__main__":
    words = parse_input()
    print(solve(words))
