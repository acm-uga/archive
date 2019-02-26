def memmove(data, dest, src, n):
    '''Copy data in the array from ``src`` to ``dest``.

    Like ``memmove(3)`` in C, the source and destination may overlap.

    Arguments:
        data (list):
            The list being manipulated.
        dest (int):
            The destination index of the copy.
        src (int):
            The source index of the copy.
        n (int):
            The number of elements to copy.
    '''
    if dest < src:
        for i in range(n):
            data[dest + i] = data[src + i]
    else:
        for i in range(n):
            data[dest + n - i - 1] = data[src + n - i - 1]


def test_memmove():
    data = ['_', '_', 'A', 'B', 'C', '_', '_', '_']

    data1 = data.copy()
    memmove(data1, 5, 2, 3)
    assert data1 == ['_', '_', 'A', 'B', 'C', 'A', 'B', 'C']

    data2 = data.copy()
    memmove(data2, 3, 2, 3)
    assert data2 == ['_', '_', 'A', 'A', 'B', 'C', '_', '_']

    data3 = data.copy()
    memmove(data3, 1, 2, 3)
    assert data3 == ['_', 'A', 'B', 'C', 'C', '_', '_', '_']

    data4 = data.copy()
    memmove(data4, 2, 2, 3)
    assert data4 == ['_', '_', 'A', 'B', 'C', '_', '_', '_']
