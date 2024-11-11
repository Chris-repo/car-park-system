class Sensor:
    type = "Sensor"
    def __init__(self, id=0, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"{(self.type)}\nid: {self.id}\nStatus: {self.is_active}\n"


class EntrySensor(Sensor):
    type = "Entry Sensor"


class ExitSensor(Sensor):
    type = "Exit Sensor"

