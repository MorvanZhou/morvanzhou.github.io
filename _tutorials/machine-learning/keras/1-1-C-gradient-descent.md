---
ref-path: _tutorials/machine-learning/ML-intro/2-8-gradient-descent.md
youku_id: XMjg1NzQwNDc4OA
youtube_id: 9sJG7LjGCnI
bilibili_id: 15999975
title: 神经网络 梯度下降
chapter: 1
thumbnail: "/static/thumbnail/ML-intro/gradient_descent.png"
description: "神经网络是当今为止最流行的一种深度学习框架, 他的基本原理也很简单, 就是一种梯度下降机制. 我们今天就来看看这神奇的优化模式吧.学习机器学习的同学们常会遇到这样的图像, 我了个天, 看上去好复杂, 哈哈, 不过还挺好看的. 这些和我们说的梯度下降又有什么关系呢? 原来这些图片展示出来了一个家族的历史, 这个家族的名字就是-”optimization” (优化问题). 优化能力是人类历史上的重大突破, 他解决了很多实际生活中的问题. 从而渐渐演化成了一个庞大的家族."
post-headings:
  - Optimization
  - 梯度下降
  - 全局 and 局部最优
---

{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}