import collections
import math
import sys
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        line = line.strip()
        inputs.append(line)

    transformations = collections.defaultdict(list)
    molecule = inputs[-1].strip()

    for line in inputs[:-1]:
        if not line:
            continue
        line = line.split("=>")
        transformations[line[0].strip()].append(line[1].strip())

    return transformations, molecule


def solve(transformations, target_molecule):
    rev_transformations = collections.defaultdict(list)

    for key in transformations:
        for item in transformations[key]:
            rev_transformations[item].append(key)

    max_key_len = len(max(rev_transformations.keys(), key=len))

    ans = math.inf
    visited = set()

    queue = collections.deque([(target_molecule, 0)])

    pprint(rev_transformations)
    rev_transformations_keys = list(rev_transformations.keys())
    rev_transformations_keys.sort(key=len, reverse=True)
    print(rev_transformations_keys)

    prev_length = len(target_molecule)

    while queue:
        molecule, steps = queue.popleft()
        visited.add(molecule)
        if molecule == "e":
            ans = steps
            break

        if len(molecule) < prev_length:
            prev_length = len(molecule)
            print(molecule, steps)

        for key in rev_transformations_keys:
            k = len(key)
            for i in range(len(molecule)):
                if molecule[i : i + k] == key:
                    for repl in rev_transformations[key]:
                        new_molecule = molecule[:i] + repl + molecule[i + k :]
                        if new_molecule not in visited:
                            if len(new_molecule) > 1 and new_molecule.count("e") > 0:
                                continue
                            visited.add(new_molecule)
                            queue.append((new_molecule, steps + 1))

    return ans


if __name__ == "__main__":
    transformations, molecule = parse_input()
    print(solve(transformations, molecule))
