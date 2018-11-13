def best_trade_v1(values):
    '''The best single trade you could make given forecasted values.

    This version has a time complexity of `O(n^2)`.

    Arguments:
        values (list of numbers):
            The forecasted values of the thing to be traded.

    Returns:
        buy (int):
            The time to buy.
        sell (int):
            The time to sell.
        profit (int):
            The profit of the trade.
    '''
    # The profit of buying on day `b` and selling on day `s`.
    def profit(b, s):
        return values[s] - values[b]

    buy = 0  # The best day to buy.
    sell = 0  # The best day to sell.

    # Loop over every combination of days.
    # We cut the inner loop short because we must buy before sell.
    n = len(values)
    for i in range(n):
        for j in range(i):
            if profit(buy, sell) < profit(j, i):
                buy = j
                sell = i

    return buy, sell, profit(buy, sell)


def best_trade_v2(values):
    '''The best single trade you could make given forecasted values.

    This version has a time complexity of `O(n)`.

    Arguments:
        values (list of numbers):
            The forecasted values of the thing to be traded.

    Returns:
        buy (int):
            The time to buy.
        sell (int):
            The time to sell.
        profit (int):
            The profit of the trade.
    '''
    # The profit of buying on day `b` and selling on day `s`.
    def profit(b, s):
        return values[s] - values[b]

    buy = 0  # The best day to buy.
    sell = 0  # The best day to sell.
    lo = 0  # The day with the lowest value.

    # We loop over all the days. At the end of each loop, we ensure `buy`,
    # `sell`, and `lo` are correct for the forecast up to that day.
    for today, value in enumerate(values):
        if values[today] < values[lo]:
            lo = today
        if profit(buy, sell) < profit(buy, today):
            sell = today
        if profit(buy, sell) < profit(lo, today):
            buy = lo
            sell = today

    return buy, sell, profit(buy, sell)
