---
youku_id: XMTkyMDY5MTk2OA
youtube_id: AINrxEjflaM
bilibili_id: 15987194
title: 强化学习方法汇总 (Reinforcement Learning)
description: "了解强化学习中常用到的几种方法,以及他们的区别, 对我们根据特定问题选择方法时很有帮助.
强化学习是一个大家族, 发展历史也不短, 具有很多种不同方法. 比如说比较知名的控制方法 Q learning, Policy gradients, 还有基于对环境的理解的 model-based RL 等等. 接下来我们通过分类的方式来了解他们的区别."
chapter: 1
thumbnail: /static/thumbnail/ML-intro/RL_methods.png
post-headings:
  - Model-free 和 Model-based
  - 基于概率 和 基于价值
  - 回合更新 和 单步更新
  - 在线学习 和 离线学习
ref-path: _tutorials/machine-learning/ML-intro/4-02-RL-methods.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}