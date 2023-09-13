#right now I'm trying to create a successful triangulation with bowyer-watson algorithm with my program
#at the moment the program plots a single triangle and a circle around it

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
    def __init__(self, node_a: tuple, node_b: tuple, node_c: tuple):
        self.node_a = node_a
        self.node_b = node_b
        self.node_c = node_c
        self.circumcenter = findCircumcenter([self.node_a, self.node_b, self.node_c])
        self.circum_circles_radius = distanceBetweenPoints(self.circumcenter, self.node_a)

        self.edges = [[self.node_a, self.node_b],
                      [self.node_b, self.node_c],
                      [self.node_c, self.node_a]]

    def plot(self):
        for e in self.edges:
            pygame.draw.line(display, GREEN, e[0], e[1])

    def circumCircle(self):
        pygame.draw.circle(display, RED, self.circumcenter, radius=self.circum_circles_radius, width=2)

#def plotCircumcircle(coordinates: list):
#    centerpoint = findCircumcenter(coordinates)
#    radius = distanceBetweenPoints(centerpoint, coordinates[0])
#
#    pygame.draw.circle(display, RED, centerpoint, radius=radius, width=2)

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

def bowyerWatson(coordinates: list):
    triangulation = []

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