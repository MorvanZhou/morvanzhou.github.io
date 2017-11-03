---
chapter: 2
ref-path: _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md
youku_id: XMjk0NzE0MjgxNg
youtube_id: BEquIwfEXes
bilibili_id: 15983143
title: 遗传算法 (Genetic Algorithm)
thumbnail: /static/thumbnail/ML-intro/genetic-algorithm.png
description: "这次我们尝试踏足机器学习中的另外一个领域, 用进化理论来解决复杂的问题. 遗传算法是进化算法的一个分支. 它将达尔文的进化理论搬进了计算机.
所以你会发现在程序中, 我们还时不时出现什么染色体, DNA, 遗传, DNA交叉, 变异 这些东西. 不过想想也能明白, 在自然界中, 优胜劣汰, 我们人类也是靠着这些手段一步步从猴子"
post-headings:
  - 进化算法
  - 猴子的进化
  - 种群的进化
  - 电脑里的 DNA
  - 别人的实验
---
{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}
