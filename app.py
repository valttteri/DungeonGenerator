'''
At the moment this program visualises Delaunay triangulation with Bowyer-Watson algorithm.
The algorithm doesn't work if the the nodes end up forming an approximately straight line.
In this case it returns an empty list. I don't know if there is a way to fix this problem.
With larger inputs (about 10+ nodes) the algorithm appears to work 99% of the time.
The variable "node_count" equals to the number of nodes given to the algorithm.

In order to run the tests, comment out the three lines under the variable display_height
and the while-loop on the bottom of the file.
'''

import itertools
import pygame
from random import *
from math import *
from prim import primsAlgorithm, findNearestNode, plotMST

display_width = 800
display_height = 400

#comment out the following three lines for testing
pygame.init()
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Welcome to the Dungeon')

#node_count equals to the number of nodes given to the algorithm
node_count = 20
x_min = 100
x_max = display_width-100
y_min = 50
y_max = display_height-50
display_center = (display_width/2, display_height/2)

'''
Hard coded coordinates for the super triangle. I might add a function for randomly generating
a super triangle later.
'''
super_coordinates = [(-10, -400), (1500, 300), (-10, 1200)]

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Triangle():
    new_id = itertools.count()
    def __init__(self, node_a: tuple, node_b: tuple, node_c: tuple):
        self.node_a = node_a
        self.node_b = node_b
        self.node_c = node_c

        self.id = next(self.new_id)
        self.circumcenter = findCircumcenter([self.node_a, self.node_b, self.node_c])
        self.circum_circles_radius = distanceBetweenPoints(self.circumcenter, self.node_a)

        self.nodes = [self.node_a, self.node_b, self.node_c]

        self.triangle_edges = [[self.node_a, self.node_b],
                                [self.node_b, self.node_c],
                                [self.node_c, self.node_a]]
    
    def __str__(self):
        return f'Triangle with edges {self.triangle_edges}'
    
    def __repr__(self):
        return f'Triangle with edges {self.triangle_edges}'

    def __eq__(self, other): 
        if not isinstance(other, Triangle):
            return 'triangles only'

        return self.id == other.id
    
    def showID(self):
        return self.id

    def showEdges(self):
        return self.triangle_edges
    
    def showNodes(self):
        return self.nodes

    def circumCenter(self):
        return self.circumcenter
    
    def ccRadius(self):
        return self.circum_circles_radius
    
    def plot(self):
        for e in self.triangle_edges:
            pygame.draw.line(display, GREEN, e[0], e[1])

    def circumCircle(self):
        pygame.draw.circle(display, RED, self.circumcenter, radius=self.circum_circles_radius, width=2)

'''
Find cartesian coordinates of a triangle's circumcenter.
I found the formula from this website: https://en.wikipedia.org/wiki/Circumcircle
'''
def findCircumcenter(coordinates: list):
    ax = coordinates[0][0]
    ay = coordinates[0][1]
    bx = coordinates[1][0]
    by = coordinates[1][1]
    cx = coordinates[2][0]
    cy = coordinates[2][1]
    
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    ux = ((ax * ax + ay * ay) * (by - cy) + (bx * bx + by * by) * (cy - ay) + (cx * cx + cy * cy) * (ay - by)) / d
    uy = ((ax * ax + ay * ay) * (cx - bx) + (bx * bx + by * by) * (ax - cx) + (cx * cx + cy * cy) * (bx - ax)) / d
    return ux, uy

#Plot a triangle's circumcircle
def plotCircumcircle(coordinates: list):
    centerpoint = findCircumcenter(coordinates)
    radius = distanceBetweenPoints(centerpoint, coordinates[0])

    pygame.draw.circle(display, RED, centerpoint, radius=radius, width=2)

#Calculate the distance between two points
def distanceBetweenPoints(a: tuple, b: tuple):
    distance = sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
    return distance

#Generate coordinates in a way to avoid duplicates
def generateCoordinates(count: int):
    coordinates = []
                
    while len(coordinates) < count:
        x = randint(x_min, x_max)
        y = randint(y_min, y_max)
        candidate = (x, y)

        if candidate not in coordinates:
            coordinates.append(candidate)
    
    g=[(448, 339),
        (226, 167),
        (269, 292),
        (100, 341),
        (105, 243),
        (690, 269)]
    
    return coordinates

#Check if two separate triangles have a common edge
def areEdgesEqual(edge_1: list, edge_2: list):
    return (edge_1[0] == edge_2[0] and edge_1[1] == edge_2[1]) or (edge_1[0] == edge_2[1] and edge_1[1] == edge_2[0])

'''
Bowyer-Watson algorithm for generating a Delaunay triangulation. Steps:

1. Create an empty list for the triangulation. Create a 'super triangle' i.e. a triangle which is large enough to contain every single node inside it.
Add the super triangle into the triangulation.

2. Start the process of adding each node into the triangulation

3. Check if the node is inside one or more circumcircles. All triangles which have a node inside their circumcircle are now 'bad' triangles.

4. Go through each triangle in bad_triangles. If a triangle has an edge which is not shared with another triangle, add it to the list named "polygon".

5. Remove each bad triangle from the triangulation.

6. Create a new triangle between the node and every edge in the list polygon.

7. Check if there are triangles in the triangulation that share a node or an edge with the original super triangle. If so, remove these triangles.
'''
def bowyerWatson(nodelist: list):
    #Step 1.
    triangulation = []
    super_triangle = Triangle(super_coordinates[0], super_coordinates[1], super_coordinates[2])
    super_triangle_nodes = []

    super_triangle_edges = super_triangle.showEdges()
    super_triangle_nodes = super_triangle.showNodes()

    triangulation.append(super_triangle)

    #Step 2.
    for node in nodelist:

        bad_triangles = []

        #Step 3.
        for triangle in triangulation:
            circumcenter = triangle.circumCenter()
            circum_circles_radius = triangle.ccRadius()

            distance = distanceBetweenPoints(node, circumcenter)
            if distance <= circum_circles_radius:
                bad_triangles.append(triangle)
                        
        polygon = []

        #Step 4.
        for bad_triangle in bad_triangles:
            edges = bad_triangle.showEdges()
            for edge in edges:
                found = False
                for other_triangle in bad_triangles:
                    other_triangles_edges = other_triangle.showEdges()
                    if bad_triangle == other_triangle:
                        continue

                    for other_edge in other_triangles_edges:
                        if areEdgesEqual(other_edge, edge):
                            found = True
                if not found:
                    polygon.append(edge)

        #Step 5.
        for bad_triangle in bad_triangles:
            triangulation.remove(bad_triangle)
        
        #Step 6.
        for edge in polygon:
            newTriangle = Triangle(edge[0], edge[1], node)
            triangulation.append(newTriangle)
    
    #Step 7.
    remove_triangles = []
    for triangle in triangulation:
        nodes = triangle.showNodes()
        found = False
        for n in nodes:
            if found:
                continue
            if n in super_triangle_nodes:
                found = True
                remove_triangles.append(triangle)
    for triangle in remove_triangles:
        triangulation.remove(triangle)

    return triangulation

#visualising with pygame
#comment out the entire loop for testing
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))

    coordinates = generateCoordinates(node_count)

    for c in coordinates:
        pygame.draw.circle(display, BLUE, c, 4)

    t = Triangle(super_coordinates[0], super_coordinates[1], super_coordinates[2])
    t.plot()

    triangulation = bowyerWatson(coordinates)
    minimum_spanning_tree = primsAlgorithm(triangulation)
    pygame.draw.circle(display, RED, minimum_spanning_tree[-1], 5)


    for triangle in triangulation:
        triangle.plot()

    pygame.display.flip()
    pygame.time.wait(2000)

    display.fill((0, 0, 0))
    for c in coordinates:
        pygame.draw.circle(display, BLUE, c, 4)
    pygame.draw.circle(display, RED, minimum_spanning_tree[-1], 5)

    plotMST(minimum_spanning_tree, display)

    #print(findNearestNode(mst, mst[-1]))
    
    pygame.display.flip()
    pygame.time.wait(4000)
