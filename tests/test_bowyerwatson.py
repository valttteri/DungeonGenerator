import unittest
import tools
from bowyerwatson import bowyer_watson, are_edges_equal

class TestBowyerWatson(unittest.TestCase):
    """Testing Bowyer-Watson's algorithm"""
    def setUp(self):
        self.DISPLAY_WIDTH = 800
        self.DISPLAY_HEIGHT = 400
        self.NODE_COUNT = 12
        self.X_MIN = 100
        self.X_MAX = self.DISPLAY_WIDTH - 100
        self.Y_MIN = 50
        self.Y_MAX = self.DISPLAY_HEIGHT - 50
        self.super_coordinates = [
            (-self.DISPLAY_WIDTH**2, -self.DISPLAY_HEIGHT**2),
            (self.DISPLAY_WIDTH**2, 0), (0, self.DISPLAY_HEIGHT**2)
        ]
        

    def test_bowyer_watson(self):
        for i in range(1000):
            triangulation = get_triangulation(4, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT, self.super_coordinates)

            self.assertGreater(len(triangulation), 1)
            self.assertLess(len(triangulation), 4)

        for i in range(1000):
            triangulation = get_triangulation(3, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT, self.super_coordinates)

            self.assertEqual(len(triangulation), 1)
    
    def test_are_edges_equal(self):
        self.assertTrue(are_edges_equal([(3, 4), (7, 6)], [(3, 4), (7, 6)]))
        self.assertTrue(are_edges_equal([(3, 4), (7, 6)], [(7, 6), (3, 4)]))
        self.assertFalse(are_edges_equal([(3, 4), (7, 6)], [(3, 4), (7, 4)]))
        self.assertFalse(are_edges_equal([(3, 4), (7, 6)], [(7, 6), (1, 1)]))

def get_triangulation(count, width, height, super_coordinates):
    while True:
        coords = tools.generate_coordinates(count, width, height)
        triangulation = bowyer_watson(coords, super_coordinates, 1)

        if len(triangulation) == 0:
            continue
        return triangulation