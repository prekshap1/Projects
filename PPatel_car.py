class Car:
    """Car Class"""

    def __init__(self):
        """Initialize the Car object."""
        self.x = 0
        self.y = 0
        self.heading = "n"

    def turn(self, direction):
        """Change the car's heading based on the given direction.
        Parameters:
        - direction (str): The direction to turn. It can be "l" for left or "r" for right.
        """
        if direction == "l":
            if self.heading == "n":
                self.heading = "w"
            elif self.heading == "w":
                self.heading = "s"
            elif self.heading == "s":
                self.heading = "e"
            else:
                self.heading = "n"
        elif direction == "r":
            if self.heading == "n":
                self.heading = "e"
            elif self.heading == "e":
                self.heading = "s"
            elif self.heading == "s":
                self.heading = "w"
            else:
                self.heading = "n"

    def drive(self, distance=1):
        """Drive the car forward.
        Parameters:
        distance (int): The distance to drive. Default is 1.
        """
        if self.heading == "n":
            self.y += distance
        elif self.heading == "e":
            self.x += distance
        elif self.heading == "s":
            self.y -= distance
        else:
            self.x -= distance

    def status(self):
        """Print the current position and heading of the car.
        """
        print(f"Coordinates: ({self.x}, {self.y})")
        print(f"Heading: {self.heading}")
