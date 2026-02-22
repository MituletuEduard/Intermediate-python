import unittest
from coffee_menu import CoffeeMenu


class TestCoffeeMenu(unittest.TestCase):

    # Setup method: New CoffeeMenu instance before each test
    def setUp(self):
        self.menu = CoffeeMenu()
    # Teardown method: Clean up resources after each test

    def tearDown(self):
        self.menu = None

    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('espresso'), 2.50)
        self.assertEqual(self.menu.get_price('latte'), 2.75)
        self.assertEqual(self.menu.get_price('cappuccino'), 3.20)
        self.assertEqual(self.menu.get_price('americano'), 2.70)

    def test_get_price_non_existing_item(self):
        with self.assertRaises(KeyError):
            self.menu.get_price('beer')

    def test_add_item(self):
        self.menu.add_item('beer', 2.00)
        self.assertEqual(self.menu.get_price('beer'), 2.00)


if __name__ == '__main__':
    unittest.main()
