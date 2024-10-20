import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []

    for line in sys.stdin:
        lhs, rhs = line.strip().split("->")
        lhs = lhs.strip().split()
        rhs = rhs.strip()

        for i in range(len(lhs)):
            if lhs[i].isdigit():
                lhs[i] = int(lhs[i])

        inputs.append([lhs, rhs])

    return inputs


def solve(inputs):
    vals = {}

    while inputs != []:
        # Replace variables with values
        for i in range(len(inputs)):
            for j in range(len(inputs[i][0])):
                if inputs[i][0][j] in ["NOT", "LSHIFT", "RSHIFT", "AND", "OR"]:
                    continue

                # Replace variable with value if present
                if inputs[i][0][j] in vals:
                    inputs[i][0][j] = vals[inputs[i][0][j]]

        # Perform operations
        processed_indices = set()
        for i in range(len(inputs)):
            if (
                (
                    "OR" in inputs[i][0]
                    or "AND" in inputs[i][0]
                    or "LSHIFT" in inputs[i][0]
                    or "RSHIFT" in inputs[i][0]
                )
                and isinstance(inputs[i][0][0], int)
                and isinstance(inputs[i][0][2], int)
            ):
                if "OR" in inputs[i][0]:
                    vals[inputs[i][1]] = inputs[i][0][0] | inputs[i][0][2]
                elif "AND" in inputs[i][0]:
                    vals[inputs[i][1]] = inputs[i][0][0] & inputs[i][0][2]
                elif "LSHIFT" in inputs[i][0]:
                    vals[inputs[i][1]] = inputs[i][0][0] << inputs[i][0][2]
                elif "RSHIFT" in inputs[i][0]:
                    vals[inputs[i][1]] = inputs[i][0][0] >> inputs[i][0][2]

                vals[inputs[i][1]] %= 65536
                processed_indices.add(i)

            elif "NOT" in inputs[i][0] and isinstance(inputs[i][0][1], int):
                vals[inputs[i][1]] = ~inputs[i][0][1]
                vals[inputs[i][1]] %= 65536
                processed_indices.add(i)

        # Resolve direct assignments
        for i in range(len(inputs)):
            if isinstance(inputs[i][0][0], int) and len(inputs[i][0]) == 1:
                vals[inputs[i][1]] = inputs[i][0][0]

        # Remove all direct assignments
        new_inputs = []
        for idx, item in enumerate(inputs):
            if (len(item[0]) == 1 and isinstance(item[0][0], int)) or (
                idx in processed_indices
            ):
                continue
            else:
                new_inputs.append(item)
        inputs = new_inputs

    return vals["a"]


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
