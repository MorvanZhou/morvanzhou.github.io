---
youku_id: XMTU5OTQzOTMzNg
youtube_id: nhn8B0pM9ls
description: 我们已经建立好了一个完整的神经网络,如果能够可视化训练的结果,就能够更好的理解神经网络是如何训练的.这次就提到了 matplotlib 这个模块,用它来进行结果可视化处理.我们看到了神经网络的模型是如何 fit 上原始的 data 的.
author: 赵孔亚
chapter: 3
title: 例子3 结果可视化
date: 2016-11-3
---
* 学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/tensorflowTUT/tf12_plot_result)


首先，导入本次所需的模块,其中`matplotlib`模块通常用作数据的可视化。

```python
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
```

构造添加一个神经层的函数。

```python
def add_layer(inputs, in_size, out_size, activation_function=None):
    Weights = tf.Variable(tf.random_normal([in_size, out_size]))
    biases = tf.Variable(tf.zeros([1, out_size]) + 0.1)
    Wx_plus_b = tf.matmul(inputs, Weights) + biases
    if activation_function is None:
        outputs = Wx_plus_b
    else:
        outputs = activation_function(Wx_plus_b)
    return outputs
```

构建所需的数据。

```python
# Make up some real data
x_data = np.linspace(-1,1,300)[:, np.newaxis]
noise = np.random.normal(0, 0.05, x_data.shape)
y_data = np.square(x_data) - 0.5 + noise
```

用占位符定义神经网络所需的输入。

```python
# define placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None, 1])
ys = tf.placeholder(tf.float32, [None, 1])
```

构建隐藏层和输出层。

```python
# add hidden layer
l1 = add_layer(xs, 1, 10, activation_function=tf.nn.relu)
# add output layer
prediction = add_layer(l1, 10, 1, activation_function=None)
```

预测值和真实值之间的误差。

```python
# the error between prediciton and real data
loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                     reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)
```

使用变量时，都要对它进行初始化，这是必不可少的。

```python
init = tf.initialize_all_variables()
```

定义`Session`，并用 `Session` 来执行 `init` 初始化步骤。

```python
sess = tf.Session()
sess.run(init)
```

构建图形，用散点图描述真实数据之间的关系。
（注意：`plt.ion()`用于连续显示。）

```python
# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()#本次运行请注释，全局运行不要注释
plt.show()
```

散点图的结果为：

<img class="course-image" src="/static/results/tensorflow/3_3_1.png">

接下来，我们来显示预测数据。

每隔50次训练刷新一次图形，用红色、宽度为5的线来显示我们的预测数据和输入之间的关系，并暂停0.1s。

```python
for i in range(1000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # to visualize the result and improvement
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        # plot the prediction
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)
```

最后，机器学习的结果为：

<img class="course-image" src="/static/results/tensorflow/3_3_2.png">


