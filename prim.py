from math import *
from heapq import *
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#tuples = [((448, 339), (226, 167)),
#        ((269, 292), (100, 341)),
#        ((448, 339), (100, 341)),
#        ((100, 341), (105, 243)),
#        ((105, 243), (269, 292)),
#        ((226, 167), (690, 269)),
#        ((690, 269), (448, 339)),
#        ((448, 339), (269, 292)),
#        ((100, 341), (269, 292)),
#        ((226, 167), (448, 339)),
#        ((105, 243), (226, 167)),
#        ((269, 292), (226, 167)),
#        ((269, 292), (105, 243)),
#        ((226, 167), (269, 292)),
#        ((269, 292), (448, 339))]

def uniqueEdges(triangles: list):
    edge_list=set()

    for t in triangles:
        edges = t.showEdges()
        for e in edges:
            edge_list.add((e[0], e[1]))
    
    return edge_list

def distanceBetweenNodes(a: tuple, b: tuple):
    distance = sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
    return distance

def createGraph(tuples: list):
    graph = {}

    for tuple in tuples:
        if tuple[0] not in graph:
            graph[tuple[0]] = []
        if tuple[1] not in graph:
            graph[tuple[1]] = []

    #for g in graph:
    #    print(g)

    for edge in tuples:
        distance = round(distanceBetweenNodes(edge[1], edge[0]), 3)
        if len(graph[edge[0]]) == 0:
            graph[edge[0]].append([edge[1], distance])
        else:
            found = False
            for node in graph[edge[0]]:
                if node[0] == edge[1]:
                    found = True
            if not found:
                graph[edge[0]].append([edge[1], distance])

        if len(graph[edge[1]]) == 0:
            graph[edge[1]].append([edge[0], distance])
        else:
            found = False
            for node in graph[edge[1]]:
                if node[0] == edge[0]:
                    found = True
            if not found:
                graph[edge[1]].append([edge[0], distance])
    
    return graph

def findMinimumEdge(edges: list):
    min_edge = None
    min_weight = 10**10
    for node in edges:
        if edges[node] < min_weight:
            min_edge = node
            min_weight = edges[node]
    
    return min_edge, min_weight

def primsAlgorithm(triangulation: dict):
    tuples = uniqueEdges(triangulation)
    graph = createGraph(tuples)

    minimum_spanning_tree = []
    starting_node = list(graph.keys())[0]
    
    minimum_spanning_tree.append(starting_node)
    edges = {}

    for n in graph[starting_node]:
        edges[n[0]] = n[1] 

    while len(minimum_spanning_tree) < len(graph):
        min_edge, min_weight = findMinimumEdge(edges)
        
        minimum_spanning_tree.append(min_edge)

        for node in graph[min_edge]:
            if node[0] not in minimum_spanning_tree:
                edges[node[0]] = node[1]

        del edges[min_edge]

    return minimum_spanning_tree

def findNearestNode(coordinates: list, node: tuple):
    min_distance = 10**10
    nearest_node = None
    for c in coordinates:
        if c == node:
            continue
        if distanceBetweenNodes(c, node) < min_distance:
            min_distance = distanceBetweenNodes(c, node)
            nearest_node = c
    
    return nearest_node

def plotMST(coordinates: list, display):

    for i in range(len(coordinates)-1):

        #if i == len(coordinates):
        #    nearest_node = findNearestNode(coordinates, coordinates[-1])
        #    pygame.draw.line(display, GREEN, nearest_node, coordinates[-1])
        #else:
        pygame.draw.line(display, GREEN, coordinates[i], coordinates[i+1])

