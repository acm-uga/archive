from collections import defaultdict


def top_k(data, k):
    '''Return the `k` most occuring elements, in order of most occurences.

    Ties are broken by the natural order of the data.

    Arguments:
        data (list):
            The data being queried.
        k (int):
            The number of elements to return.

    Returns:
        top_k_datum (list):
            The ``k`` elements which occur the most in ``data``, sorted by
            number of occurences. If fewer than ``k`` unique elements exist,
            then the list will contain all unique elements.
    '''
    # We first count the number of occurences of each datum using a dictionary
    # (Python's hashmap type, also called a dict). Then we sort the pairs of
    # ``(datum, count)`` first by ascending datum then by descending count.
    #
    # Sorting the pairs this way ensures that ties are broken by the natural
    # order of the datum (e.g. lexicographic order for strings).
    #
    # P.S. Since we only care about the top-k elements, we could use a heap
    # to avoid completely sorting the data. It may save some time for large
    # lists, but the time complexity is still the same.

    # Do the counting. The defaultdict assigns a default value (in this case 0)
    # to elements which don't yet exist. This makes it easy to write the
    # counting loop.
    counts = defaultdict(lambda: 0)
    for x in data:
        counts[x] += 1

    # ``count.items()`` gives us an iterator over ``(datum, count)`` pairs.
    pairs = counts.items()

    # Do the sorting. We sort first by ascending datum then by descending count.
    # Note that it is only valid to stack sorts like this when using a
    # __stable__ sorting algorithm (like merge sort). Python's builtin sort is
    # stable, but quicksort is not (for example).
    pairs = sorted(pairs, key=lambda pair: pair[0])   # ascending datum
    pairs = sorted(pairs, key=lambda pair: -pair[1])  # descending count

    # Pull out the top k
    top_k_pairs = pairs[:k]
    top_k_datum = [pair[0] for pair in top_k_pairs]
    return top_k_datum


def test():
    data = ["let's", "go", "dawgs", "let's", "go", "sic", "em"]
    assert top_k(data, 2) == ['go', 'lets']
