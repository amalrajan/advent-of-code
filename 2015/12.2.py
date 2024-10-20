import json
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = json.loads(input().strip())
    return inputs


def solve(documents):
    total = 0

    def summation(item, add_flag):
        nonlocal total

        if isinstance(item, int):
            if add_flag:
                total += item
            return

        elif isinstance(item, str):
            return

        elif isinstance(item, dict):
            if "red" in item.values():
                add_flag = False
            for node in item:
                summation(item[node], add_flag)

        elif isinstance(item, list):
            for node in item:
                summation(node, add_flag)

    summation(documents, True)
    return total


if __name__ == "__main__":
    documents = parse_input()
    print(solve(documents))
