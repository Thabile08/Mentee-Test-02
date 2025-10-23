import unittest
from fundamentals import *

class TestFundamentals(unittest.TestCase):

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 3), -3)
        self.assertEqual(multiply_numbers(0, 5), 0)

    def test_is_positive(self):
        self.assertTrue(is_positive(2))
        self.assertFalse(is_positive(-5))
        self.assertFalse(is_positive(0))

    def test_count_letters(self):
        self.assertEqual(count_letters("Hello"), 5)
        self.assertEqual(count_letters(""), 0)

    def test_smallest_number(self):
        self.assertEqual(smallest_number([3, 1, 7, 0]), 0)
        self.assertEqual(smallest_number([-5, -2, -10]), -10)

    def test_capitalize_word(self):
        self.assertEqual(capitalize_word("python"), "Python")
        self.assertEqual(capitalize_word("alex"), "Alex")

    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3]), 6)
        self.assertEqual(sum_list([]), 0)

    def test_contains_number(self):
        self.assertTrue(contains_number(3, [1, 2, 3, 4]))
        self.assertFalse(contains_number(5, [1, 2, 3, 4]))

    def test_square_number(self):
        self.assertEqual(square_number(4), 16)
        self.assertEqual(square_number(-3), 9)

    def test_remove_spaces(self):
        self.assertEqual(remove_spaces("a b c"), "abc")
        self.assertEqual(remove_spaces("  hello world  "), "helloworld")

    def test_repeat_word(self):
        self.assertEqual(repeat_word("hi", 3), "hihihi")
        self.assertEqual(repeat_word("a", 1), "a")

    def test_count_words(self):
        self.assertEqual(count_words("Python is fun"), 3)
        self.assertEqual(count_words("One two three four"), 4)

    def test_second_largest(self):
        self.assertEqual(second_largest([3, 1, 7, 7, 5]), 5)
        self.assertEqual(second_largest([10]), None)

if __name__ == "__main__":
    unittest.main()
