---
youku_id: XMTk2NTQxMzQxNg
youtube_id: HTZ5xn12AL4
bilibili_id: 15987795
title: 什么是 Q Leaning
description: "今天我们会来说说强化学习中一个很有名的算法, Q-learning. 我们做事情都会有一个自己的行为准则, 比如小时候爸妈常说”不写完作业就不准看电视”. 所以我们在 写作业的这种状态下, 好的行为就是继续写作业, 直到写完它, 我们还可以得到奖励, 不好的行为 就是没写完就跑去看电视了, 被爸妈发现, 后果很严重. 小时候这种事情做多了, 也就变成我们不可磨灭的记忆. 这和我们要提到的 Q learning 有什么关系呢? 原来 Q learning 也是一个决策过程, 和小时候的这种情况差不多. 我们举例说明."
chapter: 2
thumbnail: /static/thumbnail/ML-intro/what_is_QLearning.png
post-headings:
  - 行为准则
  - Q-Learning 决策
  - Q-Learning 更新
  - Q-Learning 整体算法
  - Q-Learning 中的 Gamma
ref-path: _tutorials/machine-learning/ML-intro/4-03-q-learning.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}