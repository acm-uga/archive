---
title: "Say Yes to Compress"
date: 2019-03-18
---

An important topic in Computer Science is the concept of data compression.

Data compression is defined as a reduction in the number of bits needed to represent data. Compressing data can save storage capacity, speed up file transfer, and decrease costs for storage hardware and network bandwidth. Compression is performed by a program that uses a formula or algorithm to determine how to shrink the size of the data. Data compression can dramatically decrease the amount of storage a file takes up

## P1: Run Length Encoding

Run-length encoding (RLE) is a very simple form of lossless data compression in which runs of data (that is, sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run. This is most useful on data that contains many such runs.

Good candidates for RLE include simple graphic images such as icons, line drawings, Conway’s Game of Life, and animations. It is not useful with files that don't have many runs as it could greatly increase the file size. RLE schemes were used in the early transmission of television signals going back to 1967.

For our first problem, implement a method to perform basic string compression using the counts of repeated characters. If the compressed string doesn't result in a smaller string, simply return the original. You can assume the string only has uppercase and lowercase alphabetical letters (A-z).

### Example

| Input String      | Result        |
|-------------------|---------------|
| `aabcccccaaa`     | `a2b1c5a3`    |
| `AAAaaaAAAb`      | `A3a3A3b1`    |
| `a`               | `a`           |


## P2: Huffman Coding

Huffman coding is another lossless compression technique for text. In this technique, each character is represented by a variable length list of bits called Huffman codes, where the most common characters have the shortest codes. To compress some input, you simply replace each character with its corresponding Huffman code.

Here's the catch: since Huffman codes are variable length, how do you know when one ends and another begins? The solution is to ensure that no code is the prefix of another code. That is, you can't use both `01` and `011` since the first is a prefix of the second.

Your challenge is to build a table of Huffman codes for some input. How good is the compression using your table? What is the time complexity to produce your table?

### Example

Consider the input `this is an example of a huffman tree`. An optimal Huffman code table is given below:

| Character | Frequency | Code    |
|-----------|-----------|---------|
| space     |         7 | `111`   |
| a         |         4 | `010`   |
| e         |         4 | `000`   |
| f         |         3 | `1101`  |
| h         |         2 | `1010`  |
| i         |         2 | `1000`  |
| m         |         2 | `0111`  |
| n         |         2 | `0010`  |
| s         |         2 | `1011`  |
| t         |         2 | `0110`  |
| l         |         1 | `11001` |
| o         |         1 | `00110` |
| p         |         1 | `10011` |
| r         |         1 | `11000` |
| u         |         1 | `00111` |
| x         |         1 | `10010` |

Read that example input closely for a hint.


## Solutions

As usual, [sample solutions][csip-uga/archive] are posted on GitHub.

[csip-uga/archive]: https://github.com/csip-uga/archive
