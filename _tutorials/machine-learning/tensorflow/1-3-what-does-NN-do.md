---
youku_id: XMTYxMzQzNDc5Ng
youtube_id: tM4z02cDNa4
bilibili_id: 16001893
description: 机器学习 其实就是让电脑不断的尝试模拟预测已知的数据.
chapter: 1
title: 神经网络在干嘛
date: 2016-11-3
author: 张乐
post-headings:
  - 拟合曲线
  - 拟合参数
---


学习资料:
  * 本节的代码会在 [这一节]({% link _tutorials/machine-learning/tensorflow/3-1-add-layer.md %}) 中一一实现.

{% include assign-heading.html %}

机器学习 其实就是让电脑不断的尝试模拟已知的数据.
他能知道自己拟合的数据离真实的数据差距有多远,
然后不断地改进自己拟合的参数,提高拟合的相似度.

本例中蓝色离散点是我们的数据点,
红线是通过神经网络算法拟合出来的曲线,

{% include tut-image.html image-name="1_3_1.png" %}

它是对我们数据点的一个近似表达. 可以看出, 在开始阶段, 红线的表达能力不强, 误差很大.
不过通过不断的学习, 预测误差将会被降低. 所以学习到后来. 红线也能近似表达出数据的样子.

{% include tut-image.html image-name="1_3_2.png" %}

{% include assign-heading.html %}


如果红色曲线的表达式为：`y = a*x + b`
其中`x`代表`inputs`, 
`y`代表`outputs`, `a`和`b`是神经网络训练的参数.
模型训练好了以后,`a`和`b`的值将会被确定, 比如 `a=0.5`, `b=2`,当我们再输入`x=3`时,
我们的模型就会输出 `0.5*3 + 2` 的结果.
模型通过学习数据, 得到能表达数据的参数, 然后对我们另外给的数据所作出预测.
