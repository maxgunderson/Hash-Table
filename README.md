# Hash-Table

This project aims to replicate the functionality of Python dictonaries or Java maps through a custom hash table implementation. It uses linear probing with a probing factor inputed as a parameter during creation, to minimize clustering. In addition lazy deletion is used to improve efficiency.

## Features
- Insert: Adds key-value pairs to the table.
- Delete: Removes key-value pairs from the table.
- Get: Returns value associated with a specific key,
- To_list: Converts contents of table into list for easy visualization.

## Hashing Technique 

The hash table utilizes prime numbers for the size of the array to reduce collisons and create a wide spread distribution of items. The inital array size is 11. Each time the mapping reaches a size of half capacity from insertions, the size is doubled and then the closest prime number is used before re-hashing.

