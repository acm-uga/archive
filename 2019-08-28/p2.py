from collections import defaultdict

def first_non_repeat(s):
    '''Return the first non-repeated element of ``s``.

    The algorithm is simple. We make two passes over the input. In the
    first pass, we count how many times each element appears. We store
    those counts in a hash-map. In the second pass, we search for the
    first element with a count of one.

    Arguments:
        s (sequence):
            The string to search. Technically this can be any sequence.

    Returns:
        object:
            The first element of the sequence that does not repeat.

    Raises:
        ValueError:
            No non-repeated element was found.
    '''
    # A :class:`defaultdict` is like a normal Python dictionary,
    # except it returns a default value if a key is not yet in the
    # dictionary. In this case, the default is 0.
    counts = defaultdict(lambda: 0)

    # Count the number of times each element appears.
    for elem in s:
        counts[elem] += 1

    # Find the first element with a count of one.
    for elem in s:
        if counts[elem] == 1:
            return elem

    # If no element has a count of 1, raise a :class:`ValueError`.
    raise ValueError('No non-repeated element')


def test():
    '''Test the :func:`first_non_repeat` function.
    '''
    assert first_non_repeat('foo') == 'f'
    assert first_non_repeat('fof') == 'o'

    try:
        first_non_repeat('')
        assert False  # This should not happen.
    except ValueError:
        pass  # This is what we want to happen

    try:
        first_non_repeat('aabbcc')
        assert False  # This should not happen.
    except ValueError:
        pass  # This is what we want to happen
