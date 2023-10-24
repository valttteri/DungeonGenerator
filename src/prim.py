import tools

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Hard coded edges for testing
t = [
    ((491, 173), (674, 166)),
    ((388, 324), (361, 223)),
    ((674, 166), (658, 185)),
    ((491, 173), (549, 268)),
    ((658, 185), (549, 268)),
    ((361, 223), (491, 173)),
    ((549, 268), (388, 324)),
    ((491, 173), (658, 185))
]


def prims_algorithm(triangulation: list):
    """
    Prim's algorithm for creating a minimum spanning tree based on a triangulation. 

    Keyword arguments:
        triangulation (list) -- array containing triangle objects i.e. the Delaunay triangulation

    Returns:
        minimum_spanning_tree (list) -- array containing edges i.e. the minimum spanning tree 
    """
    #Remove all duplicate edges from the triangulation and create a graph
    tuples = tools.unique_edges(triangulation)
    graph = tools.create_graph(tuples)

    minimum_spanning_tree = []
    starting_node = list(graph.keys())[0]
    edges = {}

    #the edges will be stored in tuples a way that their parent node is
    #on the first spot and the distance to the parent on the second spot
    #in this case: parent=starting_node, distance=n[1]

    for n in graph[starting_node]:
        edges[n[0]] = (starting_node, n[1])

    #start filling the minimum spanning tree one node at a time
    while len(minimum_spanning_tree) < len(graph)-1:
        #find the shortest edge
        min_edge = find_minimum_edge(edges)
        minimum_spanning_tree.append(min_edge)

        #check if the node (short edge's ending node) has any child nodes in the
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

def find_minimum_edge(edges: dict):
    """This function finds the shortest edge from a graph"""
    min_edge = None
    min_weight = 10**10
    for node in edges:
        if edges[node][1] < min_weight:
            min_edge = (edges[node][0], node)
            min_weight = edges[node][1]

    return min_edge

if __name__ == '__main__':
    mst = prims_algorithm(t)
    print(mst)
