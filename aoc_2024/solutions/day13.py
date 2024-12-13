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

    def add_iteration(self, position, step, route=""):
        new_position = position + step
        if new_position > self.total[0]:
            print(route)
            return -1
        if new_position == self.total[0]:
            print(route)
            return 0
        press_a = self.add_iteration(new_position, self.button_a[0], f"{route}a")
        press_b = self.add_iteration(new_position, self.button_b[0], f"{route}b")
        if press_a >= 0 and press_b >= 0 :
            press_a_cost = press_a + 3
            press_b_cost = press_b + 1
            return min(press_a_cost, press_b_cost)
        if press_a >= 0:
            return press_a + 3
        if press_b >= 0:
            return press_b + 1
        return -1
    
    def cheapest_prize(self):
        cheapest_cost = False
        for a in range(1,101):
            for b in range(1,101):
                position = (a * self.button_a[0]) + (b * self.button_b[0])
                if position > self.total[0]:
                    break
                if position == self.total[0]:
                    cost = (a * 3) + b
                    if not cheapest_cost or cost < cheapest_cost:
                        cheapest_cost = cost 
        return cheapest_cost

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
        cost = machine.cheapest_prize()
        if cost:
            tokens += cost
    
    return tokens, None

aoc_2024_runner.add_daily_solution("13", solution)