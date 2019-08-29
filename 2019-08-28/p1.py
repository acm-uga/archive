def reverse_inplace(s):
    '''Reverse a list in-place.

    The original problem was worded to reverse a string in-place, but
    Python strings are immutable, so we reverse a list instead.

    The algorithm is simple. We start with two pointers, one pointing
    to the first letter and one pointing to the last letter. We swap
    the elements under each, then move both pointers towards the center.
    We stop when they cross in the middle.

    Arguments:
        s (list):
            The "string" to reverse.
    '''
    i = 0  # First index of `s`.
    j = len(s) - 1  # Last index of `s`.

    # Until the pointers cross...
    while i < j:
        # Swap the elements.
        s[i], s[j] = s[j], s[i]

        # Update the pointers.
        i += 1
        j -= 1


def test_reverse_inplace():
    '''Test the :func:`reverse_inplace` function.

    Raises:
        AssertionError:
            One of the test cases failed.
    '''
    # The general test code, specifically designed to check
    # that the algorithm works in-place.
    def test(input, output):
        reverse_inplace(input)
        assert input == output

    # The test cases, including some edge cases.
    test([], [])
    test([1], [1])
    test([1, 2], [2, 1])
    test([1, 2, 3], [3, 2, 1])
    test([1, 1, 1], [1, 1, 1])
    test(['a', 'b', 'c'], ['c', 'b', 'a'])


def palindrome(s):
    '''Check if a string is a palindrome.

    A palindrome is a string that is the same when reversed.

    The algorithm is simple. We start with two pointers, one pointing
    to the first letter and one pointing to the last letter. We check
    that the elements under each are equal, then move both pointers
    towards the center. We stop when they cross in the middle.

    Arguments:
        s (sequence):
            The input string. Technically this can be any sequence.

    Returns:
        bool:
            Returns true if ``s`` is a palindrome or false otherwise.
    '''
    i = 0  # First index of `s`.
    j = len(s) - 1  # Last index of `s`.

    # Until the pointers cross...
    while i < j:
        # If the elements are not equal, it's not a palindrome.
        if s[i] != s[j]:
            return False

        # Update the pointers.
        i += 1
        j -= 1

    return True


def test_palindrome():
    '''Test the :func:`palindrome` function.

    Raises:
        AssertionError:
            One of the test cases failed.
    '''
    assert palindrome('tacocat')
    assert palindrome([1, 2, 3, 2, 1])
    assert palindrome('')
    assert palindrome('a')
    assert palindrome('aa')
    assert palindrome('aaa')
    assert not palindrome('foo')


def test():
    '''Test all solutions.

    Raises:
        AssertionError:
            One of the test cases failed.
    '''
    test_reverse_inplace()
    test_palindrome()
