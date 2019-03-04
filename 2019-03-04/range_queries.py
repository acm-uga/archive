class SegmentTree:
    def __init__(self, root, left, right, lo, hi):
        self.root = root
        self.left = left
        self.right = right
        self.lo = lo
        self.hi = hi

    def __str__(self):
        return f'({self.root} {self.left} {self.right})'

    def min(self, lo, hi):
        if lo <= self.lo and self.hi <= hi:
            return self.root

        if self.left is not None and lo <= self.left.hi:
            left_val = self.left.min(lo, hi)
        else:
            left_val = float('inf')

        if self.right is not None and self.right.lo <= hi:
            right_val = self.right.min(lo, hi)
        else:
            right_val = float('inf')

        return min(left_val, right_val)

    @classmethod
    def from_list(cls, data):
        # Sanity check
        if len(data) == 0:
            return None

        # Convert data into leaf nodes
        nodes = []
        for i, val in enumerate(data):
            node = SegmentTree(root=val, left=None, right=None, lo=i, hi=i)
            nodes.append(node)

        # Combine nodes pairwise until the entire tree is built.
        while 1 < len(nodes):
            i = 1
            next_nodes = []
            while i < len(nodes):
                left = nodes[i-1]
                right = nodes[i]
                root = min(left.root, right.root)
                node = SegmentTree(root, left, right, lo=left.lo, hi=right.hi)
                next_nodes.append(node)
                i += 2
            if i == len(nodes):
                # one remaining node didn't get combined
                next_nodes.append(nodes[i-1])
            nodes = next_nodes

        # ``nodes`` only contains a single tree.
        return nodes[0]


def test_segment_tree():
    data = [5, 8, 1, 7, 4, 2, 3, 7, 5, 0]
    tree = SegmentTree.from_list(data)

    assert tree.min(0, 0) == 5
    assert tree.min(1, 1) == 8
    assert tree.min(2, 2) == 1
    assert tree.min(3, 3) == 7
    assert tree.min(4, 4) == 4
    assert tree.min(5, 5) == 2
    assert tree.min(6, 6) == 3
    assert tree.min(7, 7) == 7
    assert tree.min(8, 8) == 5
    assert tree.min(9, 9) == 0

    assert tree.min(0, 1) == 5
    assert tree.min(1, 2) == 1
    assert tree.min(2, 3) == 1
    assert tree.min(3, 4) == 4
    assert tree.min(4, 5) == 2
    assert tree.min(5, 6) == 2
    assert tree.min(6, 7) == 3
    assert tree.min(7, 8) == 5
    assert tree.min(8, 9) == 0
