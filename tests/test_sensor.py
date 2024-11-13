import unittest
from car_park import CarPark
from sensor import Sensor, EntrySensor, ExitSensor


class TestSensor(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.entry_sensor = EntrySensor(1, True, self.car_park)
        self.exit_sensor = ExitSensor(2, False, self.car_park)

    def test_init_method(self):
        self.assertIsInstance(self.entry_sensor, Sensor)
        self.assertEqual(self.entry_sensor.id, 1)
        self.assertEqual(self.entry_sensor.is_on, True)

        self.assertIsInstance(self.exit_sensor, Sensor)
        self.assertEqual(self.exit_sensor.id, 2)
        self.assertEqual(self.exit_sensor.is_on, False)

    def test_detect_vehicle(self):
        self.entry_sensor.detect_vehicle()
        self.assertEqual(self.car_park.plates[0][0:4], "FAKE")
        self.exit_sensor.detect_vehicle()
        self.assertEqual(self.car_park.plates, [])

        self.entry_sensor.detect_vehicle("TEST")
        self.assertEqual(self.car_park.plates[0], "TEST")
        self.exit_sensor.detect_vehicle("TEST")
        self.assertEqual(self.car_park.plates, [])
