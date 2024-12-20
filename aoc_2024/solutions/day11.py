from . import aoc_2024_runner

def blink(stones):
    new_stones = {}
    for stone in stones.keys():
        if stone == "0":
            new_stones["1"] = new_stones.get("1", 0) + stones["0"]
        elif len(stone) % 2 == 0:
            left_stone = stone[:int(len(stone)/2)]
            new_stones[left_stone] = new_stones.get(left_stone, 0) + stones[stone]
            
            right_stone = str(int(stone[int(len(stone)/2):]))
            new_stones[right_stone] = new_stones.get(right_stone, 0) + stones[stone]
        else:
            new_stone = str(int(stone)*2024)
            new_stones[new_stone] = new_stones.get(new_stone, 0) + stones[stone]

    return new_stones

def stones_length(stones):
    occurances = 0
    for stone_occurance in stones.values():
        occurances += stone_occurance
    return occurances

def solution(input_lines):
    stones = input_lines[0].split(" ")
    stones = {stone: 1 for stone in stones}
    for _ in range(25):
        stones = blink(stones)

    stone_length_25 = stones_length(stones)

    for _ in range(50):
        stones = blink(stones)


    stone_length_75 = stones_length(stones)

    return stone_length_25, stone_length_75

aoc_2024_runner.add_daily_solution("11", solution)