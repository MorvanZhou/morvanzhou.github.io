---
ref-path: _tutorials/machine-learning/ML-intro/5-03-neuro-evolution.md
youku_id: XMzAwNzU0NzI1Ng
youtube_id: tWoS8Td6biQ
bilibili_id: 15983148
title: 什么是神经网络进化 (Neuro-Evolution)
chapter: 4
thumbnail: /static/thumbnail/ML-intro/NE_thumbnail.png
description: "在进化算法这系列的内容中我做了很久铺垫, 现在总算到了最前沿最先进的技术了. 我们知道机器学习, 深度学习很多时候都和神经网络是分不开的. 那将进化和神经网络结合也在近些年有了突破.
你大多数时候所见到的人工神经网络是一种计算机能理解的数学模型, 这个模型将观测到的信息通过类似电信号的方式正向传播, 获取深程度的理解, 然后输出自己的判断. 最后通过对比自己的判断和真是数据, 将误差反向传播, 更新自己的网络参数. 但是生物中的神经网络却没有这一套反向传播的系统, 它往往是只产生正向传播, 然后通过刺激产生新的神经联结, 用这些产生的联结理解事物. 这就是大家为什么都在说人工神经网络是和生物神经网络不同的原因之一. 但是早在二十一世纪初, 科学家们已经将生物神经网络的这套系统用程序给实现了, 我们就来看看他们是如何应用的, 他们的优势和劣势各是什么?如果用进化理论来实现神经网络的更新,"
post-headings:
  - 人工神经网络和生物神经网络
  - 遗传算法 和 进化策略 加 神经网络
  - 梯度 or 进化
  - 局部 and 全局最优
  - 并行强化学习
---

{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}