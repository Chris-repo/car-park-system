class CarPark:

    def __init__(self, location="unknown", capacity=0, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):
        return f"Car Park Information\nlocation: {self.location}\nCapacity: {self.capacity}\n"
