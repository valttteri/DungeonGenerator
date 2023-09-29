import tools

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


def prims_algorithm(triangulation: dict):
    """
    Prim's algorithm for creating a minimum spanning tree based on a triangulation. 
    I had to improvise a little in order to get this to work and therefore the code 
    is probably not very readable.
    """
    #remove all duplicate edges from the triangulation
    tuples = tools.unique_edges(triangulation)
    #create a graph based on the triangulation
    graph = tools.create_graph(tuples)

    minimum_spanning_tree = []

    #starting node is always the first one in the list
    starting_node = list(graph.keys())[0]

    #empty data structure to keep track of the edges we need to examine
    edges = {}

    """
    the edges will be stored in tuples a way that their parent node is 
    on the first spot and the distance to the parent on the second spot
    in this case: parent=starting_node, distance=n[1]
    """
    for n in graph[starting_node]:
        edges[n[0]] = (starting_node, n[1])

    #start filling the minimum spanning tree one node at a time
    while len(minimum_spanning_tree) < len(graph)-1:
        #find the shortest edge
        min_edge = tools.find_minimum_edge(edges)

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
    print(tools.find_removed_edges(mst, tuples))
