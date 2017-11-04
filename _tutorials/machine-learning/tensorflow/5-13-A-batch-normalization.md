---
youku_id: XMTg1MTYwNDg2OA
youtube_id: -5hESl-Lj-4
bilibili_id: 16000304
title: 什么是批标准化 (Batch Normalization)
description: Batch Normalization, 批标准化, 和普通的数据标准化类似, 是将分散的数据统一的一种做法, 也是优化神经网络的一种方法. 在之前 Normalization 的简介视频中我们一提到, 具有统一规格的数据, 能让机器学习更容易学习到数据之中的规律.
chapter: 5
thumbnail: /static/thumbnail/ML-intro/BN.png
post-headings:
  - 普通数据标准化
  - 每层都做标准化
  - BN 添加位置
  - BN 效果
  - BN 算法
ref-path: _tutorials/machine-learning/ML-intro/3-08-batch-normalization.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}