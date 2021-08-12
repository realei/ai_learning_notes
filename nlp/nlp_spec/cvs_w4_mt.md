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

## [Locality sensitive hashing](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/ieYM6/locality-sensitive-hashing)

One key method that you will use to reduce the computational cost of finding k-nearest neighbors in high-dimensional spaces is locality-sensitive hashing. In this video, I will teach you what hashes are and where they are used.

### Locality sensitive hashing

To start thinking about locality-sensitive hashing, let's first assume that you're using word vectors with just two dimensions. I'll *depict 描绘* each vector as a circle instead of arrows. So let's say you want to find a way to know that these blue dots are somehow close to each other, and that these gray dots are also related to each other. **First**, divide the space using these dashed lines, which I'll call **planes**. I'll explain why I called them planes in a bit. Notice how the blue plane slices up the space into vectors that are above it or below it. The blue vectors all happen to be on the same side of the blue plane. Similarly, the gray vectors happen to be above the gray plane. It looks like the planes can help us bucket the vectors into subsets based on their location. This is exactly what you want. A hashing function that is sensitive to the location of the items that it's assigning into buckets. You're working your way towards locality-sensitive hashing.

### Planes

Now, let's see **why I'm calling these dashed lines planes.** A plane would be this magenta line into two-dimensional space, and it actually represents all the possible vectors that would be sitting on that plane. In other words, they would be parallel to the plane, such as this blue vector or this orange vector. You can define a plane with a single vector. This magenta vector is *perpendicular 垂直* to the plane, and it's called the **normal vector 法线向量** to that plane. **The normal vector is perpendicular to any vectors that lie on the plane.**

It might help to think about this in **three dimensions**. Find a sheet of paper and find a pencil. Place the paper on the table and draw some vectors on it, then hold the pencil vertically over the paper. Any vectors on the paper are perpendicular to the pencil.

### Which side of the plane?

Let's go back to two dimensions. You are able to see visually when the vector is on one side of the plane or the other, but how do you do this mathematically? Here are three sample vectors in blue, orange, and green. The normal vector to the plane is labeled P. Let's focus on vector 1. What if you take the dot product of P with vector one? You get three. I'll explain in a bit why you're doing this. Now, let's look at the vector 2. If you take the dot product of P with vector 2, you get zero. Finally, let's look at vector 3. If you take the dot product of P with vector 3, you get negative three. So the dot products are 3, 0, and negative 3. **Do you notice something about the signs and how they're related to their position relative to the red plane?** When the dot product is **positive**, the vector is on one side of the plane. If the dot product is **negative**, the vector is on the opposite side of the plane. If the dot product is **zero**, the vector is on the plane. 

### Visualizing a dot product

So what's the dot product doing? To visualize the dot product, imagine one of the vectors such as P, as if it's the surface of the Earth. **Gravity 重力** pulls all objects straight down towards the surface of the Earth. Next, pretend you're standing at the end of the vector, V1. You tie a *string 绳子* to a rock and let gravity pull the rock to the surface of vector P. The string is perpendicular to vector P. Now, if you draw a vector that's in the same direction of P but ends up at the rock, you'll have what's called the **projection 投影** of vector V1 onto vector P. The magnitude or length of that vector is equal to the dot product of V1 and P. Furthermore, if you had this other green vector and projected it onto vector P, the projected vector would be pointing in the parallel but opposite direction of P. The dot product would be a negative number. **This means that the *sign 符号* of the dot product indicates the direction of the projection with respect to the purple normal vector.** So whether the dot product is positive or negative can tell you whether the vector V1 or V2 are on one side of the plane or the other. 

### Which side of the plane?

```
def side_of_plane(P,v):
    dotproduct = np.dot(P, v.T)
	sign_of_dot_product = np.sign(dotproduct)
	sign_of_dot_product_scalar = np.asscalar(sign_of_dot_product)
    
```

Let's use code to check which side of the plane the vector is on. The function side of plane takes in the normal vector P, and the vector v. Use numpy dot to take the dot products. Use numpy.sign to get a plus one if the dot product is positive, minus one if the dot product is negative, or zero if the dot product is zero. I'm using numpy.asscalar. Notice the pronunciation of that function. If a vector can be represented as *a single scalar 单个纯量/标量*, this function *retrieves 提取* that scalar, and that's it. Please try it out for yourself.

## Multiple Planes

In this section, you will learn about combining information from multiple planes into a single hash value.

### Outline

* `Multiple planes ------>  Dot products ------> Hash values`

In the last video, you saw how by the sign of the dot product between the *normal vector of a plane* and *a vector representing your data*, you could get a relative position relative to that plane. In this lecture, I'm going to show you how to use this information for multiple planes to get a hash value for your data in your vector space.

### Multiple planes

In order to divide your vector space into manageable regions, you'll want to use more than one *plane 平面*. For each plane, you can find out whether a vector is on the positive or negative side of that plane. So you'll get multiple signals, one for each plane and you want to **find a way to combine all of those signals into a single hash value. This hash value will define a particular region within the vector space.**

### Multiple planes, single  hash value

Let's walk through an example. Then you will see the general formula for combining signals from multiple planes. So for a single vector, let's say that it's dot product with plane 1 is 3, so the sign is positive, and the hash value is set to 1 to indicate that the sign is positive(url). For the second plane, the dot product is 5, so the sign is again positive and the hash value is 1. For the third plane, the dot product is -2, so the sign is -1 and the hash value is set to 0 to Iindicate that the vector v is on the negative side of plane 3. To combine these intermediates hash values into a single hash value, you'll do the following. Take 2 to the power of 0 times h1 + 2 to the power of 1 times h2 + 2 to the power of 2 times h3, it gives us a combined hash value of 3. So just as a reminder you have multiple planes and it helps us to divide the vector space into smaller sub regions. But you want to have a single hash value, so you will know which *bucket 存储桶* to assign the vectoring. You do this by combining the signals from all the planes into a single hash value.

**Here are the rules you applied written out**, if the sign of the *dot product 点积* is greater than or equal to 0, assign the *intermediate hash value 中间值* of 1. Otherwise if the dot product is less than 0, assign the intermediate hash value of 0. To combine the intermediate as values, use this formula, **this is how you get locality sensitive hashing**. Let's implement this in code.

`$hash = sum_{i}^{H} 2^{i} x h_{i}$`

```
def hash_multiple_plane(P_1,v):
    hash_value = 0

	for i, P in enumerate(P_1):
	    sign = side_of_plane(P,v)
		hash_i = 1 if sign >= 0 elso 0
		hash_value += 2**i*hash_i
	
	return hash_value
```

Given a list of planes and vector, starts with a hash_value of 0, which you'll use to accumulate the sum of intermediate hash values. Then for each plane, you want to calculate the sign of the dot product. Set the intermediate hash_value to 1 if the sign is greater than or equal to 0. I'll set it to 0 then you multiply the intermediate add value by 2 raised to the 8th power and added to the hash_value. Finally, you return the hash_value.

So if you run code in the lecture notes book, you'll get the same results as the example you saw earlier, go ahead and try it out. >> Now you have seen what it means for a hash function to be locality sensitive, and examples of such hash functions. Next, you will see how this is useful for speeding up the k-nearest neighbor computation. Let's go to the next video.

## [Approximate nearest neighbors](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/Rnp5U/approximate-nearest-neighbors)

Good to see you again. In the last video, you learned about locality-sensitive hashing. Now it is time to put all this knowledge to use. You will make an algorithm that computes k-nearest neighbors much faster than *brute search*.

### Random planes

So far, we've seen that a few planes, such as these three, can divide the vector space into regions. But are these planes the best way to divide up the vector space? What if, instead, you divided the vector space like this? In fact, you can't know for sure which sets of planes is the best way to divide up the vector space, so why not create **multiple sets of random planes 多组随机平面**? so that you can divide up the vector space into multiple, independent sets of hash tables. You can think of it like creating multiple copies of the universe, or a *multiverse 多元宇宙*, if you will.  You can make use of all these different sets of random planes in order to help us find a good set of friendly neighborhood vectors, I mean, a set of k-nearest neighbors. 

### Multiple sets of random planes

So back to our multiple sets of random planes. Over here, for instance, let's say you have a vector space, and this magenta dot in the middle represents the transformation of an English word into a French word vector. You are trying to find other French word vectors that may be similar. So maybe one *universe of random planes 随机平面的宇宙* helped us to determine that this magenta vector and these green vectors are all assigned to the same hash bucket. Another entirely different set of random planes helped us determine that these blue vectors are in the same hash bucket as the red vector. A third set of random planes helped us determine that these orange vectors are in the same hash bucket as the magenta vector. **By using multiple sets of random planes for locality-sensitive hashing, you have a more robust way of searching the vector space for a set of vectors that are possible candidates to be nearest neighbors.** This is called **approximate nearest neighbors** because you're not searching the entire vector space, but just a subset of it.

So it's not the absolute k-nearest neighbors, *but it's approximately the k-nearest neighbors*. **You sacrifice some precision in order to gain efficiency in your search.** 

### Make one set of random planes

So let's see how to make **a set of random planes** in code:

```
num_dimensions = 2 # 300 in assignment
num_planes = 3 # 10 in assignment
```

Assuming that your word vectors have two dimensions and you want to generate three random planes. You'll use `numpy.random.normal` to generate a matrix of three rows and two columns, as you see here. You'll create a vector v, and for each random plane, see which side of the plane the vector is on. So you'll find out whether the vector v is on the positive or negative side of each of these three planes. Notice that instead of using a for loop to work on one plane at a time, you can use numpy.dot to do this in one step. Let's call the function. The result is that vector v is on the positive side of each of the three random planes. You've already seen how to combine these intermediate hash values into a single hash value, but please, do check out the lecture notebook to see all the code and to practice this last step.

**As you see, locality-sensitive hashing allows to compute k-nearest neighbors much faster than naive search.** This powerful tool can be used for many tasks related to our vectors, and I will show you how it can be applied to search in the next video.

## [Searching documents](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/x6aJN/searching-documents)

I will finish this week by showing you how you can use fast k-nearest neighbor to search for pieces of text related to a query in a large collection of documents. You simply create vectors for both and find the nearest neighbors.

### Document representation

To get ready to perform document search, **first, think about how to represent documents as vectors instead of just words as vectors.** Let's say you have this documents composed of three words. `I love learning.`  How can you represent this entire documents as a vector? Well, you can find the word vectors for each individual word. I love learning. Then just add them together, so the sum of all these words vectors becomes a documents vector, where the same dimension as the word vectors, in this case, three-dimensions. You can then apply document search by using k-nearest neighbors.

### Document vectors

Let's go this up, 

* Create a mini dictionary for word embeddings.

* Here's the list of what's contained in the document.

* You're going to initialize the documents embedding as an array of zeros. 

* Now for each word in a document, you'll get the word vector if the word exists in the dictionary else zero.

* You add these all up and return the documents embedding.

Please try it out. 

You learned in this video an example of a very general method that text can be embedded into vector space so that nearest neighbors refer to text with similar meaning. Well, you will learn more advanced ways to embed text. This basic structure will reappear again and again as it's used throughout modern NLP.
