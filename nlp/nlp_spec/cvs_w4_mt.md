# Machine Translation

## Transforming word vectors

Welcome back, last week, you learned about word vectors and you saw that they can capture important properties of words. This week, you will make use of word vectors to learn to **align words in two different languages**, which will give you your first basic translation program. Later, I will teach you *locality sensitive hashing 局部敏感哈希* to speed it up.

### Overview of Translation

Let's first get an overview of machine translation by starting with an example of **English to French translation**. In order to translate an English word to a French word, **one way** would be to generate an *extensive 广泛的* list of English words and their *associated French word*.

If you ask the human to do this, you would find someone who knows both languages to start making a list. **If you want a machine to learn how to do this**, you would calculate *word embeddings associated with English and word embeddings associated with French*. **Next**, retrieve the English word embedding of a particular English word such as cats, **then** find some way to transform the English word embedding into word embedding that has a meaning in the French word vector space.

We will see how to convert from the English word vector space to the French word vector space in a moment. **Next**, you'll take the *transformed word vector* and search for word vectors in the French word vector space that are most similar to it. The most similar words are candidates words for your translation. If your machine does a good job, it's may find the word `chat`, which is the French word for cats. You'll want to find the matrix that can do this transformation for you. So let's talk about **transforming vectors using matrices**.

### Transforming vectors

To try this out for yourself, you can write the following code, which is also in the notebook associated with this lecture. Define the matrix R, then define the vector x, multiply x by R using np.dot, and the result is another two dimensional vector, which is what you saw earlier.

```
R = np.array([[2,0], [0,2]])
x = np.array([[1,1]])
np.dot(x,R)
```

`array([[2,-2]])`

### Align word vectors

Now that we know that there can be **a matrix that transforms our English word vectors into relevant French word vectors**, `XR ~~ Y` how do we define this transformation matrix, which we'll denote as `R`? We can start with a randomly selected matrix `R` and then see how it performs when you try to translate the English vectors in matrix `x` and compare that to the actual French word vectors, which is in the matrix `Y`.

In order for this to work, you will **first** need to get `a subset of English words` and `different equivalence 不同的相关对应`, get the respective *word vectors单字向量*, and stack the word vectors in their respective matrices `X` and `Y`. **The key here** is to keep the rows lined up or to align the word vectors. This means that if the first row of matrix X contains the word cat, then the first row of the matrix y should contain the French word for cats, which is chat.

Now you may be asking, wait a minute, if I already have the English words and their French translations, why do I need to train the model to do this? Why not just save this information in a key value mapping, like a python dictionary? Well, **the nice thing** is that **you can just collect a subset of these words to find your transformation matrix**. And if it works well, then the model can be used to translate words that are not part of your original training set. **So you only need to train on a subset of the English French vocabulary and not the entire vocabulary.**

### Solving for R

So let's see how to find a good matrix `R`. First, we compare the translation X times R with the actual French word embeddings in Y. We do this by taking the X matrix times the R matrix and subtracting the Y matrix. `Loss = || XR - Y ||_{F}`. I'll explain in more detail what this expression means and also what this capital F subscript means. But for now, think of it as a **measure** of how far apart the attempt to translation and the actual French vectors are. If you start with a random matrix R, you can gradually improve this matrix R in a loop:

  - First, compute the gradient by taking the derivative of this loss function with respect to the matrix R. 

  - Next, update the matrix R by subtracting the gradient, but note that it's the gradient rated by the learning grade alpha. You can either pick a fixed number of times to go through the loop or check the loss at each iteration and break out of the loop when the loss falls between a certain threshold.

### Frobenius norm 

Now, let's explain what this notation with the double vertical lines means. **This is measuring the magnitude or the norm of a matrix.** Let's see an example of calculating this norm and then see the general formula. Let's say that the results of XR- Y is a matrix. We'll pretend for this example that there's only two words in this dictionary, which is the number of rows in the matrix and the word embeddings have two dimensions. So that's the number of columns in the matrix. So matrices X, R, Y and A are all 2 by 2 matrices. If the matrix A looks like this, then to calculate its norm, we take 2 squared + 2 squared + 2 squared + 2 squared, then take square roots, this gives us 4. Here's the actual formula, you just take all the elements in the matrix, square them, and add them up. This norm has the subscript F because this is called the Frobenius norm.

**Now, let's calculate the Frobenius norm in code.** You start with a matrix A, use np.square to square all the elements, then use np.sum, then np.sqrt to get 4. Try it out for yourself. 

```
A = np.array([[2, 2],
			  [2, 2]])
A_squared = np.square(A)
A_squared
```

array([[4,4],
       [4,4]])

```
A_Frobenious = np.sqrt(np.sum(A_squared))
A_Frobenious
```

4.0

### Fibenius norm squared

*$||XR - Y||_{F}^{2}$*

**Know that in practice, it's easier to minimize the square of the Frobenius norm.** In other words, we can cancel out the square root by taking the square. I'll explain in a moment why it's easier to work with the square of the norm. If we go back to our example with matrix A, the square root of Frobenius norm is just 2 squared + 2 squared + 2 squared + 2 squared. Then we take the square root, but then cancel it out by squaring that sum. So the square of the Frobenius norm is 16.

### Gradient

Now, let's also go into detail on how you can calculate the gradient of the loss function.

  * The loss is defined as the square of the Frobenius norm.

  * The gradient is the derivative of the loss with respect to the matrix R.

If it looks like this, the scalar m is the number of rows or words in the subset that we're using for training. If you remember from calculus, this may look familiar to you if you pretend that R is a single variable instead of a matrix and X and Y are constants. If you don't recognize this, don't worry, you won't need to know calculus here. You'll be able to look up these derivatives online if you ever need to. Now going back to Y, it helps to use the square of the Frobenius norm. It's easier to take the derivative of this expression rather than dealing with the square root that's in the Frobenius norm. You will implement this formula in the assignment.

## [K-Nearest Neighbors](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/avTgO/k-nearest-neighbors)

One key operation needed to find a matching word in the previous video was finding the K-nearest neighbors of a vector. We will focus on this operation in the next few videos as it's a basic building block for many NLP techniques.

### Finding the translation

Notice that it transformed word vector after the transformation of its embedding through an R matrix would be in the French word vector space. But it is not going to be necessarily identical to any of the word vectors in the French word vector space. ut it is not going to be necessarily identical to any of the word vectors in the French word vector space. You need to search through the actual French word vectors to find a French word that is similar to the one that you created from the transformation. You may find words such as salut or bonjour, which you can return as the French translation of the word hello. **So the question is, how do you find similar word vectors?**

### Nearest neighbors

To understand how to find similar word vectors, let's look at a related question. How do you find your friends who are living nearby? Let's pretend that you are visiting San Francisco in the United States and you're visiting your dear friend Andrew. You also want to visit your other friends over the weekend, preferably those who live nearby. One way to do this is to go through your address book and for each friend get their address, calculate how far they are from San Francisco. So one friend is in Shanghai, the other friend is in Bangalore, and another friend is in Los Angeles. You can sort your friends by their distances to San Francisco, then rank them by how close they are. Notice that if you have a lot of friends, which I'm sure you do, this is a very *time intensive process 时间密集的过程*. Is there a more efficient way to do this? Notice that two of these friends live in another continent, while the third friend lives in the United States. Could you have just searched for a subset of friends who live in the United States? You might have realized that it may not have been necessary to go through all of your friends in your address in order to find the ones closest to you. You might have imagined if you somehow could filter on which friends were all in a general region, such as North America, then you could just search within that sub group of friends. If there is a way to slice up the geographic space into regions, you could search just within those regions. When you think about organizing subsets of a dataset efficiently, you may think about placing your data into buckets. If you think about buckets, then you'll definitely want to think about hash tables. **Hash tables are useful tools for any kind of work involving data, and you'll learn about hash tables next.**

### Summary

In this video, I showed you how using K-nearest neighbors you could translate a word even if it's transformation doesn't exactly match the word embedding in the desired language. And I introudced you to hash tables, a useful data structure that you will learn about in the next video.

## [Hash Tables and Hash Functions](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/UFnGD/hash-tables-and-hash-functions)

### Hash tables

So let us say you have several data items and you want to group them into buckets by some kind of similarity. One bucket can hold more than one item and each item is always assigned to the same bucket. So the results would be these blue *ovals 椭圆形* and up in bucket number one, these gray *rectangles 长方形*, and up in bucket number two. And these *magenta triangles 洋红色三角形* are assigned to buckets three.

Now let's think about how we'd like to do this with word vectors. **First**, let's assume that the word vectors have just 1 dimension instead the 300 dimensions. So each word is represented by a single number, such as 100, 14 ,17, 10 and 97. You need to find a way to give each vector a hash value which is a key that tells it which bucket it's assigned to. **A function that assigns a hash value is called a hash function.** In this example, here is a hash table which is a set of buckets. In this case, the hash table has ten buckets. Notice how the word vectors 100 and 10 are assigned to bucket 0. The word vector 14 is assigned to buckets 4 and the word vectors 17 and 97 are assigned to bucket 7. Do you notice a pattern?

`Hash function(vector) ------> Hash value`

`Hash value = vector%'number of buckets'`

This formula here is the hash function that's being used to assign the word vectors to their respective buckets. The *modulo operator 模运算符* takes the remainder after dividing by ten. The *remainder 余* is the hash value that tells us where the word vector should be stored. For example, 14 divided by 10 has a remainder of 4, so it goes to buckets 4.

### Create a basic hash table

```
# Python

def basic_hash_table(value_1, n_buckets):
    def hash_function(value_1, n_buckets):
	    return int(value) % n_buckets
	hash_table = {i:[] for i in range(n_buckets)}

	for value in value_1:
	    hash_value = hash_function(value, n_buckets)
		hash_table[hash_value].append(value)

	return hash_table
```

Now let's build a basic hash table in code. Here is a definition of a function that takes in a list of values. You can think of each value as a one-dimensional vector. It also takes in the number of pockets. Define the hash function used in the modulo operator. Then you create the hash table, notice that this is a dictionary comprehension. The key is an integer and the value is an empty list, which you'll use as a bucket for storage. For each word vector, calculate its hash value, then append it to the appropriate list. The hash table that is returned can be seen in the notebook that's goes with this vector. You will see that the hash table is the same as what you saw in the previous slide.

Now let's take another look at this basic hash table. Recall that **your original goal was to put similar word vectors into the same bucket**, but here it doesn't look like numbers that are close to each other are in the same bucket. For instance, 10, 14 and 17 are in different buckets. Ideally, you want to have a hash function that puts similar word vectors in the same bucket like this. To do this you'll need to use what's called **locality sensitive hashing. Locality is another word for location, sensitive is another word for caring. So locality sensitive hashing is a hashing method that's cares very deeply about assigning items based on where they're located in vector space. You'll learn about locality sensitive hashing next.**
