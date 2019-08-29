---
title: "New Semester!"
date: 2019-04-29
---

Welcome! We're trying something new this semester. Today we have a selection of problems broken down by experience level.


## P1: Freshperson

For those just getting started in their CS career, give these problems a shot.

- Write a function that reverses a string in place (HINT: do not use StringBuilder or any library objects / functions)

- Write a function that checks whether or not a word is a palindrome.

- BONUS: implement both above recursively

**NOTE**: Both should ideally be in O(n) time. If you don't know what that is don't worry.


## P2: Underclassperson

For those with a little more exposure to data-structures, try this:

- Write a function that finds the first non-repeated character in a string in O(n) time


## P3: Upperclassperson

Here are a pair of problems for those looking for a challenge

First, write a function that prints all permutations of a string.

```
Example:
- Input -> "abc"
- Output -> "abc", "acb", "bac", "bca", "cab", "cba"
```

Then write a function that prints all _subsets_ of a given string.

Remember that two subsets that differ only in ordering of their characters are the same subset.

```
Example:
- Input -> "123"
- Output -> "", "1", "2", "3", "12", "23", "123"
```


## P4: Bonus

Write a function that prints all words that can be generated from a given telephone number.

You can assume you have a function called `numToLet(int num)` that gives you the appropriate letters for a given number. For example, `numToLet(2)` returns the list `['a', 'b', 'c']`.

- All letters are lowercase (i.e., don't worry about uppercase).

- All numbers in a valid telephone number WITHOUT letters return a space, e.g. 0 and 1.


## Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
