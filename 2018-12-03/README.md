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

## Example
**Input**:
```
        15
     /      \
    10       20
  /   \     /  \
 8     12  25   16
```

**Output:** 66

# Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
