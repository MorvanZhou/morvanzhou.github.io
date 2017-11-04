---
youku_id: XMTU5NjEzOTA4NA
youtube_id: FTR36h-LKcY
bilibili_id: 16002970
description: 在 Tensorflow 里定义一个添加层的函数可以很容易的添加神经层,为之后的添加省下不少时间.
author: 赵孔亚
chapter: 3
title: 例子3 添加层 def add_layer()
date: 2016-11-3
post-headings:
  - 定义 add_layer()
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tensorflowTUT/tensorflow10_def_add_layer.py){:target="_blank"}
  * 为 TF 2017 打造的[新版可视化教学代码](https://github.com/MorvanZhou/Tensorflow-Tutorial){:target="_blank"}

{% include assign-heading.html %}

在 Tensorflow 里定义一个添加层的函数可以很容易的添加神经层,为之后的添加省下不少时间.

神经层里常见的参数通常有`weights`、`biases`和激励函数。

首先，我们需要导入`tensorflow`模块。

```python
import tensorflow as tf
```

然后定义添加神经层的函数`def add_layer()`,它有四个参数：输入值、输入的大小、输出的大小和激励函数，我们设定默认的激励函数是`None`。

```python
def add_layer(inputs, in_size, out_size, activation_function=None):    
```

接下来，我们开始定义`weights`和`biases`。

因为在生成初始参数时，随机变量(normal distribution)会比全部为0要好很多，所以我们这里的`weights`为一个`in_size`行, `out_size`列的随机变量矩阵。

```python
Weights = tf.Variable(tf.random_normal([in_size, out_size]))
```

在机器学习中，`biases`的推荐值不为0，所以我们这里是在0向量的基础上又加了`0.1`。

```python
biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
```

下面，我们定义`Wx_plus_b`, 即神经网络未激活的值。其中，`tf.matmul()`是矩阵的乘法。

```python
Wx_plus_b = tf.matmul(inputs, Weights) + biases
```

{% include google-in-article-ads.html %}

当`activation_function`——激励函数为`None`时，输出就是当前的预测值——`Wx_plus_b`，不为`None`时，就把`Wx_plus_b`传到`activation_function()`函数中得到输出。

```python
if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
```

最后，返回输出，添加一个神经层的函数——`def add_layer()`就定义好了。

```python
return outputs
```

