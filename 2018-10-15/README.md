# CSIP 2018-10-15

Sign in: https://tinyurl.com/csip-contact


## Linked List Review

A doubly linked list consists of nodes which contain three parts: a value, a pointer to the next node, and a pointer to the previous node. The following figure demonstrates a list with four nodes:

```
+------------+    +------------+    +------------+    +------------+
| Value:  10 |    | Value: 2   |    | Value: 42  |    | Value: 99  |
+------------+    +------------+    +------------+    +------------+
| Next  ========> | Next  ========> | Next  ========> | Next: NULL |
+------------+    +------------+    +------------+    +------------+
| Prev: NULL | <========  Prev | <========  Prev | <========  Prev |
+------------+    +------------+    +------------+    +------------+
```

A doubly linked list in Java might look something like this:

```java
class Node {
	int value;
	Node next;
	Node prev;
}
```


## Problem 1: Insertion Sort

Given the first node of a doubly linked list, sort the list using [insertion
sort][1]. Here's a quick explanation of insertion sort. Starting at the front
of the list, for each node, move the node backwards in the list until the
value in the previous node is less than or equal to the value in the current
node.

See [this graphic][2] for a visual explanation.

Hint: The nodes can be moved to the proper position in one move.

[1]: https://en.wikipedia.org/wiki/Insertion_sort
[2]: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif


## Problem 2: Merge

Given the first nodes of two sorted doubly linked lists, merge them into one. In the case of equal values, the values from the first list should come before values in the second list, and equal values in the same list should maintain their relative order.

This is a subroutine for merge sort.


## Bonus: Merge Sort

Conceptually, a [merge sort][3] works as follows:

1. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
2. Repeatedly merge adjacent sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.

See [this graphic][4] for a visual explanation.

Hint: There are two ways to implement merge sort. The "top-down" approach is recursive; the "bottom-up" approach is iterative. In our case, the top-down algorithm is way easier. But if our lists wrapped around, then the bottom-up algorithm would be feasible. By "wrap around" I mean that the `prev` pointer of the first node points to the last node, and the `next` pointer of the last node points to the first node.


[3]: https://en.wikipedia.org/wiki/Merge_sort
[4]: https://en.wikipedia.org/wiki/Merge_sort#/media/File:Merge-sort-example-300px.gif
