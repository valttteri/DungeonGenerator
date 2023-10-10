import unittest
import tools
from random import randint
from bowyerwatson import bowyer_watson
from prim import prims_algorithm

class TestPrim(unittest.TestCase):
    """Testing Bowyer-Watson's algorithm"""
    def setUp(self):
        self.DISPLAY_WIDTH = 900
        self.DISPLAY_HEIGHT = 500
        self.super_coordinates = [
            (-self.DISPLAY_WIDTH**2, -self.DISPLAY_HEIGHT**2),
            (self.DISPLAY_WIDTH**2, 0), (0, self.DISPLAY_HEIGHT**2)
        ]

    def test_prim(self):
        for i in range(500):
            valid = True
            count = randint(3, 15)

            coords = tools.generate_coordinates(count, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)
            triangulation = bowyer_watson(coords, self.super_coordinates, 1)
            mst = prims_algorithm(triangulation)
            graph = tools.create_graph(mst)

            if len(graph) != count:
                self.assertFalse(valid)
            else:
                self.assertTrue(valid)