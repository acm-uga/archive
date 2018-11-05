def merge(left, right):
    '''Merge two sorted lists into a new sorted list.
    '''
    # Handle the edge case where either side is empty.
    if len(left) == 0: return right.copy()
    if len(right) == 0: return left.copy()

    # Merge the two lists together.
    merged = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if right[r] < left[l]:
            val = right[r]
            merged.append(val)
            r += 1
        else:
            val = left[l]
            merged.append(val)
            l += 1

    # One of this lists may have elements which have not yet been added to the
    # merged list. We append everything in `left` between `l` and `len(left)`
    # and everything in `right` between `r` and `len(right)`. At most one of
    # these will be non-empty.
    merged.extend(left[l:])
    merged.extend(right[r:])

    return merged


def merge_median(left, right):
    '''Find the median of the elements partitioned across two sorted lists.

    This algorithm uses `O(n)` extra space, where `n` is the total number of
    elements. This algorithm expects `n` to be odd.
    '''
    merged = merge(left, right)
    n = len(merged)

    # `n` must be odd
    assert n % 2 == 1

    # We use `//` to perform integer division in Python.
    # This gives us the index of the median element in the merged list.
    median_index = n // 2

    median = merged[median_index]
    return median
