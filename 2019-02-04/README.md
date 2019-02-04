---
title: "Beachfront Frequencies"
date: 2019-02-04
---

# Beachfront Frequencies

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100.

Determine the perimeter of the island.

### Example:

### Input:
```
[[0,1,0,0],

 [1,1,1,0],

 [0,1,0,0],

 [1,1,0,0]]
```

### Output:
```
16
```

### Explanation:

The perimeter is the 16 yellow stripes in the image below:

![Island Perimeter](https://assets.leetcode.com/uploads/2018/10/12/island.png)


## Top K Frequent Words ##

Given a non-empty list of words, return the k most frequent elements. Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

### Input: ###
```
["let's", "go", "dawgs", "let's", "go", "sic", "em"], k = 2
```

### Output: ###
```
["go", "let's"]
```

### Explanation: ###
``` "let's" ``` and ```"go"``` are the two most frequent words. Note that ```"go"``` comes before ```"let's"``` due to a lower alphabetical order.


# Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
