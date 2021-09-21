# Overview of the ML Lifecycle and Deployment

## The Machine Learning Project Lifecycle

### Steps of an ML Project

1. Scoping

  * Define project

2. Data

  * Define data and establish baseline

  * Label and organize data

3. Modeling

  * Select and train model

  * Perform error analysis

4. Deployment

  * Deploy in production

  * Monitor & maintain system


### Case study: speech recognition

1. Scoping --- **Define project**:

  * Decide to work on speech recognition for voice search

  * Decide on key metrics:

    * Accuracy, latency, throughput

  * Estimate resources and timeline

2. Data --- **Define data and establish baseline** & **Label and organize data**:

  - Define data:

    * Is the data labeled consistently?
	* How much silence before/after each clip?
	* How to perform volume normalization?

3. Modeling --- **Select and train model** & **Perform error analysis**:

  The three key inputs that go into training a machine learning model are:

  * Code(algorithm/model)
  	
  * Hyperparameters

  * Data

  Running the code with your hyperparameters on your data gives your the ML model.

  - Reaearch/Academia:

    * Code(algorithm/model)  

	* Hyperparameters

  - Product Team:

    * Hyperparameters 

	* Data

4. Deployment -- **Deploy in production** & **Monitor & maintain system**

  - Mobile phone (edge device)    --->  Speech API ---> Prediction Server

    * Local Software

	  * VAD module  <- Microphone

  VAD -- Voice Activity Detection, and it's usually a relatively simple algorithm, maybe a learning algorithm and the job of the VAD allows the smartphone to select out just the audio that contains hopefully someone speaking so that you can send only that audio clip to your prediction server.

  One of the **key challenges** when it comes to deployment is **concept drift / data drift**. Which is what happens when the data distribution changes, such as there are more and young voices being fed to the speech recognition system. And knowing how to put in place appropriate monitors to spot such problems and then also how to fix them in a timely way is a **key skill needed** to make sure your production deployment creates a value. 

**The key idea in MLOps** is that systematic ways to think about scoping, data, modeling, and deployment, and also software tools to support best practices.


## Deployment

### Concept drift and Data drift

Loosely 松散地, this means what if your data changes after your system has already been deployed. 

- Speech recognition example

  **Training set:**

    * Purchased data, historical user data with transcripts

  **Test set:**

    * Data from a few months ago

  How has the data changes?

When data changes, sometimes it is a **gradual 渐进的 change**, such as the English language which does change, but change very slowly with new vocabulary. Sometimes data changes **very suddently** where there's a sudden shock to a system.

Sometimes the terminology of how to describe these data changes is not used completely consistently, but some time the term **data drift** is used to describe if the input distribution `x` changes. Such as if a new politician or celebrity suddenly becomes well known and he's mentioned much more than before. The term **concept drift** refers to if the desired mapping. From x to y changes such as if, before COVID-19. Perhaps for a given user, a lot of surprising online purchases, should have flagged that account for fraud. After the start of COVID-19, maybe those same purchases, would not have really been any cause for alarm, in terms of flagging. That the credit card may have been stolen.

 When you deploy a machine learning system, **one of the most important tasks**, will often be to make sure you can detect and manage any changes. Including both **Concept drift**, which is when the definition of what is y given x changes. As well as **Data drift**, which is if the distribution of x changes, even if the mapping from x or y does not change.

In addition to managing these changes to the data, a second set of issues, that you will have to manage to deploy a system successfully, are **Software engineering issues**. You are implementing a prediction service whose job it is to take queries `x` and output prediction `y`, you have a lot of design choices as to how to implement this piece of software. Here's a **checklist of questions**, that might help you with making the appropriate decisions for managing the software engineering issues.

- Software engineering issues **Checklist of questions**:

  * Realtime or Batch

  * Cloud vs. Edge/Browser

  * Compute resources (CPU/GPU/memory)

  * Latency, throughput (QPS)

  * Logging

  * Security and privacy

**To summarize**, deploying a system requires two broad sets of tasks: there is writing the **software** to enable your to deploy the system in production. There is what you need to do to **monitor** the system performance and to continue to maintain it, expecially in the face of concepts drift as well as data drift.
## Vocabulary

* fall short --- 达不到

* QPS --- Queries Per Second
