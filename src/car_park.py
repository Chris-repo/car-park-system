from pathlib import Path
from datetime import datetime
from sensor import Sensor
from display import Display


class CarPark:
    _available_bays = 0

    def __init__(
            self, location="unknown",
            capacity=0,
            plates=None,
            sensors=None,
            displays=None,
            log_file="../logs/car_park_log.txt"
    ):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)

    def __str__(self):
        return f"Car Park Information\nlocation: {self.location}\nCapacity: {self.available_bays} of {self.capacity}\n"

    @property
    def available_bays(self):
        self._available_bays = max(0, self.capacity - len(self.plates))
        return self._available_bays

    def register(self, component):
        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a sensor or display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    def add_car(self, plate):
        self.plates.append(plate)
        self._log_car_activity(plate, "entered")
        self.update_displays()

    def remove_car(self, plate):
        try:
            self.plates.remove(plate)
            self._log_car_activity(plate, "exited")
        except ValueError as value_error:
            raise value_error
        finally:
            self.update_displays()

    def update_displays(self):
        data = {
            "Available bays": self.available_bays,
            "Capacity": self.capacity
        }
        for display in self.displays:
            display.update(data)

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now():%Y-%m-%d %H:%M:%S}\n")
