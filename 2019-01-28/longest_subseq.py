def lmis(data):
    '''Longest Monotonically Increasing Subsequence.

    Arguments:
        data (list):
            All elements must be comparable to all other elements.

    Returns:
        i (int):
            The index of the first element in the longest monotonically
            increasing subsequence.
        n (int):
            The length of the first element in the longest monotonically
            increasing subsequence.
    '''
    best_i = 0
    best_n = 0

    start = 0  # Index of the first element in the subsequence.
    stop = 0   # Index of the last element in the subsequence.
    while stop < len(data):
        stop += 1
        if stop == len(data) or not data[stop - 1] <= data[stop]:
            n = stop - start
            if best_n < n:
                best_n = n
                best_i = start
            start = stop

    return best_i, best_n
