---
title: "Stock Buy/Sell and Exact Change"
date: 2018-11-12
---

# P1: Stock Buy & Sell to Maximize Profit

You are given an array containing the forecasted price of a certain stock over several days. Each element is a non-negative integer giving the price of that stock in dollars for the associated day.

You trade the stock by picking one day to buy and one day to sell. Write a program to compute the profit of the best single trade you could make on those days.

Remember that you must have bought stock before you can sell it!

## Examples

| Input                | Output |
|----------------------|--------|
| `[7, 1, 5, 3, 6, 4]` | 5      |
| `[7, 6, 4, 3, 1]`    | 0      |

For the first example, the best profit is $5 by buying on day 2 ($1) and selling on day 5 ($6). Time travel is not allowed. You cannot earn $6 by buying on day 2 ($1) and selling on day 1 ($7)

For the second example, no trade could ever earn a profit. The best you can do is to hold for a profit of 0.


# P2: Exact Change

You are given an amount of money and asked to make change, but you only have coins of denomination 1¢, 4¢, and 5¢. What is the fewest number of coins you could use to make exact change?

You only need to give the total number of coins, not the amounts of each denomination.

## Examples

| Input | Output                         |
|-------|--------------------------------|
| 8     | 2 coins (two 4¢)               |
| 13    | 3 coins (two 4¢, one 5¢)       |
| 25    | 5 coins (five 5¢)              |
| 107   | 22 coins (nineteen 5¢, two 4¢) |

## Hints

Recursion is a good place to start with this problem. However, you may run into an exponential time complexity. Dynamic programming can cut that down to `O(n)`.

## Bonus

Return the number of coins broken down by denomination.


# Solutions

Per usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
