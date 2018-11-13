---
title: "Stock Buy/Sell and Exact Change"
date: 2018-11-12
---

# P1: Stock Buy & Sell to Maximize Profit

You are given an array that has the price of stocks each day. Each element is a positive integer but can include zero. An example input could be `[100, 180, 260, 310, 40, 535, 695]`.

You are only allowed to buy or sell stock each day. Find and return the maximum profit that you can make by buying and selling in those days.

Remember that you must have bought stock before you can sell it!

## Examples

| Input            | Output |
|------------------|--------|
| `[7,1,5,3,6,4]`  | 5      |
| `[7,6,4,3,1]`    | 0      |

For the first example, you buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5, **not** 7-1 = 6 because selling price needs to be larger than buying price.

For the second example, no transaction is done, i.e. max profit = 0.


# P2: Exact Change

What is the fewest number of coins you need to make exact change of some amount?

For this problem, lets assume that we have an infinite amount of coins in the denominations 1¢, 4¢, and 5¢. If we wanted to form 13¢ of change, we would need three coins (two 4¢ and one 5¢). Your goal is to write an algorithm that will take some value and return the minimum number of coins in these three denominations needed to make value.

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
