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

### [Testing Naive Bayes](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/nquvt/testing-naive-bayes)

It's time to **test the peformance of your classifier on unseen data,** just like you already did for a different scenario in the previous module. Let's quickly review that process, as applied to *Naive Bayes* this week's assignments include a validation set. This data was set aside during training and is composed of a set of raw tweets, so `$X_{val}$`, and their corresponding  sentiments, `$Y_{val}`. You'll have to implement the **accuracy function** to **measure the performance** of your trained  model represented by the `Lambda table` and the `log  prior` using this data.

* First, compute the score of each entry in `$X_{val}$`, lik you you just did previously.

* Then evaluates whether each score is greater than 0, this produces a vector populated with 0 and  1 indicating if the predicted sentiment is negative or positive respectively for each tweet in the validation sets.

* With your new predictions vector, you can compute the **accuracy of your model over the validation sets**. To do this  part, you will compare your predictions against the true value for each observation from your validation data, `$Y_{val}`. If the values are equal and your prediction is correct, you will get a value of 1 and 0 if incorrect. Once you have compared the values of every prediction with the true labels of your validation sets, you can compute the accuracy as the sum of this vector divided by the number of examples in the validation sets, just like you did for the logistic regression.

### Summary

* `$X_{val} Y_{val}$` ------> Peformance on unseen data

* Predict using  `Lambda` and `logprior` for each new tweet

* Accuracy ------> `$(1/m)*sum_{i=1}^{m (pred_{i} == Y_{val_{i}})}$`

* What about words that do not appear in `Lambda(w)`?

## [Applications of Naive Bayes](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/aQTbY/applications-of-naive-bayes)

Earlier in the week, you used Naive Bayes method to classify tweets. But that can be used to do a number of other things like **identify who's an author of a text**. I will give  you a few ideas of what those things may be.

### Application of Naive Bayes

  `P(pos|tweet) ~~ P(pos)P(tweet|pos)`

  `P(neg|tweet) ~~ P(neg)P(tweet|neg)`

When you use Naive Bayes to predict the sentiments of a tweet, what you're actually doing is **estimating the probability for each class** by using **the joint probability 联合概率 of the words in classes**. The Naive Bayes formula is the ratio between these two probablities, the products of the priors and the likehoods`P(pos|tweet)/P(neg|tweet) = (P(pos)/P(neg)*"likelihood")`. You can use this ratio between conditional probabilities for much more than sentiment analysis.

- Applications:

  * Sentiment Anaysis

  * Author Identification

  If you have large *corporal 文集*, each written by different authors, you can  train the model to reconize whether a new document  was written by one or the other. Or if you had some works by *Shakespeare 莎士比亚* and some works by *Hemingway 海明威*, you could calculate the `Lambda` for each word to predict how likely a new word is to be used by Shakespeare or alternatively by Hemingway. This method also allows you to determine author identity.

  * Spam Filtering

  Using information taken from the sender, subject and content, you could decide whether an email is spam or not.

  * Information retrieval 信息检索

    - $P(document_{k}|query)  \infty  \prod_{i=0}^{|query|} P(query_{i}|document_{k})$

    - Retrieve document if `P(document_{k}|query) > threshold`

  One of the earliest uses of Naive Bayes was filtering between relevant and irrelevant documents in a database. Given the sets of keywords in a query, in this case, you only need to calculate the likelihood of the documents given the query. You can't know *beforehand 预先* what's irrelevant or a relevant document looks like. So you can compute the likelihood for each document in your dataset and then store the documents based on its likelihoods. You can choose to keep the first M results or the ones that have a likelihood larger than a certain threshold.

  * Word Disambiguation 词消歧

  Finally, you can also use Naive Bayes for word dis-ambiguation, which is  to  say, breaking dwon words for  contextual clarity. Consider you have only  two possible *interpretations 解释* of a given word within a text. Let's say you don't know if the word `bank` in your reading is referring to the bank of a river or to a financial institution. To disambiguate your word, calculate the score of the document, given that refers to each one of the  possible meanings. In this case, if the text refers to the concept of the river instead of the concept of money, then the score will be bigger than 1. `Bank: P(river|text)/P(money|text)`

  **Simple, fast and robust!**

## [Naive Bayes Assumptions](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/xoi1w/naive-bayes-assumptions)

  This week, I'll go into the **assumptions underlyhing the Naive Bayes metho**. **The main one is independence of words in a sentence** and I'll tell you why this can be **a big problem** when the method is applied.

### Outline 

- Indenpendence 

- Relative frequency in corpus

Naive Bayes is a very simple model bacause it doesn't require setting any custom parameters. This method is referred to as naive because of the assumptions it makes about the data. **The first assumtpion is independence between the predictors or features associated with each class** and **the second has to  do with your validation sets**. Let's explore each of these assumptions and  how they could affect your results. 

To illustrate towards independence between features looks like, let's looks at the following  sentence:

`It is sunny and hot in the Sahara desert.`

Naive Bayes assumes that the words in a piece of text are independent of one another, but as you can see, this typically isn't the case. *The word `summy` and `hot` often appear together as they do in this example.* Taken together, they might also be related to the thing they're describing like a beach or a desert. So the words in a sentence are not always necessarily indepenent of one another, but Naive Bayes assumes that they are. **This could lead you to under or over estimates the conditional probabilities of individual words.** When using Naive Bayes, for example, if your task was to complete the sentence, `it always cold and snowy in__`, Naive Bayes might assign equal probability to the words `spring, summer, fall and winter` even though from the context you can see that winter should be the most likely candidate.

**Another issue with Naive Bayes is that it relies on the distribution of the training datasets.** A good dataset will contain the same proportion of positive and negative tweets as a random sample would. However, most of the available annotated *corpora 语料库* are artificially balanced just  like  the dataset you'll use for the assignment. In the real tweet stream, positive  tweet is sent to  occur more often than their negative counterparts. One reason for this is that negative tweets might contain coutent that is banned by the platform or muted by the user such as  inappropriate or offensive vocabulary. Assuming that reality behaves as your training corpus, this could  result in a very optimistic or very pressimistic model. There's a lot more on this in the last video of this module, which analyzes the sources of errors in Naive Bayes.

### Summary

- Independence: Not true in NLP

- Relative frequency of classes affect the model

The assumption of independence in Naive Bayes is very difficult to guarantee, but despite that, the model works pretty well in certainsitutations. And for the assignment of this module, the relative frequency of positive and negative tweets in your training datasets needs to be balanced in order to deliver an accurate results.

## [Error Analysis](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/clcHR/error-analysis)

No matter what NLP method you use, you will one day find yourself faced with an error, for example, a misclassified  sentence. In this video, I'll show you how to analyze such errors.

### Outline

- Removing punctuation and stop words

- Word order

- Adversarial attacks 对抗性攻击

Let us consider some possible errors in the model prediction that can be caused by these issues:

* One, semantic meaning lost in the pre-processing step.
* Two, how word order affects the meaning of a sentence.
* And three, some *quirks 怪癖* of languages come naturally to humans but confuse Naive Bayes Models.

### Processing  as a Source of Errors: `Punctuation`

Tweet: `My beloved grandmother:(`

One of your main considerations when analyzing errors in NLP systems is what the processed version of the text actually looks like. Let's look at above tweet. "My beloved grandmother" with some punctuation `:(` indicating a sad face. The sad face punctuation in this case is very important to the sentiment to the tweet because it tells you what's happening. But if you removing punctuation, then the processed tweet will leave hehind only `beloved  grandmother`, which looks like a very positive tweet. 'My beloved grandmother', exclamation mark would be a very different sentiment. So remember, **always check what the actual text looks like**.

### Processing as a Source of Errors: `Removing Words`

It's not just about punctuation either. Check out this tweet:

Tweet: `This is not good, because your attitude is not even close to being nice.`

If you remove netural words like `not` and `this`, what  you're left with is following:

**Processed_tweet:**[good, attitude, close, nice]

From this set of words, any classifier will infer that this is something very positive. I'll talk later on about handling `nots` and  `word orders`. But remember, **double check what your process text looks like to make sure your model will be able to  get an accurate read**.

### Processing  as a Source of Errors: `Word Order`

This inputs pipeline isn't the only potential source of trouble. Look at these tweets:

Tweet: `I am happy because I did not go.`   ---   A purely positive tweet.

Tweet: `I am not happy because I did go.`   ---   A negative sentiment.

In this case, **the `not` is important to the sentiment but get missed by your Naive Bayes classifier.** So word order can be as important to  spelling. There are many other factors to consider as well, and you will see more and  more ways to build  system that handle them in the weeks to come.

### Adversarial attacks 对抗性攻击

The term "adversarial attack" describes some **common language phenomenon 共同语言现象**, like:

`Sarcasm, Irony and Euphemisms` (讽刺、讽刺和委婉语)

Humans pick these up quickly but machines are terrible at it. This tweet:

**Tweet:** `This is a ridiculously powerful movie. The plot was gripping and I cried right through until the ending!`  ~~~ "这是一部可笑的强大的电影。 情节扣人心弦，我哭到最后."

contains a somewhat positive movie review, but pre-processing might suggest otherwise. If you pre-process this tweet, you'll get a list of mostly negative words:

**processed_tweet:** [ridicul, power, movi, plot, grip, cry, end]

but as you can see, they were actually used to describe a movie that the author enjoyed. If you use Naive Bayes on this list of words, it would end up giving  a very negative score regardless.
