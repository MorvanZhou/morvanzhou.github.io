---
youku_id: XMTYxMzYzNTc2OA
youtube_id: HhjtJ73AwIY
bilibili_id: 16002136
description: Session 是每个 Tensorflow 文件都需要的步骤. 运行 seesion.run()可以获得你要得知的运算结果, 或者是你所要运算的部分.
author : 商晋
chapter: 2
title: Session 会话控制
date: 2016-11-3
post-headings:
  - 简单运用
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tensorflowTUT/tensorflow6_session.py){:target="_blank"}
  * 为 TF 2017 打造的[新版可视化教学代码](https://github.com/MorvanZhou/Tensorflow-Tutorial){:target="_blank"}

{% include assign-heading.html %}

欢迎回来！这一次我们会讲到 Tensorflow 中的 `Session`, `Session` 是 Tensorflow 为了控制,和输出文件的执行的语句.
运行 `session.run()` 可以获得你要得知的运算结果, 或者是你所要运算的部分. 

首先，我们这次需要加载 Tensorflow ，然后建立两个 `matrix` ,输出两个 `matrix` 矩阵相乘的结果。

```python
import tensorflow as tf

# create two matrixes

matrix1 = tf.constant([[3,3]])
matrix2 = tf.constant([[2],
                       [2]])
product = tf.matmul(matrix1,matrix2)
```

因为 `product` 不是直接计算的步骤, 所以我们会要使用 `Session` 来激活 `product` 并得到计算结果.
有两种形式使用会话控制 `Session` 。

```python
# method 1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()
# [[12]]

# method 2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)
# [[12]]
```

以上就是我们今天所学的两种 `Session` 打开模式，欢迎继续学习下一章 ———— Tensorflow 中的 `Variable`。
