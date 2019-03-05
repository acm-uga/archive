class MinSegmentTree:
    '''A segment tree for minimum lookups.

    A min segment tree represents a sequence and provides a method efficiently
    query the minimum value of any subsequence. The runtime of this query is
    in ``O(log(n))`` where ``n`` is the size of the sequence.

    The leaf nodes of the tree contain the sequence, and each branch node
    contains the minimum value amongst its descendants.
    '''

    def __init__(self, root, left, right, lo, hi):
        '''Construct a minimum segment tree from a root value, left and right
        subtrees, and the lower and upper indices of the subsequence represented
        by the tree.

        This method **does not** check the validity of the tree. Use the
        classmethod ``MinSegmentTree.from_list`` to construct a valid min
        segment tree for any iterable.

        Arguments:
            root (any):
                The minimum value of the subsequence represented by this tree.
            left (MinSegmentTree or None):
                The left subtree.
            right (MinSegmentTree or None):
                The right subtree.
            lo (int):
                The index of the first element in the subsequence represented
                by this tree.
            hi (int):
                The index of the last element in the subsequence represented
                by this tree.
        '''
        self.root = root
        self.left = left
        self.right = right
        self.lo = lo
        self.hi = hi

    def min(self, lo, hi):
        '''Get the minimum value between indicies ``lo`` and ``hi`` inclusive.

        If ``lo`` is less than the lower index of this tree, it is rounded up
        to that index. Likewise if ``hi`` is greater than the upper index of
        this tree, it is rounded down.

        Arguments:
            lo (int):
                The lower index of the query, inclusive.
            hi (int):
                The upper index of the query, inclusive.
        '''
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
        '''Construct a balanced min segment tree for data in a list.

        This method works bottom-up by turning each element in ``data`` into a
        leaf node then iteratively combining pairs of nodes until only one node
        remains, the root node.

        Arguments:
            data (iterable):
                The sequence for which the segment tree is built.

        Returns:
            MinSegmentTree:
                A min segment tree over ``data``.
        '''
        # Sanity check.
        if len(data) == 0:
            return None

        # Convert data into leaf nodes.
        nodes = []
        for i, val in enumerate(data):
            node = MinSegmentTree(root=val, left=None, right=None, lo=i, hi=i)
            nodes.append(node)

        # Combine nodes pairwise until the entire tree is built.
        while 1 < len(nodes):
            i = 1
            next_nodes = []
            while i < len(nodes):
                left = nodes[i-1]
                right = nodes[i]
                root = min(left.root, right.root)
                node = MinSegmentTree(root, left, right, lo=left.lo, hi=right.hi)
                next_nodes.append(node)
                i += 2
            if i == len(nodes):
                # One remaining node didn't get combined.
                next_nodes.append(nodes[i-1])
            nodes = next_nodes

        # ``nodes`` only contains a single node, the root.
        return nodes[0]


def test_segment_tree():
    data = [5, 8, 1, 7, 4, 2, 3, 7, 5, 0]
    tree = MinSegmentTree.from_list(data)

    # Exhaustivly test all subsequences.
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

    assert tree.min(0, 2) == 1
    assert tree.min(1, 3) == 1
    assert tree.min(2, 4) == 1
    assert tree.min(3, 5) == 2
    assert tree.min(4, 6) == 2
    assert tree.min(5, 7) == 2
    assert tree.min(6, 8) == 3
    assert tree.min(7, 9) == 0

    assert tree.min(0, 3) == 1
    assert tree.min(1, 4) == 1
    assert tree.min(2, 5) == 1
    assert tree.min(3, 6) == 2
    assert tree.min(4, 7) == 2
    assert tree.min(5, 8) == 2
    assert tree.min(6, 9) == 0

    assert tree.min(0, 4) == 1
    assert tree.min(1, 5) == 1
    assert tree.min(2, 6) == 1
    assert tree.min(3, 7) == 2
    assert tree.min(4, 8) == 2
    assert tree.min(5, 9) == 0

    assert tree.min(0, 5) == 1
    assert tree.min(1, 6) == 1
    assert tree.min(2, 7) == 1
    assert tree.min(3, 8) == 2
    assert tree.min(4, 9) == 0

    assert tree.min(0, 6) == 1
    assert tree.min(1, 7) == 1
    assert tree.min(2, 8) == 1
    assert tree.min(3, 9) == 0

    assert tree.min(0, 7) == 1
    assert tree.min(1, 8) == 1
    assert tree.min(2, 9) == 0

    assert tree.min(0, 8) == 1
    assert tree.min(1, 9) == 0

    assert tree.min(0, 9) == 0
