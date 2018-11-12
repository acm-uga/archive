def stock(values):
    memo = []

    best_buy = 0
    best_sell = 0
    best_profit = 0

    for sell_day, value in enumerate(values):
        if sell_day == 0:
            memo.append(0)
            continue

        buy_day_a = memo[sell_day - 1]
        buy_day_b = sell_day - 1
        if values[buy_day_a] < values[buy_day_b]:
            buy_day = buy_day_a
        else:
            buy_day = buy_day_b

        profit = values[sell_day] - values[buy_day]
        memo.append(buy_day)

        if best_profit < profit:
            best_buy = buy_day
            best_sell = sell_day
            best_profit = profit

    return best_buy, best_sell, best_profit
