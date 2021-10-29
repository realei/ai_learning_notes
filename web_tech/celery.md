# Celery 

[Celery in Chinese](https://www.celerycn.io/ru-men/celery-jian-jie)

[Celery in English](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)

## What's a Task Queue?

**Task queues** are used as a mechanism to distribute work across **threads or machines**.

任务队列一般用于线程或计算机之间分配工作的一种机制。

A task queue’s input is a unit of work called a task. Dedicated worker processes constantly monitor task queues for new work to perform.

任务队列的输入是一个称为任务的工作单元，有专门的**职程（Worker)**进行不断的监视任务队列，进行执行新的任务工作。

Celery communicates via messages, usually using a broker to mediate between clients and workers. To initiate a task the client adds a message to the queue, the broker then delivers that message to a worker.

Celery 通过消息机制进行通信，通常使用中间人（Broker）作为客户端和职程（Worker）调节。启动一个任务，客户端向消息队列发送一条消息，然后中间人（Broker）将消息传递给一个职程（Worker），最后由职程（Worker）进行执行中间人（Broker）分配的任务。

A Celery system can consist of multiple workers and brokers, giving way to high availability and horizontal scaling.

Celery 可以有多个职程（Worker）和中间人（Broker），用来提高Celery的高可用性以及横向扩展能力。

Celery is written in Python, but the protocol can be implemented in any language. In addition to Python there’s node-celery and node-celery-ts for Node.js, and a PHP client.

Language interoperability互操作性 can also be achieved exposing an HTTP endpoint and having a task that requests it (webhooks).

## Celery is..

* Simple

* Highly Available

  Workers and clients will automatically retry in the event of connection loss or failure, and some brokers support HA in way of Primary/Primary or Primary/Replica replication.

* Fast 

  A single Celery process can process millions of tasks a minute, with sub-millisecond round-trip latency (using RabbitMQ, librabbitmq, and optimized settings).

* Flexible

  Almost every part of Celery can be extended or used on its own, Custom pool implementations, serializers, compression schemes, logging, schedulers, consumers, producers, broker transports, and much more.

  Celery 的每个部分几乎都可以自定义扩展和单独使用，例如自定义连接池、序列化方式、压缩方式、日志记录方式、任务调度、生产者、消费者、中间人（Broker）等。
