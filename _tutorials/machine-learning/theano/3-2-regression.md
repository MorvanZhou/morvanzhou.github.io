---
youku_id: XMTY2NDE2MjA5Ng
youtube_id: EULCWeavwPU
title: Regression 回归例子
description: 用 theano 做回归的问题可以像视频中提到的这种方法来做. 我们要做一个非线性的回归问题,,所以我们添加了两层 layer, 还是用了不同的激励函数. 神经网络成功的使预测误差得到了减小.
author: C.Cui
chapter: 3
date: 2016-11-3
post-headings:
  - 导入模块
  - 定义层结构
  - 伪造数据
  - 搭建网络
  - 训练
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/theanoTUT/theano9_regression_nn){:target="_blank"}
  
{% include assign-heading.html %}

在上一节课程中，我么学习了如何利用`Theano`定义神经网络的层类，我们设计了一个`Layer`类来规划神经网络层的信息。 

这节我们学习如何利用神经网络解决简单的回归问题。
首先，和之前所有的练习一样，我们引入需要使用的Python包： 

```python
import theano
import theano.tensor as T
import numpy as np
import matplotlib.pyplot as plt
```

与之前的代码不同的地方是我们在这里引入了`matplotlib`这个工具包, 用来实现绘图及数据可视化。 

大家可以利用我的视频教程来学习或复习 Matplotlib 这个工具： [Matplotlib 数据可视化神器 Python](/tutorials/data-manipulation/plt/)。

{% include assign-heading.html %}

接下来我们声明我们的Layer类。 对于神经网络的每个Layer， 
它需要具备输入来源`input`，输入神经元维度`in_size`，输出神经元纬度`out_size`,
和我们之前设计的神经元的激活函数`activation_function`， 默认为`None`。
这段代码和上节课一致，此处不再重复。

```python
class Layer(object):
    def __init__(self, inputs, in_size, out_size, activation_function=None):
        self.W = theano.shared(np.random.normal(0, 1, (in_size, out_size)))
        self.b = theano.shared(np.zeros((out_size, )) + 0.1)
        self.Wx_plus_b = T.dot(inputs, self.W) + self.b
        self.activation_function = activation_function
        if activation_function is None:
            self.outputs = self.Wx_plus_b
        else:
            self.outputs = self.activation_function(self.Wx_plus_b)
```

{% include assign-heading.html %}

接下来，我们首先人工生成一个简单的带有白噪声的一维数据 `y = x^2 - 0.5 + noise`。

```python
# Make up some fake data
x_data = np.linspace(-1, 1, 300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise        # y = x^2 - 0.5 + wihtenoise
```

然后，我们用散点图（Scatter）把它显示出来, 横轴是`x_data`, 纵轴是`y_data`。

```python
# show the fake data
plt.scatter(x_data, y_data)
plt.show()
```

显示结果: 

{% include tut-image.html image-name="3_2_1.png" %}

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

然后，我们定义神经网络的输入与目标；

```python
# determine the inputs dtype
x = T.dmatrix("x")
y = T.dmatrix("y") 
```

这里，`T.dmatrix` 意味着我使用的是float64的数据类型, 和我的输入数据一致。

接着我们设计我们的神经网络，它包括两层，构成`1-10-1`的结构。
对于`l1`我们的`input_size`要和我们的`x_data`一致，然后我们假设了该层有10个神经元，并且以`relu`作为激活函数。
所以，`l2`以`l1.output`为输入，同时呢，它的输出为1维，和我们的`y_data`保持一致，作为神经网络的输出层，我们采用默认的线性激活函数。


```python
# determine the inputs dtype
# add layers
l1 = Layer(x, 1, 10, T.nnet.relu)
l2 = Layer(l1.outputs, 10, 1, None)
```

然后，我们定义一个`cost`，也就是损失函数（cost/loss function），我们采用的是`l2.outputs` 神经网络输出与目标值`y`的的平均平方差。

```python
# compute the cost
cost = T.mean(T.square(l2.outputs - y))
```

根据 `cost` 我们可以计算我们神经网络权值和偏置值的梯度（gradient）, 这里Theano已经集成好了对应的函数：

```python
# compute the gradients
gW1, gb1, gW2, gb2 = T.grad(cost, [l1.W, l1.b, l2.W, l2.b])
```

有了以上的基本运算步骤后，我们就可以开始，利用梯度下降法训练我们的神经网络。
首先我们定义一个学习率 `learning_rate`, 这个学习率的取值一般是根据数据及实验的经验估计的，它会对模型的收敛性造成一定的影响，一般倾向于采用较小的数值。

然后，我们定义`train`这个函数来描述我们的训练过程，首先我们定义了函数的输入`inputs=[x, y],` 函数的输出为`outputs=cost`, 同时更新网络的参数。

```python
# apply gradient descent
learning_rate = 0.05
train = theano.function(
    inputs=[x, y],
    outputs=cost,
    updates=[(l1.W, l1.W - learning_rate * gW1),
             (l1.b, l1.b - learning_rate * gb1),
             (l2.W, l2.W - learning_rate * gW2),
             (l2.b, l2.b - learning_rate * gb2)])
```

然后我们定义一个预测函数来输出我们最终的结果`predict`.

```python
# prediction
predict = theano.function(inputs=[x], outputs=l2.outputs)
```

{% include assign-heading.html %}

最后，我们就要开始真正的训练啦！我们要把神经网络训练1000次，同时呢每训练50次时就输出此时的误差（cost）：

```python
for i in range(1000):
    # training
    err = train(x_data, y_data)
    if i % 50 == 0:
        print(err)
```

你大概会得到一下类似的结果：

```python
"""
2.2858426513500967
0.011148671551881364
0.008641346716060181
0.007188403510180637
0.006250296000631469
0.005628021126864056
0.005142288453451058
0.004793442944984919
0.004539827398288326
0.004376693858775578
0.0042555015795511615
0.004156078781653181
0.0040801312408181726
0.004022424092526545
0.003974514689028584
0.003934815285052449
0.0039030377541023824
0.003875222239897254
0.003848930488582809
0.0038275646534826836 
"""
```

结果显示我们的训练误差是在不断的减小的，也就是说我们的神经网络在一点一点的逼近目标值。
再下一小节中我们将学习使用`matplotlib`来动态的显示我们训练的神经网络的预测结果。








