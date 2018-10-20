---
title: "Sudoku"
date: 2018-10-22
---

Sudoku is a number placement game invented by Howard Garns under the name Number Place and popularized by Japanese puzzle magazine Nikoli.

Sudoku is played on a 9x9 board subdivided into nine 3x3 blocks. The goal is to fill the board with the numbers such that every row, column, and block contain the numbers one through nine exactly once. In general, there are many ways to form a valid board, but in practice players start from a partially filled board which yields exactly one solution.

{:style="line-height:1"}
```

╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
║ 5 │ 3 │   ║   │ 7 │   ║   │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 6 │   │   ║ 1 │ 9 │ 5 ║   │   │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │ 9 │ 8 ║   │   │   ║   │ 6 │   ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║ 8 │   │   ║   │ 6 │   ║   │   │ 3 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 4 │   │   ║ 8 │   │ 3 ║   │   │ 1 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║ 7 │   │   ║   │ 2 │   ║   │   │ 6 ║
╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
║   │ 6 │   ║   │   │   ║ 2 │ 8 │   ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║ 4 │ 1 │ 9 ║   │   │ 5 ║
╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
║   │   │   ║   │ 8 │   ║   │ 7 │ 9 ║
╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝

```

Can you write a program to solve Sudoku?


# Formal Description

You are given a 9x9 2D array representing a Sudoku board. All elements of the array take integer values zero through nine, where zero indicates empty space. You are also given a function, `check_sudoku`, which takes a 2D array and returns true if the (possibly partial) Sudoku board it represents is valid. If you prefer, you may assume the `check_sudoku` function throws an exception for invalid arrays.

You must implement a function, `solve_sudoku`, which accepts the input array and returns a similar array, except all zeros have been eliminated and the result is still a valid Sudoku. You may modify the input array in-place.


# Hints

One conceptually simple algorithm for these kinds of constraint satisfaction algorithms is called **[backtracking][]**. For each point where a decision needs to be made, you make one arbitrarily. If you ever find yourself in an invalid state, you "backtrack" to your most recent decision point and try again. If you exhaust all possible choices without finding a solution, you backtrack to the second most recent decision point, et cetera. Eventually, you'll either find a solution or exhaust all possible states and prove that no solution exists.

[backtracking]: https://en.wikipedia.org/wiki/Backtracking


# Solution

Per usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
