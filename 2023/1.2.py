import sys


try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
    sys.stdout = open(sys.path[0] + "/output.txt", "w")
except FileNotFoundError:
    pass


ssum = 0
digits = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

while True:
    try:
        line = input()
    except EOFError:
        break

    n = len(line)

    left_digit = 0
    while left_digit < n and line[left_digit].isdigit() == False:
        left_digit += 1

    right_digit = n - 1
    while right_digit >= 0 and line[right_digit].isdigit() == False:
        right_digit -= 1

    left_word_pos = n
    left_word_name = -1
    right_word_pos = -1
    right_word_name = -1

    for digit in digits:
        find_left_pos = line.find(digit)
        find_right_pos = line.rfind(digit)

        if find_left_pos != -1:
            if find_left_pos < left_word_pos:
                left_word_pos = find_left_pos
                left_word_name = digits[digit]
        if find_right_pos != -1:
            if find_right_pos > right_word_pos:
                right_word_pos = find_right_pos
                right_word_name = digits[digit]

    if left_digit < left_word_pos:
        final_left = int(line[left_digit])
    else:
        final_left = left_word_name

    if right_digit > right_word_pos:
        final_right = int(line[right_digit])
    else:
        final_right = right_word_name

    num = 10 * final_left + final_right
    # print(num, left, right)
    ssum += num

print(ssum)
