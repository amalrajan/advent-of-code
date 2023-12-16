import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def find_start_of_packet(datastream):
    for i in range(len(datastream) - 14):
        if len(set(datastream[i : i + 14])) == 14:
            return i + 14


datastream = input().strip()
print("Ans:", find_start_of_packet(datastream))
