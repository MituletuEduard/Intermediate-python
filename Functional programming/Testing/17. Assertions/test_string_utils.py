from string_utils import reverse_string, capitalize_string, is_capitalized
import unittest


class MyTestCase(unittest.TestCase):
    def test_reverse_string(self):

        # Verify that the reversed string is correct
        self.assertTrue(reverse_string('hello') == 'olleh')

    def test_capitalize_string(self):
        # Verify that the capitalized string is correct
        self.assertEqual(capitalize_string('hello, world!'), 'Hello, world!')

    def test_is_capitalized(self):
        self.assertTrue(is_capitalized('Hello'))
        self.assertFalse(is_capitalized('hello'))
        # Verify that the function correctly identifies a capitalized string


if __name__ == '__main__':
    unittest.main()
