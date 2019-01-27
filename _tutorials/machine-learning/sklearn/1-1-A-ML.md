---
b_av: 17003173
b_cid: 27793625
b_page: 1
youku_id: XMTYyMjk2NDIwOA
youtube_id: YY7-VKXybjc
title: 机器学习 (Machine Learning)
description: "在这里我们介绍了什么是机器学习, 还有机器学习包含了哪些方法.
通常来说, 机器学习的方法包括:
监督学习 supervised learning;
非监督学习 unsupervised learning;
半监督学习 semi-supervised learning;
强化学习 reinforcement learning;
遗传算法 genetic algorithm.
大家就在影片中看看这些方法究竟都有哪些不同吧."
chapter: 1
post-headings:
  - 多种多样的机器学习
ref-path: _tutorials/machine-learning/ML-intro/1-1-machine-learning.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}