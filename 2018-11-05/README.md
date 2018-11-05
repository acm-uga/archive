---
title: "Merge Median"
date: 2018-11-05
---

# P1: Merge Median

Consider a set of integers partitioned into two arrays. Both arrays are sorted, but their range of values may overlap. Given these two arrays, can you compute the median of the set?

You may assume that the number of elements in the set is odd.

## Example

| Input                 | Interpretation            | Output |
|-----------------------|---------------------------|--------|
| `[1, 3]`, `[0, 2, 4]` | `median([0, 1, 2, 3, 4])` | 2      |
| `[3, 8, 9]`, `[]`     | `median([3, 8, 9])`       | 8      |

## Bonus

1. Does your algorithm work in `O(n)` time and `O(1)` space?
2. Does your algorithm work with an even number of integers?

Remember, the median of an even set is defined as the midpoint between the two elements in the middle of the set, e.g.:

| Input              | Interpretation         | Output |
|--------------------|------------------------|--------|
| `[1, 2]`, `[3, 4]` | `median([1, 2, 3, 4])` | 2.5    |
