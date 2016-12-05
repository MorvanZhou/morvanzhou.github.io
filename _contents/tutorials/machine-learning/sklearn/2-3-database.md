---
youku_id: XMTYxNjU0NzU1Mg
youtube_id: lXznUoPCJLM
description: Sklearn 提供了很多的有用的数据库,既有真实数据也有你可以编造的数据!特别的强大.
chapter: 2
title: sklearn 强大数据库
author: Alice
date: 2016-11-3
---
* 学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk5_datasets.py)
  * 更多可用数据 [网址](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets)

安装完 Sklearn 后，不要直接去用，先了解一下都有什么模型方法，然后选择适当的方法，来达到你的目标。

Sklearn 官网提供了一个流程图，蓝色圆圈内是判断条件，绿色方框内是可以选择的算法：

<img class="course-image" src="/static/results/sklearn/2_3_1.png">

从 START 开始，首先看数据的样本是否 `>50`，小于则需要收集更多的数据。

由图中，可以看到算法有四类，**分类，回归，聚类，降维**。

其中 **分类和回归**是监督式学习，即每个数据对应一个 label。
**聚类** 是非监督式学习，即没有 label。
另外一类是 **降维**，当数据集有很多很多属性的时候，可以通过 降维 算法把属性归纳起来。例如 20 个属性只变成 2 个，注意，这不是挑出 2 个，而是压缩成为 2 个，它们集合了 20 个属性的所有特征，相当于把重要的信息提取的更好，不重要的信息就不要了。

然后看问题属于哪一类问题，是分类还是回归，还是聚类，就选择相应的算法。
当然还要考虑数据的大小，例如 `100K` 是一个阈值。

可以发现有些方法是既可以作为分类，也可以作为回归，例如 `SGD`。

