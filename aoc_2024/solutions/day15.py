from . import aoc_2024_runner
from utils import Grid
from time import sleep

EMPTY = "."
BOX = "O"
ROBOT = "@"
WALL = "#"

DIRECTIONS = {
    "v": (1,0),
    "<": (0,-1),
    ">": (0,1),
    "^": (-1,0)
}

def move(space, next_space):
    next_space.value = space.value
    space.value = EMPTY
    return next_space


def complete_movement(grid: Grid, space, direction):
    adjacent_space = grid.get_space(space.x + direction[0], space.y + direction[1])
    if adjacent_space.value == WALL:
        return space
    elif adjacent_space.value == EMPTY:
        return move(space, adjacent_space)
    elif adjacent_space.value == BOX and not (adjacent_space == complete_movement(grid, adjacent_space, direction)):
        return move(space, adjacent_space)
    else:
        return space

def solution(input_lines):
    grid_read = True
    grid_input = []
    move_input = ""
    for line in input_lines:
        if line == "":
            grid_read = False
        elif grid_read:
            grid_input.append(line)
        else:
            move_input += line

    grid = Grid(grid_input)
    robot = grid.find_values(ROBOT)[0]

    for movement in move_input:
        robot = complete_movement(grid, robot, DIRECTIONS[movement])

    gps_total = 0
    boxes = grid.find_values(BOX)
    for box in boxes:
        gps_total += (100 * box.x) + box.y

    return gps_total, None

aoc_2024_runner.add_daily_solution("15", solution)