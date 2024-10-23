import math
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        inputs.append(int(line.strip()))

    return inputs


def solve(weights):
    CONTAINER_COUNT = 3

    total_weight = sum(weights)
    if total_weight % CONTAINER_COUNT != 0:
        return

    target_weight = total_weight // CONTAINER_COUNT
    min_qe = math.inf
    min_container1_length = math.inf

    visited = set()

    def backtrack(
        idx,
        container1,
        container2,
        container3,
        container1_length,
        container2_length,
        container3_length,
        quantum_entanglement,
    ):
        nonlocal min_qe, min_container1_length

        if container1_length > min_container1_length:
            return

        if idx >= len(weights) and (
            container1 == container2 == container3 == target_weight
        ):
            if container1_length < min_container1_length:
                min_container1_length = container1_length
                min_qe = quantum_entanglement
            elif container1_length == min_container1_length:
                min_qe = min(min_qe, quantum_entanglement)

            return

        if idx >= len(weights):
            return

        item = weights[idx]

        # Put the item in container 1
        if container1 + item <= target_weight:
            key = (
                container1 + item,
                container2,
                container3,
                container1_length + 1,
                container2_length,
                container3_length,
            )
            if key not in visited:
                visited.add(key)
                backtrack(
                    idx + 1,
                    container1 + item,
                    container2,
                    container3,
                    container1_length + 1,
                    container2_length,
                    container3_length,
                    quantum_entanglement * item,
                )

        # Put the item in container 2
        if container2 + item <= target_weight:
            key = (
                container1,
                container2 + item,
                container3,
                container1_length,
                container2_length + 1,
                container3_length,
            )
            if key not in visited:
                visited.add(key)
                backtrack(
                    idx + 1,
                    container1,
                    container2 + item,
                    container3,
                    container1_length,
                    container2_length + 1,
                    container3_length,
                    quantum_entanglement,
                )

        # Put the item in container 3
        if container3 + item <= target_weight:
            key = (
                container1,
                container2,
                container3 + item,
                container1_length,
                container2_length,
                container3_length + 1,
            )
            if key not in visited:
                visited.add(key)
                backtrack(
                    idx + 1,
                    container1,
                    container2,
                    container3 + item,
                    container1_length,
                    container2_length,
                    container3_length + 1,
                    quantum_entanglement,
                )

    backtrack(0, 0, 0, 0, 0, 0, 0, 1)

    return min_qe


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
