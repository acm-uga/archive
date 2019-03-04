---
title: "Breeze in the Trees"
date: 2019-03-04
---
# Breeze in the Trees

This week, we will be focusing again on Trees. If you're hazy on your data structures, check out our previous [Introduction to Trees](https://csip-uga.github.io/problems/2018-12-03/README).

## P1: Minimal Tree

Our first problem will involve creating a binary search tree (commonly abbreviated as a BST). Remember that a BST is a tree in which each node has up to two children but no more. The height of a tree is the length of the longest path from the root to a leaf.

You are given a sorted array of unique integers that is in ascending order. Create an algorithm to create a binary search tree with minimal height.

### Example

**Input Array:**
`[1, 2, 3, 4, 5]`

**Output Tree:**
```
       4
     /   \
    2      5
  /   \      \
 1     3       6
```

Note that if you use the simple BST algorithm, you would end up with an unbalanced tree which can be seen in the example below. 
```
   1
    \
     2
      \
       3
        \
         4
          \
           5
```
An unbalanced tree like this would cancel out any search performance benefits we would usually get with a BST. Naturally we want to avoid this so your algorithm must be able to balance the BST.
