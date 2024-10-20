import collections
import math
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        locations, trip_cost = line.split("=")
        from_location, to_location = locations.split("to")
        inputs.append(
            [
                from_location.strip(),
                to_location.strip(),
                int(trip_cost.strip()),
            ]
        )

    return inputs


def hamiltonian_path(graph, start):
    res = []

    def backtrack(curr, visited, dist):
        if len(visited) == len(graph):
            res.append(dist)
            return

        for nei, nei_dist in graph[curr]:
            if nei not in visited:
                backtrack(nei, visited | {nei}, dist + nei_dist)

    backtrack(start, {start}, 0)
    return res


def solve(inputs):
    graph = collections.defaultdict(list)

    for source, dest, dist in inputs:
        graph[source].append([dest, dist])
        graph[dest].append([source, dist])

    ans = 0
    for start in graph:
        ans = max(ans, max(hamiltonian_path(graph, start)))

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
