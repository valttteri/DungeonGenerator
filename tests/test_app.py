import unittest
import xmlrunner
import app

'''
In order to run the tests, each line in app.py referring to pygame must be commented out
'''

class TestApp(unittest.TestCase):
    def setUp(self):
        self.coordinates = app.generate_coordinates(10)
        self.no_duplicates = True
        self.not_near_each_other = True
        self.enough_coordinates = True

    def test_find_circumcenter(self):
        self.assertEqual(app.find_circumcenter([(1,1), (3,5), (7,3)]), (4,2))
        result = app.find_circumcenter([(2,4), (3,-7), (7,-2)])
        x = float(str(result[0])[:5])
        y = float(str(result[1])[:7])
        self.assertEqual(x, 1.377)
        self.assertEqual(y, -1.602)
    
    def test_distance_between_points(self):
        self.assertEqual(app.distance_between_points((1, 1), (5, 1)), 4)
        self.assertEqual(app.distance_between_points((2, 3), (2, -2)), 5)
        self.assertEqual(round(app.distance_between_points((3, 5), (7, 3)), 6), 4.472136)
    
    def test_are_edges_equal(self):
        self.assertTrue(app.are_edges_equal([(3, 4), (7, 6)], [(3, 4), (7, 6)]))
        self.assertTrue(app.are_edges_equal([(3, 4), (7, 6)], [(7, 6), (3, 4)]))
        self.assertFalse(app.are_edges_equal([(3, 4), (7, 6)], [(3, 4), (7, 4)]))
        self.assertFalse(app.are_edges_equal([(3, 4), (7, 6)], [(7, 6), (1, 1)]))
    
    def test_bowyer_watson(self):
        triangulation = app.bowyer_watson([(100, 100), (300, 200), (150, 300)])
        self.assertEqual(len(triangulation), 1)
        triangulation = app.bowyer_watson([(100, 100), (300, 200), (150, 300), (250, 350)])
        self.assertEqual(len(triangulation), 2)
        triangulation = app.bowyer_watson([(100, 100), (300, 200), (150, 300), (250, 350), (400, 125)])
        self.assertEqual(len(triangulation), 4)
        triangulation = app.bowyer_watson([(100, 100), (300, 200), (150, 300), (250, 350), (400, 125), (300, 400)])
        self.assertEqual(len(triangulation), 6)
    
    def test_generate_coordinates(self):
        for coordinate in self.coordinates:
            if self.coordinates.count(coordinate) > 1:
                self.no_duplicates = False
            for other in self.coordinates:
                if coordinate == other:
                    continue
                if app.distance_between_points(coordinate, other) < 100:
                    self.not_near_each_other = False
        if len(self.coordinates) != 10:
            self.enough_coordinates = False
        
        self.assertTrue(self.no_duplicates)
        self.assertTrue(self.not_near_each_other)
        self.assertTrue(self.enough_coordinates)
    
class TestTriangle(unittest.TestCase):
    
    def setUp(self):
        self.triangle_1 = app.Triangle((1, 5), (4, 5), (7, 2))
        self.triangle_2 = app.Triangle((1, 5), (4, 5), (7, 2))
        self.triangle_3 = app.Triangle((2, 6), (8, 10), (5, 16))
    
    def tearDown(self):
        del self.triangle_1
        del self.triangle_2
        del self.triangle_3

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
        self.assertEqual(self.triangle_1.circum_center(), self.triangle_1.circum_center())

    def test_cc_radius(self):
        self.assertEqual(self.triangle_1.cc_radius(), self.triangle_1.cc_radius())

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='results'),
    failfast=False, buffer=False, catchbreak=False, exit=False)