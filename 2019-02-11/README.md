---
title: "Keep the Heap"
date: 2019-02-11
---

# Keep the Heap

Building upon some previous concepts we've seen in CSIP recently, this week we are going to discuss Heaps. Heaps are an extremely
useful data structure to understand and be able to implement but many people don't seem to have a good grasp of the concept even
after taking Data Structures. Hopefully we can change that today!

A heap is defined as a specialized tree-based data structure which is essentially an almost complete tree that satisfies the 
heap property.

*If you're hazy on your tree data structures - check out our previous [tree introduction](http://https://csip-uga.github.io/problems/2018-12-03/README "tree introduction")*

There are two types of heaps: a maximum heap and a minimum heap.

### Max Heap
- The root node of a max heap is the highest value in the heap.
- The value of each node is less than or equal to the value of its parent.

## Min Heap
- The root node of a minimum heap is the lowest value in the heap.
- The value of each node is greater than or equal to the value of its parent.


### Example:



### Input:

```

[[0,1,0,0],



 [1,1,1,0],



 [0,1,0,0],



 [1,1,0,0]]

```



### Output:

```

16

```



### Explanation:



The perimeter is the 16 yellow stripes in the image below:



![Island Perimeter](https://assets.leetcode.com/uploads/2018/10/12/island.png)





## Top K Frequent Words ##



Given a non-empty list of words, return the k most frequent elements. Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.



### Input: ###

```

["let's", "go", "dawgs", "let's", "go", "sic", "em"], k = 2

```



### Output: ###

```

["go", "let's"]

```



### Explanation: ###

``` "let's" ``` and ```"go"``` are the two most frequent words. Note that ```"go"``` comes before ```"let's"``` due to a lower alphabetical order.





# Solutions



As usual, [sample solutions][csip-uga/archive] are posted on GitHub.



[csip-uga/archive]: https://github.com/csip-uga/archive

