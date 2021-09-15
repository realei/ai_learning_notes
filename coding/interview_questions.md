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

When you need an array-like data structure that offers **dynamic resizing**, you would usually use an Arraylist. An Arraylist is an array that resizes itself as needed while still providing 0(1) access. A typical implementation is that when the array is full, the array doubles in size. Each doubling takes 0( n) time, but happens so rarely that its amortized insertion time is still O(1).

**This is an essential data structure for interviews.** Be sure you are comfortable with dynamically resizable arrays/lists in whatever language you will be working with. Note that the name of the data structure as well as the "resizing factor" (which is 2 in Java) can vary.

### StringBuilder

- Remember:

  `1 + 2 +3 + ... + n = n*(n+1)/2`
  
  So: O(x + 2x + ... + nx) ~~ O(xn^2)

- StringBuilder simply creates a resizable array of all the strings, copying them back to a string only when necessary.


## Linded Lists

A linked list is a data structure that represents a sequence of nodes. In **a singly linked list**, each node points to the next node in the linked list. **A doubly linked list** gives each node pointers to both the next node and the previous node.

**Unlike an array**, a linked list does not provide constant time access to a particular "index" within the list. This means that if you'd like to find the Kth element in the list, you will need to iterate through K elements.

### Creating a Linked List

**Remember** that when you're discussing a linked list in an interview, you must understand whether it is a singly linked list or a doubly linked list.

### Deleting a Node from a Singly Linked List

Deleting a node from a linked list is fairly straightforward. Given a node `n`, we find the previous node `prev` and set `prev.next` equal to `n.next`. If the list is **doubly linked**, we **must also** update `n.next` to set `n.next`. prev equal to `n.prev`. The important things to remember are:

1. to check for the null pointer 
2. to update the head or tail pointer as necessary.

Additionally, if you implement this code in C, C++ or another language that requires the developer to do **memory management**, you should consider if the removed node should be deallocated.

### The "Runner" Technique

**The "runner" (or second pointer) technique** is used in many linked list problems. The runner technique means that you iterate through the linked list with two pointers simultaneously, with one ahead of the other. The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each one node that the "slow" node iterates through.

### Recursive Problems

A number of linked list problems rely on recursion. If you're having trouble solving a linked list problem, you should explore if a recursive approach will work. We won't go into depth on recursion here, since a later chapter is devoted to it.

However, you should remember that **recursive algorithms take at least O(n) space**, where n is the depth of the recursive call. **All recursive algorithms can be implemented iteratively**, although they may be much more complex.
