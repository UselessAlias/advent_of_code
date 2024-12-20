from . import aoc_2024_runner

def parse_line(line, movement_divider="+"):
    _, movement = line.split(":")
    x, y = movement.split(",")
    x_movement = int(x.strip().split(movement_divider)[1])
    y_movement = int(y.strip().split(movement_divider)[1])
    return (x_movement, y_movement)


class Machine:
    
    def __init__(self, button_a, button_b, total):
        self.button_a = button_a
        self.button_b = button_b
        self.total = total
    
    def cheapest_prize(self):
        cheapest_cost = False
        for a in range(1,101):
            for b in range(1,101):
                total_x = (a * self.button_a[0]) + (b * self.button_b[0])
                total_y = (a * self.button_a[1]) + (b * self.button_b[1])
                if total_x > self.total[0] or total_y > self.total[1]:
                    break
                if total_x == self.total[0] and total_y == self.total[1]:
                    cost = (a * 3) + b
                    if (not cheapest_cost) or cost < cheapest_cost:
                        cheapest_cost = cost 
        return cheapest_cost
    
    def mincost(self):
        b, brem = divmod(self.button_a[1] * self.total[0] - self.button_a[0] * self.total[1], self.button_a[1] * self.button_b[0] - self.button_a[0] * self.button_b[1])
        a, arem = divmod(self.total[0] - b * self.button_b[0], self.button_a[0])
        return 0 if arem or brem else a * 3 + b

def solution(input_lines):
    machines = []
    for line in input_lines:
        if line.startswith("Button A"): 
            buttonA = parse_line(line)
        elif line.startswith("Button B"):
            buttonB = parse_line(line)
        elif line.startswith("Prize"):
            prize = parse_line(line, "=")
        else:
            machines.append({"buttonA": buttonA, "buttonB": buttonB, "prize": prize})

    tokens = 0
    for machine in machines:
        machine = Machine(machine["buttonA"], machine["buttonB"], machine["prize"])
        cost = machine.mincost()
        if cost:
            tokens += cost

    adjusted_tokens = 0
    adjustment = 10_000_000_000_000

    for machine in machines:
        machine = Machine(machine["buttonA"], machine["buttonB"], machine["prize"])
        machine.total = (machine.total[0] + adjustment, machine.total[1] + adjustment)
        cost = machine.mincost()
        if cost:
            adjusted_tokens += cost
    
    return tokens, adjusted_tokens

aoc_2024_runner.add_daily_solution("13", solution)