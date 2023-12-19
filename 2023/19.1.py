import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


def parse_input():
    workflows = {}
    ratings = []

    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        name, conds_inp = line[:-1].split("{")
        conds_inp = conds_inp.split(",")
        conds_cleaned = []
        for cond in conds_inp:
            cond = cond.split(":")
            if len(cond) == 2:
                conds_cleaned.append((cond[0], cond[1]))
            else:
                conds_cleaned.append((cond[0]))

        workflows[name] = conds_cleaned

    for line in sys.stdin:
        line = line.strip()[1:-1].split(",")
        temp = {}
        for vpoint in line:
            lhs, rhs = vpoint.split("=")
            temp[lhs] = int(rhs)
        ratings.append(temp)

    return workflows, ratings


def evaluate(workflows, key, rating):
    workflow = workflows[key]
    for work in workflow:
        if not isinstance(work, tuple):
            return work
        else:
            # print(work, len(work))
            cond, next_key = work
            ch, op, num = cond[0], cond[1], int(cond[2:])

            if eval(f"rating['{ch}'] {op} {num}"):
                return next_key


def solve(workflows, ratings):
    ans = 0

    for rating in ratings:
        curr = "in"
        while curr not in ("A", "R"):
            curr = evaluate(workflows, curr, rating)
        #     print(curr)

        if curr == "A":
            ans += sum(rating.values())

    return ans


workflows, ratings = parse_input()

# for x in workflows:
#     print(x, workflows[x])
# for x in ratings:
#     print(x)

print("Ans:", solve(workflows, ratings))
