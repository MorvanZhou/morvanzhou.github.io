---
youku_id: XMTYxMzQ1NzUwOA
youtube_id: 9l_c5260JQ8
bilibili_id: 16002144
description: Tensorflow 首先要定义神经网络的结构, 然后再把数据放入结构当中去运算和 training.
chapter: 2
title: 处理结构
date: 2016-11-3
author: 张乐
post-headings:
  - 计算图纸
  - Tensor 张量意义
---



{% include assign-heading.html %}

Tensorflow 首先要定义神经网络的结构,
然后再把数据放入结构当中去运算和 training.

{% include tut-image.html image-name="1_4_1.png" %}

<p style="text-align: center; font-size: 0.8em;">(动图效果请点击<a href="https://www.tensorflow.org/images/tensors_flowing.gif" alt="{{ page.title }}">这里</a>)</p>

因为TensorFlow是采用数据流图（data　flow　graphs）来计算,
所以首先我们得创建一个数据流流图,
然后再将我们的数据（数据以张量(tensor)的形式存在）放在数据流图中计算.
节点（Nodes）在图中表示数学操作,图中的线（edges）则表示在节点间相互联系的多维数据数组,
即张量（tensor). 训练模型时tensor会不断的从数据流图中的一个节点flow到另一节点,
这就是TensorFlow名字的由来.

{% include assign-heading.html %}

**张量（Tensor)**:
* 张量有多种. 零阶张量为 纯量或标量 (scalar) 也就是一个数值. 比如 ```[1]```
* 一阶张量为 向量 (vector), 比如 一维的 ```[1, 2, 3]```
* 二阶张量为 矩阵 (matrix), 比如 二维的  ```[[1, 2, 3],[4, 5, 6],[7, 8, 9]]```
* 以此类推, 还有 三阶 三维的 ...


