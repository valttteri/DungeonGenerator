import unittest
import tools
from random import randint
from bowyerwatson import bowyer_watson
import prim
from tools import generate_coordinates

class TestPrim(unittest.TestCase):
    """Testing Bowyer-Watson's algorithm"""
    def setUp(self):
        self.DISPLAY_WIDTH = 900
        self.DISPLAY_HEIGHT = 500
        self.super_coordinates = [
            (-self.DISPLAY_WIDTH**2, -self.DISPLAY_HEIGHT**2),
            (self.DISPLAY_WIDTH**2, 0), (0, self.DISPLAY_HEIGHT**2)
        ]
        self.coordinates = tools.generate_coordinates(10, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)

    def test_prim(self):
        for i in range(1000):
            count = randint(3, 15)

            coords = get_coordinates(count, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)

            triangulation = bowyer_watson(coords, self.super_coordinates, 1)
            mst = prim.prims_algorithm(triangulation)
            graph = tools.create_graph(mst)

            self.assertEqual(len(graph), count)

    def test_find_minimum_edge(self):
        found_correct_edge = True
        extra_coordinate = (1111, 1234)
        extra_end_node = ((1111, 1244), randint(1, 80))
        edges = {}

        edges[extra_coordinate] = extra_end_node

        for coordinate in self.coordinates:
            other_node = (randint(1000, 1500), randint(1000, 1500))
            distance = (randint(200, 300))
            edges[coordinate] = (other_node, distance)
        
        
        minimum_edge = prim.find_minimum_edge(edges)
        if minimum_edge != (extra_end_node[0], extra_coordinate):
            self.assertTrue(found_correct_edge)
        self.assertTrue(found_correct_edge)

def get_coordinates(NODE_COUNT: int, DISPLAY_WIDTH: int, DISPLAY_HEIGHT: int):
    while True:
        coordinates = generate_coordinates(NODE_COUNT, DISPLAY_WIDTH, DISPLAY_HEIGHT)
        if coordinates == 1:
            continue
        return coordinates