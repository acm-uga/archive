'''Answers to the "Upperclassperson" problems.

These functions are implemented as a Python generator using the
``yield`` keyword. This is a very useful tool for whiteboard problems.

Essentially, functions using the ``yield`` keyword don't run when
you call them. Instead, they return a generator object. For example:

    >>> import p3
    >>> perms = p3.permute('abc')
    >>> perms
    <generator object permute at 0x1135afc50>

You can pass a generator to the :func:`next` builtin function. The
function will then execute until it reaches a ``yield`` statement:

    >>> next(perms)
    'abc'

The next time you call ``next``, the generator will resume where it
left off until it reaches another ``yield``:

    >>> next(perms)
    'bac'
    >>> next(perms)
    'bca'
    >>> next(perms)
    'acb'
    >>> next(perms)
    'cab'
    >>> next(perms)
    'cba'

Finally, if you call ``next`` and the function returns instead of
yielding, it will raise a :class:`StopIteration` exception:

    >>> next(perms)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration

Genrators are especially useful because you can loop over them:

    >>> for perm in p3.permute('abc'):
    ...     print(perm)
    ...
    abc
    bac
    bca
    acb
    cab
    cba

You can also collect generators into a list or set:

    >>> list(p3.permute('abc'))
    ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

    >>> set(p3.permute('abc'))
    {'bca', 'acb', 'cab', 'cba', 'abc', 'bac'}

Finally, the ``subsets`` solution uses the ``yield from`` statement.
Essentially, this:

    >>> yield from some_generator

Is equivalent to this:

    >>> for x in some_generator:
    ...     yield x
'''


def permute(s):
    '''Iterate over permutations of s.

    This is implemented recursivly. In the first base case, if the
    string is empty, we return without yielding anything because there
    are no permutations of the empty string. In the second base case,
    if the string has only one character, we yield it as the only
    permutation.

    Otherwise, we split the string into ``first`` (containing only the
    first element) and ``rest`` (containing the rest of the string). We
    loop over all permutations of ``rest``, then for each index in that
    permutation, we split it into ``before`` and ``after`` strings, then
    recombine them with the ``first`` element in-between.

    Arguments:
        s (sequence):
            The string to permute. Technically this can be any sequence.

    Yields:
        Permutations of ``s``.
    '''
    if len(s) == 0:
        return

    if len(s) == 1:
        yield s
        return

    first = s[0]
    rest = s[1:]

    for substr in permute(rest):
        for i in range(len(substr) + 1):
            before = substr[:i]
            after = substr[i:]
            yield before + first + after


def test_permute():
    '''Test the :func:`permute` function.

    Raises:
        AssertionError:
            One of the test cases failed.
    '''
    # Note that ``{}`` is the empty dictionary, not the empty set.
    # The empty set is ``set()``.
    assert set(permute('')) == set()
    assert set(permute('a')) == {'a'}
    assert set(permute('ab')) == {'ab', 'ba'}
    assert set(permute('abc')) == {'abc', 'bac', 'bca', 'acb', 'cab', 'cba'}


def subsets(s):
    '''Iterate over the powerset of ``s``.

    The powerset is the set of all subsets.

    This algorithm depends on a helper function that iterates over all
    subsets of a particular size.

    Arguments:
        s (collection):
            The base set. It may contain duplicates.

    Yields:
        Subsets of s.
    '''
    s = set(s)
    for n in range(len(s) + 1):
        yield from _subsets_helper(s, n)

def _subsets_helper(s, n):
    '''Iterate over all subsets of ``s`` with size ``n``.

    This is a recursive algorithm with two base cases. If ``n`` is
    equal to the size of ``s``, then ``s`` is the only subset. And if
    ``n`` is zero, the only subset is the empty set.

    After the base case, we take out an arbitrary element from the set,
    then follow two recursive cases. First, we find all subsets of the
    remaining set of size `n-1` then add in the element we took out.
    Next we find all subsets of size `n` from the remaining set, i.e.
    all subsets without the element we picked.

    Arguments:
        s (set):
            The base set. The must NOT contain duplicates.
        n (int):
            The size of the subsets.

    Yields:
        Subsets of ``s`` with size ``n``.
    '''
    if len(s) == n:
        yield s
        return

    if n == 0:
        yield set()
        return

    # Get an arbitrary element from the set.
    # This admittedly odd syntax allows us to get the element without
    # modifying the original set.
    elem = next(iter(s))

    # Get the elements of ``s`` minus ``elem``.
    rest = s - set(elem)

    # The syntax ``{*foo, x, y}`` means to create a new set containing all
    # of the elements of ``foo`` and additional elements ``x`` and ``y``.
    for subcombo in _subsets_helper(rest, n-1):
        yield {*subcombo, elem}

    for subcombo in _subsets_helper(rest, n):
        yield subcombo


def test_subsets():
    '''Test the :func:`subsets` function.

    Raises:
        AssertionError:
            One of the test cases failed.
    '''
    # We need a special compare function since the ``subsets`` function
    # does not guarantee the order of the subsets it yields.
    def same_elements(output, expected):
        output = list(output)
        expected = list(expected)
        for x in expected:
            if x not in output:
                return False
        return len(output) == len(expected)

    # Note that ``{}`` is the empty dictionary, not the empty set.
    # The empty set is ``set()``.
    assert same_elements(subsets(''), [set()])
    assert same_elements(subsets('a'), [set(), {'a'}])
    assert same_elements(subsets('ab'), [set(), {'a'}, {'b'}, {'a', 'b'}])
    assert same_elements(subsets('abc'), [
        set(),
        {'a'}, {'c'}, {'b'},
        {'c', 'a'}, {'a', 'b'}, {'c', 'b'},
        {'a', 'b', 'c'},
    ])


def test():
    '''Test all solutions.

    Raises:
        AssertionError:
            One of the test cases failed.
    '''
    test_permute()
    test_subsets()
