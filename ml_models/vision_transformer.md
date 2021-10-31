# [Vision Transformer 超详细解读 (原理分析+代码解读) (一)](https://zhuanlan.zhihu.com/p/340149804)

Transformer 是 Google 的团队在 2017 年提出的一种 NLP 经典模型，现在比较火热的 Bert 也是基于 Transformer。Transformer 模型使用了 **Self-Attention** 机制，**不采用 RNN 的顺序结构**，使得模型**可以并行化训练**，而且能够拥有**全局信息**。

## 1. 一切从Self-attention开始
