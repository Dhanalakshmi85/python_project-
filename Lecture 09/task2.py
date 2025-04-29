class Elevator:
    def __init__(self, bottom, top):
        self.current = bottom

    def go_to_floor(self, target):
        while self.current < target:
            self.current += 1
            print(f"Elevator at floor {self.current}")
        while self.current > target:
            self.current -= 1
            print(f"Elevator at floor {self.current}")


class Building:
    def __init__(self, bottom, top, count):
        self.elevators = [Elevator(bottom, top) for _ in range(count)]

    def run_elevator(self, number, target):
        self.elevators[number].go_to_floor(target)


# Main program
b = Building(0, 5, 2)  # Building with 2 elevators (floors 0–5)
b.run_elevator(0, 3)   # Move elevator 0 to floor 3
b.run_elevator(1, 5)   # Move elevator 1 to floor 5
b.run_elevator(0, 0)   # Bring elevator 0 back to floor 0
