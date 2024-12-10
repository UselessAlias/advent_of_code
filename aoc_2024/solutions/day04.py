from . import aoc_2024_runner

END = "END"

next_letter = {
    "X": "M",
    "M": "A",
    "A": "S",
    "S": END
}

class GridSpot:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value = value

class Grid:

    def __init__(self, input):
        self.x_length = len(input)
        self.y_length = len(input[0])

        self.grid = []
        for x in range(self.x_length):
            row = []
            for y in range(self.y_length):
                row.append(GridSpot(x,y,input[x][y]))
            self.grid.append(row)
        


    def get(self, x, y):
        if not 0 <= x < self.x_length:
            return None
        if not 0 <= y < self.y_length:
            return None
        return self.grid[x][y]
    
    def __iter__(self):
        self._iter_x = 0
        self._iter_y = 0
        return self
    
    def __next__(self):
        grid_spot = self.get(self._iter_x, self._iter_y)
        self._iter_y += 1
        if self._iter_y >= self.y_length:
            self._iter_x += 1
            self._iter_y = 0
        if self._iter_x >= self.x_length:
            raise StopIteration()
        return self.get(self._iter_x, self._iter_y)

dirs = [-1, 0, 1]

def find_word(grid, spot, x_dir, y_dir):
    next_value = next_letter.get(spot.value, None)
    if next_value == END:
        return True
    else:
        next_spot = grid.get(spot.x + x_dir, spot.y + y_dir)
        if not next_spot or next_spot.value != next_value:
            return False
        else:
            return find_word(grid, next_spot, x_dir, y_dir)

def find_across(grid, spot, x_dir, y_dir, match_set):
    ul_spot = grid.get(spot.x - x_dir, spot.y - y_dir)
    if not ul_spot:
        return False
    
    dr_spot = grid.get(spot.x + x_dir, spot.y + y_dir)
    if not dr_spot:
        return False

    if not {ul_spot.value, dr_spot.value} == match_set:
        return False  
    
    return True

def find_xmas(grid, spot):
    match_set = {"M", "S"}
    if find_across(grid, spot, 1, 1, match_set) and find_across(grid, spot, 1, -1, match_set):
        return True
    return False

def solution(input_lines):
    input_grid = []
    for line in input_lines:
        input_grid.append([spot for spot in line])

    xmas_count = 0
    cross_count = 0
    grid = Grid(input_grid)
    for spot in grid:
        if spot.value == "X":
            for dir_x in dirs:
                for dir_y in dirs:
                    if find_word(grid, spot, dir_x, dir_y):
                        xmas_count += 1
        if spot.value == "A":
            if find_xmas(grid, spot):
                cross_count += 1


    return xmas_count, cross_count

aoc_2024_runner.add_daily_solution("04", solution)