from . import aoc_2024_runner

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            new_stones += [stone[:int(len(stone)/2)], str(int(stone[int(len(stone)/2):]))]
        else:
            new_stones.append(str(int(stone)*2024))

    return new_stones


def solution(input_lines):
    stones = input_lines[0].split(" ")
    i = 1
    for _ in range(25):
        stones = blink(stones)
        print(f"Blink {i}, length {len(stones)}")
        i += 1

    stone_length_25 = len(stones)

    for _ in range(50):
        stones = blink(stones)
        print(f"Blink {i}, length {len(stones)}")
        i += 1


    stone_length_50 = len(stones)

    return stone_length_25, stone_length_50

aoc_2024_runner.add_daily_solution("11", solution)