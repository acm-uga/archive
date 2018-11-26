---
title: "Longest Run"
date: 2018-11-26
---

# P1: Longest Run

This week, we're looking at variations on a substring searching problem that we'll call the Longest Run.

We start by defining a __run__ as a contiguous substring containing exactly one unique character. The first problem this week is to find the length of the longest run in a string.

## Example

| Input                   | Output   | Explanation                  |
|-------------------------|----------|------------------------------|
| `"1222345"`             | 3        | The longest run is `222`.    |
| `"abccbaabc"`           | 2        | Both `cc` and `aa` are runs. |


# P2: Longest 2-Run

For our next problem, we'll generalize the fist.

Let's define an __*m*-run__ as a contiguous substring containing up to *m* unique characters. The second problem is to find the length of the longest 2-run in a string.

## Example

| Input                   | Output   | Explanation                        |
|-------------------------|----------|------------------------------------|
| `"abbcba"`              | 4        | The longest 2-run is `bbcb`.       |
| `"121232345"`           | 4        | Both `1212` and `2323` are 2-runs. |


# Bonus: Longest *m*-Run

The naive solution to the longest 2-run above involves a nested loop with a worst case runtime in `O(n^2)`. To find the longest 3-run, you'd need a doubly nested loop with a worst case runtime in `O(n^3)`. And in general, the naive solution to find the longest *m*-run is in `O(n^m)`.

But there's a better way! Using dynamic programming, we can solve any *m*-run problem in `O(n)`.

Can you write a function that takes a string and *m* and returns the length of the longest *m*-run in `O(n)`?


# Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
