from . import aoc_2024_runner
from itertools import combinations, permutations
import numpy as np

PASSED_THROUGH = "X"
BARRIER = "#"
GUARD = "^"

class Guard:

    directions = {
        "L": (0,-1),
        "R": (0,1),
        "U": (-1,0),
        "D": (1,0)
    }

    right_turn = {
        "L": "U",
        "U": "R",
        "R": "D",
        "D": "L"
    }

    def __init__(self, initial_space, direction):
        self.initial_space = initial_space
        self.occupying_space = initial_space
        self.direction = direction
        self.movement = Guard.directions[direction]

    def turn_right(self):
        self.direction = Guard.right_turn[self.direction]
        self.movement = Guard.directions[self.direction]

    def reset(self):
        self.occupying_space = self.initial_space

class Space:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return f"{self.value}"
    
    def __str__(self):
        return f"{self.value}"

class Grid:
    def __init__(self, input_lines):
        self.x_length = len(input_lines)
        self.y_length = len(input_lines[0])
        self.initial_grid = self.generate_grid(input_lines)
        self.grid = [l.copy() for l in self.initial_grid]
        self.hit_barriers = []

    def generate_grid(self, input_lines):
        grid = []
        for x in range(self.x_length):
            row = []
            for y in range(self.y_length):        
                row.append(Space(x,y,input_lines[x][y]))
            grid.append(row)
        return grid

    def get_space(self, x, y):
        if not 0 <= x < self.x_length:
            return None
        
        if not 0 <= y < self.y_length:
            return None
        
        return self.grid[x][y]
    
    def put_space(self, space):
        self.grid[space.x][space.y] = space
    
    def find_guard(self):
        for row in self.grid:
            for space in row:
                if space.value == GUARD:
                    return space
                
    def step_guard(self, guard: Guard):
        guard_space = guard.occupying_space
        next_spot = self.get_space(guard_space.x + guard.movement[0], guard_space.y + guard.movement[1])
        if next_spot and next_spot.value == "#":
            self.hit_barriers.append(next_spot)
            guard.turn_right()
        else:
            guard.occupying_space.value = PASSED_THROUGH
            guard.occupying_space = next_spot
        return guard
    
    def reset(self):
        self.grid = [l.copy() for l in self.initial_grid]

    def __repr__(self):
        return "\n".join([str(row) for row in self.grid])
    
    def __str__(self):
        return "\n".join([str(row) for row in self.grid])
    
    def __iter__(self):
        self._iter_x = 0
        self._iter_y = 0
        return self
    
    def __next__(self):
        current_space = self.get_space(self._iter_x, self._iter_y)
        self._iter_y += 1
        if self._iter_y >= self.y_length:
            self._iter_x += 1
            self._iter_y = 0
        if self._iter_x >= self.x_length:
            raise StopIteration()
        return current_space
    
def guard_loops(grid, guard):
    step_count = 0
    while guard.occupying_space:
        grid.step_guard(guard)
        step_count += 1
        if step_count == 50000:
            return True
    return False

def solution(input_lines):
    grid = Grid([[value for value in line] for line in input_lines])
    guard_space = grid.find_guard()
    guard = Guard(guard_space, "U")
    while guard.occupying_space:
        grid.step_guard(guard)

    pass_through_count = 0
    for space in grid:
        if space.value == PASSED_THROUGH:
            pass_through_count += 1

    loop_count = 0
    for space in grid:
        if space.value in [BARRIER]:
            continue
        else:
            guard.reset()
            replacement_barrier = Space(space.x, space.y, BARRIER)
            grid.put_space(replacement_barrier)
            if guard_loops(grid, guard):
                loop_count += 1
            grid.put_space(space)
            
    return pass_through_count, loop_count

aoc_2024_runner.add_daily_solution("06", solution)