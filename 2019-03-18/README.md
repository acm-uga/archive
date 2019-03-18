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

