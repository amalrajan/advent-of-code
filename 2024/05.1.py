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


def solve(page_order, page_updates):
    # Topsort won't work here because the graph can contain cycles.
    # Perhaps a modified topsort may worr? Not sure.
    ans = 0

    for page_update in page_updates:
        if is_page_update_valid(page_update, page_order):
            ans += page_update[len(page_update) // 2]

    return ans


if __name__ == "__main__":
    page_order, page_updates = parse_input()
    print(solve(page_order, page_updates))
