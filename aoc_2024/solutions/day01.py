from . import aoc_2024_runner

def solution(input_lines):
    left_list = []
    right_list = []
    for line in input_lines:
        left, right = line.split("   ")
        left_list.append(int(left.strip()))
        right_list.append(int(right.strip()))

    left_list.sort()
    right_list.sort()

    total_distance = 0

    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])

    right_count = {}
    for id in right_list:
        right_count[id] = right_count.get(id, 0) + 1

    modified_distance = 0
    for id in left_list:
        modified_distance += id * right_count.get(id, 0)

    return total_distance, modified_distance

aoc_2024_runner.add_daily_solution("01", solution)