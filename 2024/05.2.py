import itertools
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    page_order = []
    page_updates = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        first, second = line.split("|")
        page_order.append([int(first), int(second)])

    for line in sys.stdin:
        page_update = line.strip().split(",")
        page_updates.append([int(num) for num in page_update])

    return page_order, page_updates


def is_page_update_valid(page_update, page_order):
    seen = set()

    for num in page_update:
        for source, dest in page_order:
            if source == num and dest in seen:
                return False
        seen.add(num)

    return True


def make_page_update_valid(page_update, page_order):
    # Bubble sort it to make it valid
    for i in range(len(page_update)):
        swapped = False
        for j in range(len(page_update) - i - 1):
            for source, dest in page_order:
                if page_update[j] == dest and page_update[j + 1] == source:
                    swapped = True
                    page_update[j], page_update[j + 1] = (
                        page_update[j + 1],
                        page_update[j],
                    )

        if not swapped:
            break

    return page_update


def solve(page_order, page_updates):
    ans = 0

    for page_update in page_updates:
        if not is_page_update_valid(page_update, page_order):
            page_update = make_page_update_valid(page_update, page_order)
            ans += page_update[len(page_update) // 2]

    return ans


if __name__ == "__main__":
    page_order, page_updates = parse_input()
    print(solve(page_order, page_updates))
