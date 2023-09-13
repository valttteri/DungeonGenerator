#right now I'm trying to create a successful triangulation with bowyer-watson algorithm with my program
#at the moment the program plots a single triangle and a circle around it
import itertools
import pygame
from random import *
from math import *

pygame.init()

displayWidth = 1000
displayHeight = 600
display = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption('Welcome to the Dungeon')

counter = 3
x_min = 300
x_max = displayWidth-300
y_min = 200
y_max = displayHeight-200
displayCenter = (displayWidth/2, displayHeight/2)
super_coordinates = [(150, -100), (950, 300), (150, 700)]

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

        self.edges = [[self.node_a, self.node_b],
                      [self.node_b, self.node_c],
                      [self.node_c, self.node_a]]
    
    def __str__(self):
        return f"Triangle number {self.id}"
    
    def __repr__(self):
        return f'Triangle with edges {self.edges}'

    def __eq__(self, other): 
        if not isinstance(other, Triangle):
            #don't attempt to compare against unrelated types
            return 'triangles only'

        return self.id == other.id
    
    def showID(self):
        return self.id

    def edges(self):
        return self.edges

    def circumCenter(self):
        return self.circumcenter
    
    def ccRadius(self):
        return self.circum_circles_radius
    
    def plot(self):
        for e in self.edges:
            pygame.draw.line(display, GREEN, e[0], e[1])

    def circumCircle(self):
        pygame.draw.circle(display, RED, self.circumcenter, radius=self.circum_circles_radius, width=2)

#plot a single triangle
def plotATriangle(coordinates: list):
    for i in range(len(coordinates)):
        next = i+1

        if next == len(coordinates):
            pygame.draw.line(display, GREEN, coordinates[i], coordinates[0])
        else:
            pygame.draw.line(display, GREEN, coordinates[i], coordinates[next])

#plot center points of triangles edges
#not sure if this was necessary to make
def plotCenterPoints(coordinates: list):
    for i in range(len(coordinates)):
        next = i+1
    
        if next == len(coordinates):
            center_point_x = (coordinates[i][0]+coordinates[0][0])/2
            center_point_y = (coordinates[i][1]+coordinates[0][1])/2

            pygame.draw.circle(display, RED, (center_point_x, center_point_y), 3)
        else:
            center_point_x = (coordinates[i][0]+coordinates[next][0])/2
            center_point_y = (coordinates[i][1]+coordinates[next][1])/2

            pygame.draw.circle(display, RED, (center_point_x, center_point_y), 3)

#coordinates = [((randint(100, displayWidth-100), (randint(100, displayHeight-100)))) for i in range(counter)]
#coordinates = [(178, 169), (585, 179), (513, 393)]
#print(coordinates)

#find cartesian coordinates of the circumcenter of a triangle
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

#draw a circle around a triangle
def plotCircumcircle(coordinates: list):
    centerpoint = findCircumcenter(coordinates)
    radius = distanceBetweenPoints(centerpoint, coordinates[0])

    pygame.draw.circle(display, RED, centerpoint, radius=radius, width=2)

#calculate the distance between two points
def distanceBetweenPoints(a: tuple, b: tuple):
    distance = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
    return distance

#generate coordinates in a way to avoid duplicates
def generateCoordinates(count: int):
    coordinates = []
                
    while len(coordinates) < count:
        x = randint(x_min, x_max)
        y = randint(y_min, y_max)
        candidate = (x, y)

        if candidate not in coordinates:
            coordinates.append(candidate)
    
    return coordinates

def areEdgesEqual(edge_1: list, edge_2: list):
    return edge_1[0] == edge_2[0] and edge_1[1] == edge_2[1] or edge_1[0] == edge_2[1] and edge_1[1] == edge_2[0]

def bowyerWatson(nodelist: list):
    triangulation = []

    #algorithm part1
    super_triangle = Triangle(super_coordinates[0], super_coordinates[1], super_coordinates[2])
    super_triangle_nodes = []

    super_triangle_edges = super_triangle.edges
    for edge in super_triangle_edges:
        super_triangle_nodes.append(edge[0])
    print(super_triangle_nodes)
    #tri2 = Triangle((1, 4), (10, 10), (100, 100))
    #tri3 = Triangle((1, 4), (10, 10), (100, 100))
    #print(tri2.edges)
    #print(areEdgesEqual(tri2.edges[1], tri2.edges[1]))

    triangulation.append(super_triangle)
    #triangulation.append(tri2)
    #triangulation.append(tri3)
    #print(triangulation)
    #print(triangulation[1] == tri2)

    for node in nodelist:

        badTriangles = []

        for triangle in triangulation:
            circumcenter = triangle.circumCenter()
            circum_circles_radius = triangle.ccRadius()

            #algorithm part 2: distance between the triangles circumcenter and the node
            distance = distanceBetweenPoints(node, circumcenter)
            if distance < circum_circles_radius:
                badTriangles.append(triangle)
                #print(f'distance between {circumcenter} and {node} is {distance} which is less than {circum_circles_radius}')
            
        polygon = []
        #algorithm part 3: define the polygonal hole
        for triangle in badTriangles:
            print(f'part 3 for {triangle}')
            edges = triangle.edges
            for edge in edges:
                print(f'looking at edge {edge}')
                found = False
                
                for otherTriangle in badTriangles:
                    print(f'comparing edge {edge} to {otherTriangle}')
                    other_triangles_edges = otherTriangle.edges
                    if otherTriangle == triangle:
                        continue

                    for other_edge in other_triangles_edges:
                        if areEdgesEqual(other_edge, edge):
                            print(f'similar edges {edge} and {other_edge}')
                            found = True
                if not found:
                    print(f'adding edge {edge} to polygon')
                    polygon.append(edge)
        print(f'polygon: {polygon}')

        for triangle in triangulation:
            if triangle in badTriangles:
                #print(triangulation)
                print('this triangle is bad')
                triangulation.remove(triangle)
                print(f'triangulation after deletion: {triangulation}')
        
        for edge in polygon:
            newTriangle = Triangle(edge[0], edge[1], node)
            print(f'new triangle is {newTriangle}')
            triangulation.append(newTriangle)
    
    for triangle in triangulation:
        edges = triangle.edges
        found = False
        for edge in edges:
            if found:
                continue
            if edge[0] in super_triangle_nodes or edge[1] in super_triangle_nodes:
                triangulation.remove(triangle)
                found = True
                
    return triangulation



bowyerWatson(generateCoordinates(3))

'''
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))

    coordinates = generateCoordinates(counter)

    for c in coordinates:
        pygame.draw.circle(display, BLUE, c, 2)

    t = Triangle(super_coordinates[0], super_coordinates[1], super_coordinates[2])
    t.plot()
    t.circumCircle()

    #area where points can be plotted
    pygame.draw.line(display, RED, (x_min, y_min), (x_max, y_min))
    pygame.draw.line(display, RED, (x_min, y_min), (x_min, y_max))
    pygame.draw.line(display, RED, (x_min, y_max), (x_max, y_max))
    pygame.draw.line(display, RED, (x_max, y_min), (x_max, y_max))

    #pygame.draw.circle(display, BLUE, displayCenter, 2)

    #plotATriangle(coordinates)
    #plotCircumcircle(coordinates)

    pygame.display.flip()
    pygame.time.wait(500)
'''