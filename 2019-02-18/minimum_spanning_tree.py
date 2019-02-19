def minimum_spanning_tree(edges):
    '''Solves the minimum spanning tree (MST) problem using Prim's algorithm.

    This algorithm "grows" the tree by starting with the smallest edge and then
    iterativly adding the smallest edge that extends the tree without creating
    a cycle.

    Our version simply sorts the edges by weight and linearly searches the list
    for the first edge it can add. Since we're searching the list every time,
    this algorithm has a time complexity in ``O(e^2)`` where ``e`` is the
    number of edges. In practice, this is fine for small graphs (a few hundred
    edges), but it can be a problem for large graphs.

    You can improve the time complexity by using a min-heap of unvisited nodes
    ordered by the smallest edge that connects it to the tree (or infinity if
    no such edge exists). As you add nodes/edges to the tree, you update the
    heap. (You'd also want a map from nodes to the set of edges involving that
    node). This can bring your time complexity down to ``O(e * log(n))`` where
    ``n`` is the number of nodes. This version is left as an exercise to the
    reader.

    Arguments:
        edges (list of edges):
            The list of edges forming the graph. Each edge is a tripple
            ``(A, B, W)`` where ``A`` and ``B`` are labels for the nodes
            connected by the edge and ``W`` is the weight of the edge.

    Returns:
        tree (list of edges):
            The minimum spanning tree of the input graph. It is an edge list
            like the input, but only containg the edges of the MST.
    '''
    # Sort edges by weight.
    edges.sort(key=lambda edge: edge[2])

    # We "grow" the tree by appending to this list.
    tree = []

    # We also keep up with the nodes visited by the tree as a hash-set.
    # This lets us check if adding an edge creates a cycle in constant time.
    visited = set()

    # Extend the tree by adding the smallest edge that extends the tree without
    # creating a cycle. If the tree is currently empty, this adds the edge with
    # the lowest weight.
    #
    # This returns False if no acceptable edge is found and True otherwise.
    def grow_tree():
        for i, edge in enumerate(edges):
            (a, b, w) = edge

            # One of the nodes must touch the existing tree and the other
            # node must be new, or the tree must be empty.
            valid = (a in visited and b not in visited) or \
                    (a not in visited and b in visited) or \
                    len(tree) == 0

            # As soon as we find a valid edge, we add it to the graph and exit.
            # This is why the algorithm is called "greedy".
            if valid:
                del edges[i]
                tree.append(edge)
                visited.add(a)
                visited.add(b)
                return True

        return False

    # Call `grow_tree` until nothing new can be added.
    while grow_tree():
        pass

    # This creates the minimum spanning tree!
    return tree


def test_mst():
    # The example graph from Wikipedia:
    # https://en.wikipedia.org/wiki/Minimum_spanning_tree
    # https://upload.wikimedia.org/wikipedia/commons/d/d2/Minimum_spanning_tree.svg
    edges = [
        (0, 1, 6),  (0, 2, 3),  (0, 3, 9),
        (1, 2, 4),  (1, 4, 2),  (1, 5, 9),
        (2, 4, 2),  (2, 3, 9),  (2, 6, 9),
        (3, 6, 8),  (3, 7, 18), (4, 5, 9),
        (4, 6, 8),  (5, 6, 7),  (5, 8, 4),
        (5, 9, 5),  (6, 7, 10), (6, 9, 9),
        (7, 8, 4),  (7, 9, 3),  (8, 9, 1)
    ]

    soln = [
        (0, 2, 3),
        (1, 4, 2),
        (2, 4, 2),
        (3, 6, 8),
        (4, 6, 8),
        (5, 6, 7),
        (5, 8, 4),
        (7, 9, 3),
        (8, 9, 1)
    ]

    # Compare the output of our function and the solution as sets,
    # since the order of edges does not matter.
    mst = minimum_spanning_tree(edges)
    assert set(soln) == set(mst)
