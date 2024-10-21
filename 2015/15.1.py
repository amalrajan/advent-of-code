import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    cookies = []

    for line in sys.stdin:
        line = line.strip().split(":")
        line[1] = [int(x.split()[1]) for x in line[1].strip().split(",")]
        cookies.append(line)

    return cookies


def solve(cookies):
    MAX_TEASPOONS = 100
    ans = 0

    def calculate_score(arr):
        total_score = 1

        for i in range(len(cookies[0][1]) - 1):
            # Calculate the score for each ingredient
            score = 0

            for j in range(len(arr)):
                arr_val = arr[j]
                ingredient_val = cookies[j][1][i]
                score += arr_val * ingredient_val

            if score < 0:
                return 0
            total_score *= score

        return total_score

    def backtrack(arr, total):
        nonlocal ans

        if total < 0:
            return

        if len(arr) > len(cookies):
            return

        if len(arr) == len(cookies) and total == 0:
            ans = max(ans, calculate_score(arr))
            return

        for i in range(1, total + 1):
            if len(arr) < len(cookies):
                backtrack(arr + [i], total - i)

    backtrack([], MAX_TEASPOONS)

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
