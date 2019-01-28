def two_sum(data, target):
    '''Returns the index of two elements that sum to the target.

    The output is unique: the lower index is always first, and the first
    combination found is the one returned.

    Arguments:
        data (list of int):
            The data to search.
        target (int):
            The target value of the sum.

    Returns:
        i (int):
            The index of the first value in the sum.
        j (int):
            The index of the second value in the sum.

    Raises:
        ValueError:
            No solution was found.
    '''
    if len(data) == 0:
        raise ValueError("no solution found")

    for i, a in enumerate(data):
        for j, b in enumerate(data[i+1:]):
            if a + b == target:
                return i, j

    raise ValueError("no solution found")
