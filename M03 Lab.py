class Vehicle:
    def __init__(self):
        self.vehicle_type = None


class Automobile(Vehicle):
    def __init__(self):
        super().__init__()
        self.year = None
        self.make = None
        self.model = None
        self.doors = None
        self.roof = None

    def input_data(self):
        self.vehicle_type = "car"
        self.year = input("Enter the year: ")
        self.make = input("Enter the make: ")
        self.model = input("Enter the model: ")
        self.doors = input("Enter the number of doors (2 or 4): ")
        self.roof = input("Enter the type of roof (solid or sun roof): ")

    def display_data(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make", self.make)
        print("Model", self.model)
        print("Number of doors", self.doors)
        print("Type of roof:", self.roof)    