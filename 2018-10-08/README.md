---
title: "With and Without Parens"
date: 2018-10-08
---

# Problem 1: Recognize Matching Parens

You are given a string containing only braces, brackets, and parens. Determine whether the string contains only valid groupings.

## Examples

| Input          | Output |
|----------------|--------|
| `"({[]})"`     | True   |
| `"[{}()][]"`   | True   |
| `"()}]"`       | False  |
| `"[{]}"`       | False  |
| `"[{}"`        | False  |


# Problem 2: RPN Calculator

Evaluate arithmetic formulas in postfix notation, also known as *reverse polish notation*. The calculator should support addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).

## Examples

| Postfix             | Infix                     | Value          |
|---------------------|---------------------------|----------------|
| `1`                 | `1`                       | 1              |
| `1 2 +`             | `(1 + 2)`                 | 3              |
| `1 2 + 3 *`         | `((1 + 2) * 3)`           | 9              |
| `1 2 + 3 4 + /`     | `((1 + 2) / (3 + 4))`     | 3/7 = 0.4286   |
| `1 2 * 3 - 4 5 + /` | `((1 * 2) - 3) / (4 + 5)` | -1/9 = -0.1111 |

## Hints
Unlike infix notation, postfix notation never requires
parenthesis or an order of operations.
