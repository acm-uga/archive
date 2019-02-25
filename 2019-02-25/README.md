---
title: "Arrays for Days"
date: 2019-02-25
---

## P1: `memmove(3)`
In the C library, there exists a useful function named **memmove** which is used to copy a block of data from a source address to a destination address.

The function has the following signature:

```
void *memmove(void *dest, const void *src, size_t n)
```

Where each argument has the following purpose:

- `dest`: The pointer to the destination where the data is to be copied.
- `src`: The pointer to the first byte of data to be copied.
- `n`: The number of bytes to copy.

One important feature of `memmove` is that it works even when the source and destination overlap.

### The problem

We will implement a function that is like `memmove` but for arrays. Thus you can use any programming language you'd like. Your function should take four inputs:

- `data`: The array in being manipulated;
- `dest`: The index into the array where the data is to be copied.
- `src`: The index of the first element to be copied.
- `n`: The number of elements to copy.

Remember that your code must work when the source and destination overlap!


### Example

| Input Array                | dest | src | n | Result                     |
|----------------------------|------|-----|---|----------------------------|
| `[_, _, A, B, C, _, _, _]` |    5 |   2 | 3 | `[_, _, A, B, C, A, B, C]` |
| `[_, _, A, B, C, _, _, _]` |    3 |   2 | 3 | `[_, _, A, A, B, C, _, _]` |
| `[_, _, A, B, C, _, _, _]` |    1 |   2 | 3 | `[_, A, B, C, C, _, _, _]` |


## P2: Deque

A double-ended queue is a queue that allows you to push and pop from both the front and back of the list and to access any element by index, all in constant time. For this problem, you will need to design and implement a data structure that supports these operations.

### Details

You should define a class with the following methods:

- **Deque(capacity)**: The constructor should take a capacity. Your deque may panic or throw an exception if the user tries to use more than the initial capacity.
- **push_front(val)** / **push_back(value)**: The deque must have methods to insert at both ends.
- **pop_front()** / **pop_back()**: The deque must have methods to remove elements from both ends.
- **get(i)**: The deque must have a methods to access elements by index.

### Bonus

As a bonus, you may support reallocation to increase the capacity when the user tries to insert more elements than you have capacity. This reallocation may take linear time but **must not** effect the *amortized* runtime of the above methods.


## Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
