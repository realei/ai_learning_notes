# Natural Language Processing Specialization

## Week 1: Logistic Regression

1. Supervised ML & Sentiment Analysis

2. Vocabulary & Feature Extraction

- **Vocabulary**: In this video, you're going to learn how to **represent a text as a vector**. In order for you to do so, you **first have to build a vocabulary** and that will allow you to **encode any text or any tweet as an array of numbers**.

- **Feature extraction**

  The type of representation with a small relative number of non-zero values is called a **sparse representation**.

	- Problems with **sparse representations**

	  This representation would have a number of features equal to the size of your entire vocabulary. This would have a lot of features equal to 0 for every tweet. **With the sparse representation, a logistic regression model would have to learn `n + 1` parameters, where `n` would be equal to the size of your vocabulary** and you can imagine that for large vocabulary sizes, this would be problematic.

	  1. Large training time

	  2. Large prediction time

- **Negative and Positive Frequencies**

  We'll now learn to **generates counts**, which you can then use as features into your logistic regression classifier.

  *freq*: dictionary mapping from *(word, class)* to  *frequency*.

- **Feature Extraction with Frequencies**

  1. Feature extraction

    - *freq*: dictionary mapping from (word, class) to frequency
	  
	  For *an arbitrary tweet m*:

	  **Feature 1**: a Bias unit equal to '1'

	  **Feature 2**: The sum of the positive frequencies for every unique word on tweet m.

	  **Feature 3**: The sum of negative frequencies for  every  unique word on the tweet.
