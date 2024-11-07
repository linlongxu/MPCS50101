import unittest

class TestTemperatureConversion(unittest.TestCase):
    def test_valid_conversion(self):
        self.assertAlmostEqual(convert_to_celsius(32), 0.00, places=2)
        self.assertAlmostEqual(convert_to_celsius(100), 37.78, places=2)

    def test_invalid_input(self):
        self.assertIsNone(convert_to_celsius("abc"))  # Non-numeric input
        self.assertIsNone(convert_to_celsius(None))

if __name__ == "__main__":
    unittest.main()