from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


def main():

    car_park = CarPark("moondalup",100, log_file="../logs/moondalup.txt")

    entry_sensor = EntrySensor(id=1, is_on=True, car_park=car_park)
    car_park.register(entry_sensor)

    exit_sensor = ExitSensor(id=2, is_on=True, car_park=car_park)
    car_park.register(exit_sensor)

    welcome_display = Display(id=1, message="Welcome to Moondalup", car_park=car_park)
    car_park.register(welcome_display)

    # drive 10 cars into the car park
    for _ in range(10):
        entry_sensor.detect_vehicle()

    # drive 2 cars out of the car park
    for _ in range(2):
        exit_sensor.detect_vehicle()


if __name__ == "__main__":
    main()
