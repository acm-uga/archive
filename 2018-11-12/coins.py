import math


def coins_v1(amount):
    '''The minimum number of coins to make an amount.

    This version has a time complexity of `O(3^n)`. It cannot solve 107 in a
    reasonable amount of time.

    Arguments:
        amount (non-negative int):
            The amount to be met.

    Returns:
        coins (int):
            The minimum number of coins required to make amount using
            coins of denomination 1, 4, and 5.
    '''
    # We must have a non-negative amount to make.
    # Having this case return infinity is useful.
    if amount < 0:
        return math.inf

    # Base cases.
    if amount == 0: return 0  # no coins
    if amount == 1: return 1  # one 1¢
    if amount == 4: return 1  # one 4¢
    if amount == 5: return 1  # one 5¢

    # What's the sub-solution for 1¢ less, 4¢ less, and 5¢ less?
    sub_solutions = [
        coins(amount - 1),
        coins(amount - 4),
        coins(amount - 5),
    ]

    # The solution is one coin more than the best sub-solution.
    return min(sub_solutions) + 1


def coins_v2(amount, denoms=[1,4,5]):
    '''The minimum number of coins to make an amount.

    This is the generalization of v1 to arbitrary denominations.

    This version is still too slow to solve 107. It has a time complexity of
    `O(d^n)` where `d` is the number of denominations.

    Arguments:
        amount (non-negative int):
            The amount to be met.
        denoms (list of positive int):
            The denominations of coins to use.

    Returns:
        coins (int):
            The minimum number of coins required to make an amount using
            the given denominations of coins.
    '''
    if amount < 0: return math.inf
    if amount == 0: return 0
    if amount in denoms: return 1

    sub_solutions = [coins(amount - i, denoms) for i in denoms]
    return min(sub_solutions) + 1


def coins_v3(amount, denoms=[1,4,5], memo=None):
    '''The minimum number of coins to make an amount.

    This version introduces a memo to reduce the runtime complexity to `O(d*n)`.

    In the previous versions, recursive calls on different paths duplicate work
    for the same input. We eliminate redundant work by storing results in a
    dictionary. The second time we need those results, we look it up rather
    than falling into recursive calls.

    Arguments:
        amount (non-negative int):
            The amount to be met.
        denoms (list of positive int):
            The denominations of coins to use.
        memo (dict):
            A dictionary of sub-solutions. The default is to create a new,
            empty dictionary. You can pass your own dictionary to be populated
            or a dictionary used by a previous call of the same denominations.

    Returns:
        coins (int):
            The minimum number of coins required to make an amount using
            the given denominations of coins.
    '''
    if memo is None: memo = {}
    if amount in memo: return memo[amount]

    if amount < 0: return math.inf
    if amount == 0: return 0
    if amount in denoms: return 1

    sub_solutions = [coins(amount - i, denoms, memo) for i in denoms]
    solution = min(sub_solutions) + 1

    memo[amount] = solution
    return solution
