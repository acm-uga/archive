---
title: "Polish Phones"
date: 2019-04-29
---

## P1: Phone Strings

If you've ever watched an infomercial, you probably know that phone numbers can represent strings. However, the same phone number can represent *multiple* strings. The image below shows which numbers correspond to which letters.

![A telephone keypad using the ITU E 1.161 International Standard.](https://en.wikipedia.org/wiki/Telephone_keypad#/media/File:Telephone-keypad2.svg)

From the image above, we see that the number 2 can represent the letters 'A', 'B', or 'C'; the number 3 can represent the letters 'D', 'E', or 'F'; and so on. Each digit can represent the three letters following those represented by the previous digit, with the exception of 8 and 9 which can represent four letters. The 0 is a special case that can represent a space. The buttons for 1, pound, and star do not represent any letters.

For today's first problem, given a string containing the digits 2 through 9 and 0, return all strings that could be represented by those digits.

### Examples

| Input | Output                                               |
|-------|------------------------------------------------------|
| `2`   | `a`, `b`, `c`                                        |
| `23`  | `ad`, `bd`, `cd`, `ae`, `be`, `ce`, `af`, `bf`, `cf` |


## P2: RPN Parser

An RPN expression is an arithmetic expression written in reverse Polish notation, a.k.a. postfix notation. In other words, the operator comes after both of its arguments.

For example, this RPN expression:

	123 456 + 789 *

is equivalent to this expression, in the usual infix notation:

	(123 + 456) * 789

Note that RPN expressions never require parentheses.

For this problem, your task is to generate a **parse tree** for a given RPN expression. The parse tree of an RPN expression is a binary tree where the leaf nodes are the numbers, and the branch nodes are the operators.

For example, the expression above yields this parse tree:

          *
         / \
        +   789
       / \
    123   456

The input string only contains integers and the operators `+`, `-`, `*`, and `/`. Each token is separated by exactly one space.

To get started, you can use this simple binary tree class:

```python
class BinaryTree:
    def __init__(self, root, left=None, right=None):
        '''Construct a binary tree.

        Arguments:
            root (str or int): The value of the root node.
            left (BinaryTree or None): The left subtree.
            right (BinaryTree or None): The right subtree.
        '''
        self.root = root
        self.left = left
        self.right = right
```


## Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
