---
youku_id: XMTY2MTU4MzM4MA
youtube_id: sPu4KpzLaDQ
title: 神经网络在做什么
description: Theano 能做的机器学习种类一般分两种, 一种是回归学习,一种是分类学习. 大家可以下载代码自己看看theano, 神经网络是如何进行分类学习的.
author: 缘
chapter: 1
post-headings:
  - 动画演示
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/theanoTUT/theano3_what_does_ML_do.py){:target="_blank"}
  * [本例的代码讲解教程]({% link _tutorials/machine-learning/theano/3-1-layer.md %})

{% include assign-heading.html %}

今天我们会用图像呈现神经网络所做的事情.
我们会让 theano 做出来的的神经网络拟合上这些数据点. 从中学习数据点的规律, 并能预测这些规律.
很多时候, 我们遇到的会是一个数据拟合问题, 比如我们有这样一些数据点:

{% include tut-image.html image-name="1_3_1.png" %}

神经网络所要做的事情就是学习一条红色的曲线来概括图中的蓝色的数据点, 也是神经网络学习出来的拟合曲线.

{% include tut-image.html image-name="1_3_2.gif" %}

这个神经网络的具体的搭建方法, 我们会在之后的教程中逐步来讲解, 这个例子只是为了展示神经网络的工作流程.