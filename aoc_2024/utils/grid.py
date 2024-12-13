from .space import Space

class Grid:
    def __init__(self, input_lines):
        self.x_length = len(input_lines)
        self.y_length = len(input_lines[0])
        self.initial_grid = self.generate_grid(input_lines)
        self.grid = [l.copy() for l in self.initial_grid]

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

    def find_values(self, value):
        return [space for space in self if space.value == value]

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
        if not current_space:
            raise StopIteration()
        return current_space
  