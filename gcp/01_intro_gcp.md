# GCP Fundentials -- Core Infrastruction

## Introducing Google Cloud Platform

This .md file only record some basic concepts form the course course.

Please read this .md together with coursera video course "Google Cloud Fundamentals"

- The Google network

According to some estimates out there publicly, Google's network carries as much as 40 percent of the world's Internet traffic every day. Google's network is the largest of its kind on earth and the company has invested billions of dollars over the years to build it. It's designed to give its users the **highest possible throughput** and **the lowest possible latencies** for their applications. The network interconnects at more than 90 Internet exchanges and more than 100 points of presence worldwide. When an Internet user sends traffic to a Google resource, Google responds to the user's request from an edge network location that will provide the lowest latency. Google's Edge-caching network sites content close to end users to minimize latency.

- GCP regions and zones

  * Zone (the finest grain level)

  A zone is a deployment area for Google Cloud Platform Resources.

  All the zones within a region have fast network connectivity among them. Locations within regions usually have round trip network latencies of under five milliseconds. Think of a zone as a single failure domain within a region. As part of building a fault tolerant application, you can spread their resources across multiple zones in a region.

- Budgets and Billing

GCP provides four tools to help:
  * budgets & alerts
  * billing export
  * reports (Reports is a visual tool in the GCP console that allows you to monitor your expenditure.)
  * quotas (Quotas are designed to prevent the over-consumption of resources, whether because of error or *malicious attack 恶意攻击*.)
  
  There are two types of quotas: **rate quotas** and **allocation quotas**

## Module Introduction

IAM - Identity and Access Management

**The principle of "least privilege 最低权限"** is very important in managing any kind of compute infrastructure, whether it's in the Cloud or on-premises. This principle says that each user should have only those privileges needed to do their jobs. In a least-privilege environment, people are protected from an entire class of errors.

There are four ways to interact with GCP's management layer:

* through the web-based console,
* through the SDK and its command-line tools,
* through the APIs,
* through a mobile app.

When you build an application on your **on-premises infrastructure**, you're responsible for the entire stack security. From the physical security of the hardware, and the premises in which they're housed, through **the encryption of the data on disk, the integrity of your network, all the way up to securing the content stored in those applications**. When you move an application to Google Cloud Platform, Google handles many of the lower layers of security. Because of its scale, Google can deliver a higher level of security at these layers than most of its customers could afford to do on their own. The upper layers of the security stack remain the customers' responsibility. Google provides tools such as IAM to help customers implement the policies they choose at these layers.

## The Google Cloud Platform resource

You may find it easiest to understand the GCP resource hierarchy from the bottom up. All the resources you use, whether they're virtual machines, cloud storage buckets, tables and big query or anything else in GCP are organized into **projects**. Optionally, these projects may be organized into **folders**. *Folders can contain other folders*. All the folders and projects used by your organization can be brought together under **an organization node**.

Projects, folders and origination nodes are all places where the policies can be defined.

- **Resource hirarchy levels define trust boundaries**

  * Group your resources according to your organization structure

  * Levels of the hierarchy provide **trust boundaries** and **resource isolation**.

- **Vocabulary:**

  doable and manageable

  durable 耐用的

  tedious and error prone 乏味且容易出错

  cryptography 密码学

  from broadest to finest-grained 从最广泛到最细粒度

  drudgery 苦差事  
  drudge 苦力

  Incognito mode 隐身模式
- **Terminology**

  glitch 故障 fault, malfunction, error breakdown

  LAMP Stack, LAMP stands for Linux, Apache, MySQL, PHP

  Google provides client libraries that **take a lot of the drudgery out of the task of calling GCP from your code**.

  idioms 习语

   a full-fledged operating system 成熟的操作系统

   All data in Cloud Bigtable is encrypted in both **in-flight and at rest 传输中和静态中加密**.

## Identity and Access Management (IAM)

- Google IAM defines:

  * Who

  * Can do what

  * On which resource

- There are three types of IAM roles:

  * Primitive

  * Prefefined

  * Custom

## IAM roles

- Service Accounts control server-to-server interactions

What if you want to give permissions to a Compute Engine virtual machine, rather than to a person? Then you would use a **service account**.

  * Provide an identity for carrying out  server-to-server interactions in a project

  * Used to **authenticate** from one service to another

  * Used to **control privileges** used by rescources

    - So that applications can perform actions on behalf of authenticated end users

  * Identified with an **email** address
    
	*PROJECT_NUMBER*-comupte@developer.gserviceaccount.com

	*PROJECT_ID*@appspot.gserviceaccount.com

## Cloud Marketplace(formerly Cloud Launcher)

  - Cloud Launcher

  - Qwiklabs

  Say you want a quick way to get started with GCP with minimal effort. That's what Google Cloud Launcher provides. 

  Qwiklabs allows you to get practical hands-on experience with Google Cloud, and proficiency with Google account credentials, so that you can access the Cloud Console at no cost.

## Virtual Private Cloud (VPC) Network

VPC networks connect your Google Cloud platform resources to each other and to the internet. You can **segment your networks**, use **firewall rules** to restrict access to instances, and create **static routes** to forward traffic to specific destinations.

- Google Cloud VPC networks are global; subnets are regional

The Virtual Private Cloud networks that you define have **global scope**. They can have **subnets** in any GCP region worldwide and subnets can span the zones that make up a region.

## Compute Engine

Suppose you have a workload that no human being is sitting around waiting to finish, say a batch job analyzing large dataset, you can save money by choosing **preemptible VMs 抢占式虚拟** to run the job.

## Important VPC capabilities

- You control the topology of your VPC network

  * Use **Shared VPC** to share a network, or individual subnets, with other GCP projects.

  * Use **VPC Peering** to interconnect networks in GCP projects.

- With global Cloud Load Balancing, your application presents a single front-end to the world

  * Users get a single, global anycast IP address

  * Traffic goes over Google backbone from the closest point-of-presence to the user

  * Backends are selected based on load

  * Only healthy backends receive traffic

  * Np pre-warming is required

Cloud Load Balancing is a fully distributed, software-defined managed service for all your traffic. And because the load balancers don't run in VMs you have to manage, you don't have to worry about scaling or managing them. You can put Cloud Load Balancing in front of all your traffic - HTTP and HTTPS, other TCP and SSL traffic, and UDP traffic too. With Cloud Load Balancing, a single anycast IP frontends all your backend instances in regions around the world.

And what if you anticipate a huge spike in demand? Say, your online game is going to be a hit. Do you need to file a support ticket to warn Google of the incoming load? **No. No so-called pre-warning is required.**

- Google VPC offers a suite of load-balancing options(Table in website)

  * Global HTTP(s)  --- L7

  * Global SSL Proxy --- L4

  * Global TCP Proxy --- L4

  * Regional  --- LB of any traffic(TCP, UDP)

  * Regional internal --- LB of  traffic inside a VPC

- Google DNS is highly available and  scalable 

  * Create manage zones, then add, edit, delete DNS records

One of the most famous Google services that people don't pay for is 8.8.8.8, which provides a public domain name service to the world. DNS is what translates internet host names to addresses.

- Cloud CDN(Content Delivery Network)

  * Use Google's globally distributed **edge caches** to cache content close to your users

  * Or use CDN Interconnect if you'd prefer  to use a different CDN

- Google Cloud Platform offers many interconnect options

  * VPN

  * Direct Peering

  * Carrier Peering

  * Dedicated Interconnect

## Cloud Storage

- Cloud Storage is binary large-object storage

  * High performance, internet-scale

  * Simple administration

    - Does not require capacity management

**What's object storage?** It's not the same as **file storage**, in which you manage your data as a hierarchy of folders. It's not the same as **block storage**, in which your operating system manages your data as chunks of disk. Instead, **object storage** means **you save to your storage here, you keep this arbitrary bunch of bytes I give you and the storage lets you address it with a unique key.** That's it. Often these unique keys are in the **form of URLs** which means object storage interacts nicely with Web technologies.

Cloud Storage is not a file system because each of your objects in Cloud Storage has a URL.

- Cloud Storage is binary large-object storage

  * Data encryption at rest 静态数据加密

  * Data encryption in transit by default from Google to endpoint (https)

  * Online and offline import services are available

- There are several ways to control access to your objects and buckets:

  * For most purposes, Cloud IAM is sufficient

  * If you need *finer control 更精细的控制*, you can create **access control lists - ACLs** - that offer finer control.
    - Scope
	- Permission

- Choosing among Cloud Storage classes

  * Multi-regional  --- high performance object storage

  * Regional  --- high performance object storage

  * Nearline --- backup and archival storage

  * Codeline --- backup and archival storage

Multi-regional storage on the other hand, cost a bit more but it's **Geo-redundant**. That means you pick a broad geographical location like the United States, the European Union, or Asia and cloud storage stores your data in at least two geographic locations separated by at least 160 kilometers.

- There are several ways to bring data into Cloud Storage

  * Online transfer: Self-managed copies using command-line tools or drag-and-drop

  * Storage Transfer Service: Scheduled, managed batch transfers

  * Transfer Appliance: Rackable appliances to  securely ship your data

## Cloud Bigtable

- Cloud Bigtable is managed NoSQL

  * Fully managed NoSQL, wide-column database service for terabyte applications

  * Accessed using HBase API

  * Native compatibility with big data, Hadoop ecosystems

Cloud Bigtable is **Google's NoSQL, big data database** service. **What is NoSQL mean?** Well, this isn't a database course, so I'll give you a very informal picture. **Think first of a relational database** as offering you tables in which every row has the same set of columns, and the database engine enforces that rule and other rules you specify for each table. That's called the **database schema**. An enforce schema is a big help for some applications and a huge pain for others. Some applications call for a much more flexible approach. For example, **a NoSQL schema**. In other words, for these applications not all the rows might need to have the same columns. And in fact, the database might be designed to take advantage of that **by sparsely populating the rows 稀疏填充行**. That's part of what makes a NoSQL database what it is. Which brings us to Bigtable. **Your databases in Bigtable are sparsely populated tables that can scale to billions of rows and thousands of columns allowing you to store petabytes of data.**

- Why choose Cloud Bigtable?

  * Scalability: Managed, scalable storage

  * Data encryption in-flight and at rest

  * Control access with IAM

  * Bigtable drives major applications such as Google Analytics and Gmail

## Cloud SQL and Cloud Spanner

- Cloud SQL is a managed RDBMS

  * Offers MySQL and PostgreSQLBeta database as a service

  * Automatic replication

  * Managed backups

  * Vertical scaling (read and write)

  * Horizontal scaling (read)

  * Google security

Remember, these services use a database schema to help your application keep your **data consistent and correct**.

**Another feature of relational database services** that helps with the same goal - **transactions 数据库事务**. Your application can *designate 指定* a group of database changes as all or nothing. Either they all get made, or none do.

- Cloud Spanner is a horizontally scalable RDBMS

  * Strong global consistency

  * Managed instances with high availability

  * SQL queries
    
	- ANSI 2011 with extensions

  * Automatic replication

If Cloud SQL does not fit your requirements because you need horizontal scaleability, consider using Cloud Spanner. It offers transactional consistency at a global scale, schemas, SQL, and automatic synchronous replication for high availability. And, it can provide petabytes of capacity. Consider using Cloud Spanner if you have outgrown any relational database, or sharding your databases for throughput high performance, need transactional consistency, global data and strong consistency, or just want to consolidate your database. Natural use cases include, financial applications, and inventory applications.

## Cloud Datastore

- Cloud Datastore is a horizontally scalable NoSQL DB

  * Designed for application backends

We already discussed one GCP NoSQL database service: Cloud Bigtable. Another highly scalable NoSQL database choice for your applications is Cloud Datastore. One of its main use cases is to store structured data from App Engine apps. You can also build solutions that span App Engine and Compute Engine with Cloud Datastore as the integration point. As you would expect from a fully-managed service, Cloud Datastore automatically handles sharding and replication, providing you with a highly available and *durable 耐用的* database that scales automatically to handle load. **Unlike Cloud Bigtable, it also offers transactions that affect multiple database rows, and it lets you do SQL-like queries.** To get you started, Cloud Datastore has a free daily quota that provides storage, reads, writes, deletes and small operations at no charge.

## Comparing Storage Options

- Comparing storage options: technical details

## Containers, Kubernetes, and  Kubernetes Engine

- Introcuction

  * Iaas: Compute Engine, VM
  * Paas: App Engine
  * Kubernetes, it is like both Iaas and Paas

- Agenda

  * Introduction to Containers
  * Kubernetes and Kubernetes Engine 
  * Lab

- IaaS
  
  * VM

- App Engine

- Containers

  Containers are **loosely coupled** to their environments.

  * Docker
  * Cloud Build, a managed service for building containers
  
  * Container Registry service: Google Container Registry

- Kubernetes

Kubernetes makes it easy to **orchestrate many Containers** on many hosts. **Scale** them, **roll out new versions** of them, and even **roll back to the old version** if things go wrong.

## Introduction to Kubernetes and GKE

- Kubernetes: Pod

Whenever Kubernetes deploys a container or a set of related containers, it does so inside an abstraction called a **pod**. **A pod is the smallest deployable unit in Kubernetes**. Think of a pod as if it were a running process on your cluster. **It could be one component of your application or even an entire application.** Think of a pod as if it were a running process on your cluster. It could be one component of your application or even an entire application. It's common to have only one container per pod. But if you have multiple containers with a hard dependency, you can package them into a single pod. They'll automatically **share networking** and they can **have disk storage volumes in common**. Each pod in Kubernetes gets **a unique IP address** and **set of ports** for your containers. Because containers inside a pod can **communicate with each other using the localhost network interface**, they **don't know or care which nodes they're deployed on**.

**So what is a deployment?** A deployment represents a group of replicas of the same pod. It keeps your pods running even if a node on which some of them run on fails. You can use a deployment to contain a component of your application or even the entire application.

**By default, pods in a deployment or only accessible inside your cluster**, but what if you want people on the Internet to be able to access the content in your nginx web server? To make the pods in your deployment publicly available, you can connect **a load balancer** to it by running the kubectl expose command. Kubernetes then creates a **service** with a fixed IP address for your pods. **A service is the fundamental way Kubernetes represents load balancing.** To be specific, you requested Kubernetes to attach an external load balancer with a public IP address to your service so that others outside the cluster can access it. In GKE, this kind of load balancer is created as a network load balancer. This is one of the managed load balancing services that Compute Engine makes available to virtual machines. GKE makes it easy to use it with containers. Any client that hits that IP address will be routed to a pod behind the service.

**So what exactly is a service?** A service groups a set of pods together and provides a stable endpoint for them. In our case, a public IP address managed by a network load balancer, although there are other choices. But **why do you need a service?** Why not just use pods' IP addresses directly? Suppose instead your application consisted of a front end and a back end. Couldn't the front end just access the back end using those pods' internal IP addresses without the need for a service? Yes, but it would be a management problem. As deployments create and destroy pods, pods get their own IP addresses, but those addresses don't remain stable over time. Services provide that stable endpoint you need. As you learn more about Kubernetes, you'll discover other service types that are suitable for internal application back ends.
