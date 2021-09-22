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

### Deployment patterns

- **Common deployment cases**

  1. New product/capability

  One type of deployment is if you are offering a new product or capability that you had not previously offered. In this case, a common **design pattern** is to start up a small amount of traffic and then gradually ramp it up

  2. Automate/assist with manual task

  A second common deployment use case is if there's something that's already being done by a person, but we would now like to use a learning algorithm to either automate or assist with that task. The fact that people were previously doing this gives you a few more options for how you deploy. And you see **shadow mode deployment** takes advantage of this.

  3. Replace previous ML system
  
  And finally, a third common deployment case is if you've already been doing this task with a previous implementation of a machine learning system, but you now want to replace it with hopefully an even better one.

  Key ideas:
    
	* Gradual ramp up with monitoring

	* Rollback

- **Visual inspection example**

  * **Shadow mode**:

    * ML system shadows the human and run in parallel.

    * ML system's output not used for any decisions during this phase.

**The purpose of a shadow mode deployment** is that allows you to gather data of how the learning algorithm is performing and how that compares to the human judgment. And by something the it offers you can then verify if the learning algorithm's predictions are accurate and therefore use that to decide whether or not to maybe allow the learning algorithm to make some real decisions in the future. 

- **Canary deployment**

When you are ready to let a learning algorithm start making real decisions, a common deployment pattern is to use a **canary deployment**.

  * Roll out to small fraction (say 5%) of traffic initially.

  * Monitor system and ramp up treaffic gradually.

The phrase canary deployment is a reference to the English idiom or the English phrase canary in a coal mine, which refers to how coal miners used to use canaries to spot if there's a gas leak. But with canary the deployment, hopefully this allows you to spot problems early on before there are maybe overly large consequences to a factory or other context in which you're deploying your learning algorithm.

- **Blue green deployment**

Another deployment pattern that is sometimes used is a blue green deployment. Let me explain with the picture.

Say you have a system, a camera software for collecting phone pictures in your factory. These phone images are sent to a piece of software that takes these images and routes them into some visual inspection system. In the terminology of a blue green deployments, the **old version of your software is called the blue version** and **the new version, the Learning algorithm you just implemented is called the green version**. In a blue green deployment, what you do is have the router send images to the old or the blue version and have that make decisions. And then when you want to switch over to the new version, what you would do is have the router stop sending images to the old one and suddenly switch over to the new version. So the way the blue green deployment is implemented is you would have an old prediction service may be running on some sort of service. You will then spin up a new prediction service, the green version, and you would have the router suddenly switch the traffic over from the old one to the new one. The advantage of a blue green deployment is that there's an easy way to enable rollback. If something goes wrong, you can just very quickly have the router go back reconfigure their router to send traffic back to the old or the blue version, assuming that you kept your blue version of the prediction service running. In a typical implementation of a blue green deployment, people think of switching over the traffic 100% all at the same time. But of course you can also use a more gradual version where you slowly send traffic over.

As you can imagine, whether use **shadow mode, canary mode, blue green, or some of the deployment pattern**, quite a lot of software is needed to execute this. MLOps tools can help with implementing these deployment patterns or you can implement it yourself.

- **Degrees of automation**

One of the most useful frameworks I have found for thinking about how to deploy a system is to think about deployment not as a 0, 1 is either deploy or not deploy, but instead to design a system thinking about what is the appropriate **degree of automation**.

`Human Only` -> `Shadow Only` -> `AI Assistance` -> **`Partial Automation`** -> `Full Automation`


## Monitoring

### Monitoring dashboard

Examples:

  * Server load

  * Fraction of non-null outputs

  * Fraction of missing input values

Decide what to monitor:

  * Brainstorm the things that could go wrong.

  * Brainstorm a few statistics/metrics that will detect the problem.

  * It is ok to use many metrics initially and gradually remove the ones you find not useful.

### Examples of metrics to track

  **Software metrics:** | Memory, compute, latency, throughput, server load

  **Input metrics:**:
  	
	* Avg input length
	* Avg input volume
	* Num missing values
	* Avg image brightness

  **Output metrics:**

    * # times return ""(null)
	* # times user redoes search
	* # times user switches to typing
	* CTR --- Click-Through Rate


### Just as ML modeling is iterative, so is deployment

  ML: `-> ML model/data -> Experiment -> Error analysis ->`

  Deployment: `-> Deployment/Monitoring -> Traffic -> Peformance analysis ->`

  * Iterative process to choose the right set of metrics to monitor

  **Common practices** after you have chosen a set of metrics to measure:

    * Set thresholds for alarms
    
	* Adapt metrics and thresholds over time

**Key takeaways** are that it is only by monitoring the system that you can spot if there may be a problem that may cause you to go back to perform a deeper error analysis, or that may cause you to go back to get more data with which you can update your model so as to maintain or improve your system's performance.


### Model maintence

  * Manual retraining (more common)

  * Automatic retraning


## Pipeline monitoring

### Speech recognition example

Theory: `Audio` -> `Speech Recognition` -> `Transcript`

Realword: `Audio` -> `VAD` -> `Speech Recognition` -> `Transcript`

Some cellphones might have VAD clip audio differently, leading to degraded peformance

### User profile example

`User Data` -> `User Profile` -> `Recommender System` -> `Product recomendations`

(e.g., clickstream) -> (e.g., own car?)

### Metrics to monitor

  Monitor:

    * Software metrics

	* Input metrics

	* Output metrics

  How quickly do they change?

    * User data generally has slower drift

	* Enterprise data (B2B applications) can shift fast.

## [Week 1 Optional References](https://www.coursera.org/learn/introduction-to-machine-learning-in-production/supplement/c5tSK/week-1-optional-references)







## Vocabulary

* fall short --- 达不到

* QPS --- Queries Per Second
