import unittest
from random import randint
import tools
from bowyerwatson import bowyer_watson, are_edges_equal

class TestTools(unittest.TestCase):
    """Test tools.py"""
    def setUp(self):
        self.display_width = 800
        self.display_height = 400
        self.super_coordinates = [
            (-self.display_width**2, -self.display_height**2),
            (self.display_width**2, 0), (0, self.display_height**2)
        ]

        self.coordinates = tools.generate_coordinates(10, self.display_width, self.display_height)
        self.triangulation = bowyer_watson(self.coordinates, self.super_coordinates, 1)

    def tearDown(self):
        del self.coordinates

    def test_find_circumcenter(self):
        """Test the find_circumcenter function"""
        self.assertEqual(tools.find_circumcenter([(1,1), (3,5), (7,3)]), (4,2))
        result = tools.find_circumcenter([(2,4), (3,-7), (7,-2)])
        x = float(str(result[0])[:5])
        y = float(str(result[1])[:7])
        self.assertEqual(x, 1.378)
        self.assertEqual(y, -1.602)

    def test_distance_between_points(self):
        """Test the distance_between_points function"""
        self.assertEqual(tools.distance_between_points((1, 1), (5, 1)), 4)
        self.assertEqual(tools.distance_between_points((2, 3), (2, -2)), 5)
        self.assertEqual(round(tools.distance_between_points((3, 5), (7, 3)), 6), 4.472)

    def test_generate_coordinates(self):
        """Test the generate_coordinates function"""
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
        """Test the unique_edges function"""
        no_duplicates = True
        edges = list(tools.unique_edges(self.triangulation))

        for i in range(len(edges)):
            for j in range(len(edges)):
                if i == j:
                    continue
                if are_edges_equal(edges[i], edges[j]):
                    self.assertFalse(no_duplicates)
        self.assertTrue(no_duplicates)
