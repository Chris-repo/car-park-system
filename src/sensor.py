import random
from abc import ABC, abstractmethod


class Sensor(ABC):
    variant = "Sensor"

    def __init__(self, id=0, is_active=False, car_park=None):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    def __str__(self):
        return f"{self.variant}\nid: {self.id}\nStatus: {self.is_active}\n"

    @abstractmethod
    def update_car_park(self, plate):
        ...

    def _scan_plate(self):
        return f"FAKE-{random.randint(0, 999):03d}"

    def detect_vehicle(self, plate=None):
        vehicle_plate = plate or self._scan_plate()
        self.update_car_park(vehicle_plate)


class EntrySensor(Sensor):
    variant = "Entry Sensor"

    def update_car_park(self, plate):
        self.car_park.add_car(plate)


class ExitSensor(Sensor):
    variant = "Exit Sensor"

    def _scan_plate(self):
        if len(self.car_park.plates):
            return random.choice(self.car_park.plates)

    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
