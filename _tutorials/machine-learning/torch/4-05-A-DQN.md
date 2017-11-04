---
youku_id: XMjUyMzI1NzgwMA
youtube_id: b7PO_xfEMwE
bilibili_id: 15988613
title: 什么是 DQN
description: "今天我们会来说说强化学习中的一种强大武器, Deep Q Network 简称为 DQN. Google Deep mind 团队就是靠着这 DQN 使计算机玩电动玩得比我们还厉害.
之前我们所谈论到的强化学习方法都是比较传统的方式,
而如今, 随着机器学习在日常生活中的各种应用, 各种机器学习方法也在融汇,
合并, 升级. 而我们今天所要探讨的强化学习则是这么一种融合了神经网络和
Q learning 的方法, 名字叫做 Deep Q Network."
chapter: 4
thumbnail: /static/thumbnail/ML-intro/DQN_thumbnail.png
post-headings:
  - 强化学习与神经网络
  - 神经网络的作用
  - 更新神经网络
  - DQN 两大利器
ref-path: _tutorials/machine-learning/ML-intro/4-06-DQN.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}