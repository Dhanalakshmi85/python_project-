class Elevator:
    def __init__(self, bottom, top):
        self.current = bottom
        self.bottom = bottom

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
        self.bottom = bottom

    def run_elevator(self, number, target):
        self.elevators[number].go_to_floor(target)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)


# Main program
b = Building(0, 5, 2)  # Building with 2 elevators from floor 0 to 5
b.run_elevator(0, 3)   # Move elevator 0 to floor 3
b.run_elevator(1, 5)   # Move elevator 1 to floor 5
b.fire_alarm()         # All elevators go to bottom floor (0)
