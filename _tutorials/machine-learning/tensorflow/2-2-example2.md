---
youku_id: XMTYxMzQ2NzE0OA
youtube_id: JKR1Dxinwwc
bilibili_id: 16002275
description: "Tensorflow 是非常重视结构的, 我们得建立好了神经网络的结构, 才能将数字放进去,
运行这个结构.这个例子简单的阐述了 tensorflow 当中如何用代码来运行我们搭建的结构."
chapter: 2
title: 例子2
date: 2016-11-3
post-headings:
  - 创建数据
  - 搭建模型
  - 计算误差
  - 传播误差
  - 训练
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/tensorflowTUT/tf5_example2){:target="_blank"}
  * 为 TF 2017 打造的[新版可视化教学代码](https://github.com/MorvanZhou/Tensorflow-Tutorial){:target="_blank"}
  
Tensorflow 是非常重视结构的, 我们得建立好了神经网络的结构, 才能将数字放进去, 
运行这个结构.

这个例子简单的阐述了 tensorflow 当中如何用代码来运行我们搭建的结构.

{% include assign-heading.html %}

首先, 我们这次需要加载 tensorflow 和 numpy 两个模块, 并且使用 numpy
来创建我们的数据.

```python
import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3
```


接着, 我们用 `tf.Variable` 来创建描述 `y` 的参数. 我们可以把 `y_data = x_data*0.1 + 0.3`
想象成 `y=Weights * x + biases`, 然后神经网络也就是学着把 Weights 变成 0.1, biases 变成 0.3.

{% include assign-heading.html %}

```python
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases
```

{% include assign-heading.html %}

接着就是计算 `y` 和 `y_data` 的误差:

```python
loss = tf.reduce_mean(tf.square(y-y_data))
```

{% include assign-heading.html %}

反向传递误差的工作就教给`optimizer`了, 我们使用的误差传递方法是梯度下降法: `Gradient Descent`
让后我们使用 `optimizer` 来进行参数的更新.

```python
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

到目前为止, 我们只是建立了神经网络的结构, 还没有使用这个结构. 在使用这个结构之前, 
我们必须先初始化所有之前定义的`Variable`, 所以这一步是很重要的!

```python
# init = tf.initialize_all_variables() # tf 马上就要废弃这种写法
init = tf.global_variables_initializer()  # 替换成这样就好
```

接着,我们再创建会话 `Session`. 我们会在下一节中详细讲解 Session. 
我们用 `Session` 来执行 `init` 初始化步骤. 并且,
用 `Session` 来 `run` 每一次 training 的数据. 逐步提升神经网络的预测准确性.

```python
sess = tf.Session()
sess.run(init)          # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))
```
