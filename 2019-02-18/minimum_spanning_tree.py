def minimum_spanning_tree(edges):
    '''Solves the minimum spanning tree (MST) problem using Prim's algorithm.

    Arguments:
        edges (list of tripples):
            The list of edges forming the graph. Each edge is a tripple
            ``(A, B, W)`` where ``A`` and ``B`` are labels for the nodes
            connected by the edge and ``W`` is the weight of the edge.

    Returns:
        mst (list of tripples):
            An edge list like the input, but only containg the edges of the MST.
    '''
    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])

    # We'll "grow" the MST by appending to this list.
    mst = []

    # We'll keep up with the nodes visited by the MST.
    visited = set()

    # Extend the MST by adding the edge with the lowest weight that touches the
    # tree but does not create a cycle. If the MST is currently empty, this adds
    # the edge with the lowest weight.
    #
    # This returns False if no edge is found and True otherwise.
    def grow_mst():
        for i, edge in enumerate(edges):
            (a, b, w) = edge

            # One of the nodes must touch the existing tree and the other
            # node must be new, or the tree must be empty.
            valid = (a in visited and b not in visited) or \
                    (a not in visited and b in visited) or \
                    len(mst) == 0

            if valid:
                del edges[i]
                mst.append(edge)
                visited.add(a)
                visited.add(b)
                return True

        return False

    # Call `grow_mst` until nothing new can be added.
    while grow_mst():
        pass

    # This creates the minimum spanning tree!
    return mst
