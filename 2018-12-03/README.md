---
title: "Tree is company"
date: 2018-12-03
---

# An Introduction to Trees

This week, we will be reviewing the Tree data structure. For those of you who haven't taken Data Structures or simply need a refresher, let's go ahead and define a tree.

A tree is best described recursively as data structure composed of nodes that fulfill the following conditions:
- Each node contains a value or data.
- Nodes are connected by edges.
- The first node of the tree is called the root node.
- The root node has zero or more child nodes.
- Each child node has zero or more child nodes, and so on...

```
      tree
      ----
       j    <-- root
     /   \
    f      k
  /   \      \
 a     h      z    <-- leaves
```

Other things to note:
- A node is called a "leaf" node if it has no children.
- A binary tree is a tree in which each node has up to two children but no more.
- The height of a tree is the length of the longest path to a leaf.
- The depth of a node is the length of the path to its root.


# P1: Sum of a Tree

Given the root of a binary tree, write an algorithm that will compute the sum of the entire tree.

You can assume that each node has the following definition:

```
Tree {
    data: int;
    left: Tree;
    right: Tree;
}
```

The `left` and/or `right` subtree may be null.

For languages with tuples, you may use a 3-tuple to represent nodes of a binary tree, e.g. `(data, left, right)`.

## Example

**Input**:
```
        15
     /      \
    10       20
  /   \     /  \
 8     12  25   16
```

**Output:** 106


# P2: Trimming a Binary Search Tree

A **binary search tree** is a binary tree with the additional constraint that the **in-order traversal** yields values in sorted order.

Consider the following tree:

```
        11
     /      \
    5        20
  /   \     /  \
 1     10  19   25
```

The in-order traversal is the list of nodes in left-to-right order, regardless of vertical position. In this example, the in-order traversal is `[1, 5, 10, 11, 19, 20, 25]`. Since these values are sorted, the tree is a valid binary search tree.

For this problem, you are given the root node of a binary search tree and two values, called `min` and `max`. You must produce a new binary search tree, which is like the first, but contains no nodes with values less than `min` or greater than `max`.

You may not eliminate nodes with values between `min` and `max` (inclusive), and you may not insert nodes which did not exist in the original tree. The nodes in the new tree must maintain the same ancestor relationships, though some generations may be removed.

## Example

**Input**:
```
tree:
        11
     /      \
    5        20
  /   \     /  \
 1     10  19   25

min: 5
max: 19
```

**Output:**
```
   11
 /    \
5      19
 \
  10
```


# Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
