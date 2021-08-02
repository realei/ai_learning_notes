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

## [Native Bayes Introduction 朴素贝叶斯介绍](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/boKAa/naive-bayes-introduction)

  Last week you learned how  to classify tweets using *Logistic Regression*. This week we will solve the same problem using  a method called the **Naive Bayes**. It's a very good, quick, and dirty baseline for many text classification tasks, and the concepts you learned will be use later throughout the specialization.

- **Naive Bayes for Sentiment Analysis**

  *Naive Bayes* is an example of  supervised machine learning, and shares many similarities with *Logistic Regression* metnhod you used in the  previous assignment. It is called **naive** because **this method makes the assumption that the feature you're using for classification are all independent, which in reality  is rarely the case.**
