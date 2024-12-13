from . import aoc_2024_runner

from utils import Grid, Space

TRAILHEAD = "0"
TRAILEND = "9"
DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]

def walk_path(grid: Grid, space: Space) -> dict:    
    if space.value == TRAILEND:
        return {space: 1}
    
    destinations = {}
    next_step_value = str(int(space.value)+1)
    for direction in DIRECTIONS:
        next_step = grid.get_space(space.x + direction[0], space.y + direction[1])
        if next_step and next_step.value == next_step_value:
            combine_trailroutes(destinations, walk_path(grid, next_step))

    return destinations

def combine_trailroutes(destinations, new_paths):
    for trailend, route_count in new_paths.items():
        destinations[trailend] = destinations.get(trailend, 0) + route_count

def solution(input_lines):
    grid = Grid(input_lines)

    trailheads = grid.find_values("0")

    trailend_count = 0
    trailhead_ratings = 0
    for trailhead in trailheads:
        destinations = walk_path(grid, trailhead)
        trailend_count += len(destinations.keys())
        trailhead_ratings += sum(destinations.values())

    return trailend_count, trailhead_ratings

aoc_2024_runner.add_daily_solution("10", solution)