# Vector Space Models

This week you're going to learn about vector spaces. And specifically, you will learn what type of information these vectors could encode. You'll all see different types of applications that you can use with these vector spaces, and you'll see different types of algorithms you'll be implementing.

## [Vector Space Models](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/yYagJ/vector-space-models)

### Outline

- Vector space models

- Advantages

- Applications

### Why learn vector space models?

* `Where are you *heading*?`
* `Where are you *from?*`

**Different meaning**

So suppose you have two questions above. **These sentences have identical words, except for the last ones. However, they both have a different meaning.** On the other hand, say you have two questions:

* `What is your age?`
* `How old are you?`

**Same Meaning**

**Whose words are completely different but both sentences mean the same thing.** Vector Space Models will help you identify whether the first pair of questions or the second pair are similar in meaning even if they do not share the same words. They can be used to identify similarity for a question answering, *paraphrasing 释义*, and summarization.

### Vector space models applications

Vector Space Models will also allow you to **capture dependencies between words.** Consider this sentence:

* `You eat *cereal* from a *bowl*`  ~~~ 你从碗里吃麦片

Here, you can see that the word *cereal* and the word  *bowl* are related. Now let's look at other sentence: 

* `You *buy* something and someone  else *sells* it`

So what it's saying is that someone sells something because someone else buys it. The second half of the sentence is dependent on the  first half. With vector space  models, you will be able to capture this and many other types of relationships among different sets of words. Vector space models are used  in **information extraction** to answer questions in the style of *who, what, where, how and etc.,* in **machine translation** and in **chatbots programming**. They are also used in many many other applications.

### Fundamental  concept

- "You shall know a word by  the company it keeps"   ---   (Firth, J,R 1957:11)

As a final thoughts, I'd  like to share with you this  wujto from John Firth, a famous English linguist. "You shall know a word by the company it keeps" this is one of the most fundamental concepts in NLP. When using vector space models the way that representations are made is by identifying the context around each word in the text, and this captures the relative meaning.

### Summary

* Represent words and documents as **vectors**

* Representation that **captures** relative **meaning**

## [Word by Word and Word by Doc](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/XAYg4/word-by-word-and-word-by-doc)

In this video, you will learn **how you can construct your vectors based off a co-occurrence matrix**. Specifically, depending on the task you're trying to solve, you can have several possible designs. You will also see  **how you can encode a word or a document as a vector.** Let me show you how you can do this.

### Outline

* `Co-occurrence`  ------>  `Vector representation`

* Relationships between words/documents

To get **a vector space model** using a word by word design, you'll make a **co-occurrence matrix** and **extract vector presentations** for the words in your corpus. You'll be able to get **a vector space model** using a word by *document design* using  a similar approach. Finally, I'll show you how in a vector space you can find relationships between words and vectors, also known as their similarity.

### Word by Word Design

* **Number of times they** occur together withnin a certain distance **k**

The co-occurrence of two different words is the number of times that appear in your corpus together within a certain word distance k. For instance, suppose that your corpus has the following two sentences:

* `I like simple data`
* `I prefer simple raw data`

The **raw** of the co-occurrence matrix corresponding to the word **`data`**, with a **k** value equal to 2 would be populated with the following values. For the **column** corresponding to the word **`simple`**, you'd get a value equal to 2. Because `data` and `simple` co-occur in the first sentence within a distance of one word, and in the  second sentence within a distance of two words. The **row** of the **co-occurrence matrix** corresponding to the word data would look like this if you consider the co-occurence with the words `simple`, `raw`, `like`, and `I`. In this case, the vector representation of of the word data would be equal to `2`, `1`, `1`, `0`. With a **word by word design**, you can get a representation with **n entries** with `n` between 1 and *the size of  your entire vocabulary*.

### Word by Document Design

* **Number of times a word** occurs within a certain category

For a word by document design, the process is quite similar. In this case, you'll count the times that words from your vocabulary appear in documents that belong to specific categories. For instance, you could have a corpus consisting of a documents between different topics like `Enertainment`, `Economy` and `Machine Learning`. Here, you have to count the number of times that your words appear on the document that belong to each of the three categories. In this example, suppose that the word `data` appears 500 time in documents from your corpus related to `Entertainment`, 6620 times in `Economy` documents, and 9320 in documents related to `Machine Learning`. The word `film` appears in each documents category 7000, 4000 and 1000. Can you get a sense of where this is going already?
### Vector Space

Once you've constructed the representations for multiple sets of documents or words, you will get your **vector space**. Let's take the matrix from the last example(Word by Document Design). Here, you could take a representation for the words `data` and `film` from the rows of the table. However, I'll take the representation for every category of documents by looking at the columns. So the vector space will have two dimmensions. The number of times that the words `data` and `film` appear on the type of document. For the `Entertainment` corpus, you'd have the following vector representation. This one for the `Economy` category, and that for the `Machine Learning` category. **NOTE**, that in this space, it is easy to see that the `Ecomany` and `Machine Learning` documents are much more similar than they are to the `Entertainment` category. Coming up soon, you'll make comparisons between vector representations using the **cosine similarity** and the **Euclidean distance** in order to get the **angle and distance** between them.

### Summary

* W/W and W/D, counts of occurrence

* Vector Spaces  ------>   Similarity between words/documents

## [Euclidean Distance](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/uqakE/euclidian-distance)

Euclidean Distance is a **similarity metric**. This metric allows you to identify how far two points or two vectors are apart from each other.

### Outline

- Euclidean distance

- N-dimension vector representations comparison

During this segment, you will get the **Euclidean distance between two documents vectors** like the ones from previous video. *And then generalize that **notion概念主张** to vector spaces in higher himensions.*

### Euclidean  distance

Let's use two of the corpora vectors you saw previously. Remember, in that's example, there were two dimensions. The number of times that the word `data` and the word `film` appeared in the Corpus. 

* Corpus **A**: (500, 700)  ~~~ Entertainment Corpus
* Corpus **B**: (93200, 1000) ~~ ML Corpus

Now let's represent those vectors as points in the vector space. The Euclidean distance is the length of the *straight line segment直线段* connecting them. To get that value, you should  use  the following formula(please refer tothe url). The first term is **their horizontal distance squared** and the second term is **their vertical distance squared**. As you see, this  fornula is an example of the **Pythagorean theorem勾股定理**. If you solve for each of the terms in the equation, you should arrive at this expression(refer to the url).

### **Euclidean distance for n-dimensional vectors**

When you have higher dimensions, the Euclidean distance is not much more difficult. Let's walk through an example  using the following co-occurence matrix(refer to the url). Suppose that you want to know Euclidean distance between the `vector v` of the word `ice cream` and  the `vector representation w` of  the  word `boba`. To start, you need to get the difference between each of their dimensions, square those differences, sum them up  and then get the  queare root  of your results. This process is the generalization of the one from the last slide. This is the formula that you would use to get the Euclidean distance between vector representations on an n-dimensional vector space. If you remember from algebra, this formula is known as the **norm范数** of the difference between the vectors that  your are comparing.

### Euclidean distance in Python

```
# Create numpy vectors v and  w
v = np.array([1, 6, 8])
w = np.array([0, 4, 6])

# Calculate the Euclidean distance d
d = np.linalg.norm(v-w)

# Pring the result
print("The Euclidean distance between v and w is:", d)
```

### Summary

* Straight line between points

* Norm of the difference between vectors

**The primary takeaways** here are that the Euclidean distance is basically the length of the straight  line  that's connects two vectors. And that to get the Euclidean distance, you have to calculate the `norm` of the difference  between the vectors that you are comparing. By using this metric, you can get a sense of how similar two documents or words are.

## [Cosine Similarity Intution](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/xW4vy/cosine-similarity-intuition)

Cosine Similarity is basically makes uses of the **cosine of the angle between two vectors**. And based off that, it tells you whether two vectors are close or not.

### Outline

* Problemswith Euclidean Distance

* Cosine similarity

In this section, you will see the problem of using Euclidean distance. Especially when comparing vector representations of documents or corpora. And how the **Cosine Similarity metric** could help you overcome that problem.

### Euclidean distance  vs Cosine similarity

(Please refer to the url for chart)

To illustrate how the euclidean distance might be *problematic有问题的*, let's take the following  example. Suppose you are in a vector space where the corpora are represented by the occurence of the words `disease` and `eggs`. Here is the representation of a `Food dorpus (5, 15)` and `Agriculture corpus(20, 40)` and the `History corpus (30, 20)`. Each one of these corpora have text related to that subject. But you know that the *word totals单字总数* in the corpora differ from one another. In fact, the agriculture and the history corpus have a siilar numbers of words, while the Food corpus has a relatively small number. Let's define the Euclidean distance between the `Food` and the `Algriculture` corpus as `d1`. And let the Euclidean distance between the `Agrigulture` and the `History` corpus be `d2`. As you can see, the distance `d2` is smaller than the distance `d1`, which would suggest that the `agriculture` and `History` corpora are more similar than the `Agriculture` and `Food` corpora. **Another common  method for determining the similarity between vectors is computing the cosine of the inner angle.** If  the angle is small, the  cosine  would be close to 1; and as the angleapproaches 90 degrees, the cosine  approaches 0. As you can see here, the `angle alpha` between `Food` and `Agriculuture` is smaller than the `angle beta` between `Agriculture` and `History`. **In this particular case, the cosine of those angles is a better proxy of similarity between those vector representations than their Euclidean distance.**

### Summary

* Cosine similarity when corpora are different sizes

Now, you're familar with the main intuition between the use of Cosine similarity as a metric to compare the similarity between two *vector representations向量表示*. **Remember** that the main advantage of this metric overthe duclidean distance is that it isn't biased by the size difference between the representations.

## [Cosine Similarity](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/yasAe/cosine-similarity)

### Outline

* How to get the cosine of the angle between two vectors

* Relation of this metric to similarity

In this section, you will get the consine of the inner angle of two vectors. Then I'll show you how the value of the cosine similarity is related to the similarity of the directions of two vectoros.

### Previous definitions

First, you have to recall some definitions from *algebra 代数*. The **norm of a vector** or it's **magnitude** is  written like this(check the url). It's defined tobe the *square root* of the sum of it's elements squared. The **dot product** between two vectors is the sum of the products between their elements in each dimension of the vector space.

### Cosine Similarity

Let's take another look at two of the corpora from the last section. Remember that in this example, you have a vector space where the representation of the corpora is given by the number of occurrences of the words `disease` and `eggs`. The angle between those vector representations is denoted by `beta`. The `Agriculture` corpus is represented by the vector `v`, and the `History` corpus is going to be vector `w`. The **dot products** between those vectors is defined as follows(url). From this equation, you see that the consine of the angle `beta` is equal to the *dot product* between the vectors divided by the product of the two norms. Replacing the actual values from the vector representations should give you this expression(url). In the numerator, you have the product between the occurrences of the words, `disease` and `eggs`. And in the denominator, you have the product between the *norm* of the vector representations of the `Agriculture` and `History` corpora. *Ultimately 最终*, you should get a cosine similarity of 0.87.

### Cosine Similarity

But what does this metric tell you about the similarity of two different vectors? Consider when two vectors are *orthogonal 正交* in the vector spaces that you know so far. It is only possible to have **positive values** for any dimension. So the **maximum angel** between pair of vectors is 90 degrees. In that case, the cosine would be equal to 0(url), and it would mean that the two vectors have **orthogonal directions 正交方向** or that they are **maximally dissimilar**.

Now let's look at the case where the vectors have the same direction. In this case，the angle between them is 0 degrees and the cosine is equal to 1, because cosine of 0 is just 1. As you can see, as the cosine of the angle between two vectors approaches 1, the closer their directions are.

## Summary

* Cosine & Similarity

* Cosine Similarity gives values between 0 and 1

Now, you know how to get the cosine similarity between any pair of vectors. An important **takeaway** is that, this metric is **proportional 成比例的** to the similarity between the directions of the vectors that you are comparing. And that for the vector spaces you've seen so far, the cosine similarity takes values between 0 and  1.

## Manipulating Words in Vector Spaces

Specifically by performing some simple *vector arithmetic 矢量算术* meaning by adding vectors and subtracting vectors, you will be able to predict the countries of certain capitals.

### Outline

* How to use vector representations

In this portion, I'll show you how to manipulate vector representations in order to infer unknown relations among words.

### Manipulating word vectors

Suppose that you have a vector space with countries and their capital cities. You know that the capital of `the United States` is `Washington DC` and you don't know the capital of Russia, but you'd like to use the `known relationship` between `Washington DC` and `the USA` to figure it out. For that,  you'll just use  some simple **vector algebra 矢量代数**. 

For this example, you are in in a *hypothetical two-dimensional vector space 假设的二维向量空间* that has different representations for different countries and capital cities.

- **First**, you will have to find the relationship between the `Washington DC` and `USA` vector representations. In other words, which vector connects them? To do that, get the difference begtween the two vectors. The values from that will tell you how many units on each dimension you should move in order to find a country's capital in that vector space. 

- So to find the capital city of Russia, you will have to sum it's vector presentation with the vector that you also got in the last step.

- At the end, you should *deduce 推断/减掉/臆测* that the capital of Russia has a vector representation of `[10, 4]`. However, there are no cities with that representation, so you'll have to take the one that is the most similar to its by comparing each vector with Euclidean distances or Cosine similarities. 

In this case, the vector representation that is closet to the [10, 4] is the one for `Moscow`. Using this simple process, you could have predicted the capital of Russia if you knew the capital of the USA. *The only catch 唯一的问题* here is that you need a vector space where the representations capture the relative meaning of words.

### Summary

* Use known relationships to make predictions

Now you have a simple process to get unknown relationships between words by the use of known relationships between others. You now know the **importance of having vector spaces where the representations of words capture the relative meaning in natural language.**

You have now seen **a clustering of all vectors when plotted  on two axes.** You have also seen that the vectors of the words that occur in similar places in the sentence will be encoded in a similar way. You can take advantage of this type of *consistency encoding 一致性编码* to identify patterns. For example, if you had the word `doctor` and  you were to find the closest words that are closets to it by computing cosine similarity, you might get the word `doctors`, `nurse`, `cardiologist 心脏病专家`, `surgeon 外科医生`, etc. In the next video, you will learn how to plot these d-dimensional vectors on a 2D plane.

## [Visualization and PCA](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/7FUaZ/visualization-and-pca)

It is often the case that you'll end up having vectors in very, very high dimensions. You want to find a way to **reduce the dimension of these vectors to two dimensions** so you can plot it on an XY axis. You will now learn abou *Principal Components Analysis 主成分分析*, which will all you to do so.

### Outline

* Some motivation for visualization

* Principal Component Analysis

You are going to be using Principal Component Analysis(PCA) to visualize vector representations with higher dimensions than the ones that you've seen plotted so far. To get started, I'll give you some intuition on the motivation for visualizing vector presentation of words. And you'll see for yourself what PCA does and how it is used for dimensionality reduction.

### Visualization of word vectors

Imagine you have the following representation for your words in a vector space(url). In this scenario, your vector space dimension is higher than 2. You know that the words `oil` and `gas`, and `city`, and  `town` are related. And you want to see if that relationship is captured by the representaton of your words. So how could you visualize your words in order to see this and other possible relationships? **Dimensionality reductionis** is a perfect choice for this task. When you have a representation of your words in a high dimensional space. You could use an algorithm like PCA to get a representation on a vector space with fewer dimensions. If you want to visualize your data, you can get a reduced representation with three or fewer features. 

### Visualization of word vectors

If you peform Principal Components Analysis on your data and get a two-dimensional representation, you can then plot a visual of your words. In this case, you might find that your initial representation captured the relationship between the words `oil` and `gas`, and `city`, and `town`. Because in your two-dimensional space they appear to be clustered with related words. You can even find other relationships among your words that you didn't expect, which is a fun and useful possibility.

### Principal Component Analysis

Now that you know what PCA can help you achieve, let's go into detail on how it works. For the sake of simplicity, I'll begin with a two-dimensional vector space. Say that you want your data to be represented by one feature instead. Using PCA, **first** you'll find a set of uncorrelated features. **And then** projects your data to a one-dimensional space, trying to retain as much information as possible. As you can see, this process is quite straightforward. Coming up, you'll see for yourself the details of how this algorithm works. Along with how to get uncorrelated features, you'll also project your data for your representation in a lower-dimension while retaining as much information as possible.

### Summary

* Original Space ---> Uncorrelated features ------> Dimension reduction

* Visualization to see words relationships in the vector space

Principal component analysis is an unsupervised learning algorithm which can be used to reduce the dimension of your data. As a result, it allows you to visualize your data. It tries to combine *variances 方差* across features.

PCA is an algorithm used for dimensionality reduction that can find uncorrelated features for your data. It is very helpful for visualizing your data to check if your representation is capturing relationships among words.

## PCA Algorithm

You will now learn about **eigenvalues 特征值** and **eigenvectors 特征向量**, and you will see how you can use them to reduce the dimension of  your features.

### Outline 

* How to get uncorrelated features

* How to reduce dimensions while retaining as much information as possible

First, I'll show you how to get uncorrelated features for your data, and then how to reduce the dimensions of your word representations while trying to keep as much information as possible from your original embedding.

### Principal Component Analysis

To peform dimensionality reduction using PCA, **begain** with your original vector space. **Then** you get uncorrelated features for your data. And **finally**, you project your data to a number of  desired features that retain the most information.

### PCA Algorithm 

* **Eigenvector:** Uncorrelated features for your data

* **Eigenvalue:** the amount of information retained by each feature

You may recall from algebra that matrices have `eigenvectors` and `eigenvalues`. You do not need to remember how to get those right now. But you should keep in mind that in PCA, they are useful, because the **eigenvectors** of the *covariance matirx 协方差矩阵* form your data, they give directions of uncorrelated features. And the **eigenvalues** are the variance of your data sets in each of those new features. So to peform PCA, you will need to  get the *eigenvectors* and *enginvalues* from the *covariance matrix* of your data.

(check the url)

The **first step** is to get a set of uncorrelated features. 

* For this step, you will **mean normalize your data**.

* **Then** get the **covariance matrix 协方差矩阵**

* **Finally** perform a **singular value decomposition 奇异值分解 SVD** to get a set of three matrices. The **first** of those matrices contain the **eigenvector stacked column wise**. And the **second** one has the **eigen values on the diagonal**. The singular vector decomposition is already implemented in many programming libraries.

The **next step** is to project your data to a new set of features(url). You will be using the `eigenvecgtors` and `eigenvalues` in this step. Let's *denote 表示* the eigenvectors with `U`, and eigenvalues with `S`. 

* **First**, you will perform the *dot products* between the matrix containing your **word embedding** and the first and columns of the `U` matrix, where `n` equals the number of dimensions that you want to have at the end. For *visualization*, it's common practice to have two dimensions. 

* **Then** you will get the **Percentage of Retained Variance** retained in the new vector space. As **an important  side note**, your eigenvectors and eigenvalues should be organized according to the eigenvalues in descending order. This condition will ensure that you retainas much information as possible from your original embedding. However, most libraries  order those matrices for you.

### Summary

* Eigenvectors give the direction of uncorrelated feagtures

* Eigenvalues are the variance of the new features

* Dot product gives the projection on uncorrelated features

Wrapping up, `eigenvectors` from the `covariance matrix` of your normalized data give the directions of uncorrelated features. The `eigenvalues` associated with those `eigenvectors` tellyou the variance of your data on those  features. The `dot products` between your *word embeddings* and the *matrix of engenvectors*, will project your data onto a new vector space of  the dimension that you choose.  
