from . import aoc_2024_runner
from utils import Grid, Space

class Patch:
    def __init__(self, spaces, value):
        self.patch_spaces = spaces
        self.value = value

    def __hash__(self):
        return hash(str(self))
    
    def edges(self):
        edges = 0
        for space in self.patch_spaces:
            edges += space.edges
        return edges
    
    def area(self):
        return len(self.patch_spaces)
    
    def calc_cost(self):
        return self.edges() * self.area()

DIRECTIONS = [(0,1), (0,-1), (1,0), (-1,0)]

def find_patch(grid: Grid, space: Space) -> set:
    patch_spaces = {space}
    space.patched = True
    space.edges = 0
    for direction in DIRECTIONS:
        adj_space = grid.get_space(space.x + direction[0], space.y + direction[1])
        if adj_space and not hasattr(adj_space, "patched") and adj_space.value == space.value:
            patch_spaces.update(find_patch(grid, adj_space))
        elif not adj_space or (adj_space and not adj_space.value == space.value):
            space.edges += 1
        
    return patch_spaces

def solution(input_lines):
    grid = Grid(input_lines)
    patches = []
    for space in grid:
        if hasattr(space, "patched"):
            continue
        patches.append(Patch(find_patch(grid, space), space.value))

    total_cost = 0
    for patch in patches:
        cost = patch.calc_cost()
        total_cost += cost

    return total_cost, None

aoc_2024_runner.add_daily_solution("12", solution)