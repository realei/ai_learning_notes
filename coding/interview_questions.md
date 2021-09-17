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

## Stacks and Queues

Questions on stacks and queues will be much easier to handle if you are comfortable with the ins and outs of the data structure. The problems can be quite tricky, though. While some problems may be slight modifications on the original data structure, others have much more complex challenges.

### Implementing a Stack 

The stack data structure is precisely what it sounds like: a stack of data. In certain types of problems, it can be favorable to store data in a stack rather than in an array. **A stack uses LIFO (last-in first-out) ordering.** That is, as in a stack of dinner plates, the most recent item added to the stack is the first item to be removed.

It uses the following operations:

	* `pop()`: Remove the top item from the stack.
	* `push(item)`: Add an item to the top of the stack.
	* `peek()`: Return the top of the stack.
	* `isEmpty()`: Return true if and only if the stack is empty.

Unlike an array, a stack does not offer constant-time access to the i^th item. However, it does allow constant­time adds and removes, as it doesn't require shifting elements around.

**One case where stacks are often useful is in certain recursive algorithms.** Sometimes you need to push temporary data onto a stack as you recurse, but then remove them as you backtrack (for example, because the recursive check failed). A stack offers an intuitive way to do this.

**A stack can also be used to implement a recursive algorithm iteratively.** (This is a good exercise! Take a simple recursive algorithm and implement it iteratively.)

### Implementing a Queue

**A queue implements FIFO (first-in first-out) ordering**. As in a line or queue at a ticket stand, items are removed from the data structure in the same order that they are added.

It uses the operations:

    * `add(item)`: Add an item to the end of the list.
	* `remove()`: Remove the first item i the list.
	* `peek()`: Return the top of the queue.
	* `isEmpty()`: Return true if and only if the queue is empty.

A queue can also be implemented with a **linked list**. In fact, they are essentially the same thing, as long as items are added and removed from opposite sides.

It is especially easy to mess up the updating of the first and last nodes in a queue. Be sure to double check this.

**One place where queues are often used is in breadth-first search or in implementing a cache.**

In breadth-first search, for example, we used a queue to store a list of the nodes that we need to process. Each time we process a node, we add its adjacent nodes to the back of the queue. This allows us to process nodes in the order in which they are viewed.

## Trees and Graphs

Many interviewees find **tree and graph problems** to be some of the trickiest. Searching a tree is more complicated than searching in **a linearly organized data structure such as an array or linked list**. Additionally, the worst case and average case time may vary wildly, and we must evaluate both aspects of any algorithm. Fluency in implementing a tree or graph from scratch will prove essential.

### Types of Trees

A nice way to understand a tree is with a recursive explanation. **A tree is a data structure composed of nodes.**

* Each tree has a root node. (Actually, this isn't strictly necessary in graph theory, but it's usually how we use trees in programming, and especially programming interviews.)

* The root node has zero or more child nodes.

* Each child node has zero or more child nodes, and so on.

The tree cannot contain cycles. The nodes may or may not be in a particular order, they could have any data type as values, and they may or may not have links back to their parent nodes.

Tree and graph questions *are rife with 充斥着* ambiguous details and incorrect assumptions. Be sure to watch out for the following issues and seek clarification when necessary.

#### Trees vs. Binary Trees

**A binary tree** is a tree in which each node has up to two children. Not all trees are binary trees. For example, this tree is not a binary tree. You could call it a ternary tree(Check the book).

There are occasions when you might have a tree that is not a binary tree. For example, suppose you were using a tree to represent a bunch of phone numbers. In this case, you might use a 10-ary tree, with each node having up to 10 children (one for each digit).

A node is called a "leaf" node if it has no children.

#### Binary Tree vs. Binary Search Tree

**A binary search tree** is a binary tree in which every node fits a specific ordering property: `all left descendents <= n < all right descendents`. This must be true for each `node n`.

```
The definition of a binary search tree can vary slightly with respect to equality. Under some definitions, the tree cannot have duplicate values. In others, the duplicate values will be on the right or can be on either side. All are valid definitions, but you should clarify this with your interviewer.
```

When given a tree question, many candidates assume the interviewer means *a binary search tree*. Be sure to ask. A binary search tree imposes the condition that, for each node, its left *descendents 后代们* are less than or equal to the current node, which is less than the right descendents.

#### Balanced vs. Unbalanced 

While many trees are balanced, not all are. Ask your interviewer for clarification here. **Note that balancing a tree does not mean the left and right subtrees are exactly the same size** (like you see under "perfect binary trees" in the following diagram).

One way to think about it is that a "balanced" tree really means something more like "not terribly imbalanced:' It's balanced enough to ensure `0(log n)` times for insert and find, but it's not necessarily as balanced as it could be.

Two common types of balanced trees are **red-black trees** (pg 639) and **AVL trees** (pg 637). These are discussed in more detail in the Advanced Topics section.

- **Complete Binary Trees**

  A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the last level. To the extent that the last level is filled, it is filled left to right.

- **Full Binary Trees**

A full binary tree is a binary tree in which every node has either zero or two children. That is, no nodes have only one child.

- **Perfect Binary Trees**

A perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this level has the maximum number of nodes.

Note that perfect trees are rare in interviews and in real life, as a perfect tree must have exactly 2^k - 1 nodes (where k is the number of levels). In an interview, do not assume a binary tree is perfect.

### Binary Tree Traversal 遍历

- **In-Order Traversal**

In order traversal means to "visit"(often, print) the left branch, then the cuirrent node, the right branch.

- **Pre-Orcder Traversal**

Pre-order traversal visits the current node before its child nodes (hence the name "pre-order").

In a pre-order traversal, the root is always the first node visited.

- **Post-Order Traversal**

Post-order traversal visits the current node after its child nodes (hence the name "post-order").

In a post-order traversal, the root is always the last node visited.

### **Binary Heaps (Min-Heaps and Max-Heaps)**

We'll just discuss min-heaps here. Max-heaps are essentially equivalent, but the elements are in descending order rather than ascending order.

A min-heap is a *complete* binary tree (that is, totally filled other than the rightmost elements on the last level) where each node is smaller than its children. The root, therefore, is the minimum element in the tree.
