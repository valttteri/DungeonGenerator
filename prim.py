from math import *
from heapq import *
from random import *

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

tuples = [
    ((491, 173), (674, 166)),
    ((388, 324), (361, 223)),
    ((674, 166), (658, 185)),
    ((491, 173), (549, 268)),
    ((658, 185), (549, 268)),
    ((361, 223), (491, 173)),
    ((549, 268), (388, 324)),
    ((491, 173), (658, 185))
]

'''
This function removes all duplicate edges from a triangulation.
'''
def unique_edges(triangles: list):
    edge_list=set()

    for t in triangles:
        edges = t.show_edges()
        for e in edges:
            if (e[0], e[1]) in edge_list or (e[1], e[0]) in edge_list:
                continue
            edge_list.add((e[0], e[1]))
    
    return edge_list

def distance_between_nodes(a: tuple, b: tuple):
    distance = sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
    return round(distance, 3)

def create_graph(tuples: list):
    graph = {}

    for tuple in tuples:
        if tuple[0] not in graph:
            graph[tuple[0]] = []
        if tuple[1] not in graph:
            graph[tuple[1]] = []

    for edge in tuples:
        distance = distance_between_nodes(edge[1], edge[0])
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

def find_minimum_edge(edges: list):
    min_edge = None
    min_weight = 10**10
    for node in edges:
        if edges[node][1] < min_weight:
            min_edge = (edges[node][0], node)
            min_weight = edges[node][1]
    
    return min_edge

#Return some of the removed edges in order to create alternate routes
def find_removed_edges(mst: list, edges: list):
    removed = []

    for edge in edges:
        lottery_number = randint(0, 100)
        valid = True
        if edge in mst:
            valid = False
        if (edge[1], edge[0]) in mst:
            valid = False
        if lottery_number < 87:
            valid = False
        if valid:
            removed.append(edge)
    
    return removed

'''
Prim's algorithm for creating a minimum spanning tree based on a triangulation. I had to improvise a little in order to get
this to work and therefore the code is probably not very readable.
'''
def prims_algorithm(triangulation: dict):
    #remove all duplicate edges from the triangulation
    tuples = unique_edges(triangulation)
    #create a graph based on the triangulation
    graph = create_graph(tuples)

    minimum_spanning_tree = []

    #starting node is always the first one in the list
    starting_node = list(graph.keys())[0]
    
    #empty data structure to keep track of the edges we need to examine
    edges = {}

    '''
    the edges will be stored in tuples a way that their parent node is 
    on the first spot and the distance to the parent on the second spot
    in this case: parent=starting_node, distance=n[1]
    '''
    for n in graph[starting_node]:
        edges[n[0]] = (starting_node, n[1])
    
    #start filling the minimum spanning tree one node at a time
    while len(minimum_spanning_tree) < len(graph)-1:
        #find the shortest edge
        min_edge = find_minimum_edge(edges)

        minimum_spanning_tree.append(min_edge)

        #check if the node (short edges ending node) has any child nodes in the
        #minimum spanning tree
        for node in graph[min_edge[1]]:
            found = False
            for edge in minimum_spanning_tree:
                if node[0] == edge[0] or node[0] == edge[1]:
                    found = True

            #add a new edge if the node was not found
            if not found:
                edges[node[0]] = (min_edge[1], node[1])

        del edges[min_edge[1]]

    return minimum_spanning_tree

if __name__ == '__main__':
    mst = prims_algorithm(tuples)
    print(mst)
    print(find_removed_edges(mst, tuples))