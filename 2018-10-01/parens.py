def parens_gen(n):
    '''This is a simple generator which will produce duplicates.
    '''
    assert 0 <= n
    assert n % 2 == 0

    if n == 0:
        return
    elif n == 2:
        yield '()'
    else:
        for sub_soln in parens(n-2):
            yield f'{sub_soln}()'
            yield f'(){sub_soln}'
            yield f'({sub_soln})'


def parens(n):
    '''The easy way to remove duplicates is to use a set.
    '''
    return set(parens_gen(n))


def test_parens():
    assert parens(0)  == set()
    assert parens(2)  == {'()'}
    assert parens(4)  == {'(())', '()()'}
    assert parens(6)  == {'((()))', '(())()', '()(())', '(()())', '()()()'}
