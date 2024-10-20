import hashlib
import multiprocessing
import sys

try:
    sys.stdin = open(sys.path[0] + "/input.txt", "r")
except FileNotFoundError:
    pass


def worker(start, end, text):
    for i in range(start, end):
        plaintext = text + str(i)
        md5_hash = calculate_md5_hash(plaintext)
        if md5_hash[:6] == "000000":
            print(i, plaintext, md5_hash)
            break


def calculate_md5_hash(input_string):
    md5_hash = hashlib.md5(input_string.encode()).hexdigest()
    return md5_hash


def take_input():
    text = input().strip()
    return text


def solve(text):
    num_processes = 10
    num_tasks = 10**7
    tasks_per_process = num_tasks // num_processes

    processes = []
    for i in range(num_processes):
        start = i * tasks_per_process + 1
        end = (i + 1) * tasks_per_process

        if i == num_processes - 1:
            end = num_tasks

        process = multiprocessing.Process(target=worker, args=(start, end, text))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    text = take_input()
    print(solve(text))
