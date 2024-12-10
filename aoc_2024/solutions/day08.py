from . import aoc_2024_runner
from itertools import combinations
from utils import Space, Grid

OPEN = '.'
ANTINODE = '#'

def update_antinode(grid, antenna, direction):
    node  = grid.get_space(antenna.x - direction[0], antenna.y - direction[1])
    if node:
        node.value = ANTINODE

def update_antinode_path(grid, antenna, direction):
    space = antenna
    while space:
        space.value = ANTINODE
        space = grid.get_space(space.x - direction[0], space.y - direction[1])

def solution(input_lines):
    antenna_sets = {}
    
    grid = Grid(input_lines)
    for space in grid:
        if not space.value == OPEN:
            existing_antenna = antenna_sets.get(space.value, None)
            if not existing_antenna:
                existing_antenna = []
            existing_antenna.append(space)
            antenna_sets[space.value] = existing_antenna
    
    for antenna_set in antenna_sets.values():
        for antenna_group in combinations(antenna_set, 2):
            antenna_1, antenna_2 = antenna_group
            dist_x = antenna_1.x - antenna_2.x
            dist_y = antenna_1.y - antenna_2.y

            if antenna_2 < antenna_1:
                antenna_1, antenna_2 = antenna_2, antenna_1
                
            update_antinode(grid, antenna_1, (dist_x * -1, dist_y * -1))
            update_antinode(grid, antenna_2, (dist_x, dist_y))

    antinode_count = 0
    for space in grid:
        if space.value == ANTINODE:
            antinode_count += 1

    grid.reset()

    for antenna_set in antenna_sets.values():
        for antenna_group in combinations(antenna_set, 2):
            antenna_1, antenna_2 = antenna_group
            dist_x = antenna_1.x - antenna_2.x
            dist_y = antenna_1.y - antenna_2.y

            if antenna_2 < antenna_1:
                antenna_1, antenna_2 = antenna_2, antenna_1
                
            update_antinode_path(grid, antenna_1, (dist_x * -1, dist_y * -1))
            update_antinode_path(grid, antenna_2, (dist_x, dist_y))

    antinode_path_count = 0
    for space in grid:
        print(space)
        if space.value == ANTINODE:
            antinode_path_count += 1

    print(grid)

    return antinode_count, antinode_path_count

aoc_2024_runner.add_daily_solution("08", solution)