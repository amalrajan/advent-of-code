import heapq
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    grid = []
    for line in sys.stdin:
        grid.append(list(map(int, line.strip())))

    return grid


def solve(grid):
    # heat_loss, x, y, dx, dy, steps
    pq = [(0, 0, 0, 0, 0, 0)]
    visited = set()
    while pq:
        heat_loss, x, y, dx, dy, steps = heapq.heappop(pq)

        if (x, y) == (len(grid) - 1, len(grid[0]) - 1) and steps >= 4:
            return heat_loss

        if (x, y, dx, dy, steps) in visited:
            continue

        visited.add((x, y, dx, dy, steps))

        # If the number of steps < 10 and we're not
        # standing still
        if steps < 10 and (dx, dy) != (0, 0):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                heapq.heappush(pq, (heat_loss + grid[nx][ny], nx, ny, dx, dy, steps + 1))

        # Only turn if we have moved 4 steps or
        # we are at the starting (dx, dy)
        if steps >= 4 or (dx, dy) == (0, 0):
            for ndx, ndy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                if (ndx, ndy) not in ((dx, dy), (-dx, -dy)):
                    nx, ny = x + ndx, y + ndy
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                        heapq.heappush(pq, (heat_loss + grid[nx][ny], nx, ny, ndx, ndy, 1))


grid = parse_input()
heat_loss = solve(grid)
print('Heat loss: ', heat_loss)
