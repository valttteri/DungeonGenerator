from classes.triangleclass import Triangle
import tools

super_coordinates = [(-10, -400), (1500, 300), (-10, 1200)]

def bowyer_watson(nodelist: list, display):
    """
    Bowyer-Watson algorithm for generating a Delaunay triangulation. Steps:

    1. Create an empty list for the triangulation. Create a 'super triangle'
    i.e. a triangle which is large enough to contain every single node inside it.
    Add the super triangle into the triangulation.

    2. Start the process of adding each node into the triangulation

    3. Check if the node is inside one or more circumcircles.
    All triangles which have a node inside their circumcircle are now 'bad' triangles.

    4. Go through each triangle in bad_triangles. If a triangle has an edge
    which is not shared with another triangle, add it to the list named "polygon".

    5. Remove each bad triangle from the triangulation.

    6. Create a new triangle between the node and every edge in the list polygon.

    7. Check if there are triangles in the triangulation that share a node
    or an edge with the original super triangle. If so, remove these triangles.
    """
    # Step 1.
    triangulation = []
    super_triangle = Triangle(
        super_coordinates[0], super_coordinates[1], super_coordinates[2], display
    )
    super_triangle_nodes = []

    # super_triangle_edges = super_triangle.show_edges()
    super_triangle_nodes = super_triangle.show_nodes()

    triangulation.append(super_triangle)

    # Step 2.
    for node in nodelist:
        bad_triangles = []

        # Step 3.
        for triangle in triangulation:
            circumcenter = triangle.circum_center()
            circum_circles_radius = triangle.cc_radius()

            distance = tools.distance_between_points(node, circumcenter)
            if distance <= circum_circles_radius:
                bad_triangles.append(triangle)

        polygon = []

        # Step 4.
        for bad_triangle in bad_triangles:
            edges = bad_triangle.show_edges()
            for edge in edges:
                found = False
                for other_triangle in bad_triangles:
                    other_triangles_edges = other_triangle.show_edges()
                    if bad_triangle == other_triangle:
                        continue

                    for other_edge in other_triangles_edges:
                        if tools.are_edges_equal(other_edge, edge):
                            found = True
                if not found:
                    polygon.append(edge)

        # Step 5.
        for bad_triangle in bad_triangles:
            triangulation.remove(bad_triangle)

        # Step 6.
        for edge in polygon:
            new_triangle = Triangle(edge[0], edge[1], node, display)
            triangulation.append(new_triangle)

    # Step 7.
    remove_triangles = []
    for triangle in triangulation:
        nodes = triangle.show_nodes()
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