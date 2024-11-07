import unittest
import statistics

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 2, 3, 4]

    def test_mean(self):
        self.assertAlmostEqual(mean(self.data), statistics.mean(self.data), places=2)

    def test_median(self):
        self.assertEqual(median(self.data), statistics.median(self.data))

    def test_mode(self):
        self.assertEqual(mode(self.data), statistics.mode(self.data))

    def test_variance(self):
        self.assertAlmostEqual(variance(self.data), statistics.variance(self.data), places=2)

    def test_std_deviation(self):
        self.assertAlmostEqual(std_deviation(self.data), statistics.stdev(self.data), places=2)

if __name__ == "__main__":
    unittest.main()