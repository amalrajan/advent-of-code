import collections
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        line = line.strip().split()

        person1 = line[0]
        person2 = line[-1][:-1]
        score = int(line[3])

        if line[2] == "lose":
            score *= -1

        inputs.append([score, person1, person2])

    return inputs


def get_seating_score(edges):
    score_map = collections.defaultdict(int)
    persons = set()

    for score, person1, person2 in edges:
        key = tuple(sorted([person1, person2]))
        score_map[key] += score
        persons.update([person1, person2])

    return score_map, list(persons)


def calculate_score(seating, score_map):
    n = len(seating)
    score = 0

    for i in range(1, n):
        key = tuple(sorted([seating[i - 1], seating[i]]))
        score += score_map[key]

    key = tuple(sorted([seating[0], seating[n - 1]]))
    score += score_map[key]

    return score


def seat_yourself(score_map, persons):
    you = "You"

    for person in persons:
        key = tuple(sorted([you, person]))
        score_map[key] = 0

    persons.append(you)

    return score_map, persons


def solve(edges):
    score_map, persons = seat_yourself(*get_seating_score(edges))
    ans = 0

    def backtrack(remaining, seating):
        nonlocal ans

        if remaining == []:
            ans = max(ans, calculate_score(seating, score_map))
            return

        for i in range(len(remaining)):
            backtrack(
                remaining[:i] + remaining[i + 1 :],
                seating + [remaining[i]],
            )

    backtrack(persons, [])

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
