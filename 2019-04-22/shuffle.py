def shuffle(data):
    '''Shuffle a list.

    This is an implementation of the Fisher-Yates shuffle:
    <https://en.wikipedia.org/wiki/Fisher-Yates_shuffle>.

    Note that there are some subtle sources of bias that may appear in
    incorrect implementations. In particular, to generate a random integer ``i``
    such that ``0 <= i < n``, it is NOT okay to generate a random number ``j``
    such that ``0 <= j <= MAX_INT`` and let ``i = j % n`.

    In other words, using modulus to reduce the range of a random number is
    biased. Perfer a dedicated function that produces an unbiased value in the
    desired range.

    Fortunately, in Python, all random integer functions take the desired range
    as arguments and produce unbiased results.

    Arguments:
        data (list):
            The list to shuffle.

    Returns:
        data:
            The input is returned back to the caller.
            The list is shuffled in-place.
    '''
    import random
    n = len(data)
    for i in range(n-1):
        j = random.randrange(i, n)
        data[i], data[j] = data[j], data[i]
    return data
