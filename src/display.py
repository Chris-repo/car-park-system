class Display:
    variant = "Display"
    def __init__(self, id=0, message="", is_on=False, car_park=None):
        self.id = id
        self.message = message
        self.is_on = is_on
        self.car_park = car_park

    def __str__(self):
        return f"{self.variant}\nid: {self.id}\n{self.message}\n"

    def update(self, data):
        for key, value in data.items():
            match key:
                case "message":
                    self.message = value
                case "is_on":
                    self.is_on = value
                case _:
                    print(f"{key}: {value}")
