---
title: "Breeze in the Trees"
date: 2019-03-04
---

This week, we will be focusing again on Trees. If you're hazy on your data structures, check out our previous [Introduction to Trees](https://csip-uga.github.io/problems/2018-12-03/README).


## P1: Balanced Binary Search Tree

Our first problem will involve creating a binary search tree (commonly abbreviated as a BST). Remember that a **binary tree** is a tree in which each node has up to two children but no more. A **binary search tree** is a tree used to represent a sorted sequence, where the root node contains some item in the sequence, and the left/right subtrees represent the sequence before/after the root item. In a **balanced binary search tree** the tree is balanced, implying that the root node holds the item in the middle of the sequence and each subtree is also balanced.

Like a sorted list, a balanced binary search tree allows you to search the collection in `O(log(n))` time. Unlike a sorted list, BSTs are often implemented as linked structures. This allows them to perform both insert and delete operations in `O(log(n))` time, while a sorted list requires `O(n)` time. However, BSTs are not a panacea. Despite having better time complexity for insert and delete, linked data structures perform worse than array-based data structure in practice for small collections.

### The Problem

Given a sorted array of integers in ascending order, construct a balanced binary search tree.

### Example

#### Input Array:

`[1, 2, 3, 4, 5]`

#### Output Tree:

```
       4
     /   \
    2      5
  /   \      \
 1     3       6
```

#### Incorrect Output:

Note that the following tree is technically a binary search tree, but not a *balanced* binary search tree. When the BST is not balanced, it can no longer guarantee `O(log(n))` time complexity for any of its operations.

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


## P2: Efficient Range Queries

Consider this scenario. You are given a list of integers and asked to find the minimum value between two indices. The catch is that you will need to support millions of queries over different ranges for the same list of numbers. To support this task, you decide to preprocess the list into a new data structure that supports this query efficiently.

You may spend as much time as needed constructing the data structure so long as the queries themselves are fast.


## Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
