# Hash-Table

The goal of this project was to replicate a python dictonary/java map. 

This hash-table implementation supports insert, delete, get, and to_list methods. It uses linear probing with a probing factor inputed as a paremeter when created to reduce clustering. Lazy deletion is used.

Prime numbers are used for the size of the hash array to reduce collisons and create a wide spread distribution of items. The inital array size is 11. Each time the mapping reaches a size of half capacity from insertions, the size is doubled and then the closest prime number is used before re-hashing.

