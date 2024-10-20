import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def is_password_valid(password):
    n = len(password)
    req = [False, False]
    pairs_found = []

    disallowed_characters = [ord(x) - ord("a") for x in "iol"]

    for i in range(n):
        if i + 2 < n and password[i] == password[i + 1] - 1 == password[i + 2] - 2:
            req[0] = True
        if len(pairs_found) < 2 and i + 1 < n and password[i] == password[i + 1]:
            if not pairs_found or (pairs_found and i > pairs_found[-1]):
                pairs_found.append(i + 1)

        if password[i] in disallowed_characters:
            return False

        if len(pairs_found) == 2:
            req[1] = True

    if req == [True, True]:
        return True
    else:
        return False


def convert_password_to_num_array(password):
    arr = [ord(x) - ord("a") for x in password]

    return arr


def convert_num_array_to_string_password(arr):
    return "".join([chr(ord("a") + x) for x in arr])


def increment_password(password):
    n = len(password)
    carry = 1

    for i in range(n - 1, -1, -1):
        password[i] += carry
        carry = password[i] // 26
        password[i] %= 26

    return password


def solve(password):
    password = convert_password_to_num_array(password)

    while True:
        password = increment_password(password)
        if is_password_valid(password):
            break

    return convert_num_array_to_string_password(password)


if __name__ == "__main__":
    password = input().strip()
    print(solve(password))
