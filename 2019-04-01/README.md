---
title: "Strings, Bools, and Aprils Fools"
date: 2019-04-01
---

## P1: Canonical Gmail Address

Gmail has some nifty features with their email addresses. You can insert extra periods (`.`) anywhere in your username to use as separators. You can also append a plus (`+`) followed by arbitrary text, which causes emails sent to that address to be automatically tagged with that text.

Your boss wants you to develop some service that does not allow users to register multiple times with different versions of the same email address. To accomplish this, implement a function to _canonicalize_ the Gmail address by eliminating any extra periods or auto-tags.

### Examples

| Input                     | Output           |
|---------------------------|------------------|
| foobar@gmail.com          | foobar@gmail.com |
| foo.bar@gmail.com         | foobar@gmail.com |
| foobar+baz@gmail.com      | foobar@gmail.com |
| foobar+baz+qux@gmail.com  | foobar@gmail.com |
| foo.bar+baz@gmail.com     | foobar@gmail.com |


## P2: Integer to Roman Numeral

Roman numerals are represented by seven different symbols: ```I, V, X, L, C, D and M.```

| Symbol | Value  |
|--------|--------|
| I      | 1      |
| V      | 5      |
| X      | 10     |
| L      | 50     |
| C      | 100    |
| D      | 500    |
| M      | 1000   |

For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9.
    X can be placed before L (50) and C (100) to make 40 and 90.
    C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

### Examples

| Input      | Output       | Explanation                            |
|------------|--------------|----------------------------------------|
| ```3```    | ```III```    |                                        |
| ```4```    | ```IV```     |                                        |
| ```9```    | ```IX```     |                                        |
| ```58```   | ```LVIII```  | L = 50, V = 5, III = 3                 |
| ```1994``` | ```MCMXCIV```| M = 1000, CM = 900, XC = 90 and IV = 4 |
