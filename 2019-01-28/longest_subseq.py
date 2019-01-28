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

    if len(data) == 0:
        return 0, 0

    i = 0
    j = 0
    while j + 1 < len(data):
        if data[j] <= data[j+1]:
            j += 1
        else:
            n = j - i + 1
            if best_n < n:
                best_n = n
                best_i = i
            j += 1
            i = j

    return best_i, best_n
