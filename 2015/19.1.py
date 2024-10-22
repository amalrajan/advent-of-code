import collections
import sys

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


def solve(transformations, molecule):
    replacments = set()
    max_key_len = len(max(transformations.keys(), key=len))

    for i in range(len(molecule)):
        for j in range(max_key_len):
            key = molecule[i : i + j + 1]
            for repl_text in transformations[key]:
                new_molecule = molecule[:i] + repl_text + molecule[i + j + 1 :]
                replacments.add(new_molecule)

    return len(replacments)


if __name__ == "__main__":
    transformations, molecule = parse_input()
    print(solve(transformations, molecule))
