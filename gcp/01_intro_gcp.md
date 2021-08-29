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

  tedious and error prone 乏味且容易出错

  cryptography 密码学

  from broadest to finest-grained 从最广泛到最细粒度

  drudgery 苦差事  
  drudge 苦力

  Incognito mode 隐身模式
- **Terminology**

  LAMP Stack, LAMP stands for Linux, Apache, MySQL, PHP

  Google provides client libraries that **take a lot of the drudgery out of the task of calling GCP from your code**.

  idioms 习语

   a full-fledged operating system 成熟的操作系统

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
