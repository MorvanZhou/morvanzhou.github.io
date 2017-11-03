---
youku_id: XMjI1NjY5MTk4OA
youtube_id: AANzrFOQIiM
bilibili_id: 15988106
title: 什么是 Sarsa
description: "今天我们会来说说强化学习中一个和 Q learning 类似的算法, 叫做 Sarsa. 在强化学习中 Sarsa 和 Q learning 及其类似, 这节内容会基于之前我们所讲的 Q learning. 所以还不熟悉 Q learning 的朋友们, 请前往我制作的 Q learning 简介 (知乎专栏). 我们会对比 Q learning, 来看看 Sarsa 是特殊在哪些方面. 和上次一样, 我们还是使用写作业和看电视这个例子. 没写完作业去看电视被打, 写完了作业有糖吃."
chapter: 3
thumbnail: /static/thumbnail/ML-intro/Sarsa_thumbnail.png
post-headings:
  - Sarsa 决策
  - Sarsa 更新行为准则
  - 对比 Sarsa 和 Q-learning 算法
ref-path: _tutorials/machine-learning/ML-intro/4-04-sarsa.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}