# Native Bayes

## Probability and Bayes' Rule

To start, we are going to review what's **Probabilities** and **Conditional Probabilities** are? How they operate? How they can be expressed mathematically?

- [Probabilities](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/gK4BU/probability-and-bayes-rule)

  **One way** to think abou probabilities is by *counting how frequently events occur?*
  
  **Complementary Probability** 互补概率

  `P(Negative) = 1 - P(Positive)`

  **Note:** In order for this to be true, all tweets must be categorized as either positive or negative but not both.

  **Associated Probability** 关联概率

- Bayes' rule(Applied in different fields, including NLP)

- Build your own Native-Bayes tweet classifier!

## [Bayes' Rule 贝叶斯规则](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/1I1q1/bayes-rule)

In order to derive *Bayes' Rule*, let's first take a look at the *conditional probabilities*.

- **Conditional Probablities**

  **Conditional Probabilities** could be *interpreted as 解释为* the probability of an outcome B knowing that event A already happened. Or given that I'm looking at an element from set A, the chance that one also belongs to set B.

- Bayes' rule

  More Generally, Bayes' rule states that the probability of X given Y `P(X|Y)` is equal to the probability of Y given X times the ratio of probability of X `P(X)` over provavility of Y `P(Y)` and that's it.

  `P(X|Y) = P(Y|X)x(P(X)/P(Y))`

  This is the basic formulation of Bayes' rule, nicely done.

- Summary 

  - Conditional provabilities ------> Bayes' Rule
  - `P(X|Y) = P(Y|X)x(P(X)/P(Y))`

  The main **takeaway** for now is that **Bayes' rule is based on the mathematical formulation of conditional probabilities.** And that with Bayes' rule, you can calculate the probability of X given Y `P(X|Y)`, if you already know the probabilituy of Y given X `P(Y|X)`, and the ratio fo provabilities of X and Y `P(X)/P(Y)`.

## [Naive Bayes Introduction 朴素贝叶斯介绍](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/boKAa/naive-bayes-introduction)

  Last week you learned how  to classify tweets using *Logistic Regression*. This week we will solve the same problem using  a method called the **Naive Bayes**. It's a very good, quick, and dirty baseline for many text classification tasks, and the concepts you learned will be use later throughout the specialization.

- **Naive Bayes for Sentiment Analysis**

  *Naive Bayes* is an example of  supervised machine learning, and shares many similarities with *Logistic Regression* metnhod you used in the  previous assignment. It is called **naive** because **this method makes the assumption that the feature you're using for classification are all independent, which in reality is rarely the case.**

  Say you get a new tweet from one of your friends, and tweet says "I'm happy today; I am learning." And you want to use the table of probablities to predict the sentiments of the whole tweet. This expression is called **The Naive Bayes Inference Condition Rule for Binary Classification**. This expression says that you're going to take the product across all the words in your tweets of the probability for each word in the positive class divided by the probability in the negative class.

- **Summary**

  * Naive Bayes inference condition rule for binary classification

  * Table of probabilities

  **Compute the Likelihood Score**

## [Laplacian Smoothing 拉普拉斯平滑](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/IbV5W/laplacian-smoothing)

- Laplacian Smoothing is a technique you can use to avoid your probabilities being zero.

  Smoothing the probability function means that you will use a slightly different formula from the original. Note that I've added a '1' in the numerator分子, this little transformation avoids the probability being zero. However, it adds a new term to all the frequencies that is not correctly normalized by N class. *To account for this 考虑到这一点*, you will add a new term in the denominator分子 'V'. This is the number of unique words in your vocabulary (i.e. the entire vocabulary and not just the unique words in a single class). So now all the probabilities in each column will sum to one. This process is called Laplacian Smoothing.

- Summary

  * Laplacian smoothing to avoid P(...) = 0

  * Naive Bayes formula

## [Log Likelihood 对数似然, Part 1](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/lNljj/log-likelihood-part-1)

- Ratio of probabilities

  Words can have many *shades 色调* of emotional meaning. **But for the purpose of sentiment classification, they are simplified into three categories:*neurtal*, *positive*, *negative*.** All can be identified by using their conditional probabilities. These *categories* can be numerically estimated just by dividing the corresponding conditional probabilities.

  **Neutral** words have  already show  you one; **Positive** words have a ratio larger than one, the  larger the ratio the more positive the word's going to be; On the other hand, **negative** words has  a ratio smaller than one, the smaller the value the more negative the word.

  **Naive Bayes' Inference 朴素贝叶斯推理**

  These ratios are **essential** in *Naive Bayes' for binary classification*. 

  Recall early where you used the formula to categorize a tweet as positive if the products of the corresponding ratios of every word appears in the tweet is bigger than one. And we said it was negative if it was less than one. this is called the **likelihood**. If you're to take a ratio between the positive and negative tweets `P(pos)/P(neg)`, you'd have what's called **prior ratio 先验比率**. *When your'rebuilding your own application, remember that this term **prior ratio** becomes important for **unbalanced datasets**.* With the addition of the *prior ratio*, you now have the **full Naive Bayes' formjula** for binary classification:
  
  * A simple, fast, and powerful baseline

  * A *probabilistic概率性的 model* used for classification

- **Log Likelihood**

  Now it's a good time to mention some other important considerations for your implementationa of *Naive Bayes'*. *Sentiments probability calculation* requires **multiplication** of many numbers with values between 0 and 1. Carring out such multiplications on the computer runs **the risk of numerical underflow数值下溢** when the number returned is so small it can't be stored on your device. **Luckily**, there is a mathematical trick to solve this. It involves using *a property of logarithms 对数的性质*. Recall that the formula you're using to calculate a score for *Naive Bayes'* is the prior multipled by the likelihood. The trick is to use a log of the score instead of the raw score. This allows you to  write the  previous expression as the sum of *log prior* and *log likelihood*. Which is a sum of the logarithms of consitional probability ratio of all unique words in your corpus.

  Remember how you use the Naive Bayes' inference condition earlier to get the sentimentscore for your tweets. Now you're going to do something very similar to get the log or your score. What you'll need to calculate the log of score is called *Lambda*. This is the log of ratio of the probability that your word is positive and you divide that by ghe probability that the word is negative.

- Summary

  * Word sentiment 
  	
	1. `ratio(w)`
	2. `lambda(w)`

  Words are often *emotionally ambiguous 感情上模棱两可*, but you can simplify them into three categories and then measure exactly where they fall within those categories for binary classification. You do so by dividing the conditional probabilities of the words in each category. This ratio can be expressed as *a logrithm对数* as well, called *Lambda*. You canuse that to reduce the risk of numerical underflow.

 ## [Log Likelihood 对数似然, Part 2](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/oYXpy/log-likelihood-part-2)

  Remember how previously you saw that the tweet was positive if the product was bigger than 1. **With the `log(1)=0`** the positive values indicate that the tweet is positive, a value less than 0 would indicate that the tweet is negative. The **log-likelihood** for this tweet is 3.3, since `3.3 > 0` the tweet is positive. **Notice** that this score is based entirely on the words "happy" and ""earning", both of which carry a *positive* sentiments; all the other words were *neutral* and  didn't contribute to the score. See how much influence the power words have.

- Summary:

  You used your new skills to predict the sentiment of a tweet by summing all the `Lambdas` for each word that's appeared in the tweets. **This score is called the log-likelihood**. For the log-likihood the **decision threshold** is 0 instead of 1, positive tweets will have a positive log-likelihood above 0, and negative tweets will have a negative log-likelihood below 0.

  Well done! Now you can compute using log-likelihood. They make many things **simpler** and they also help with **numerical stability**.

## [Training Naive Bayes](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/0imfM/training-naive-bayes)

Train the Naive Bayes classifier, in this context we're trained in something different than in *logistic regression* or *deep learning*. **There is no gradient descent**, we're just counting frequencies of words in a corpus.

### **Outline**

- Five steps for training a Naive Bayes model

You'll now be creating step by step, a Naive Bayes model for sentiment analysis using a corpus of tweets that you've already collected.

  * Step 0: Collect and annotate corpus(Get or annotate a dataset with positive and negative tweets)

  **The first step** for any supervised machine learning project is to gather the data to  train and test your model. For *sentiment analysis* of tweets, this step involves getting a corpus of tweets and dividing it into two groups, positive and negative tweets.

  * Step 1: Preprocess(`process_tweet(tweet)->[w_{1}, w_{2}, w_{3}, ...]`)

  The next step is **fundamental** to your model success. **The preprocessing step** as describe in the previous module, consisits of five smaller steps:
    
	1. Lowercase 
	2. Remove punctuation, urls, names(handles)
	3. Remove stop words
	4. Stemming(Reducing words to their common stem)
	5. Tokenize sentences(Splitting your document into single  words or tokens)

  * Step 2: Word count(computing the vocabulary for each word and class, `freq(w, class)`)

  Once you have a clean corpus of process tweets, you'll start by computing hte vocabulary for each word and calss, like you did in the previous week. This process will produce a table like the on shown (in the Title's url). You can compute the sum of words and class in each corpus in this same step. 
  
  * Step 3: `P(w|class)`----Get `P(w|pos), P(w|neg)`

  From *this table of frequencies*(Step 2), you get the *conditional probability or orobablity for a given class by using the Laplacian Smoothing Formula*. See how  the number of  unique words in `$V_{class}$` is equal to  6. **You only account for the word in the table, not the total number or words in the original corpus.** This produces **a table of conditional probabilities** for each word and each classis. This table only contains values greater than 0.

  * Step 4: Get Lambda(Get`lambda(w)`)

  For the 4th step, you'll get the Lambda score for each word, which is the `log` of the ratio of your conditional probabilities.

  * Step 5: Get the "log priori"(compute `logprior=log(P(pos)/P(neg))`)

  The 5th step is the estimation of the log prior. To do this, you'll need to count the numbers of positive and negative tweets. And the log prior is the log of the ratio of the numbers of positive over the number of negative tweets`$log = log(D_{pos}/D_{neg})$`. **If the dataset is balanced, `$D_{pos}$` = `$D_{neg}` and `logprior = 0`.** But for unbalanced data sets, this term will be important.

- Summary 

In summary, training a Naive Bayes model can be divided into six logical steps.


## Test Naive Bayes

### Outline 

- Predict using a Naive Bayes Model

- Using your validation set to compute model accuracy

Once you have trained your model, the next step is to test it. And you do so by taking the *conditional probabilities* you just derived and you use them to predict the sentiments of new unseen tweets. After that, you evaluate your model performance and you will do so just like how you did  in the last week. You use your test sets of annotated tweets. With the calculations you've done  already, you have a table  with *lambda score* for each unique word in your vocabulary. With your estimation of the **log prior**, you can predict sentiments  on a new tweet. This new tweet says, "I passed the NLP interview.", you can use your model to predict if this is a positive or negative tweet. So before anything else, you must pre-processed this text removing the punctuation, stemming the words, and tokenizing to produce a vector of words like this one `Tweet: [I, pass, the, NLP, interview]`; Now you look up each word from **the vector in your log-likelihood table**. If the word is found, such as `I pass the NLP`, you *sum over* all the corresponding `lambda terms`. The value that don't show up in the *table of lambdas*, like `interview`, are condiser **neutral** and don't contribute anything to this score. **Your model can only give a score for  words it's seen before.** Now you **add the log prior** to *account for the balance or in-balance of  the classes in the dataset.* So this course sums up to  0.48, remember, if this score is bigger than 0, then the tweet has a positive sentiment. So yes, in your model and  in real life, `passing the NLP interview` is a very positive thing. You just predicted the sentiment of a new tweet and that's awesome. 
