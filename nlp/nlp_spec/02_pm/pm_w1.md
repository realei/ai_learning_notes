# Natural Language Processing with Probabilistic Models

*Probabilistic Models 概率模型*

## [Autocorrect and Minimum Edit Distance](https://www.coursera.org/learn/probabilistic-models-in-nlp/supplement/bLbYO/connect-with-your-mentors-and-fellow-learners-on-slack)

### [Overview](https://www.coursera.org/learn/probabilistic-models-in-nlp/supplement/ap1cF/overview)

Welcome. This week, I will go over autocorrect. It is how your misspelled words are corrected automatically to the right ones. You know it already from your e-mail client on your phone. Let me show you how it works.

- Learning Objectives

  * What is autocorrect

  * Building the model

  * Minimum edit distance

  * Minimum edit diatance algorithm

 So let's go over this week's learning objectives. You'll learn about autocorrect conceptually. You've most likely used it in your phone or word processor. But what is autocorrect exactly? It can mean slightly different things depending on the context. You will learn about the **nuances 细微差别** this week. You'll practice building the model to perform autocorrect. You'll learn each step in autocorrect and key concepts to prepare you for the coding assignments. When performing autocorrect, you will want to be able to *quantify 量化* how far apart or different two strings are, and ask how many letters you can change to go from one string to another. To do this, you will learn to **measure minimum edit distance**. You will implement a really interesting algorithmic approach for solving the minimum edit distance called **dynamic programming**. At the end of the lecture, you'll demonstrate your new skills and put all these techniques to work in this week's assignments.

## [Autocorrect](https://www.coursera.org/learn/probabilistic-models-in-nlp/supplement/zCyLo/autocorrect)

- What is autocorrect?

What is autocorrect? Autocorrect is an application that changes misspelled words into the correct ones. You probably know it very well already. You have it on your phone, tablet, and on your computer inside your document editors, and email applications. For example, it takes a sentence like this one, happy birthday deah friend, and corrects the misspelled word deah to a word that you probably intended to write, which in this context would be dear, correctly spelled D-E-A-R. But what if you typed deer instead of dear? Here you see the word is spelled correctly, but its context is incorrect. Well, unless your friend happens to be an actual deer, you will not test for this contextual error this week as it's a more sophisticated problem. You'll get to learn about that another time. Instead, this week you'll only look for words that have been misspelled and make corrections to these. This involves a simple yet powerful model as you will see.

- How it works?

1. Identify a misspelled word

2. Find strings 'n' edit distance away

3. Filter candidates

4. Calculate word probablities

There are four key steps. First, identify an incorrect word, misspelling is one way to do this. Second, find strings 1, 2, 3, or any n edit distances away. Don't worry, you will learn about minimum edit distance shortly. For now, what's important to know is that if a string is one edit distance away from the string that you typed, it's more similar to your string compared to a string that is two edit distances away. Third, filter the strings for real words that are spelled correctly. Fourth, calculate word probabilities, which tell you how likely each word is to appear in this context and choose the most likely candidate to be the replacement. So now you have a better intuition for what is autocorrect and how it works. That's good. Next, you'll take a closer look at the details for implementing each step so that you can begin to build the autocorrect model. Now you know how autocorrect works. In the coding exercise of this week, you will implement it and see for yourself that it works really well. Next, I'll show you how to speed up edit distance computation.

### [Autocorrect](https://www.coursera.org/learn/probabilistic-models-in-nlp/supplement/zCyLo/autocorrect)

### [Building the model 1/2](https://www.coursera.org/learn/probabilistic-models-in-nlp/supplement/SB0aq/building-the-model)


1. Identify a misspelled word

2. Find strings 'n' edit distance away

3. Filter candidates

4. Calculate word probablities

You already know the four steps inside the autocorrect model, so it's time to look at each step in detail. You'll be implementing each of these steps in this week's assignments. 

1. Identify a misspelled word

```
if word not in vocab:
    misspelled = True
```

Step 1, identify a misspelled word. When the string `deah` is encountered, how do you know it's a misspelled word? Well, if it's spelled correctly, you'll find it in a dictionary, if not, then it's probably a misspelled word. If a word is not given in a dictionary, flag it for correction. *Recall that you're not searching for contextual errors, just spelling errors.* There are much more *sophisticated techniques 复杂的技术* for identifying words that are probably incorrect by looking at the word surrounding them, some of which you will visit later in the course. But for now, quickly identifying a word as incorrect by its apparent misspelling is a simple yet powerful model that works well. So words like `deer` will pass through this filter just fine, as it is spelled correctly, regardless of how the context may seem. `Happy birthday deer!`


2. Find strings 'n' edit distance away

[Edit Distance 编辑距离](https://zh.wikipedia.org/wiki/%E7%B7%A8%E8%BC%AF%E8%B7%9D%E9%9B%A2)

* Edit: an operation performed on a string to change it

* Insert (add a letter)      `'to': 'top', 'two'...`

* Delete (remove a letter)   `'hat': 'ha', 'at', 'ht'...`

* Switch (Switch 2 adjacent letters) `'eta': 'eat', 'tea', ...`  But not `'ate'`

* Replace (change 1 letter to another) `'jaw': 'jar', 'paw' ...`

Step 2, find strings that are one, two, three, or any number n edit distance away. When saying **n edit distance**, I'm referring to an edit distance of n, such as at the distance of one, at a distance of two, and so on. **An edit is a type of operation performed on a string to change it into another string.** And **edit distance** counts the number of these are operations, so that the n edit distance tells you how many operations away one string is from another.

Now consider an **insert operation**, for example. **This is a type of edit that adds a letter to a string in any position.** For example, starting with the word `to`, insert a `p` at the end and you get `top`, or insert `w` in the middle and you get `two`. 

A **delete operation** removes a letter. For example, start with the word hat, delete t from the end and you get ha, or delete a from the front and you get at. Or delete a from the middle and you get the string ht.

A **switch edit** swaps two adjacent letters, for example, the string eta. Switch t and a and you get eat, or switch e and t and get tea. **Notice** that you are switching two letters that are next to each other. So this does not include switching two letters that are not next to each other, such as switching the e and the a to make ate.

A **replace edit** changes one letter to another, for example the word jaw. Change w to r and you get jar, or change j to p and you get paw. So using the four edits, insert, delete, switch, and replace, you can modify any string.

- Given a string find all possible strings that are *n edit distance away* using

  * Insert
  * Delete
  * Switch
  * Replace

So using the four edits, insert, delete, switch, and replace, you can modify any string. And **by combining these edits**, you can find **a list of all possible strings** that are n edits away.

**For autocorrect, n is usually one to three edits.** You'll implement each of these edits in this week's programming exercise, and combine edits to get a list of two edit distances from the original input string. 

3. Filter candidates

Now Step 3, filter candidates. Notice how many of the strings that are generated do not look like actual words. **To filter these strings and keep ones that are real words, you only want to consider real and correctly spelled words from your candidate lists.** So again, compare it to a known dictionary or vocabulary, just like in Step 1. This time, if the string does not appear in the dictionary, remove it from the list of candidates. When you're left with a list of actual words only, then that is good progress. That's the first three steps of building the autocorrect model. In the next lesson, you'll see the fourth and final step.


### [Building the Model 2/2](https://www.coursera.org/learn/probabilistic-models-in-nlp/supplement/NaSrM/building-the-model-ii)

Now that you have a list of actual words, you can move on to step four; calculate word probabilities.

4. Calculate word probabilities

The final step is to calculate word probabilities and find the most likely word from the candidates. For example, the word "and" is more common than the word "ant" in any given body of texts, also called a corpus. This is how AutoCorrect knows which word to substitute for the incorrect one. To understand this better, look at this example sentence, `"I am happy because I am learning."` To calculate the probability of a word in the sentence, you need to first calculate the **word frequencies**. In addition, you want to count the total number of words in the body of texts or corpus, normally a corpus would be much larger. Imagine every issue of a certain magazine ever published all of the Harry Potter books, to keep this example as simple as possible, the corpus here is defined as this one sentence. For example, the word "I" appears twice, the word "m" appears twice also, and so on for the rest of the words.

**The final step is to calculate word probabilities and find the most likely word from the candidates.** For example, the word "and" is more common than the word "ant" in any given body of texts, also called a corpus. This is how AutoCorrect knows which word to *substitute 替代* for the incorrect one. To understand this better, look at this example sentence, "I am happy because I am learning." The total number of words in this corpus is seven, the probability of any word within the corpus is the number of times the word appears divided by the total number of words. For example, the word "m" appears twice and the size of the corpus is seven. For AutoCorrect, you find the word candidate with the highest probability and choose that word as the replacement, and that's it.

In summary, to implement AutoCorrect, do the following:

* You entered a word to correct, for example the misspelled word deah, D-E-A-H, 

* then you follow the four steps inside the AutoCorrect's model to get its replacement. You identify deah as being misspelled by checking it against known words. 

* Then you made a list of all the strings that are n edits away, you filter these lists of strings to include only the ones that are actual words in a given dictionary.

* Then you calculated the word probabilities for each of these words, you selected the word with the highest probability as the AutoCorrect replacement, and that was it. 

That's a lot to cover, but breaking it down step-by-step gives you a good intuition for how to implement AutoCorrect. This is something that will come in very handy for the assignment, so well done. Also, you now understand edit and edit distance and how they can be used to measure similarity between words. Next, get ready to apply these concepts to building a metric very common in NLP, for measuring similarity between words, strings, and many more.

### [Minimum edit distance](https://www.coursera.org/learn/probabilistic-models-in-nlp/supplement/sYxbc/minimum-edit-distance)

* How  to evaluate similarity between 2 strings?

* Minimum number of edits needed to transform 1 string into the other

* Spelling correction, document similarity, machine translation, DNA sequencing, and more

You have already seen how to build auto correct using edit distance. Let's consider a slightly different problem. What if you're given two words, strings or even whole documents and you wanted to evaluate how similar they are? Minimum edit distance can be used to do this. Given two strings, the minimum edit distance is the lowest number of operations needed to transform one string into the other. It has many applications. In NLP, for example, it could be used in spelling correction, document similarity, and machine translation. It can also be found in computational biology and DNA sequencing.

#### Minimum edit distance

- Edits:

  * Insert (add a letter)      `'to': 'top', 'two'...`
  * Delete (remove a letter)   `'hat': 'ha', 'at', 'ht'...`
  * Replace (change 1 letter to another)  `'jaw': 'jar', 'paw',...`



For calculating minimum edit distance, you will use three types of edits operations. All three operations that you already know, insert, delete, and replace, for example, to turn `play` into `stay`, **what is the minimum number of edits required to make this happen?** To turn `p` into `s`, you replace `p` with an `s`, and to turn `l` into `t`, you replace `l` with a `t`. Both `a` and `a` are the same, so do nothing. It's the same with `y` and `y`. The total number of edits is `2`.

- Example:

    Source: `p l a y`

	Target: `s t a y`

	p -> s: replace

	l -> t: replace

Until this point, you've considered all edits operations to cost the same. That is a cost of one. 

But now you'll consider a different cost for each type of operation. You will use these costs to calculate the edit distance, which now represents the total edits costs. This is what you are trying to minimize. It is simply the sum of costs for the edits that were made. `Inserts` and `deletes` will have a cost of 1 and `replace` has a cost of 2. This *makes intuitive sense* if you think of replacements as it deletes followed by an inserts. 

```
Edit cost:
Insert    1
Delete    1
Replace   2
```

`Edit distance = 2 + 2 = 4`

Calculate for this example, you have two replace edits at a cost of two each for a total edit distance of four. This is a relatively simple example, and it was possible to find the minimum edit distance just by looking at it.

But imagine the number of operations between *much longer strings* and *large corpora of texts* or *even DNA strings*. You can try and solve these problems by *brute force*, adding one added distance at a time and enumerating for all possibilities until one string changes to the other. But this could take a very, very long time. In fact, by solving this way, *the computational complexity increases exponentially as each string grows in length*. **A much faster way is by using a tabular approach.** You will implement this next.
