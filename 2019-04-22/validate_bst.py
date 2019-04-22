class BinaryTree:
    '''A simple binary tree.

    Each node has a value and optional left and right subtrees. The value
    ``None`` represents the empty tree.
    '''

    def __init__(self, val, left=None, right=None):
        '''Construct a new binary tree.

        Arguments:
            val (any): The value at the root.
            left (BinaryTree or None): The left subtree.
            right (BinaryTree or None): The right subtree.
        '''
        self.val = val
        self.left = left
        self.right = right

    def is_bst(self, min=float('-inf'), max=float('+inf')):
        '''Test if this tree is a valid binary search tree.

        Arguments:
            min (any): All elements must be greater than or eqaul to this value.
            max (any): All elements must be less than or eqaul to this value.
        '''
        if self.val < min:
            return False

        if max < self.val:
            return False

        if self.left is not None and not self.left.is_bst(min, self.val):
            return False

        if self.right is not None and not self.right.is_bst(self.val, max):
            return False

        return True

    @classmethod
    def from_sexp(cls, s):
        '''Construct a BinaryTree from an s-expression.

        A binary s-expression is either ``None`` or a list of three values.
        ``None`` represents an empty tree. A list of three values represents a
        binary tree such that the first element is the root value and the
        second and third elements are s-expressions describing the left and
        right subtrees respectively.

        Arguments:
            s (Sequence or None): The s-expression describing the tree.

        Returns:
            BinaryTree or None: The tree described by the s-expression.
        '''
        if s is None:
            return None

        (val, left, right) = s
        left = cls.from_sexp(left)
        right = cls.from_sexp(right)
        return cls(val, left, right)


def validate_bst(s):
    '''Validates a binary search tree described by an s-expression.

    Arguments:
        s (Sequence or None):
            The s-expression describing the tree.
            The nodes must be numbers.

    Returns:
        bool:
            True when ``s`` describes a binary search tree.
    '''
    tree = BinaryTree.from_sexp(s)
    if tree is None:
        return True
    else:
        return tree.is_bst()


if __name__ == '__main__':
    assert validate_bst([4, [2, None, None], [6, None, None]]) == True
    assert validate_bst([4, [6, None, None], [2, None, None]]) == False
    assert validate_bst(None) == True
