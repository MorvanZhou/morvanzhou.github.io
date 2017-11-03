---
ref-path: _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md
youku_id: XMjk3OTcyMTU1Mg
youtube_id: Etj_gclFFFo
bilibili_id: 15983100
title: 什么是进化策略 (Evolution Strategy)
chapter: 3
thumbnail: /static/thumbnail/ML-intro/ES_thumbnail.png
description: "进化是大自然赋予我们的礼物, 我们也能学习自然界的这份礼物, 将它放入计算机, 让计算机也能用进化来解决问题. 我们接着上回提到的遗传算法, 来说一说另一种使用进化理论的优化模式-进化策略 (Evolution Strategy).
遗传算法和进化策略共享着一些东西. 他们都用遗传信息, 比如 DNA 染色体, 一代代传承, 变异. 来获取上一代没有的东西."
post-headings:
  - 进化算法
  - 遗传算法
  - 进化策略
  - 总结
---

{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}