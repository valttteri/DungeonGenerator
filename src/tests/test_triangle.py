import unittest
from classes.triangleclass import Triangle

class TestTriangle(unittest.TestCase):
    """Test the triangle class"""
    def setUp(self):
        self.triangle_1 = Triangle((1, 5), (4, 5), (7, 2), 1)
        self.triangle_2 = Triangle((1, 5), (4, 5), (7, 2), 1)
        self.triangle_3 = Triangle((2, 6), (8, 10), (5, 16), 1)
        self.triangle_4 = Triangle((40, 50), (400, 300), (50, 200), 1)
        self.triangle_5 = Triangle((-20, -100), (300, -50), (300, 300), 1)

    def test_circum_center(self):
        """Test circum center calculation"""
        self.assertEqual(self.triangle_1.circum_center(), (2.5, 0.5))
        self.assertEqual(self.triangle_3.circum_center(), (2.875, 11.188))
        self.assertEqual(self.triangle_4.circum_center(), (264.903, 110.34))
        self.assertEqual(self.triangle_5.circum_center(), (108.75, 125))

    def test_cc_radius(self):
        """Test the calculation of a circum circle's radius"""
        self.assertEqual(self.triangle_1.cc_radius(), 4.743)
        self.assertEqual(self.triangle_3.cc_radius(), 5.261)
        self.assertEqual(self.triangle_4.cc_radius(), 232.857)
        self.assertEqual(self.triangle_5.cc_radius(), 259.233)