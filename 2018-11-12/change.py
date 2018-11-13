from functools import lru_cache

@lru_cache(maxsize=None)
def change(amount):
    # We must have a non-negative amount to make.
    # Having this case return infinity is useful.
    if amount < 0:
        return float('inf')

    # Base cases.
    if amount == 0: return 0  # no coins
    if amount == 1: return 1  # 1 * 1¢
    if amount == 2: return 2  # 2 * 1¢
    if amount == 3: return 3  # 3 * 1¢
    if amount == 4: return 1  # 1 * 4¢
    if amount == 5: return 1  # 1 * 5¢

    # What's the solution for 1¢ less, 4¢ less, and 5¢ less?
    sub_solutions = [
        change(amount - 1),
        change(amount - 4),
        change(amount - 5),
    ]

    # The solution is one more coin than the best sub-solution.
    return min(sub_solutions) + 1
