---
youku_id: XMjgxNTY1NzQwOA
youtube_id: Yp29JqL_dd4
bilibili_id: 16000257
title: "科普: 神经网络的黑盒不黑"
thumbnail: "/static/thumbnail/ML-intro/feature_representation.png"
chapter: 1
description: "今天我们来说说为了理解神经网络在做什么, 对神经网络这个黑盒的正确打开方式.
当然, 这可不是人类的神经网络, 因为至今我们都还没彻底弄懂人类复杂神经网络的运行方式. 今天只来说说计算机中的人工神经网络. 我们都听说过, 神经网络是一个黑盒."
post-headings:
  - 神经网络
  - 黑盒
  - 神经网络分区
  - 举例说明
  - 迁移学习
ref-path: _tutorials/machine-learning/ML-intro/2-7-feature-representation.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}
