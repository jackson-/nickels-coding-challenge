import unittest
import ctaridefare

class TestCtaRider(unittest.TestCase):

    def test_find_fare_combination(self):
        assert ctaridefare.find_combination(0, []) == []
        assert ctaridefare.find_combination(7, [1, 4, 6]) == [1, 6]
        assert ctaridefare.find_combination(8, [1, 4, 6]) is None
        assert ctaridefare.find_combination(57, [6, 13, 13, 21, 23, 24]) == [13, 21, 23]

if __name__ == '__main__':
    unittest.main()
