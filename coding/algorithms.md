# Cracking the coding interview

## Big O

Stack space in **recursive** call counts.

### Drop the Constants

- O(N) = O(2N) = O(3N + 100)

### Drop the Non-Dominant Terms

- O(N^{2} + N) becomes O(N^{2})

- O(N + log N) becomes O(N)

- O(5x2^{N} + 1000xN^{100}) becomes O(2^{N})

Comutational cost:

o(x!) > O(2^{x}) > O(x^{2}) > O(x * log x) > O(x) > O(log x)

### Multi-Part Algorithms: Add vs. Multiply

Suppose you have an algorithm that has two steps. When do you multiply the runtimes and when do you add them?

This is a common source of confusion for  candidates.

### Amortized Time 摊销时间

An **Array List**, or a **dynamically resizing array**, allows you to have the benefits of an array while offering flexibility in size. You won't run out of space in the Arraylist since its capacity will grow as you insert elements.

**An Arraylist is implemented with an array. When the array hits capacity, the Arraylist class will create a new array with double the capacity and copy all the elements over to the new array.**

How do you describe the runtime of insertion? This is a tricky question. **The array could be full. If the array contains N elements, then inserting a new element will take O(N) time. You will have to create a new array of size 2N and then copy N elements over. This insertion will take O(N) time.**

However, we also know that this doesn't happen very often. The vast majority of the time insertion will be in O(1) time.

We need a concept that takes both into account. **This is what amortized time does.** It allows us to describe that, yes, this worst case happens every once in a while. But once it happens, it won't happen again for so long that the cost is "amortized.'

In this case, what is the amortized time? As we insert elements, we double the capacity when the size of the array is a power of 2. So after X elements, we double the capacity at array sizes 1, 2, 4, 8, 16, ... , X. That doubling takes, respectively, 1, 2, 4, 8, 16, 32, 64, ... , X copies.

What is the sum of 1 + 2 + 4 + 8 + 16 + ... + X? If you read this sum left to right, it starts with 1 and doubles until it gets to X. If you read right to left, it starts with X and halves until it gets to 1.

**What then is the sum of X + X/2 + X/4 + X/8 + ... + 1 ?This is roughly 2X.**

Therefore, X insertions take 0(2X) time. The amortized time for each insertion is 0(1).

### Log N Runtimes

We commonly see O(log N) in runtimes. Where does this  come from?

**This is a good takeaway for you to have. When you see a problem where the number of elements in the problem space gets halved each time, that will likely be a 0( log N) runtime.**

This is the same reason why finding an element in a balanced binary search tree is O ( log N). With each comparison, we go either left or right. Half the nodes are on each side, so we cut the problem space in half each time.

### Recursive Runtimes 递归运行时

**Try to remember this pattern.** When you have a **recursive function** that makes multiple calls, the runtime will often (but not always) look like **O(branches^{depth})**, where branches is the number of times each recursive call branches. In this case, this gives us O(2^{N}).
