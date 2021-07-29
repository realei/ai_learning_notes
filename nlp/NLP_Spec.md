# Natural Language Processing Specialization

## Week 1: Logistic Regression

1. [**Supervised ML & Sentiment Analysis**](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/J9NR1/supervised-ml-sentiment-analysis)

2. [**Vocabulary & Feature Extraction**](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/m7UdZ/vocabulary-feature-extraction)

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

- [**Feature Extraction with Frequencies**](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/sfhGt/feature-extraction-with-frequencies)
  
  You previously learned to encode a tweet as a vector of dimension V. You will now learn to encode a tweet or specifically represented as a vector of dimension 3.

  1. Feature extraction

    - *freq*: dictionary mapping from (word, class) to frequency
	  
	  For *an arbitrary tweet m*:

	  **Feature 1**: a Bias unit equal to '1'

	  **Feature 2**: The sum of the positive frequencies for every unique word on tweet m
	  **Feature 3**: The sum of negative frequencies for  every  unique word on the tweet.

- [**Preporcessing**](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/SLqys/preprocessing)

  Two major concepts of preprocessing: **Stemming** & **Stop words**;

  1. **Preprocessing: stop words and punctuation** 
  
  In practice, you would have to compare your tweet against two lists. One with **stop words in English** and another with **punctuation**.

  **Note** that the overall meaning of the sentence could be inferred without any effort.

  **Note** that in some contexts you won't have to eliminate punctuation, so you should think carefully about whether punctuation adds important information to your specific NLP task or not.

  2. **Preprocessing: Handles and URLs**

  Tweets and other types of texts often have **Handles** and **URLs**, but these don't add anyvalue for the task of sentiment analysis.

  *Handles*: @YMourri; @AndrewYNg

  *URLs*: https://deeplearning.ai

  3. **Preprocessing: Stemming and lowercasing**

  **Stemming** in NLP  is simply transforming  any  word to it's base stem, which you could define as the set of characters that are used to construct the word ant it's derivatives.

- [**Putting it all together**](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/HjiGd/putting-it-all-together)

  **General Implementation:**

  1. First, build the *frequencies dictionary*:

  `freqs = build_freqs(tweets, labels) #Build frequencies dictionary`

  2. Then, initialize the matrix X to match your number of tweets

  `X = np.zeros((m,3)) #Initialize matrix X`

  3. After that, you'll want  to  go over through your sets of tweets carefully. Like, *deleting  stop words*, *steamming*, *deleting URLs & handles* and *lower casing.

  ```
  for i in range(m): #For every tweet
  	p_tweet = process_tweet(tweets[i]) #Process tweet
  ```

  4. Finally, extract the features by **summing up** the **positive and negative frequencies** of the tweets.

  `X[i,:] = extract_features(p_tweet, freqs) #Extract Features`

- [**Logistic Regression Overview**](https://www.coursera.org/learn/classification-vector-spaces-in-nlp/supplement/4GuN0/logistic-regression-overview)

  

  
