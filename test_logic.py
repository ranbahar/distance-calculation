import unittest

from logic import is_within_radius
from point import Point


class TestLocationUtils(unittest.TestCase):

    def test_within_radius(self):
        # Example location: Center of Tel Aviv
        center_point = Point(32.0853, 34.7818)
        check_point = Point(32.1053, 34.8018)
        radius = 10  # in kilometers

        # Point inside the radius (approximately 5km away)
        self.assertTrue(is_within_radius(center_point, radius, check_point))

    def test_outside_radius(self):
        # Example location: Center of Tel Aviv
        center_point = Point(32.0853, 34.7818)
        check_point = Point(32.1853, 34.8818)
        radius = 10  # in kilometers

        # Point outside the radius (approximately 15km away)
        check_lat, check_lon = 32.1853, 34.8818
        self.assertFalse(is_within_radius(center_point, radius, check_point))

    def test_within_radius_from_city_center_to_dizengoff_square(self):
        # Example location: Center of Tel Aviv
        center_point = Point(32.07519345111358, 34.77496212125395) # Dizengoff center
        check_point = Point(32.07792983113954, 34.77426474693079)  # Dizengoff square
        radius = 1  # in kilometers

        # Point inside the radius (approximately 227m away)
        self.assertTrue(is_within_radius(center_point, radius, check_point))


if __name__ == '__main__':
    unittest.main()
