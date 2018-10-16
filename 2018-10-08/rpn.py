def rpn(expr):
    tokens = expr.split()
    stack = []

    for tok in tokens:
        if tok == '+':
            rhs = stack.pop()
            lhs = stack.pop()
            val = lhs + rhs
            stack.append(val)
        elif tok == '-':
            rhs = stack.pop()
            lhs = stack.pop()
            val = lhs - rhs
            stack.append(val)
        elif tok == '*':
            rhs = stack.pop()
            lhs = stack.pop()
            val = lhs * rhs
            stack.append(val)
        elif tok == '/':
            rhs = stack.pop()
            lhs = stack.pop()
            val = lhs / rhs
            stack.append(val)
        else:
            val = float(tok)
            stack.append(val)

    assert len(stack) == 1
    return stack[0]


def test_rpn():
    assert rpn('1') == 1
    assert rpn('1 2 +') == 3
    assert rpn('1 2 + 3 *') == 9
    assert rpn('1 2 + 3 4 + /') == 3/7
    assert rpn('1 2 * 3 - 4 5 + /') == -1/9
