---
youku_id: XMTYxMjk0MzY3Ng
youtube_id: GB8SNR-cT7w
description: 处理不同问题的时候呢, 我们会要用到不同的机器学习-学习方法. Sklearn 提供了一张非常有用的流程图,供我们选择合适的学习方法. 
chapter: 2
title: 选择学习方法
author: Alice
date: 2016-11-3
post-headings:
  - 看图选方法
---


学习资料:
  * 选择模型 [流程图](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html){:target="_blank"}

{% include assign-heading.html %}

安装完 Sklearn 后，不要直接去用，先了解一下都有什么模型方法，然后选择适当的方法，来达到你的目标。

Sklearn 官网提供了一个流程图，蓝色圆圈内是判断条件，绿色方框内是可以选择的算法：

{% include tut-image.html image-name="2_1_1.png" %}

从 START 开始，首先看数据的样本是否 `>50`，小于则需要收集更多的数据。

由图中，可以看到算法有四类，**分类，回归，聚类，降维**。

其中 **分类和回归**是监督式学习，即每个数据对应一个 label。
**聚类** 是非监督式学习，即没有 label。
另外一类是 **降维**，当数据集有很多很多属性的时候，可以通过 降维 算法把属性归纳起来。例如 20 个属性只变成 2 个，注意，这不是挑出 2 个，而是压缩成为 2 个，它们集合了 20 个属性的所有特征，相当于把重要的信息提取的更好，不重要的信息就不要了。

然后看问题属于哪一类问题，是分类还是回归，还是聚类，就选择相应的算法。
当然还要考虑数据的大小，例如 `100K` 是一个阈值。

可以发现有些方法是既可以作为分类，也可以作为回归，例如 `SGD`。