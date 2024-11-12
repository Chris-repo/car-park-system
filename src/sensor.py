class Sensor:
    variant = "Sensor"
    def __init__(self, id=0, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"{(self.variant)}\nid: {self.id}\nStatus: {self.is_active}\n"


class EntrySensor(Sensor):
    variant = "Entry Sensor"


class ExitSensor(Sensor):
    variant = "Exit Sensor"

