import unittest
import tools
from random import randint
from bowyerwatson import bowyer_watson

class TestTools(unittest.TestCase):
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


        self.coordinates = tools.generate_coordinates(10, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)
        self.triangulation = bowyer_watson(self.coordinates, self.super_coordinates, 1)

    def tearDown(self):
        del self.coordinates

    def test_find_circumcenter(self):
        self.assertEqual(tools.find_circumcenter([(1,1), (3,5), (7,3)]), (4,2))
        result = tools.find_circumcenter([(2,4), (3,-7), (7,-2)])
        x = float(str(result[0])[:5])
        y = float(str(result[1])[:7])
        self.assertEqual(x, 1.378)
        self.assertEqual(y, -1.602)
    
    def test_distance_between_points(self):
        self.assertEqual(tools.distance_between_points((1, 1), (5, 1)), 4)
        self.assertEqual(tools.distance_between_points((2, 3), (2, -2)), 5)
        self.assertEqual(round(tools.distance_between_points((3, 5), (7, 3)), 6), 4.472)
    
    def test_are_edges_equal(self):
        self.assertTrue(tools.are_edges_equal([(3, 4), (7, 6)], [(3, 4), (7, 6)]))
        self.assertTrue(tools.are_edges_equal([(3, 4), (7, 6)], [(7, 6), (3, 4)]))
        self.assertFalse(tools.are_edges_equal([(3, 4), (7, 6)], [(3, 4), (7, 4)]))
        self.assertFalse(tools.are_edges_equal([(3, 4), (7, 6)], [(7, 6), (1, 1)]))
    
    def test_generate_coordinates(self):
        no_duplicates = True
        not_near_each_other = True
        enough_coordinates = True

        for coordinate in self.coordinates:
            if self.coordinates.count(coordinate) > 1:
                no_duplicates = False
            for other in self.coordinates:
                if coordinate == other:
                    continue
                if tools.distance_between_points(coordinate, other) < 80:
                    not_near_each_other = False
        if len(self.coordinates) != 10:
            enough_coordinates = False
        
        self.assertTrue(no_duplicates)
        self.assertTrue(not_near_each_other)
        self.assertTrue(enough_coordinates)

    def test_unique_edges(self):
        no_duplicates = True
        edges = list(tools.unique_edges(self.triangulation))

        for i in range(len(edges)):
            for j in range(len(edges)):
                if i == j:
                    continue
                if tools.are_edges_equal(edges[i], edges[j]):
                    self.assertFalse(no_duplicates)
        self.assertTrue(no_duplicates)

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
        
        
        minimum_edge = tools.find_minimum_edge(edges)
        if minimum_edge != (extra_end_node[0], extra_coordinate):
            self.assertTrue(found_correct_edge)
        self.assertTrue(found_correct_edge)