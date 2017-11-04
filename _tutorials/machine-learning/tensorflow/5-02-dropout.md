---
youku_id: XMTYxODI2Mzk5Ng
youtube_id: f2F9Xsd7KVk
bilibili_id: 16008342
description: 实际机器学习问题当中,我们很常遇到overfitting 的问题.Tensorflow 附有一个很好解决 overfitting 问题的工具,叫做dropout, 你只需要给予它一个不被 drop 掉的百分比就能很好的降低 overfitting.
author: Mark JingNB
chapter: 5
title: Dropout 解决 overfitting
date: 2016-11-3
post-headings:
  - 要定
  - 建立 dropout 层
  - 训练
  - 可视化结果
  - 可能会遇到的问题
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/tensorflowTUT/tf17_dropout){:target="_blank"}
  * 为 TF 2017 打造的[新版可视化教学代码](https://github.com/MorvanZhou/Tensorflow-Tutorial){:target="_blank"}
  * 机器学习-简介系列 [过拟合]({% link _tutorials/machine-learning/ML-intro/3-05-overfitting.md %})

{% include assign-heading.html %}

Overfitting 也被称为过度学习，过度拟合。 它是机器学习中常见的问题。
举个Classification（分类）的例子。

{% include tut-image.html image-name="5_02_1.png" %}

图中黑色曲线是正常模型，绿色曲线就是overfitting模型。尽管绿色曲线很精确的区分了所有的训练数据，但是并没有描述数据的整体特征，对新测试数据的适应性较差。

举个Regression (回归)的例子，

{% include tut-image.html image-name="5_02_2.png" %}

第三条曲线存在overfitting问题，尽管它经过了所有的训练点，但是不能很好的反应数据的趋势，预测能力严重不足。
TensorFlow提供了强大的dropout方法来解决overfitting问题。

{% include assign-heading.html %}

本次内容需要使用一下 sklearn 数据库当中的数据, 没有安装 sklearn 
的同学可以参考一下[这个教程]({% link _tutorials/machine-learning/sklearn/1-2-install.md %})
安装一下. 然后 `import` 以下模块.

```python
import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import LabelBinarizer
```

```python
keep_prob = tf.placeholder(tf.float32)
...
...
Wx_plus_b = tf.nn.dropout(Wx_plus_b, keep_prob)
```

这里的`keep_prob`是保留概率，即我们要保留的结果所占比例，它作为一个`placeholder`，在`run`时传入，
当`keep_prob=1`的时候，相当于100%保留，也就是dropout没有起作用。
下面我们分析一下程序结构，首先准备数据，

```python
digits = load_digits()
X = digits.data
y = digits.target
y = LabelBinarizer().fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
```

其中`X_train`是训练数据, `X_test`是测试数据。
然后添加隐含层和输出层

```python
# add output layer
l1 = add_layer(xs, 64, 50, 'l1', activation_function=tf.nn.tanh)
prediction = add_layer(l1, 50, 10, 'l2', activation_function=tf.nn.softmax)
```

loss函数（即最优化目标函数）选用交叉熵函数。交叉熵用来衡量预测值和真实值的相似程度，如果完全相同，交叉熵就等于零。

```python
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                              reduction_indices=[1]))  # loss
```
train方法（最优化算法）采用梯度下降法。

```python
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
```




{% include google-in-article-ads.html %}

{% include assign-heading.html %}

最后开始train，总共训练500次。

```python
sess.run(train_step, feed_dict={xs: X_train, ys: y_train, keep_prob: 0.5})
#sess.run(train_step, feed_dict={xs: X_train, ys: y_train, keep_prob: 1})
```

{% include assign-heading.html %}


训练中`keep_prob=1`时，就可以暴露出overfitting问题。`keep_prob=0.5`时，`dropout`就发挥了作用。
我们可以两种参数分别运行程序，对比一下结果。

当`keep_prob=1`时，模型对训练数据的适应性优于测试数据，存在overfitting，输出如下：
红线是 `train` 的误差, 蓝线是 `test` 的误差.

{% include tut-image.html image-name="5_02_3.png" %}

当`keep_prob=0.5`时效果好了很多，输出如下：

{% include tut-image.html image-name="5_02_4.png" %}

程序中用到了Tensorboard输出结果，可以参考前面教程:

* [可视化好助手 Tensorboard 1]({% link _tutorials/machine-learning/tensorflow/4-1-tensorboard1.md %})
* [可视化好助手 Tensorboard 2]({% link _tutorials/machine-learning/tensorflow/4-2-tensorboard2.md %})






{% include assign-heading.html %}

由于评论区中讨论了很多这份代码的问题, 我在此说明一下. 因为 Tensorflow 升级改版了, 原本视频中可以执行的代码可能会遇到一些问题.
强烈推荐看看我2017年根据新版本的 Tensorflow 写的[升级版, 简化版代码](https://github.com/MorvanZhou/Tensorflow-Tutorial){:target="_blank"},
比旧版本的更容易懂, 而且可视化效果做得更好. 里面也有 Dropout 这节内容.