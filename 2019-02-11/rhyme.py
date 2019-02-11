def next_value(rhyme):
    '''Get the next rhyme scheme.

    Arguments:
        rhyme (list of non-negative int):
            The rhyme scheme in list form.

    Returns:
        The next rhyme scheme in list form. The rhyme scheme will have the same
		number of lines.
    '''
    rhyme = rhyme.copy()

    if rhyme == []:
        return []

    max_val = max(rhyme[:-1]) + 1

    if rhyme[-1] == max_val:
        rhyme[:-1] = next_value(rhyme[:-1])
        rhyme[-1] = 0
    else:
        rhyme[-1] = rhyme[-1] + 1

    return rhyme


def rhyme_schemes(n):
    '''Generate all possible rhyme schemes for a poem of `n` lines.

    For example, a three line poem could have the rhyme schemes `AAA`, `AAB`,
    `ABA`, or `ABC`. Each letter corresponds to a unique syllable at the end of
    each line. Lines marked by the same letter rhyme. The first line is always
    marked by an `A` and you can't use a new letter unless you have used the
    previous letter, e.g. you can't use `C` unless you've used `B`.

    We use numbers instead of letters, where 0 represents `A`, 1 represents `B`,
    etc.

    Arguments:
        n (non-negative int):
            The number of lines

    Yields (list of non-negative int):
        Yields each rhyme scheme as a list of ints.
    '''
    start = [0 for _ in range(n)]  # [0, 0, 0] when n=3
    stop = [i for i in range(n)]  # [0, 1, 2] when n=3

    val = start.copy()
    while val < stop:
        yield val
        val = next_value(val)
    yield val
