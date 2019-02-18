---
title: "Greed is Good"
date: 2019-02-18
---

# Greed is Good

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

# A Scheduling Problem

You are a busy Computer Science student at UGA trying to stay on top of your schedule but you're struggling to keep up! There must be a better way - and you're going to use a computer to find it! To stay organized, you have a list of tasks that must be completed today along with the amount of time they'll take and the priority of each. 

You put each task into an array and create a two dimensional array with all of your tasks:
```
[[name of task 1, amount of time needed, priority], ... , name of task n-1, amount of time needed, priority]]
```

## Input:
| Task Name           | Time Needed | Priority |
|---------------------|-------------|----------|
| `Attend class`      | 60          | 1        |
| `Workout at Ramsey` | 45          | 3        |
| `Get coffee at JJ's`| 20          | 4        |
| `Go to CSIP`        | 75          | 2        |
| `Go to study group`| 20          | 4         |
| `Go to CSIP`        | 75          | 2        |


