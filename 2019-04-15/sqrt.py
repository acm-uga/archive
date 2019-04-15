def sqrt(n, accuracy=0.001):
    '''Compute the square root of `n`.

    The value of `n` must be between 0 and 16,777,216 (i.e. 2^24).

    This function implements a naive binary search. There are MUCH better
    algorithms, though most require a math background through Calc 2.

    See the Wikipedia page:
    <https://en.wikipedia.org/wiki/Methods_of_computing_square_roots>

    Most real-world software square root algorithms are based on the CORDIC
    method: <https://en.wikipedia.org/wiki/CORDIC>

    Arguments:
        n (int):
            The value to square-root. It must be between 0 and 16,777,216.
        accuracy (float):
            The error of the solution will be no greater than this value.

    Returns:
        float:
            The square root of ``n``.
    '''
    # Check that the input is valid: 0 <= n <= 16777216.
    if n < 0:
        raise ValueError('input must not be negative')
    elif n == 0:
        return 0
    elif n < 16777216:
        lo = accuracy  # The smallest non-zero solution is equal to the accuracy.
        hi = 4096
    elif n == 16777216:
        return 4096
    else:
        raise ValueError('input must not be greater than or equal to 2^24')

    # Binary search until we reach the desired accuracy.
    while accuracy < hi - lo:
        mid = (hi + lo) / 2
        if mid ** 2 <= n:
            lo = mid
        else:
            hi = mid

    # Return the average of the hi and lo estimates.
    return (hi + lo) / 2
