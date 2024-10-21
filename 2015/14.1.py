import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def parse_input():
    inputs = []
    for line in sys.stdin:
        if not line:
            continue
        line = line.strip().split()

        name = line[0]
        speed = int(line[3])
        fly_duration = int(line[6])
        rest_duration = int(line[13])

        inputs.append([name, speed, fly_duration, rest_duration])

    return inputs


def calculate_distance_traveled(deer, time_limit=1000):
    distance = 0
    _, speed, fly_duration, rest_duration = deer

    full_cycle_dist = speed * fly_duration
    full_cycle_time = fly_duration + rest_duration

    full_cycle_count = time_limit // full_cycle_time
    distance += full_cycle_count * full_cycle_dist

    remaining_time = time_limit - (full_cycle_count * full_cycle_time)

    if remaining_time > 0:
        distance += min(remaining_time, fly_duration) * speed

    return distance


def solve(deer_list):
    ans = 0
    TIME_LIMIT = 2503
    for deer in deer_list:
        ans = max(ans, calculate_distance_traveled(deer, TIME_LIMIT))

    return ans


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
