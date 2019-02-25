---
title: "INSERT TITLE"
date: 2019-02-25
---

# TITLE

## P1: Memcpy
In the C library, there exists a useful function named **memcpy** which is used to copy a block of data from a source address to a destination address.

We declare it with the following function:
```
void *memcpy(void *str1, const void *str2, size_t n)
```
* str1 − This is a pointer to the destination array where the content is to be copied, type-casted to a pointer of type void*.
* str2 − This is a pointer to the source of data to be copied, type-casted to a pointer of type void*.
* n − This is the number of bytes to be copied.

We can see an example of the function in the character array below:
```
*s = pointer to source[0]
*d = pointer to destination[7]

memcopy(*s, *d, 3)

before:
char source[15] = | 'U' | 'G' | 'A' | ' ' | 'i' | 's' | ' ' | 't' | 'h' | 'e' | ' ' | 'b' | 'e' | 's' | 't' |

after:
char destination[15] = | 'U' | 'G' | 'A' | ' ' | 'i' | 's' | ' ' | 'U' | 'G' | 'A' | ' ' | 'b' | 'e' | 's' | 't' |
```

Can you write an implementation for **memcopy** given a character array like the example given?


## P2: Memmove

Now that you've implemented **memcpy**, you will realize it's a fairly simple (but fast) algorithm. A problem arises when copying from one location to another. If your intervals are overlapping, this could reuslt in **memcpy** overwritting the source while it's being read! Not good. We can see an example of this below:
```
char[] str = "foo-bar";
memcpy(&str[3],&str[4],4); //memcopy would fail
```
To remedy this, the C library includes a function called **memmove** which can handle overlaps correctly.

The declaration of **memmove** is very similar to **memcpy**
```
void *memmove(void *str1, const void *str2, size_t n)
```

Having already implemented **memcopy** and knowing it's shortcomings, can you adapt your code to create a function for **memmove**?

