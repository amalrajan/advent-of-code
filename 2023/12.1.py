import collections
import sys
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    inp = []
    for line in sys.stdin:
        pattern, nums = line.strip().split()
        pattern = list(pattern)
        nums = list(map(int, nums.split(",")))
        inp.append((pattern, nums))

    return inp


def generate_blocks(pattern_length, nums):
    blocks = []
    for num in nums:
        blocks.append("#" * num)

    for _ in range(pattern_length - sum([len(block) for block in blocks])):
        blocks.append(".")

    return blocks


def permute(blocks):
    res = []
    n = len(blocks)
    blocks.sort()

    # Note, this 'temp' is different from the global 'blocks'
    def permuteHelper(temp, curr):
        if len(curr) == n:
            res.append(curr)
            return

        for i in range(len(temp)):
            if i > 0 and temp[i] == temp[i - 1]:
                continue
            permuteHelper(temp[:i] + temp[i + 1 :], curr + [temp[i]])

    permuteHelper(blocks, [])

    return res


def are_there_contiguous_hashes(comb):
    for i in range(1, len(comb)):
        if comb[i][0] == "#" and comb[i - 1][0] == "#":
            return True

    return False


def remove_blocks_together(combinations):
    clean_combinations = []

    for comb in combinations:
        if not are_there_contiguous_hashes(comb):
            clean_combinations.append(comb)

    return clean_combinations


def remove_non_matching_indices(pattern, combinations):
    clean_combinations = []
    pattern = "".join(pattern)
    # print(pattern)

    for comb in combinations:
        is_valid = True
        for i in range(len(pattern)):
            if pattern[i] == "#" and comb[i] != "#":
                is_valid = False
                break
            elif pattern[i] == "." and comb[i] != ".":
                is_valid = False
                break
        if is_valid:
            clean_combinations.append(comb)

    return clean_combinations


def convert_combinations_to_strings(combinations):
    single_entity_combinations = []

    for comb in combinations:
        single_entity_combinations.append("".join(comb))

    return single_entity_combinations


def remove_contiguos_blocks(combinations, nums):
    clean_combinations = []
    # nums.sort()
    # print(nums)

    for comb in combinations:
        comb_lengths = []
        comb_split = comb.split(".")

        for comb_split_item in comb_split:
            if comb_split_item and comb_split_item[0] == "#":
                comb_lengths.append(len(comb_split_item))

        # comb_lengths.sort()

        if nums == comb_lengths:
            # print(comb, comb_lengths)
            clean_combinations.append(comb)

    return clean_combinations


def validate_combinations(pattern, combinations, nums):
    combinations = remove_blocks_together(combinations)
    combinations = convert_combinations_to_strings(combinations)
    # print(combinations)
    combinations = remove_non_matching_indices(pattern, combinations)
    # print()
    # print(combinations)
    combinations = remove_contiguos_blocks(combinations, nums)

    return combinations


def generate_combinations(pattern, nums):
    plen = len(pattern)
    blocks = generate_blocks(plen, nums)
    combinations = permute(blocks)
    combinations = validate_combinations(pattern, combinations, nums)

    return combinations


inp = parse_input()
# for x, y in inp:
#     print("".join(x), y)

ans = 0
for pattern, nums in inp:
    combs = generate_combinations(pattern, nums)
    # print("".join(pattern), len(combs))
    ans += len(combs)
    # pprint(combs)

print("Ans: ", ans)
