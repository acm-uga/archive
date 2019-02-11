def next_value(num, base):
    '''Get the next number in the given base.

    Arguments:
        num (list of non-negative int):
            The number in list form.
        base (non-negative int):
            The base of the number. Must be 2 or greater.

    Returns:
        The next number in list form. The number will have the same number of
        digits. This function wraps around to 0 when it reaches the maximum
        value for the given number of digits.
    '''
    num = num.copy()
    max_digit = base - 1

    if num == []:
        return []

    if num[-1] == max_digit:
        num[:-1] = next_value(num[:-1], base)
        num[-1] = 0
    else:
        num[-1] = num[-1] + 1

    return num


def base_count(base, digits):
    '''Generate all numbers of a given base with some number of digits.

    Arguments:
        base (non-negative int):
            The base of the number. Must be 2 or greater.
        digits (non-negative int):
            The number of digits.

    Yields (list of non-negative int):
        Yields each number as a list of ints in big-endian order.
    '''
    assert 2 <= base
    assert 0 <= digits

    max_digit = base - 1

    start = [0 for _ in range(digits)]  # [0, 0, 0] when digits=3
    stop = [max_digit for _ in range(digits)]  # [4, 4, 4] when digits=3 and base=5

    val = start.copy()
    while val < stop:
        yield val
        val = next_value(val, base)
    yield val
