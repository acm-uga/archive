# CSIP 2018-10-01

## Problem 1: Color Counting

A class of students have responded to a poll asking what is their favorite color. Given the array of their responses, what is the most popular color and how many students chose it?

### Examples
For the sake of example, we'll use single letters to represent colors. For example, `'r'` for red, `'y'` for yellow, `'b'` for blue, `'k'` for black, etc.

| Input                                            | Output   |
|--------------------------------------------------|----------|
| `['c', 'v', 'c', 'b', 'm']`                      | `'c', 2` |
| `['w', 'r', 'r', 'w', 'c', 'w', 'v']`            | `'w', 3` |
| `['r', 'o', 'b', 'y', 'b', 'm', 'g', 'b', 'b']`  | `'b', 4` |


## Problem 2: Generate Matching Parens

Given a non-negative even integer `n`, generate all strings of length `n` that consist only of valid matching parens, without duplicates.

### Examples

| Input | Output                                           |
|-------|--------------------------------------------------|
| 0     | None                                             |
| 2     | `()`                                             |
| 4     | `(())`, `()()`                                   |
| 6     | `((()))`, `(())()`, `()(())`, `(()())`, `()()()` |
