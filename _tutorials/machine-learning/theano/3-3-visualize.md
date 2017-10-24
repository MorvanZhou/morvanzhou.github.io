---
youku_id: XMTY2NDE5MDY2NA
youtube_id: nslbfsN8wiU
title: 可视化结果 回归例子
description: 如果我们能可视化训练的结果,这样会对我们理解神经网络有很大的帮助,这次就举了一个例子来看看一个非线性的 regression, 怎样能够可视化他的结果
author: C.Cui
chapter: 3
date: 2016-11-3
post-headings:
  - matplotlib 可视化
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/theanoTUT/theano10_regression_visualization){:target="_blank"}
  
{% include assign-heading.html %}

接着上一节课的内容，这一小节，我们将要对我们建立的神经网络模型的输出结果在不同的训练阶段可视化（visualization）。
建筑和训练神经网络的步骤和上次内容一样, 不同的是, 这次我们要有可视化的效果。 
我们在这里引入了`matplotlib`这个工具包, 用来绘图及数据可视化。 
大家可以利用我的视频教程来学习或复习Matplotlib这个工具：[Matplotlib 数据可视化神器 Python](/tutorials/data-manipulation/plt/)。

在训练开始前，我们重新画一下我们的目标数据：也就是我们要不断的刷新我们神经网络的输出值`prediction_value`

```python
# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()
plt.show()
```

现在我们开始真正的训练啦！我们要把神经网络训练1000次，同时呢，每训练50次更新一下图片的显示：

```python
for i in range(1000):
    # training
    err = train(x_data, y_data)
    if i % 50 == 0:
        # to visualize the result and improvement
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = predict(x_data)
        # plot the prediction
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(.5)
```

此处，`ax.lines.remove(lines[0])` 的作用是删除我们之前画的红线。这里我们采用`try... catch...` 结构来避免我们第一次没有被删除的目标。

你大概会得到以下的类似结果：

{% include tut-image.html image-name="3_3_1.gif" %}

结果显示我们的神经网络在一点一点的逼近我们的目标函数, 换句话说也就是说 神经网络在逐步的学习样本的原始分布。

当然，只需要简单的修改代码，你就可以看最终的训练结果：

```python
for i in range(1000):
    # training
    err = train(x_data, y_data)
     
prediction_value = predict(x_data)
# plot the prediction
lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
```

在下一节看课程，我们将学习如何利用神经网络来解决简单的分类问题。

















 
