# Interview Questions

www.CrackingTheCodingInterview.com

## Arrays and Strings

Please note that array questions and string questions are often **interchangeable**. That is, a question that this book states using an array may be asked instead as a string question, and vice versa.

### Hash Tables

A hash table is a **data structure** that maps keys to values for highly efficient lookup. There are a number of ways of implementing this. Here, we will describe a simple but common implementation.

- First, compute the key's hash code

- Then, map the hash code to an index in the array

- At this index, there is a linked list of keys and values

Q1: What if too many *hash code* maps to the same *index*?

### ArrayList & Resizable Arrays

In some languages, arrays (often called lists in this case) are automatically resizable. The array or list will grow as you append items. In other languages, like Java, arrays are fixed length. The size is defined when you create the array.