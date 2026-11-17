import unittest

from utils.city_functions import city_country


class CityCountryTesting(unittest.TestCase):
    def test_city_country_without_population(self) -> None:
        self.assertEqual(city_country("santiago", "chile"), "Santiago, Chile.")

        with self.assertRaises(ValueError):
            city_country("", "brazil")

        with self.assertRaises(ValueError):
            city_country("paris", "")

    def test_city_country_with_population(self) -> None:
        self.assertEqual(city_country("santiago", "chile", 10000), "Santiago, Chile - population 10000.")

        with self.assertRaises(ValueError):
            city_country("santiago", "chile", -10000)


if (__name__ == "__main__"):
    unittest.main()
