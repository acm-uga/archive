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


## Problem 1

Given the first node of a doubly linked list, sort the list using [insertion
sort][1]. Here's a quick explanation of insertion sort. Starting at the front
of the list, for each node, move the node backwards in the list until the
value in the previous node is less than or equal to the value in the current
node.

See [this graphic][2] for a visual explanation.

Hint: The nodes can be moved to the proper position in one move.

[1]: https://en.wikipedia.org/wiki/Insertion_sort
[2]: https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif


## Problem 2

Given the first nodes of two sorted doubly linked lists, merge them into one. In the case of equal values, the values from the first list should come before values in the second list, and equal values in the same list should maintain their relative order.

This is a subroutine for merge sort.
