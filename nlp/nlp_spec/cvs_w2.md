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

## Bayes' Rule 贝叶斯规则

In order to derive *Bayes' Rule*, let's first take a look at the *conditional probabilities*.

- **Conditional Probablities**

  **Conditional Probabilities** could be *interpreted as 解释为* the probability of an outcome B knowing that event A already happened. Or given that I'm looking at an element from set A, the chance that one also belongs to set B.

- Bayes' rule

  More Generally, Bayes' rule states that the probability of X given Y `P(X|Y)` is equal to the probability of Y given X times the ratio of probability of X `P(X)` over provavility of Y `P(Y)` and that's it.

  `P(X|Y) = P(Y|X)x(P(X)/P(Y))`
