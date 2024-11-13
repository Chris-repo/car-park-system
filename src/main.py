from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

#JUNK TEST CODE
car_park = CarPark(capacity=10)

entry_sensor = EntrySensor(id=1, car_park=car_park)
car_park.register(entry_sensor)

entry_display = Display(id=1, message="Entry")
car_park.register(entry_display)

exit_sensor = ExitSensor(id=2, car_park=car_park)
car_park.register(exit_sensor)

exit_display = Display(id=2, message="Exit")
car_park.register(exit_display)

for _ in range(0, 20):
    entry_sensor.detect_vehicle()

for _ in range(0, 15):
    exit_sensor.detect_vehicle()

print(car_park)

for _ in range(0, 10):
    try:
        exit_sensor.detect_vehicle()
    except ValueError:
        pass

print(car_park)
