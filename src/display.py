class Display:
    variant = "Display"
    def __init__(self, id=0, message="", is_on=False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"{self.variant}\nid: {self.id}\n{self.message}\n"

    def update(self, message):
        self.message = message
