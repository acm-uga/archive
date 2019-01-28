---
title: "Play with Arrays"
date: 2019-01-22
---

# A[r,[r,a],y,s]

This week, we will be reviewing the topic of arrays. The concept of arrays are usually one of the very first concepts taught in a Computer Science curriculum and with good reason! Arrays are really important to understand since they are the framework behind many of the data structures we use, along with the actual architecture of our memory systems in our computers.

An array is defined as a collection of items stored at contiguous memory locations arranged as a numbered sequence, so that each individual item can be referred to by its position number or index. By storing multiple items together like this, we can easily calculate the position of an element by imply adding an offset to a base value, i.e., the memory location of the first element of the array.

![Array Representation](https://cdncontribute.geeksforgeeks.org/wp-content/uploads/array-2.png)

# P1: 2 Sum

You are given an array of integers and a target number. Return the indices of the two numbers such that they add up to the given target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

## Example

**Input**:
```
[2, 7, 11, 15], target = 9
```
**Output**
```
[0,1]
```

# P2: Combination Sum

Similar to the previous question, you are given an array of integers and a target number. Find all unique combinations in the array in which integers sum to target.

The same repeated number may be chosen from the array an unlimited number of times.

**Input**:
```
[2,3,6,7], target = 7,
```

**Output**

A solution set is:
```
[
  [7],
  [2,2,3]
]
```

# Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
