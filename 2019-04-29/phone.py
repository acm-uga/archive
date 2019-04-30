def phone_strings(digits):
    '''Yield all string that the given phone number could represent.

    The input is a string giving the digits of a phone number. Each digit can
    represent multiple letters, which you can see by looking at a phone dialer.
    This function generates all of the strings that a phone number could
    represent. Note that the symbols ``1``, ``#``, and ``*`` cannot represent
    any letter and are thus invlid in the input.

    Arguments:
        digits (string):
            The phone number. The only valid characters are the digits 2
            through 9, representing letters, and 0, representing a space.

    Yields:
        string:
            A string that the phone number could represent.
    '''
    # We implement this algorithm recursivly. First, we split the string into
    # the first digit and the remaining digits. Then we find the set of letters
    # that can be represented by the first digit. We make a recursive call on
    # the remaining digits and prepend each letter for this digit onto the
    # strings returned by the recursive call.

    # If the input is an empty string, our base case returns the empty string.
    if digits == '':
        yield ''
        return

    # This is slice notation in Python. `first` is a string containing the
    # first character of `digits` (Python has no char type). `rest` is the
    # substring of `digits` starting at index 1 and extending to the end.
    first = digits[0]
    rest = digits[1:]

    # Depending on the first digit, we need to get the set of letters it can
    # represent. For best performance, we do this before entering the loop.
    if first == '2':
        lhs_choices = ('a', 'b', 'c')
    elif first == '3':
        lhs_choices = ('d', 'e', 'f')
    elif first == '4':
        lhs_choices = ('g', 'h', 'i')
    elif first == '5':
        lhs_choices = ('j', 'k', 'l')
    elif first == '6':
        lhs_choices = ('m', 'n', 'o')
    elif first == '7':
        lhs_choices = ('p', 'q', 'r', 's')
    elif first == '8':
        lhs_choices = ('t', 'u', 'v')
    elif first == '9':
        lhs_choices = ('w', 'x', 'y', 'z')
    elif first == '0':
        lhs_choices = (' ',)
    else:
        raise ValueError(f'invalid digit: {first}')

    # The recursive call is expensive. It has an exponential time complexity
    # with respect to the number of characters in the input. Therefore we
    # only call it once. If the order of the loops were swapped, we would
    # multiply our time complexity by ~3 (the average size of `lhs_choices`).
    # When nesting loops, ALWAYS put the most expensive loop on the outside.
    for rhs in phone_strings(rest):
        for lhs in lhs_choices:
            yield lhs + rhs


if __name__ == '__main__':
    assert set(phone_strings('2')) == {'a', 'b', 'c'}

    assert set(phone_strings('23')) == {
        'ad', 'bd', 'cd',
        'ae', 'be', 'ce',
        'af', 'bf', 'cf',
    }
