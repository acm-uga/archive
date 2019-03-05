class BinarySearchTree:
    '''A binary search tree, or BST for short.

    A binary search tree is a tree represents a sorted sequence, where the root
    node contains some item in the sequence, and the left/right subtrees
    represent the subsequence before/after the root item.

    When balanced, a binary search tree offers a lookup operation in
    ``O(log(n))`` time where ``n`` is the number of elements.
    '''

    def __init__(self, root, left, right):
        '''Construct a BST from a root value and left/right subtrees.

        This constructor checks that the root nodes of the subtrees are valid,
        i.e. the root of the left is less than or equal to this root, and the
        root of the right is greater than or equal to this root. This check is
        enough to verify that the entire tree is a BST if all subtrees are
        constructed this way.

        Arguments:
            root (any):
                The root value of the tree.
            left (BinarySearchTree or None):
                The left subtree.
            right (BinarySearchTree or None):
                The right subtree.
        '''
        self.root = root
        self.left = left
        self.right = right

        # verify that the left and right are valid
        if left is not None:
            assert left.root <= root
        if right is not None:
            assert root <= right.root

    def __str__(self):
        '''Returns this tree as a string s-expression.
        '''
        return f'({self.root} {self.left} {self.right})'

    def __contains__(self, item):
        '''Search for a value in the BST.

        This method is called with the ``in`` operator, e.g:

            bst = BinarySearchTree.from_sorted_list([1, 3, 5, 7, 9])
            assert 3 in bst
            assert 4 not in bst

        Arguments:
            item (any):
                The value to search for.

        Returns:
            bool:
                True when the value is contained in the collection
        '''
        if item == self.root:
            return True

        if item < self.root and self.left is not None:
            return item in self.left

        if self.root < item and self.right is not None:
            return item in self.right

        return False

    @classmethod
    def from_sorted_list(cls, data):
        '''Construct a balanced BST from a sorted list.

        Arguments:
            data (list):
                The data forming the tree. This list must be sorted.
        '''
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
