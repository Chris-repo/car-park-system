import unittest
from pathlib import Path
from car_park import CarPark


class TestCarPark(unittest.TestCase):
    TEST_DEFAULT_LOG_FILEPATH = "../logs/car_park_log.txt"
    TEST_LOG_FILEPATH = "new_log.txt"
    TEST_CONFIG_FILEPATH = "test_config.json"

    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.car_park_with_log = CarPark("123 Example Street", 100, log_file=self.TEST_LOG_FILEPATH)
        self.car_park_with_config = CarPark("123 Example Street", 100, config_file=self.TEST_CONFIG_FILEPATH)

    def tearDown(self):
        Path(self.TEST_LOG_FILEPATH).unlink(missing_ok=True)
        Path(self.TEST_CONFIG_FILEPATH).unlink(missing_ok=True)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path(self.TEST_DEFAULT_LOG_FILEPATH))

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")

        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        # Overfilling the car park should not change the number of available bays
        self.assertEqual(self.car_park.available_bays, 0)

        # Removing a car from an overfilled car park should not change the number of available bays
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def test_log_file_created(self):
        self.assertTrue(Path(self.TEST_LOG_FILEPATH).exists())

    def test_car_logged_when_entering(self):
        self.car_park_with_log.add_car("NEW-001")
        with self.car_park_with_log.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("entered", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_car_logged_when_exiting(self):
        self.car_park_with_log.add_car("NEW-001")
        self.car_park_with_log.remove_car("NEW-001")
        with self.car_park_with_log.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("NEW-001", last_line)  # check plate entered
        self.assertIn("exited", last_line)  # check description
        self.assertIn("\n", last_line)  # check entry has a new line

    def test_config_file_created(self):
        self.assertTrue(Path(self.TEST_CONFIG_FILEPATH).exists())

    def test_config_write(self):
        self.car_park_with_config.write_config()
        with self.car_park_with_config.config_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("123 Example Street", last_line)

    def test_car_park_object_created_from_config(self):
        test_config = Path(self.TEST_CONFIG_FILEPATH)
        test_config.write_text('{"location":"123 Test Street","capacity":69,"log_file":"new_log.txt"}')
        test_class_from_config = CarPark.from_config(self.TEST_CONFIG_FILEPATH)
        self.assertIsInstance(test_class_from_config, CarPark)
        self.assertEqual("123 Test Street", test_class_from_config.location)
        self.assertEqual(69, test_class_from_config.capacity)


if __name__ == "__main__":
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()
