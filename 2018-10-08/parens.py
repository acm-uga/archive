def assert_parens(input):
    '''Raises an exception if the input does not contain only matching braces,
    brackets, and parens.

    This function may raise an AssertionError or an IndexError.
    '''
    # Note that ``stack.pop()`` will raise an ``IndexError`` when empty.
    stack = []
    for char in input:
        if char == ')':
            top = stack.pop()
            assert top == '('
        elif char == ']':
            top = stack.pop()
            assert top == '['
        elif char == '}':
            top = stack.pop()
            assert top == '{'
        else:
            assert char in '([{'
            stack.append(char)
    assert len(stack) == 0


def check_parens(input):
    '''True when the input contains only matching braces, brackets, and parens.
    '''
    try:
        assert_parens(input)
        return True
    except:
        return False


def test_parens():
    assert check_parens('({[]})')
    assert check_parens('[{}()][]')
    assert not check_parens('()}]')
    assert not check_parens('[{]}')
    assert not check_parens('[{}')
