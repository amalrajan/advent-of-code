import sys
import collections
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    # sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


directions = input().strip()
graph = collections.defaultdict(tuple)
nodes = []

for line in sys.stdin:
    if line.isspace():
        continue
    source, remaining = line.split("=")
    left, right = remaining.strip()[1:-1].split(",")
    source = source.strip()
    left = left.strip()
    right = right.strip()

    graph[source] = (left, right)

    # Check if this is a starting node
    if source[-1] == "A":
        nodes.append(source)


dirx = 0
directions_length = len(directions)
directions_numeric = [1 if x == "R" else 0 for x in directions]


steps = 0
while True:
    # Brute force, but only break when all
    # nodes are at target
    z_in_node = True
    for node in nodes:
        if node[-1] != "Z":
            z_in_node = False
            break
    if z_in_node:
        break

    nodes_length = len(nodes)
    print(nodes_length, steps)

    for i in range(nodes_length):
        nodes[i] = graph[nodes[i]][directions_numeric[dirx]]
    steps += 1
    # print(nodes)

    dirx = (dirx + 1) % directions_length

# print(nodes)
# for x in graph:
#     print(x, graph[x])

print(steps)
