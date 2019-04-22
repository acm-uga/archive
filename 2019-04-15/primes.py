def primes(n):
    '''Yields all primes less than or equal to ``n``.

    This algorithm works by counting up from 2 to ``n`` and keeping track of
    each prime it finds along the way. For each number ``i`` in this sequence,
    we only need to check if one of the previously found prime numbers is a
    factor. We don't need to check if composite numbers are factors because any
    number can be broken into prime factors (by the fundamental theorem of
    arithmetic).

    This algorithm is known as the Sieve of Eratosthenes:
    <https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes>

    Arguments:
        n (int):
            A non-negative integer.

    Yields:
        int:
            A prime number less than ``n``.
    '''
    if n % 1 != 0:
        raise ValueError('input must be an integer')
    if n < 0:
        raise ValueError('input must not be negative')

    # Special case for 1.
    yield 1

    prev_primes = []  # All non-one primes seen so far.
    for i in range(2, n+1):
        for p in prev_primes:
            if i % p == 0:
                break
        else:
            prev_primes.append(i)
            yield i
