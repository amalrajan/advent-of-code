import sys
import collections

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    return input().strip().split(",")


def calculate_hash(word):
    res = 0

    for ch in word:
        res += ord(ch)
        res = (res * 17) % 256

    return res % 256


def simulate_boxes(sequence):
    boxes = [[] for _ in range(256)]

    for word in sequence:
        label = None
        focal_length = None
        if "=" in word:
            label, focal_length = word.split("=")
            focal_length = int(focal_length)
        else:
            label = word[:-1]

        hash_val = calculate_hash(label)
        box_content = (label, focal_length)

        if "=" in word:
            idx = -1
            for i in range(len(boxes[hash_val])):
                if boxes[hash_val][i][0] == label:
                    idx = i
                    break

            if idx == -1:
                boxes[hash_val].append(box_content)
            else:
                boxes[hash_val][idx] = box_content
        else:
            idx = -1
            for i in range(len(boxes[hash_val])):
                if boxes[hash_val][i][0] == label:
                    idx = i
                    break
            if idx != -1:
                del boxes[hash_val][idx]

    return boxes


def calculate_focusing_power(boxes):
    res = 0
    box_no = 1
    for box in boxes:
        if box:
            slot = 1
            for item in box:
                res += box_no * slot * item[1]
                slot += 1
        box_no += 1

    return res


sequence = parse_input()
boxes = simulate_boxes(sequence)

print("Ans: ", calculate_focusing_power(boxes))
