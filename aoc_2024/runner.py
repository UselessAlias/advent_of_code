from solutions import *
import solutions
import argparse

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-d', '--day', required=True)
    arg_parser.add_argument('-t', '--test', action='store_true')

    args = arg_parser.parse_args()
    day = args.day

    if args.test:
        solutions.aoc_2024_runner.test_daily_solution(day)
    else:
        solutions.aoc_2024_runner.run_daily_solution(day)

if __name__ == "__main__":
    main()