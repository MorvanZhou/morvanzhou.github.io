---
youku_id: XMTc2MjA0ODQyOA
youtube_id: UlUGGB7akfE
bilibili_id: 15998264
title: 加速神经网络训练 (Speed Up Training)
description: "今天我们会来聊聊怎么样加速你的神经网络训练过程. 里面的方法包括: 
Stochastic Gradient Descent (SGD);
Momentum;
AdaGrad;
RMSProp;
Adam."
chapter: 3
post-headings:
  - Stochastic Gradient Descent (SGD)
  - Momentum 更新方法
  - AdaGrad 更新方法
  - RMSProp 更新方法
  - Adam 更新方法
ref-path: _tutorials/machine-learning/ML-intro/3-06-speed-up-learning.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}