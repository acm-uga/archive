# Welcome to CSIP!
### Feburary 5th, 2020

Welcome! We will start with three open-ended coding questions you might be asked over the phone, 
and then move into hard-code questions at various difficulty levels.

Feel free to hand a copy of your resume or LinkedIn url to any current officer, and they will have it back to you with 
critique by the next meeting!


## P1: Beginner

Anyone getting started in their CS career, give these problems a shot.

- Write a function that gives the nth fibonacci. Do it both recursively and iteratively.



## P2: Underclassperson

For those with a little more exposure to data-structures, try this:

- Given a value k, generate all well ordered numbers of length k. 
Well ordered means that digits should be in increasing.

```
Example:
Input : K = 7
Output :
1234567 1234568 1234569 1234578 1234579
1234589 1234678 1234679 1234689 1234789 
1235678 1235679 1235689 1235789 1236789 
1245678 1245679 1245689 1245789 1246789 
1256789 1345678 1345679 1345689 1345789 
1346789 1356789 1456789 2345678 2345679 
2345689 2345789 2346789 2356789 2456789 
3456789
```


## P3: Upperclassperson

You are made of code.

 - Chef has a binary tree. The binary tree consists of 1 or more nodes. 
 Each node has a unique integer id. Each node has up to 2 children, 
 which are identified by their ids, and each node is the child of at 
 most 1 other node. A node X is considered to be an ancestor of node Y 
 if node Y is a child of node X or if there is some node Z for which X 
 is an ancestor of Z and Y is a child of Z. No node is an ancestor of itself. 
 A special node called the root node is an ancestor of all other nodes.
 
Chef has forgotten which node of his tree is the root, and wants you to help him to 
figure it out. Unfortunately, Chef's knowledge of the tree is incomplete. 
He does not remember the ids of the children of each node, but only remembers the 
sum of the ids of the children of each node.

Input:
  Input begins with an integer T, the number of test cases. Each test case begins with an integer N, 
  the number of nodes in the tree. N lines follow with 2 integers each: the id of a node, and the 
  sum of the ids of its children. The second number will be 0 if the node has no children.
  
 Output:
  For each test case, output on a line a space separated list of all possible values for the id of the root 
  node in increasing order. It is guaranteed that at least one such id exists for each test case.
  
 ```
 Example
 Input:
2
1
4 0
6
1 5
2 0
3 0
4 0
5 5
6 5
  Output:
 4
 6
 ```

# Solutions
