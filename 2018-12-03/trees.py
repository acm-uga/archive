def sum_tree(root):
    """Sums the nodes of a tree.

    Arguments:
        root (binary tree):
            The root of a binary tree. A binary tree is either a 3-tuple
            ``(data, left, right)`` where ``data`` is the value of the root node
            and ``left`` and ``right`` are the left and right subtrees or
            ``None`` for the empty tree.

    Returns:
        n (int):
            The sum of the nodes of the tree.
    """
    if root is None:
        return 0

    (data, left, right) = root

    return data + sum_tree(left) + sum_tree(right)


def trim_bst(root, min, max):
    """Select a range from a binary search tree between ``min`` and ``max``.

    Arguments:
        root (binary search tree):
            The root of a binary search tree. A binary tree is either a 3-tuple
            ``(data, left, right)`` where ``data`` is the value of the root node
            and ``left`` and ``right`` are the left and right subtrees or
            ``None`` for the empty tree. A binary search tree is a binary tree
            whose in-order traversal is sorted.
        min:
            The minimum value of the trim.
        max:
            The maximum value of the trim.

    Returns:
        new_root (binary search tree):
            A new binary search tree that is like the input, but only contains
            nodes with values between ``min`` and ``max``, inclusive.
    """
    if root is None:
        return None

    (data, left, right) = root

    if data < min:
        return trim_bst(right, min, max)
    elif max < data:
        return trim_bst(left, min, max)
    else:
        new_left = trim_bst(left, min, max)
        new_right = trim_bst(right, min, max)
        return (data, new_left, new_right)


def test_sum_tree():
    # The example tree encoded as a 3-tuple.
    tree = (15, (10, (8, None, None), (12, None, None)), (20, (25, None, None), (16, None, None)))

    # The sum of the tree.
    ans = 106

    # Assert that ``sum_tree`` outputs the answer.
    assert sum_tree(tree) == ans


def test_trim_bst():
    # The example tree encoded as a 3-tuple.
    tree = (11, (5, (1, None, None), (10, None, None)), (20, (19, None, None), (25, None, None)))

    # The answer as a 3-tuple.
    ans = (11, (5, None, (10, None, None)), (19, None, None))

    # Assert that ``trim_bst`` outputs the answer.
    assert trim_bst(tree, min=5, max=19) == ans
