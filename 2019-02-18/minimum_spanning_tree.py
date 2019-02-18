def minimum_spanning_tree(edges):
    # Sort edges by weight
    edges.sort(key=lambda edge: edge[2])
    
    # We'll add edges of the MST to this list.
    mst = []
    
    # We'll add nodes visited by the MST to this set.
    visited = set()
    
    # Finds the edge with the lowest weight that can be added to the MST
    # without creating a cycle, then adds it to the MST and removes it from the
    # `edges` list. Returns False if no edge is found, otherwise returns True.
    def add_best_edge():
        for i, edge in enumerate(edges):
            (a, b, w) = edge
            
            # One of the edges must touch the existing tree and the other
            # edge must be new.
            valid = (a in visited and b not in visited) or (a not in visited and b in visited) or len(visited) == 0
            
            if valid:
                del edges[i]
                mst.append(edge)
                visited.add(a)
                visited.add(b)
                return True
        return False
        
    # Call `add_best_edge` until nothing new can be added.
    while add_best_edge():
        pass
        
    # This creates the minimum spanning tree!
    return mst