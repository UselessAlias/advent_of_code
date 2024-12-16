from . import aoc_2024_runner

MAX_X = 101
MAX_Y = 103

class Robot:
    def __init__(self, starting_x, starting_y, vel_x, vel_y):
        self.starting_x = starting_x
        self.starting_y = starting_y
        self.current_x = self.starting_x
        self.current_y = self.starting_y
        self.vel_x = vel_x
        self.vel_y = vel_y

    def move(self):
        self.current_x = (self.current_x + self.vel_x) % MAX_X
        self.current_y = (self.current_y + self.vel_y) % MAX_Y

    def __str__(self):
        return f"({self.current_x}:{self.current_y})"
    
    def __repr__(self):
        return str(self)

def split_vector(vector_str):
    _, vector = vector_str.split("=")
    x, y = vector.split(",")
    return int(x.strip()), int(y.strip()) 

def solution(input_lines):
    robots = []
    for line in input_lines:
        pos, vel = line.split(" ")
        pos_x, pos_y = split_vector(pos)
        vel_x, vel_y = split_vector(vel)
        robots.append(Robot(pos_x, pos_y, vel_x, vel_y))

    for _ in range(100):
        for robot in robots:
            robot.move()
    
    quads = [[],[],[],[]]
    for robot in robots:
        if robot.current_x < (MAX_X-1)/2:
            if robot.current_y < (MAX_Y-1)/2:
                quads[0].append(robot)
            elif robot.current_y > (MAX_Y-1)/2:
                quads[1].append(robot)
        elif robot.current_x > (MAX_X-1)/2:
            if robot.current_y < (MAX_Y-1)/2:
                quads[2].append(robot)
            elif robot.current_y > (MAX_Y-1)/2:
                quads[3].append(robot)

    quad_sum = 1
    for quad in quads:
        quad_sum *= len(quad)

    return quad_sum, None

aoc_2024_runner.add_daily_solution("14", solution)