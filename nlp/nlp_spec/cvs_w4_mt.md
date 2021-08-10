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


