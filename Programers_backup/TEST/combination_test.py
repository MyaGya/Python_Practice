import unittest
from itertools import combinations

from Programers_backup.TEST import combination_test_util


class TestCombination(unittest.TestCase):

    def test_add(self):
        a, b = 1, 2
        self.assertEqual(a + b, combination_test_util.add(a, b))

    def test_combination_print(self):
        print(list(combinations([1, 2, 3], 2)))


if __name__ == "__main__":
    unittest.main()
