---
title: "Play with Arrays"
date: 2019-01-28
---

# Arrays

This week, we will be reviewing the topic of arrays. The concept of arrays are usually one of the very first concepts taught in a Computer Science curriculum and with good reason! Arrays are really important to understand since they are the framework behind many of the data structures we use, along with the actual architecture of our memory systems in our computers.

An array is defined as a collection of items stored at contiguous memory locations arranged as a numbered sequence, so that each individual item can be referred to by its position number or index. By storing multiple items together like this, we can easily calculate the position of an element by imply adding an offset to a base value, i.e., the memory location of the first element of the array.

![Array Representation](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/array-2.png)


# P1: 2 Sum

You are given an array of integers and a target number. Return the indices of the two numbers such that they add up to the given target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Example

| Array            | Target       | Output      |
|------------------|--------------|-------------|
| `[2, 7, 11, 15]` |            9 | `[0, 1]`    |


# P2: Longest Monotonically Increasing Subsequence

A ***monotonically increasing sequence*** is a sequence where every value is greater than or equal to the previous.

Given an array or random integers, return the index and length of the longest monotonically increasing subsequence.

## Example

| Input                      | Subsequence    | Start Index | Length |
|----------------------------|----------------|-------------|--------|
| `[4, 1, 3, 5, 4]`          | `[1, 3, 5]`    |           1 |      3 |
| `[5, 6, 7, 2, 4, 7, 9, 7]` | `[2, 4, 7, 9]` |           3 |      4 |
| `[]`                       | `[]`           |           0 |      0 |


# Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
