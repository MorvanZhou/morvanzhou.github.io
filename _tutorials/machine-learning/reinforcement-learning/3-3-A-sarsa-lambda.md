---
youku_id: XMjI1OTczMjQ3Mg
youtube_id: PANBb46qiYI
bilibili_id: 15988888
title: 什么是 Sarsa(lambda)
description: "今天我们会来说说强化学习中基于 Sarsa 的一种提速方法, 叫做 sarsa-lambda. 通过上个视频的介绍, 我们知道这个 Sarsa 的算法是一种在线学习法, on-policy. 但是这个 lambda 到底是什么. 其实吧, Sarsa 是一种单步更新法, 在环境中每走一步, 更新一次自己的行为准则, 我们可以在这样的 Sarsa 后面打一个括号, 说他是 Sarsa(0), 因为他等走完这一步以后直接更新行为准则. 如果延续这种想法, 走完这步, 再走一步, 然后再更新, 我们可以叫他 Sarsa(1). 同理, 如果等待回合完毕我们一次性再更新呢, 比如这回合我们走了 n 步, 那我们就叫 Sarsa(n). 为了统一这样的流程, 我们就有了一个 lambda 值来代替我们想要选择的步数, 这也就是 Sarsa(lambda) 的由来. 我们看看最极端的两个例子, 对比单步更新和回合更新, 看看回合更新的优势在哪里."
chapter: 3
thumbnail: /static/thumbnail/ML-intro/Sarsa-lambda_thumbnail.png
post-headings:
  - Sarsa(n)
  - 单步更新 and 回合更新
  - 有时迷茫
  - Lambda 含义
  - Lambda 取值
ref-path: _tutorials/machine-learning/ML-intro/4-05-sarsa-lambda.md
---


{% assign post = site.tutorials | where: "category", "ML-intro" | where: "path", page.ref-path %}

{{ post[0].content }}