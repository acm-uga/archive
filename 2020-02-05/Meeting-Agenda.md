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

 - Make a Quine. That is, create a program that when run, produces its own source code. For a real challenge, do not step outside the program's scope, as in simply calling the file and telling it to print.
 

# Solutions

## P1
 - Recursive Solution
 ```
 public static int FibRecurse(int n) {
        if(n <= 1) { return n; }
        return FibRecurse(n-1) + FibRecurse(n-2);
    }
 ```
 
  - Iterative
 ```
 public static int FibIter (int n) {
        int firstNum = 1;
        int secondNum;
        int fibOfNth = 1;

        if(n <= 1) { return n; }

        for(int i = 2; i < n; i++) {
            secondNum = fibOfNth;
            fibOfNth += firstNum;
            firstNum = secondNum;
        }
        return fibOfNth;
    }
 ```

## P2
 - Solution
```
public static void printWellOrdered(int number, int x, int k) {
        if (k == 0) {
            System.out.print(number+" ");
            return;
        }
        // Try all possible greater digits
        for (int i = (x + 1); i < 10; i++) {
            printWellOrdered(number * 10 + i, i, k - 1);
        }
    }

// Generates all well ordered numbers of length k.
public static void generateWellOrdered(int k) {
    printWellOrdered(0, 0, k);
}
```

## P3
 - Solution
```
class Q{public static void main(String[]a){String s="class Q{public static void main(String[]a){String s=%c%s%1$c;System.out.printf(s,34,s);}}";System.out.printf(s,34,s);}}
```
