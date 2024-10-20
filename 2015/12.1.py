import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(line.strip())

    return inputs


def sum_numbers(document):
    summation = 0

    i = 0
    n = len(document)

    while i < n:
        j = i + 1

        if document[i].isdigit():
            while j < n and document[j].isdigit():
                j += 1
            number = int(document[i:j])

            if i - 1 >= 0 and document[i - 1] == "-":
                number *= -1

            summation += number

        i = j

    return summation


def solve(documents):
    ans = 0
    for document in documents:
        ans += sum_numbers(document)

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
