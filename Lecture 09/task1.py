class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        self.current += 1
        print(f"Now at floor {self.current}")

    def floor_down(self):
        self.current -= 1
        print(f"Now at floor {self.current}")

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()


# Main program
e = Elevator(0, 5)  # Elevator from floor 0 to 5
e.go_to_floor(3)    # Move to floor 3
e.go_to_floor(0)    # Back to bottom
