import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []

    for line in sys.stdin:
        line = line.strip()
        first_colon = line.find(":")
        belongings = line[first_colon + 1 :].split(",")
        belongings = [item.strip().split(":") for item in belongings]

        items_map = {}
        for k, v in belongings:
            items_map[k.strip()] = int(v.strip())

        inputs.append(items_map)

    return inputs


def solve(aunts):
    requirements = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    for idx, sue in enumerate(aunts):
        is_correct_sue = True

        for item in sue:
            if item in requirements and requirements[item] != sue[item]:
                is_correct_sue = False
                break

        if is_correct_sue:
            return idx + 1


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
