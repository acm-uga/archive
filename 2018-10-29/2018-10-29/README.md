---
title: "Image Rotation & Online Average"
date: 2018-10-29
---

# P1: Image Rotation

You are given a grayscale image, represented as an array with shape `H x W`. Each pixel of the image is a floating point value between 0 and 1 giving the intensity.

Write a method to rotate the image by 90 degrees. Can you do this in place?

{:style="line-height:1"}
```
Input:
╔═══╤═══╤═══╗
║ 1 │ 2 │ 3 ║
╟───┼───┼───║
║ 4 │ 5 │ 6 ║
╟───┼───┼───║
║ 7 │ 8 │ 9 ║
╚═══╧═══╧═══╝

90 degree clockwise rotation:
╔═══╤═══╤═══╗
║ 7 │ 4 │ 1 ║
╟───┼───┼───║
║ 8 │ 5 │ 2 ║
╟───┼───┼───║
║ 9 │ 6 │ 3 ║
╚═══╧═══╧═══╝
```

## Hint

There are many ways to solve this problem but matrix manipulation techniques from Linear Algebra are very helpful to know!


# P2: Online Average

One day, your boss asks you for the average of `n` numbers. "No problem" you say, because you know the formula for the mean. Two weeks later, your boss brings you `m` new numbers and asks for an update to your previous average. You remember the previous average, and you remember how many numbers were used; the problem is, you've lost the original numbers themselves. How do you compute the new average?

## Hint

This boils down to a math problem:

- Let `x` be a list of numbers, e.g. `(x[1], x[2], x[3], ...)`.
- Let `M(n)` be the mean of the first `n` numbers.
- Write a formula for `M(n)` in terms of `M(n-1)` and the next value `x[n]`.


# Solutions

Per usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
