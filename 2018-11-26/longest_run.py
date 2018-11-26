def longest_run_1(string):
    '''Find the length of the longest 1-run in a string or list.

    A 1-run is a subsequence with at most 1 unique element.

    Arguments:
        string (Sequence):
            The sequence to search.

    Returns:
        int:
            The length of the longest 1-run.
    '''
    if len(string) == 0:
        return 0

    best = 0  # The longest run so far.
    count = 0  # The length of the current run.
    current = None  # The character of the current run.

    for ch in string:
        if ch != current:
            count = 0
            current = ch

        count += 1
        if best < count:
            best = count

    return best


def longest_run_2(string):
    '''Find the length of the longest 2-run in a string or list.

    A 2-run is a subsequence with at most 2 unique element.

    Arguments:
        string (Sequence):
            The sequence to search.

    Returns:
        int:
            The length of the longest 2-run.
    '''
    if len(string) == 0:
        return 0

    elm1 = string[0]  # The first element of the run.
    elm2 = string[0]  # The second element of the run.
    best = 0  # The longest run so far.

    for i, ch in enumerate(string):
        if ch != elm2:
            elm1 = elm2
            elm2 = ch

        count = 0
        j = i
        while 0 <= j and string[j] in {elm1, elm2}:
            count += 1
            j -= 1

        if best < count:
            best = count

    return best


def longest_run_m(string, m):
    '''Find the length of the longest m-run in a string or list.

    An m-run is a subsequence with at most m unique element.

    Arguments:
        string (Sequence):
            The sequence to search.
        m (int):
            The m in m-run. A non-negative integer.

    Returns:
        int:
            The length of the longest 2-run.
    '''
    if len(string) == 0:
        return 0

    elms = [string[0]] * m  # The list of `m` elements in the run.
    best = 0  # The longest run so far.

    for i, ch in enumerate(string):
        if not ch in elms:
            elms = elms[1:m] + [ch]
        else:
            k = elms.index(ch)
            elms = elms[0:k] + elms[k+1:m] + [ch]

        count = 0
        j = i
        while 0 <= j and string[j] in elms:
            count += 1
            j -= 1

        if best < count:
            best = count

    return best


def longest_run_m_optimized(string, m):
    '''Find the length of the longest m-run in a string or list.

    An m-run is a subsequence with at most m unique element.

    We optimize this version with dynamic programming by refactoring the
    inner loop out into a memoized function called ``count_run``.

    Arguments:
        string (Sequence):
            The sequence to search.
        m (int):
            The m in m-run. A non-negative integer.

    Returns:
        int:
            The length of the longest 2-run.
    '''
    if len(string) == 0:
        return 0

    elms = [string[0]] * m  # The list of `m` elements in the run.
    best = 0  # The longest run so far.

    for i, ch in enumerate(string):
        if not ch in elms:
            elms = elms[1:m] + [ch]
        else:
            j = elms.index(ch)
            elms = elms[0:j] + elms[j+1:m] + [ch]

        count = count_run(string, i, frozenset(elms))

        if best < count:
            best = count

    return best


from functools import lru_cache

@lru_cache(maxsize=None)
def count_run(string, i, elms):
    '''Get the length of the run containing elements from ``elms``
    and ending at index ``i``.

    This is a memoized helper for ``longest_run_m_optimized``.

    Since we use ``lru_cache`` to memoize this function, all arguments must
    be hashable.

    Arguments:
        string (Sequence):
            The sequence to search.
        i (int):
            The index where the run ends.
        elms (frozenset):
            The elements allowed in the run.

    Returns:
        int:
            The length of the subsequence in ``string`` that ends at ``i`` and
            contains only elements from ``elms``.
    '''
    count = 0
    while 0 <= i and string[i] in elms:
        count += 1
        i -= 1
    return count
