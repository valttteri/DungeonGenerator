import unittest
import xmlrunner
import app
import tools
from random import randint
from classes.triangleclass import Triangle
from bowyerwatson import bowyer_watson
from prim import prims_algorithm

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
        

class TestTriangle(unittest.TestCase):
    """Testing the triangle class"""
    def setUp(self):
        self.triangle_1 = Triangle((1, 5), (4, 5), (7, 2), 1)
        self.triangle_2 = Triangle((1, 5), (4, 5), (7, 2), 1)
        self.triangle_3 = Triangle((2, 6), (8, 10), (5, 16), 1)
        self.triangle_4 = Triangle((40, 50), (400, 300), (50, 200), 1)
        self.triangle_5 = Triangle((-20, -100), (300, -50), (300, 300), 1)
    
    def tearDown(self):
        del self.triangle_1
        del self.triangle_2
        del self.triangle_3
        del self.triangle_4
        del self.triangle_5

    def test_triangle_nodes(self):
        triangle = self.triangle_1
        self.assertEqual(triangle.show_nodes()[0], (1, 5))
        self.assertEqual(triangle.show_nodes()[1], (4, 5))
        self.assertEqual(triangle.show_nodes()[2], (7, 2))

    def test_triangle_edges(self):
        triangle = self.triangle_1
        self.assertEqual(triangle.show_edges()[0][0], (1, 5))
        self.assertEqual(triangle.show_edges()[0][1], (4, 5))
        self.assertEqual(triangle.show_edges()[1][0], (4, 5))
        self.assertEqual(triangle.show_edges()[1][1], (7, 2))
        self.assertEqual(triangle.show_edges()[2][0], (7, 2))
        self.assertEqual(triangle.show_edges()[2][1], (1, 5))
    
    def test_equality(self):
        self.assertEqual(self.triangle_1, self.triangle_1)
    
    def test_show_id(self):
        self.assertNotEqual(self.triangle_1.show_id(), self.triangle_2.show_id())
        self.assertNotEqual(self.triangle_2.show_id(), self.triangle_3.show_id())
    
    def test_circum_center(self):
        self.assertEqual(self.triangle_1.circum_center(), (2.5, 0.5))
        self.assertEqual(self.triangle_3.circum_center(), (2.875, 11.188))
        self.assertEqual(self.triangle_4.circum_center(), (264.903, 110.34))
        self.assertEqual(self.triangle_5.circum_center(), (108.75, 125))

    def test_cc_radius(self):
        self.assertEqual(self.triangle_1.cc_radius(), 4.743)
        self.assertEqual(self.triangle_3.cc_radius(), 5.261)
        self.assertEqual(self.triangle_4.cc_radius(), 232.857)
        self.assertEqual(self.triangle_5.cc_radius(), 259.233)

class TestPrim(unittest.TestCase):
    """Testing Bowyer-Watson's algorithm"""
    def setUp(self):
        self.DISPLAY_WIDTH = 800
        self.DISPLAY_HEIGHT = 400
        self.super_coordinates = [
            (-self.DISPLAY_WIDTH**2, -self.DISPLAY_HEIGHT**2),
            (self.DISPLAY_WIDTH**2, 0), (0, self.DISPLAY_HEIGHT**2)
        ]

    def test_prim(self):
        for i in range(500):
            valid = True
            count = randint(3, 14)

            coords = tools.generate_coordinates(count, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)
            triangulation = bowyer_watson(coords, self.super_coordinates, 1)
            mst = prims_algorithm(triangulation)
            graph = tools.create_graph(mst)

            if len(graph) != count:
                self.assertFalse(valid)
            else:
                self.assertTrue(valid)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='results'),
    failfast=False, buffer=False, catchbreak=False, exit=False)