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

## Word by Word and Word by Doc

In this video, you will learn **how you can construct your vectors based off a co-occurrence matrix**. Specifically, depending on the task you're trying to solve, you can have several possible designs. You will also see  **how you can encode a word or a document as a vector.** Let me show you how you can do this.

### Outline

* `Co-occurrence`  ------>  `Vector representation`

* Relationships between words/documents

To get **a vector space model** using a word by word design, you'll make a **co-occurrence matrix** and **extract vector presentations** for the words in your corpus. You'll be able to get **a vector space model** using a word by *document design* using  a similar approach. Finally, I'll show you how in a vector space you can find relationships between words and vectors, also known as their similarity.

### Word by Word Design

* *Number of times they* occur together withnin a certain distance **k**

The co-occurrence of two different words is the number of times that appear in your corpus together within a certain word distance k. For instance, suppose that your corpus has the following two sentences:

* `I like simple data`
* `I prefer simple raw data`

The **raw** of the co-occurrence matrix corresponding to the word **`data`**, with a **k** value equal to 2 would be populated with the following values. For the **column** corresponding to the word **`simple`**, you'd get a value equal to 2. Because `data` and `simple` co-occur in the first sentence within a distance of one word, and in the  second sentence within a distance of two words. The **row** of the **co-occurrence matrix** corresponding to the word data would look like this if you consider the co-occurence with the words `simple`, `raw`, `like`, and `I`. In this case, the vector representation of of the word data would be equal to `2`, `1`, `1`, `0`. With a **word by word design**, you can get a representation with **n entries** with `n` between 1 and *the size of  your entire vocabulary**.
