from os.path import dirname, basename, isfile, join
import glob

class AOCRunner():
    def __init__(self):
        self.solutions = {}

    def add_daily_solution(self, day, day_solution):
        self.solutions[day] = day_solution

    def run_daily_solution(self, day):
        self.run_solution(day, f"./inputs/day_{day}.txt")

    def run_solution(self, day, input_path):
        try:
            solution = self.solutions[day]
        except KeyError:
            print(f"Solution for day {day} is missing")
            raise Exception("Solution Error")

        with open(input_path, "rt") as f:
            input_lines = f.readlines()

        cleaned_lines = [line.strip() for line in input_lines]

        part_1, part_2 = solution(cleaned_lines)

        print(f"The solution to part one for day {day}: {str(part_1)}")
        print(f"The solution to part two for day {day}: {str(part_2)}")

    def test_daily_solution(self, day):
        self.run_solution(day, f"./inputs/test_data/day_{day}.txt")

aoc_2024_runner = AOCRunner()

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
