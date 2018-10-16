# Linked List Review
# --------------------------------------------------
# A doubly linked list consists of nodes which contain three parts: a value, a
# pointer to the next node, and a pointer to the previous node. Here we define
# a class to represent the nodes, along with a function to easily construct
# a doubly linked list.

class Node:
    ''' A node in a doubly linked list.
    '''

    def __init__(self, val, prev=None, next=None):
        '''Construct a new node with the given value and next/prev pointers.
        '''
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self):
        '''Return a string representing the list starting at this node.

        In Python, the ``__repr__`` method should return a string that can be
        used to reconsturct the structure. So our output represents a call to
        the :func:`linked_list` helper constructor.

        This will be used when printing the node/list.
        '''
        values = ''
        node = self

        while True:
            values += repr(node.val)
            if node.next is None:
                break
            else:
                values += ', '
                node = node.next

        return 'linked_list(' + values + ')'

    def __len__(self):
        '''Return the length of the list starting at this node.

        This is used for ``len(my_linked_list)``.
        '''
        count = 0
        node = self
        while node is not None:
            count += 1
            node = node.next
        return count


def linked_list(*args):
    '''Construct a doubly linked list from the given values.

    Example:
        >>> my_list = linked_list(1, 2, 3, 4)
        >>> my_list
        linked_list(1, 2, 3, 4)
        >>> my_list.next
        linked_list(2, 3, 4)
        >>> my_list.next.next
        linked_list(3, 4)
        >>> my_list.next.next.next
        linked_list(4)
        >>> my_list.next.next.next.next is None
        True
    '''
    if len(args) == 0:
        return None

    front = None
    back = None
    for val in args:
        node = Node(val)
        if front is None:
            front = node
            back = node
        else:
            node.prev = back
            back.next = node
            back = node

    return front


def is_sorted(front):
    '''Given the front of a doubly linked list, returns True if it's sorted.
    '''
    # The empty list.
    if front is None:
        return True

    # Non empty lists.
    node = front
    while node.next is not None:
        if node.next.val < node.val:
            return False
        node = node.next
    return True


# Problem 1
# --------------------------------------------------
# Given the first node of a doubly linked list, sort the list using insertion
# sort [1]. Here's a quick explanation of insertion sort. Starting at the front
# of the list, for each node, move the node backwards in the list until the
# value in the previous node is less than or equal to the value in the current
# node.
#
# See this graphic [2] for a visual explanation.
#
# Hint: The nodes can be moved to the proper position in one move.
#
# [1]: https://en.wikipedia.org/wiki/Insertion_sort
# [2]: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif

def insertion_sort(front):
    '''Sort a doubly linked list using insertion sort.

    This function sorts the nodes in place and returns the node at the front
    of the sorted list
    '''
    # Handle the empty list as a special case.
    if front is None:
        return None

    # ``current`` is the node being moved.
    # The loop advances ``current`` until it reaches the end.
    # Skipping the first element avoids the edge case ``current is front``.
    current = front.next
    while current is not None:
        # The original ``next`` and ``prev``
        # should skip over the current node.
        # Note that ``prev`` could never be None.
        prev = current.prev
        next = current.next
        prev.next = next
        if next is not None:
            next.prev = prev

        # Walk backwards until ``pos`` gives us the node
        # which should come before ``current``.
        pos = prev
        while pos is not None and current.val < pos.val:
            pos = pos.prev

        # Swap the ``next`` and ``prev`` references around
        # to put ``current`` right the new spot.
        if pos is None:
            current.prev = None
            current.next = front
            front.prev = current
            front = current
        else:
            current.prev = pos
            current.next = pos.next
            pos.next = current
            if current.next is not None:
                current.next.prev = current

        # The original ``next`` is the new ``current``
        # for the next iteration.
        current = next

    # We've kept up with ``front``; it's the front of the sorted list.
    return front


def test_insertion_sort():
    import random
    for size in range(255):
        vals = [random.randint(0, 10) for _ in range(size)]
        l = linked_list(*vals)
        l = insertion_sort(l)
        assert is_sorted(l)
        assert len(l) == size


# Problem 2
# --------------------------------------------------
# Given the first nodes of two sorted doubly linked lists, merge them into one.
# In the case of equal values, the values from the first list should come
# before values in the second list, and equal values in the same list should
# maintain their relative order.
#
# This is a subroutine for merge sort.

def merge(left, right):
    '''Merges two sorted doubly linked lists together into a single sorted
    doubly linked list.

    This function merges the two lists in place and returns the node at the
    front of the merged list.
    '''
    # Edge cases for empty lists.
    if left is None: return right
    if right is None: return left

    # Determine which will be the front of the new list.
    # ``front`` is the first merged node.
    if right.val < left.val:
        front = right
        right = right.next
    else:
        front = left
        left = left.next

    # Loop until we've merged all of one list.
    # ``back`` is the last merged node.
    back = front
    while left is not None and right is not None:
        # Decide to merge either the first node of either the left or the right,
        # and advance the pointer for whichever one was merged.
        if right.val < left.val:
            back.next = right
            right.prev = back
            back = right
            right = right.next
        else:
            back.next = left
            left.prev = back
            back = left
            left = left.next

    # We've merged all of one of the list.
    # So just append the remaining nodes of the other list.
    # Note that it is impossible for both left and right to be None.
    assert not (left is None and right is None)
    if left is None:
        back.next = right
        right.prev = back
    else:
        back.next = left
        left.prev = back

    # We decided which would be the front of the merged list earlier.
    return front


def test_merge():
    import random
    for left_size in range(64):
        for right_size in range(64):
            left_vals = [random.randint(0, 10) for _ in range(left_size)]
            left = linked_list(*left_vals)
            left = insertion_sort(left)

            right_vals = [random.randint(0, 10) for _ in range(right_size)]
            right = linked_list(*right_vals)
            right = insertion_sort(right)

            merged = merge(left, right)
            assert is_sorted(merged)

            if right_size == left_size == 0:
                assert merged == None
            else:
                assert len(merged) == left_size + right_size
