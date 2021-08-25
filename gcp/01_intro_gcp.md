# GCP Fundentials -- Core Infrastruction

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
