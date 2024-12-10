from . import aoc_2024_runner
import itertools

BEFORE = "before"
AFTER = "after"

class Instructions:
    def __init__(self, instructions_lines):
        self.instructions = {}
        self.build_instuctions(instructions_lines)

    def build_instuctions(self, instruction_lines):
        for line in instruction_lines:
            before_page, after_page = line.split("|")
            
            existing_before_page = self.get_page_instruction(before_page)
            existing_before_page[BEFORE].add(after_page)
            self.instructions[before_page] = existing_before_page

            existing_after_page = self.get_page_instruction(after_page)
            existing_after_page[AFTER].add(before_page)
            self.instructions[after_page] = existing_after_page

            
    def get_page_instruction(self, page):
        existing = self.instructions.get(page, None)
        if not existing:
            existing = {BEFORE: set(), AFTER: set()}
        return existing
    
    def check_page(self, page, earlier_pages, later_pages):
        page_instructions = self.get_page_instruction(page)
        if not page_instructions:
            return True
        
        if set(later_pages) & page_instructions[AFTER]:
            return False
        
        if set(earlier_pages) & page_instructions[BEFORE]:
            return False
        
        return True

def check_manual(manual, instructions):
    for page_number in range(len(manual)):
        page = manual[page_number]

        if page_number == 0:
            before_pages = []
        else:
            before_pages = manual[:page_number]

        if page_number == len(manual) - 1:
            after_pages = []
        else:
            after_pages = manual[page_number+1:]

        if not instructions.check_page(page, before_pages, after_pages):
            return False
        
    return True


def solution(input_lines):
    instruction_lines = []
    page_lines = []
    next_part = False
    for line in input_lines:
        if line == "":
            next_part = True
        elif next_part:
            page_lines.append(line)
        else:
            instruction_lines.append(line)
    
    instructions = Instructions(instruction_lines)
    correct_manuals = []
    incorrect_manuals = []
    for manual in page_lines:
        manual = manual.split(",")
        if check_manual(manual, instructions):
            correct_manuals.append(manual)
        else:
            incorrect_manuals.append(manual)
       
    
    medium_page_sum = 0
    for manual in correct_manuals:
        medium_page_sum += int(manual[int((len(manual) - 1)/2)])

    incorrect_medium_page_sum = 0
    for manual in incorrect_manuals:
        manual_set = set(manual)
        correct_manual = [0 for _ in range(len(manual_set))]
        for page in manual_set:
            other_pages_set = manual_set - set(page)
            after_pages = instructions.get_page_instruction(page)[AFTER]
            after_page_count = len(other_pages_set & after_pages)
            page_index = len(correct_manual) - 1 - after_page_count
            correct_manual[page_index] = page
        incorrect_medium_page_sum += int(correct_manual[int((len(correct_manual) - 1)/2)])

    
    return medium_page_sum, incorrect_medium_page_sum

aoc_2024_runner.add_daily_solution("05", solution)