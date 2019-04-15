---
title: "Attributes of Primes and Roots"
date: 2019-04-15
---

## P1: Square Root

Today's first problem is easy to describe and lends itself to a variety of solutions: given an integer, `n`, compute its square root.

For simplicity's sake, we'll say that `n` is a non-negative integer less than `2^24`. It can be losslessly cast to a single precision float. Your output should be a single precision float that is accurate to three decimal places.

You may use a calculator to compute a few square-roots offline, but computing a table of all possible square roots doesn't count as a solution.

### Examples

For reference, `2^24 = 16,777,216`.

| Input      | Output   |
|------------|----------|
|          2 |    1.414 |
|      4,096 |   64.000 |
| 16,777,216 | 4096.000 |

## P2: Find the Primes

> “Mathematicians have tried in vain to this day to discover some order in the sequence of prime numbers, and we have reason to believe that it is a mystery into which the human mind will never penetrate.”
>
> -Leonhard Euler, 18th century mathematician

A prime number is an integer that is greater than 1 and has only two factors: 1 and itself. Remember that factors of a number are a set of numbers that when multiplied together equal the original number. For example, the numbers 3 and 7 are factors of 21. The number 12 has factors 2 and 6, but also 3 and 4.

Every number has factors of 1 and itself. The numbers 1 and 21 are factors of 21. The numbers 1 and 12 are factors of 12. If no other factors exist for that number, then that number is **prime**.

Given a positive integer `n` less than `2^16` (65,536), find all prime numbers less than or equal to `n`.

### Examples

| Input  | Output                                                    |
|--------|-----------------------------------------------------------|
|      1 | 1, 2                                                      |
|      5 | 1, 2, 3, 5                                                |
|     12 | 1, 2, 3, 5, 7, 11                                         |
|     50 | 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47 |


## Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
