class BinarySearchTree:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

        # verify that the left and right are valid
        if left is not None:
            assert left.root <= root
        if right is not None:
            assert root <= right.root

    def __str__(self):
        return f'({self.root} {self.left} {self.right})'

    @classmethod
    def from_sorted_list(cls, data):
        if len(data) == 0:
            return None
        mid = len(data) // 2
        root = data[mid]
        left = cls.from_sorted_list(data[:mid])
        right = cls.from_sorted_list(data[mid+1:])
        return cls(root, left, right)


def test_bst():
    data = [1, 2, 3, 4, 5, 6, 7]
    tree = BinarySearchTree.from_sorted_list(data)
    soln = '(4 (2 (1 None None) (3 None None)) (6 (5 None None) (7 None None)))'
    assert str(tree) == soln
