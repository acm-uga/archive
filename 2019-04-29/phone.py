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
    if len(digits) == 0:
        yield ''
        return

    (first, *rest) = digits

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
