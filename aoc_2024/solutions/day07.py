from . import aoc_2024_runner
from itertools import product

def add(x,y):
    return x + y

def times(x,y):
    return x * y

def concat(x,y):
    return int(str(x) + str(y))

operations = {
    "+": add,
    "*": times
}

def check_equation(total, operands, operants):
    combination_total = operands[0]
    for i in range(len(operants)):
        combination_total = operations[operants[i]](combination_total, operands[i+1])
        if combination_total > total:
            return False

    if total == combination_total:
        return True

def check_line(total, operands):
    for operation_combination in product(operations.keys(), repeat=len(operands) - 1):
        if check_equation(total, operands, operation_combination):
            return True
    return False

def solution(input_lines):
    calibrated = 0
    non_calibrated = []
    for line in input_lines:
        total, equation = line.split(":")
        total = int(total)
        operands = [int(i) for i in equation.strip().split(" ")]
        if check_line(total, operands):
            calibrated += total
        else:
            non_calibrated.append((total, operands))

    extra_operator = calibrated

    operations["||"] = concat

    for line in non_calibrated:
        total, operands = line
        if check_line(total, operands):
            extra_operator += total

    return calibrated, extra_operator

aoc_2024_runner.add_daily_solution("07", solution)