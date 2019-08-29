def telephone(number):
    '''Iterate over all possible "telephone strings" of some number.

    On a telephone dial pad, each digit may represent several letters.
    This function iterates over all possible strings that could be
    interpreted by dialing a number. Both 0 and 1 are interpreted as
    spaces.

    The algorithm is simple. We iterate over the digits and lookup
    their corresponding characters from a dictionary.

    This is implemented as a generator. To learn more about generators,
    see ``p3.py``.

    Arguments:
        number (int or str):
            A non-negative number to interpret.

    Yields:
        str:
            Telephone strings for the number.
    '''
    LETTERS = {
        '0': (' '),
        '1': (' '),
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z'),
    }

    # Treat the number as a string.
    number = str(number)

    if len(number) == 0:
        yield ''
        return

    first = number[0]
    rest = number[1:]

    for substr in telephone(rest):
        for l in LETTERS[first]:
            yield l + substr


def test():
    '''Test the :func:`telephone` function.

    Raises:
        AssertionError:
            One of the test cases failed.
    '''
    assert set(telephone('')) == {''}
    assert set(telephone('1')) == {' '}
    assert set(telephone('2')) == {'a', 'b', 'c'}
    assert set(telephone('9')) == {'w', 'x', 'y', 'z'}

    assert set(telephone('23')) == {
        'ad', 'ae', 'af',
        'bd', 'be', 'bf',
        'cd', 'ce', 'cf',
    }
