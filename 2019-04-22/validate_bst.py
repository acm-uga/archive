def is_bst(tree, min=float('-inf'), max=float('+inf')):
    '''Check if a tree is a binary search tree.

    Arguments:
        tree:
            The tree to check. The empty tree is represented by ``None``.
            Otherwise the tree is a 3-tuple, ``(val, left, right)``, where
            ``val`` is the value of the root node and ``left`` and ``right``
            are subtrees.
        min:
            The minimum allowed value in the BST.
        max:
            The maximum allowed value in the BST.
    '''
    if tree is None:
        return True

    (val, left, right) = tree

    if val < min or max < val:
        return False

    if not is_bst(left, min, val):
        return False

    if not is_bst(right, val, max):
        return False

    return True


if __name__ == '__main__':
    assert is_bst([4, [2, None, None], [6, None, None]]) == True
    assert is_bst([4, [6, None, None], [2, None, None]]) == False
    assert is_bst(None) == True
