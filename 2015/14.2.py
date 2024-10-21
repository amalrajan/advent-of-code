import collections
import heapq
import sys
from dataclasses import dataclass
from enum import Enum
from pprint import pprint

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


class DeerStateEnum:
    RESTING = 0
    FLYING = 1


@dataclass
class Deer:
    speed: int
    fly_duration: int
    rest_duration: int


@dataclass
class DeerState:
    state: DeerStateEnum
    fly_duration_remaining: int
    rest_duration_remaining: int
    distance_traveled: int
    score: int


def parse_input():
    inputs = {}
    for line in sys.stdin:
        if not line:
            continue
        line = line.strip().split()

        name = line[0]
        speed = int(line[3])
        fly_duration = int(line[6])
        rest_duration = int(line[13])

        inputs[name] = Deer(
            speed,
            fly_duration,
            rest_duration,
        )

    return inputs


def solve(deer_map):
    state_map = {}
    for name, deer in deer_map.items():
        state_map[name] = DeerState(
            DeerStateEnum.FLYING,
            deer.fly_duration,
            deer.rest_duration,
            0,
            0,
        )

    current_time = 1
    time_limit = 2503

    while current_time <= time_limit:
        leading_deers = []
        leading_deer_distance = 0

        for deer in state_map:
            deer_state = state_map[deer]

            # If out of fly duration, reset it
            if (
                deer_state.state == DeerStateEnum.FLYING
                and deer_state.fly_duration_remaining == 0
            ):
                deer_state.state = DeerStateEnum.RESTING
                deer_state.fly_duration_remaining = deer_map[deer].fly_duration

            # If out of rest duration, reset it
            if (
                deer_state.state == DeerStateEnum.RESTING
                and deer_state.rest_duration_remaining == 0
            ):
                deer_state.state = DeerStateEnum.FLYING
                deer_state.rest_duration_remaining = deer_map[deer].rest_duration

            if deer_state.state == DeerStateEnum.FLYING:
                deer_state.fly_duration_remaining -= 1
                deer_state.distance_traveled += deer_map[deer].speed
            elif deer_state.state == DeerStateEnum.RESTING:
                deer_state.rest_duration_remaining -= 1

            if deer_state.distance_traveled > leading_deer_distance:
                leading_deer_distance = deer_state.distance_traveled
                leading_deers = [deer]
            elif deer_state.distance_traveled == leading_deer_distance:
                leading_deers.append(deer)

        for deer in leading_deers:
            state_map[deer].score += 1

        current_time += 1

    return max(state_map.values(), key=lambda x: x.score).score


if __name__ == "__main__":
    inputs = parse_input()
    print(solve(inputs))
