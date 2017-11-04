---
youku_id: XMTczNjA2Nzc5Ng
youtube_id: e9OKufD6lRM
bilibili_id: 15999993
title: 什么是过拟合 (Overfitting)
description: 今天我们会来聊聊机器学习中的过拟合 overfitting 现象, 和解决过拟合的方法. 在细说之前, 我们先用实际生活中的一个例子来比喻一下过拟合现象. 说白了, 就是机器学习模型于自信. 已经到了自负的阶段了. 那自负的坏处, 大家也知道, 就是在自己的小圈子里表现非凡,  不过在现实的大圈子里却往往处处碰壁. 所以在这个简介里,  我们把自负和过拟合画上等号.
chapter: 5
post-headings:
  - 过于自负
  - 回归分类的过拟合
  - 解决方法
ref-path: _tutorials/machine-learning/ML-intro/3-05-overfitting.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}