from . import aoc_2024_runner
import re

def solution(input_lines):
    multipled = 0
    conditional_multplies = 0
    conditional_enabled = True
    for line in input_lines:
        all_muls = re.findall("(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))", line)
        for mul in all_muls:
            if mul[4] == "don't()":
                conditional_enabled = False
            elif mul[3] == "do()":
                conditional_enabled = True
            else:
                multiple = int(mul[1]) * int(mul[2])
                multipled += multiple
                if conditional_enabled:
                    conditional_multplies += multiple

    return multipled, conditional_multplies

aoc_2024_runner.add_daily_solution("03", solution)