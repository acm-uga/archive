class BinaryTree:
    '''A simple binary tree.
    '''

    def __init__(self, root, left=None, right=None):
        '''Construct a binary tree.

        Arguments:
            root (str or int): The value of the root node.
            left (BinaryTree or None): The left subtree.
            right (BinaryTree or None): The right subtree.
        '''
        self.root = root
        self.left = left
        self.right = right

    def __str__(self):
        '''Represent the tree as an s-expression string.
        '''
        if self.left is None and self.right is None:
            return str(self.root)
        else:
            return f'({self.root} {self.left} {self.right})'


def parse_rpn(expr):
    '''Parse an RPN expression.

    An RPN expression is an arithmetic expression written in reverse Polish
    notation, a.k.a. postfix notation. In other words, the operator comes after
    both of its arguments.

    For example, this RPN expression::

        123 456 + 789 *

    is equivalent to this expression, in the usual infix notation::

        (123 + 456) * 789

    Note that RPN expressions never require parentheses.

    Arguments:
        expr (str):
            The RPN expression to parse. The expression may contain integers
            and the operators '+', '-', '*', and '/'. Each token is separated
            by exactly one space.

    Returns:
        BinaryTree:
            The parse tree of the RPN expression. Numbers are stored in the leaf
            nodes (i.e. both the left and right subtrees are `None`), and
            operators are stored in branch nodes, where the left and right
            subtrees are the parse trees of the left and right arguments.
    '''
    stack = []

    for val in expr.split():
        if val in ('+', '-', '*', '/'):
            right = stack.pop()
            left = stack.pop()
            tree = BinaryTree(val, left, right)
            stack.append(tree)
        else:
            tree = BinaryTree(int(val))
            stack.append(tree)

    if len(stack) != 1:
        raise SyntaxError(f'invalid RPN expression: {repr(expr)}')

    tree = stack.pop()
    return tree


if __name__ == '__main__':
    assert str(parse_rpn('123 456 + 789 *')) == '(* (+ 123 456) 789)'
