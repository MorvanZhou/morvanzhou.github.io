---
youku_id: XMTYxMjQ2NTYyNA
youtube_id: aNjdw9w_Qyc
bilibili_id: 16008322
description: 机器学习中的监督学习(supervised learning)问题大部分可以分成 Regression (回归)和 Classification(分类) 这两种. Tensorflow 也可以做到这个. 回归是说我要预测的值是一个连续的值,比如房价,汽车的速度,飞机的高度等等.而分类是指我要把东西分成几类,比如猫狗猪牛等等. 我们之前的教程都是在用 regression 来教学的,这一次就介绍了如何用 Tensorflow 做 classification.
author: Mark JingNB
chapter: 5
title: Classification 分类学习
date: 2016-11-3
post-headings:
  - MNIST 数据
  - 搭建网络
  - Cross entropy loss
  - 训练
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/tensorflowTUT/tf16_classification){:target="_blank"}
  * 为 TF 2017 打造的[新版可视化教学代码](https://github.com/MorvanZhou/Tensorflow-Tutorial){:target="_blank"}

这次我们会介绍如何使用TensorFlow解决Classification（分类）问题。
之前的视频讲解的是Regression (回归)问题。
分类和回归的区别在于输出变量的类型上。
通俗理解定量输出是回归，或者说是连续变量预测；
定性输出是分类，或者说是离散变量预测。如预测房价这是一个回归任务；
把东西分成几类, 比如猫狗猪牛，就是一个分类任务。 

{% include assign-heading.html %}


首先准备数据（MNIST库）

```python
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)
```

MNIST库是手写体数字库，差不多是这样子的

{% include tut-image.html image-name="5_01_1.png" %}

数据中包含55000张训练图片，每张图片的分辨率是28×28，所以我们的训练网络输入应该是28×28=784个像素数据。

{% include assign-heading.html %}


```python
xs = tf.placeholder(tf.float32, [None, 784]) # 28x28
```

每张图片都表示一个数字，所以我们的输出是数字0到9，共10类。

```python
ys = tf.placeholder(tf.float32, [None, 10])
```

调用add_layer函数搭建一个最简单的训练网络结构，只有输入层和输出层。

```python
prediction = add_layer(xs, 784, 10, activation_function=tf.nn.softmax)
```

其中输入数据是784个特征，输出数据是10个特征，激励采用softmax函数，网络结构图是这样子的

{% include tut-image.html image-name="5_01_2.png" %}

{% include google-in-article-ads.html %}

{% include assign-heading.html %}


loss函数（即最优化目标函数）选用交叉熵函数。交叉熵用来衡量预测值和真实值的相似程度，如果完全相同，它们的交叉熵等于零。

```python
cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
reduction_indices=[1])) # loss
```
train方法（最优化算法）采用梯度下降法。

```python
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)
sess = tf.Session()
# tf.initialize_all_variables() 这种写法马上就要被废弃
# 替换成下面的写法:
sess.run(tf.global_variables_initializer())
```

{% include assign-heading.html %}

现在开始train，每次只取100张图片，免得数据太多训练太慢。

```python
batch_xs, batch_ys = mnist.train.next_batch(100)
sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
```

每训练50次输出一下预测精度

```python
if i % 50 == 0:
        print(compute_accuracy(
            mnist.test.images, mnist.test.labels))
```

输出结果如下：

{% include tut-image.html image-name="5_01_3.png" %}

有没有很惊讶啊，如此简单的神经网络结构竟然可以达到这样的图像识别精度，其实稍作改动后，识别的精度将大幅提高。
请关注后续课程哦。

