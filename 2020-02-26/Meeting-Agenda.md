# Welcome to CSIP!
### Feburary 26th, 2020
#### This Page URL: https://tinyurl.com/rvvbcp5
#### Attendance URL (In email as well): https://tinyurl.com/ttlytr6

Welcome! We will start with 2 logic questions often asked during 30 minute in person screens, 
and then move into hard-code questions at various difficulty levels. Solutions to these questions are at the end of the
file -- look if you want, but it's to your benefit to try the problems before seeing the answers.
SPECIAL: Each of these three coding problems I had to code in 20 minutes apiece. They were part of my AT&T interview.

Feel free to hand a copy of your resume or LinkedIn url to any current officer, and they will have it back to you with 
critique by the next meeting!

.

.

.

.

## Screen 1
 - You have a scale, and 8 pool balls. One of them weighs more than the others. What is the least number of weighs you can use to find which ball that is?
 
 ## Screen 2
  - You have 3 baskets. Each baskets contains either:
    B1: Oranges
    B2: Apples
    B3: Both
 However, the labels are incorrect, and you cannot see inside. You may withdraw a SINGLE fruit from a basket.
 Then you must correctly identify which basket is which.

.

.

.

.

## P1

This problem is the easiest out of the set.

- You are a robber. There is a rich neighborhood with houses all neatly lined up.
Conveninently, the security systems suck, and if you rob NON-ADJACENT houses, the alarms do not
go off. Given an array of the dollar amount you would be able to rob from each house,
return the highest total you could steal.
NOTE: You may only loop through the array a single time.

```
Example:
  Input: 1 4 2 6 9 9 2 3
  Output: 22
  Logic: You can rob every other, so
    1 + 2 + 9 + 2 = 14
    4 + 6 + 9 + 3 = 22
```



## P2

This problem is the second easiest. There are two approaches to it, one of which you could take after having only completed
1301...
There is a third approach, and it will work, but it is slower, and violates the NOTE.

- You are given an array of 1000 integers. Every integer in the list can be defined as -10,000 <= x <= 10,000.
Print out or return an array of the repeated integers. If a number repeats more than twice, still only print it once.
NOTE: Only loop through the array once.

```
Example:
Input : [ -9999, 10, 6, 7, 2, -9999, 6, 20 ... ]
Output :
-9999, 6, ...
```


## P3

This problem was the hardest, and I did not fully solve it during the interview -- Its solution is not lengthy, however.

 - You are given a binary tree of ints, and a number. Return true if there exists a ROOT to LEAF path 
 that adds up to the provided number. Otherwise, return false.
 
```
Example:
Input : 23
```
![Image of Yaktocat](https://media.geeksforgeeks.org/wp-content/cdn-uploads/sum_property_tree1.gif)
```
Output : True
```
 

# Solutions

## P1

Java Solution
```
int oddHouses = 0;
int evenHouses = 0;
for(int i = 0; i < givenArray.length; i++) {
 evenHouses += givenArray[i]; // Remember that 0 is even
 i++;
 oddHouses += givenArray[i];
}
System.out.print((evenHouses > oddHouses ? evenHouses : oddHouses));
```

## P2

Java Solution
```
int [] duplicates = new Int[20,000];
int temp;
// Record duplicates
for(int i = 0; i < givenArray.length; i++) {
 temp = givenArray[i];
 if(temp < 0) {
  temp = temp*-1 + 10,000
 }
 duplicates[temp] += 1;
 if(duplicates[temp] == 2) {
  System.out.print(givenArray[i])
 }
}
```

## P3

Java Solution
```
boolean haspathSum(Node node, int sum)  
    { 
        if (node == null) 
            return (sum == 0); 
        else 
        { 
            boolean ans = false; 
   
            /* otherwise check both subtrees */
            int subsum = sum - node.data; 
            if (subsum == 0 && node.left == null && node.right == null) 
                return true; 
            if (node.left != null) 
                ans = ans || haspathSum(node.left, subsum); 
            if (node.right != null) 
                ans = ans || haspathSum(node.right, subsum); 
            return ans; 
        } 
    }
```
