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
