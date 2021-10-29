# Todo

1. [re](https://docs.python.org/3/library/re.html) library to perform regular expression operations on our tweet

2. Python: np.squeeze & whatis `zip`

  ```
  def build_freqs(tweets, ys):
    """Build frequencies.
    Input:
        tweets: a list of tweets
        ys: an m x 1 array with the sentiment label of each tweet
            (either 0 or 1)
    Output:
        freqs: a dictionary mapping each (word, sentiment) pair to its
        frequency
    """
    # Convert np array to list since zip needs an iterable.
    # The squeeze is necessary or the list ends up with one element.
    # Also note that this is just a NOP if ys is already a list.
    yslist = np.squeeze(ys).tolist()

    # Start with an empty dictionary and populate it by looping over all tweets
    # and over all processed words in each tweet.
    freqs = {}
    for y, tweet in zip(yslist, tweets):
        for word in process_tweet(tweet):
            pair = (word, y)
            if pair in freqs:
                freqs[pair] += 1
            else:
                freqs[pair] = 1
    return freqs
  ```

  3. scatter plot
    *raw counts* vs *logarithmic scale*

 4. *static methon* for javascript & python

 5. Static Way cs Dinamic Way in Numpy:

 Note that some operations can be performed using static functions like np.sum() or np.mean(), or by using the inner functions of the array.

```
nparray2 = np.array([[1, 3], [2, 4], [3, 5]]) # Define a 3 x 2 matrix.

mean1 = np.mean(nparray2) # Static way
mean2 = nparray2.mean()   # Dinamic way

print(mean1, ' == ', mean2)
```

**Even if they are equivalent, we recommend the use of the static way always.**

6. RESTful service 
  * param
  * Authorization 
  * Headers
  * Body
