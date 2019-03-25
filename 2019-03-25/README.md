---
title: "Collect Em All"
date: 2019-03-25
---

For most of us, we learn about the concepts of data types in our very earliest introduction to Computer Science (CS1301 here at UGA). In essence, since Computer Science is the study of how data is stored and manipulated - we can consider data types as the building blocks of programming.

Languages like Java or C++ are considered statically-typed languages which means they do type checking (i.e. the process of verifying and enforcing the constraints of types) at compile-time as opposed to run-time. This results in a statically-typed language requiring each variable to be explicitly declared while a dynamically-typed language like Python skips this specification. This ease of declaration is one of the many reasons that Python is so concise (and why we recommend learning it!). 

An example of this can be seen below:

### Java Code
```
int result = 0;
for(int i=0; i<100; i++)
{
    result += i;
}
```

While in Python the equivalent operation could be written this way:

#### Python code
```
result = 0
for i in range(100):
    result += i
```
Just like Java, Python has built-in types like: ```int```, ```float```, ```bool```, and ```str```. ```int```, ```float```, and ```bool``` are considered to be simple or primitive data types because their values are not composed of any smaller parts. They cannot be broken down. On the other hand, strings and lists are different from the others because they are made up of smaller pieces. In the case of strings, they are made up of smaller strings each containing one character.

Types that are comprised of smaller pieces are called collection data types. Depending on what we are doing, we may want to treat a collection data type as a single entity (the whole), or we may want to access its parts. Collection data types tend to have tons of useful methods that can come in handy during a technical interview! Whatever your interviewing language, it's always a good idea to know your collection methods!

## P1: Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s. You may assume the string contains only lowercase alphabets.

### Example
```
Input: s = "anagram", t = "nagaram"
Output: true
```
```
Input: s = "rat", t = "car"
Output: false
```

## P2: Custom Collection

Design a collection that supports the following methods in constant time:

| Method                 | Description                                        |
|------------------------|----------------------------------------------------|
| `insert(elm)`          | Insert an element into the collection.             |
| `find(elm) -> bool`    | Return `true` if the element is in the collection. |
| `delete(elm)`          | Remove an element from the collection.             |
| `pick_random() -> elm` | Return a random element from the collection.       |


## Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
