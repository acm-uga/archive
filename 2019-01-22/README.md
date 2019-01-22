---
title: "Fun with Recursion"
date: 2019-01-22
---

# An Introduction to Recursion

>"To understand recursion, one must first understand recursion."

This week, we will be reviewing the topic of recursion. Recursion is a fundamental concept of Computer Science yet many people seem to struggle with this concept. Hopefully we will be able to clear things up!

"Recursion" comes from the adjective "recursive" which originates from the Latin verb "recurrere", which means "to run back". This is actually a great defintion of exactly what a recursive function does: "running back" or returning to itself. Generally we use recursion in Computer Science to break a problem into subproblems which may be easier to solve than the whole.

Every recursive function has to fulfil an important condition to be used in a program: it has to be able to terminate. In order to do this, it must include a base case. A base case is a condition in which the problem can no longer be broken into smaller subproblems with further recursion. If you don't have a base case to terminate the recursion, you would create an infinite loop - not good!

The first example used in many lectures on recursion involves calculating a factorial. For those that don't remember what a factorial is:

A factorial is defined as the product of an integer and all the integers below it.
```
n! = n(n - 1)(n - 2)... 1
0! = 1
1! = 1
2! = 2 x 1 = 2
3! = 3 x 2 x 1 = 6
...
```
Notice that a factorial has a base case which is 0! and 1!. Once a problem reaches this point, it can't go any further so it must terminate. We could visualize this in Python code as follows:
```
def factorial(n):
    #Base case
    if n == 1:
        return 1
    #Recursive function call
    else:
        return n * factorial(n-1)
```

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

