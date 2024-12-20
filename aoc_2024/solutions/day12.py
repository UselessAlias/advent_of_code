from . import aoc_2024_runner
from utils import Grid, Space

DIRECTIONS = {
    "R": (0,1),
    "L": (0,-1),
    "D": (1,0), 
    "U": (-1,0)
}

ADJACENT = {
    "U": ("L","R"),
    "D": ("L","R"),
    "R": ("U","D"), 
    "L": ("U","D")
}

class Patch:
    def __init__(self, spaces, value):
        self.patch_spaces = spaces
        self.value = value

    def __hash__(self):
        return hash(str(self))
    
    def edges(self):
        edges = 0
        for space in self.patch_spaces:
            edges += len(space.edges)
        return edges
    
    def area(self):
        return len(self.patch_spaces)
    
    def calc_cost(self):
        return self.edges() * self.area()
    
    def find_sides(self, grid: Grid):
        corners = 0
        for space in self.patch_spaces:
            if not space.edges:
                continue
            for edge in space.edges:
                for adjacent in ADJACENT[edge]:
                    adjacent_space = grid.get_space(space.x + DIRECTIONS[adjacent][0], space.y + DIRECTIONS[adjacent][1])
                    if adjacent_space and edge in adjacent_space.edges and space.value == adjacent_space.value:
                        continue
                    corners += 1
        return corners/2
    
    def calc_side_cost(self, grid):
        return int(self.area() * self.find_sides(grid))


def find_patch(grid: Grid, space: Space) -> set:
    patch_spaces = {space}
    space.patched = True
    space.edges = []
    for direction in DIRECTIONS:
        adj_space = grid.get_space(space.x + DIRECTIONS[direction][0], space.y + DIRECTIONS[direction][1])
        if adj_space and not hasattr(adj_space, "patched") and adj_space.value == space.value:
            patch_spaces.update(find_patch(grid, adj_space))
        elif not adj_space or (adj_space and not adj_space.value == space.value):
            space.edges.append(direction)
        
    return patch_spaces

def solution(input_lines):
    grid = Grid(input_lines)
    patches = []
    for space in grid:
        if hasattr(space, "patched"):
            continue
        patches.append(Patch(find_patch(grid, space), space.value))

    total_cost = 0
    side_cost = 0
    for patch in patches:
        cost = patch.calc_cost()
        total_cost += cost
        side_cost += patch.calc_side_cost(grid)

    return total_cost, side_cost

aoc_2024_runner.add_daily_solution("12", solution)