import sys
import copy

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


class TreeNode:
    def __init__(self, val=None) -> None:
        self.val = None
        self.size = None
        self.children = {}


def parse_input():
    history = []

    for line in sys.stdin:
        history.append(line.strip().split())

    return history


def level_order(root):
    queue = [root]
    print(root.children["a"].val)

    while queue:
        for node in queue:
            if node:
                print(node.val, end=" ")
        print()

        temp = []
        for node in queue:
            print(node)
            if node and node.children:
                for child in node.children:
                    queue.append(child)

        queue = copy.deepcopy(temp)


def create_tree(history):
    dummy = TreeNode(None)
    curr = dummy

    ptr = 0
    while ptr < len(history):
        entry = history[ptr]
        if entry[0] == "$":
            # Command
            if entry[1] == "cd":
                if entry[2] not in curr.children:
                    curr.children[entry[2]] = TreeNode(entry[2])
                curr = curr.children[entry[2]]
            elif entry[1] == "ls":
                ptr += 1
                while ptr < len(history) and history[ptr][0] != "$":
                    entry = history[ptr]
                    print(entry)
                    if entry[1] not in curr.children:
                        curr.children[entry[1]] = TreeNode(entry[1])
                        if entry[0].isdigit():
                            curr.children[entry[1]].size = int(entry[0])
                    ptr += 1
        ptr += 1

    return dummy.children["/"]


history = parse_input()

# for hist in history:
#     print(hist)
root = create_tree(history)
level_order(root)
