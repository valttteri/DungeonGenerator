import unittest
import tools
from bowyerwatson import bowyer_watson, are_edges_equal

class TestBowyerWatson(unittest.TestCase):
    """Testing Bowyer-Watson's algorithm"""
    def setUp(self):
        self.display_width = 800
        self.display_height = 400
        self.super_coordinates = [
            (-self.display_width**2, -self.display_height**2),
            (self.display_width**2, 0), (0, self.display_height**2)
        ]


    def test_bowyer_watson(self):
        """Test Bowyer-Watson's algorithm"""
        for i in range(1000):
            triangulation = get_triangulation(
                4,
                self.display_width,
                self.display_height,
                self.super_coordinates
            )

            self.assertGreater(len(triangulation), 1)
            self.assertLess(len(triangulation), 4)

        for i in range(1000):
            triangulation = get_triangulation(
                3,
                self.display_width,
                self.display_height,
                self.super_coordinates
            )

            self.assertEqual(len(triangulation), 1)

    def test_are_edges_equal(self):
        """Test the are_edges_equal function"""
        self.assertTrue(are_edges_equal([(3, 4), (7, 6)], [(3, 4), (7, 6)]))
        self.assertTrue(are_edges_equal([(3, 4), (7, 6)], [(7, 6), (3, 4)]))
        self.assertFalse(are_edges_equal([(3, 4), (7, 6)], [(3, 4), (7, 4)]))
        self.assertFalse(are_edges_equal([(3, 4), (7, 6)], [(7, 6), (1, 1)]))

def get_triangulation(count, width, height, super_coordinates):
    """Make sure that a valid triangulation is used"""
    while True:
        coords = tools.generate_coordinates(count, width, height)
        triangulation = bowyer_watson(coords, super_coordinates, 1)

        if len(triangulation) == 0:
            continue
        return triangulation
