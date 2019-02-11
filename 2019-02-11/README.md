---
title: "Weird Bases"
date: 2019-02-11
---

# Counting in base N

As a computer science student, you're likely familiar with counting in different bases.

For this problem, you are given two natural numbers `b` and `d`, and your task is to generate all `d` digit numbers in base `b`.

Each "number" is represented as a list of `d` integers in "big endian" meaning the most significant digit comes first (the usual way humans write numbers). For example, in base 10, the number 1337 would be represented by the list `[1, 3, 3, 7]`. In base 16, the number 0xAF would be represented be `[10, 15]` (because A is 10 and F is 15).

## Example

| Input        | Numbers          | Output                             |
|--------------|------------------|------------------------------------|
| `b=2`, `d=2` | 00, 01, 10, 11   | `[[0, 0], [0, 1], [1, 0], [1, 1]]` |
| `b=6`, `d=1` | 0, 1, 2, 3, 4, 5 | `[[0], [1], [2], [3], [4], [5]]`   |


# Rhyme Schemes

In poetry, we have a syntax for talking about rhyme schemes. For example, a three line poem could have the rhyme schemes `AAA`, `AAB`, `ABA`, `ABB`, or `ABC`. Each letter corresponds to a unique syllable at the end of each line. Lines marked by the same letter rhyme. The first line is always marked by an `A` and you can't use a new letter unless you have used the previous letter, e.g. you can't use `C` unless you've used `B`.

For this problem, your task is to generate all possible rhyme schemes for a poem of `n` lines. We'll use numbers instead of letters to make things easier, where 0 represents `A`, 1 represents `B`, etc.

## Example

| Input | Output                                                    |
|-------|-----------------------------------------------------------|
| `2`   | `[[0, 0], [0, 1]]`                                        |
| `3`   | `[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [0, 1, 2]]` |


# Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
