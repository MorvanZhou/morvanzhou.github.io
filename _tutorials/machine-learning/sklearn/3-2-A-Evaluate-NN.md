---
youku_id: XMTY5MTk1NzIzMg
youtube_id: vBJ_XbRnzKE
title: 检验神经网络 (Evaluation)
description: 检验神经网络有没有学习到东西很重要. 应该如何来评价自己的神经网络, 从评价当中如何改进我们的神经网络. 其实评价神经网络的方法, 和评价其他机器学习的方法大同小异. 我们首先说说为什么要评价,检验学习到的神经网络. 
chapter: 3
post-headings:
  - Training and Test data
  - 误差曲线
  - 准确度曲线
  - 正规化
  - 交叉验证
ref-path: _tutorials/machine-learning/ML-intro/3-01-Evaluate-NN.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}