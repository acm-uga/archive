---
title: "Greed is Good"
date: 2019-02-18
---

A greedy algorithm is a simple, intuitive algorithm that is used in optimization problems. True to it's name - a greedy algorithm always makes the choice that appears to be the best at that moment. The hope is that a locally-optimal solution will lead us to a globally-optimal solution.

```
Finding the largest integer using greedy choices (marked with an x)
                    ----
                     7x    
                   /   \
                  3      12x
                /   \      \
               1     2      19x    
```

Greedy algorithms work well when you have a problem that needs to be optimized (either maximized or minimized) at a given point. At each decision, the greedy algorithm has only **one** chance to make a decision so it never goes back and reverses the decision. You will notice this is very different than backtracking or dynamic programming! Due to this behaviour, a greedy strategy can often result in the wrong solution as seen in the example below:

```
Finding the largest integer using greedy choices (marked with an x)
                    ----
                     7x    
                   /     \
                  3       12x
                /   \    /   \
              99     2  5     6x    
```
Obviously the correct value should be **99** but the greedy algorithm fails to find the largest sum. This error is due to it making decisions only based on information available on a given step rather than evaluating the problem as a whole. With that being said, greedy algorithms are really successful with other types of problems such as Huffman encoding, used for data compression, and Dijkstra's Shortest Path Algorithm.
