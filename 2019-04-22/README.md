---
title: "Shuffle a Deck and Do a BST Check"
date: 2019-04-22
---

For today's session, we won't follow a problem type theme as we've done previously. Instead we'll cover some various problems that are known to be popular choices in technical interviews. Remember when you're studying for interviews that the subject matter can touch on just about anything you've learned in your Computer Science classes (and sometimes things you haven't!). While this might make you feel like preparation isn't useful - the opposite is true! The better you understand the fundamentals - the easier it is to break down and solve problems you haven't seen before.


## P1: Card Shuffle
You have a deck of standard playing cards which contains:

- 4 suits: clubs (♣), diamonds (♦), hearts (♥) and spades (♠)
- 10 number cards per suit: Ace (1) through 10
- 3 face cards per suit: King (K), Queen (Q), and Jack (J)
- 52 cards total

We will assume that the deck is represented with an array but the rest of the implementation is up to you.

Given this array of cards, can you write an algorithm to shuffle the deck both effectively and efficiently?


## P2: Validate a BST
A binary search tree (BST) is a binary tree such that:

- The value of the root is greater than or equal to the values of all nodes in the left subtree,
- The value of the root is less than or equal to the values of all nodes in the right subtree, and
- Both the left and right subtrees are also BSTs.

Given a binary tree of numbers, determine if it is a valid binary search tree.

Your input is given as an **s-expression**, a way of describing trees as lists. In an s-expression, the empty tree is represented by a null value. Otherwise, the s-expression is a triple `[val, left, right]` where `val` is the value of the root node and `left` and `right` are s-expressions describing the left and right subtrees.

### S-Expressions

This s-expression:

    [4,
        [2,
            [1, None, None],
            [3, None, None]
        ],
        [6,
            [5, None, None],
            [7, None, None]
        ]
    ]

describes this tree:

          4
       /     \
      2       6
     / \     / \
    1   3   5   7

which is a valid BST.

### Examples

| Input                                   | Output |
|-----------------------------------------|--------|
| `[4, [2, None, None], [6, None, None]]` | true   |
| `[4, [6, None, None], [2, None, None]]` | false  |
| `None`                                  | true   |


## Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
