from . import aoc_2024_runner

def solution(input_lines):
    class Report:
        def __init__(self, readings):
            self.direction = None
            self.readings = readings

        def is_safe_readings(self, first_reading, second_reading):
            if not 0 < abs(first_reading - second_reading) < 4:
                return False
            
            direction = "Up" if first_reading < second_reading else "Down"
            if not self.direction:
                self.direction = direction
            elif not self.direction == direction:
                return False
            
            return True

        def is_safe(self, dampener=False):
            previous_reading = self.readings[0]
            for i in range(1, len(self.readings)):
                if self.is_safe_readings(previous_reading, self.readings[i]):            
                    previous_reading = self.readings[i]
                elif dampener:
                    dampener = False
                else:
                    return False
            return True

    safe_count = 0
    safe_dampener_count = 0
    for line in input_lines:
        report = Report([int(i) for i in line.split()])
        if report.is_safe():
            safe_count += 1
        if report.is_safe(dampener=True):
            safe_dampener_count += 1
        else:
            for i in range(len(report.readings)):
                list_copy = report.readings.copy()
                list_copy.pop(i)
                dampened_report = Report(list_copy)
                if dampened_report.is_safe():
                    safe_dampener_count += 1
                    break
                
    return safe_count, safe_dampener_count

aoc_2024_runner.add_daily_solution("02", solution)