from romanToInt import Solution
from unittest import TestCase

class TestRomanToInt(TestCase):
    def test_output_is_str(self):
        s = Solution("III").romanToInt()
        self.assertIsInstance(s, str)