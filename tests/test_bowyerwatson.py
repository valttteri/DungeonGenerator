import unittest
import tools
from bowyerwatson import bowyer_watson

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
        for i in range(500):
            valid = True
            coords = tools.generate_coordinates(4, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)
            triangulation = bowyer_watson(coords, self.super_coordinates, 1)
            if len(triangulation) == 2 or len(triangulation) == 3:
                self.assertTrue(valid)
            else:
                self.assertFalse(valid)

        for i in range(500):
            valid = True
            coords = tools.generate_coordinates(3, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)
            triangulation = bowyer_watson(coords, self.super_coordinates, 1)
            if len(triangulation) == 1:
                self.assertTrue(valid)
            else:
                self.assertFalse(valid)