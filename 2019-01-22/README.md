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

Simple right? Now let's visualize our factorial problem as a tree.

![Factorial Tree Representation](https://copingwithcomputers.files.wordpress.com/2013/11/factorialrecursion-e1384837049546.png)

This is where recursion gets to be really interesting in CS - we can use it to traverse trees! Meaning we can use recursion to visit (checking and/or updating) each node in a tree data structure, exactly once. This opens up all sorts of possibilites for solving problems with trees! If you're hazy on how trees work, check out our [previous Tree lecture](https://csip-uga.github.io/problems/2018-12-03/README).

Now that you understand the basics of recursion, let's try our coding problems for this week!


# P1: Height of a tree

Given the root of a binary tree of integers, write an algorithm that will return the height of the tree. The height of a tree is the length of the longest path to a leaf.

**Input**:
```
       2    <-- root
     /   \
    7      5
  /   \      \
 2     6       9    
     /   \     
    5     11
```
**Output**: 3.

The longest path would be 2, 7, 6, and either 5 or 11. This is three edges (or connections) between nodes which is the height of the tree.


# P2:



Given the root of a binary tree, write an algorithm that will compute the sum of the entire tree.



You can assume that each node has the following definition:


# Solutions
As usual, [sample solutions][csip-uga/archive] are posted on GitHub.
[csip-uga/archive]: https://github.com/csip-uga/archive

