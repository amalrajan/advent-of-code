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
        vowel_count = 0
        consecutive_repeating_char = False

        present_in_avoid_list = False
        avoid_list = set(["ab", "cd", "pq", "xy"])

        for i in range(n):
            if word[i] in vowels:
                vowel_count += 1

            if i + 1 < n:
                if consecutive_repeating_char == False and word[i] == word[i + 1]:
                    consecutive_repeating_char = True
                if word[i : i + 2] in avoid_list:
                    present_in_avoid_list = True
                    break
        if (
            vowel_count >= 3
            and consecutive_repeating_char == True
            and present_in_avoid_list == False
        ):
            ans += 1

    return ans


if __name__ == "__main__":
    words = parse_input()
    print(solve(words))
