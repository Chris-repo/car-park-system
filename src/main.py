from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display

#JUNK TEST CODE
car_park = CarPark(capacity=100)

entry_sensor = EntrySensor(id=1, car_park=car_park)
car_park.register(entry_sensor)

entry_display = Display(id=1, message="Entry")
car_park.register(entry_display)

exit_sensor = ExitSensor(id=2, car_park=car_park)
car_park.register(exit_sensor)

exit_display = Display(id=2, message="Exit")
car_park.register(exit_display)


entry_sensor.detect_car("TEST")
#print(car_park)

exit_sensor.detect_car("TEST")
#print(car_park)

exit_sensor.detect_car("TEST")
#print(car_park)
