---
youku_id: XMTc4MDIxNTkwNA
youtube_id: x5jjul-vLv4
bilibili_id: 16015027
title: RNN Regressor 循环神经网络
description: "使用 LSTM RNN 来预测一个 sin, cos 曲线. 这次我们使用RNN来求解回归(Regression)问题.
首先生成序列 sin(x), 对应输出数据为cos(x), 设置序列步长为20，每次训练的 BATCH_SIZE 为50."
publish-date: 2016-10-30
author: Mark JingNB
chapter: 2
thumbnail: "/static/thumbnail/keras/08RNN2.jpg"
post-headings:
  - 生成序列
  - 搭建模型
  - 训练
---

学习资料:
  * [代码链接](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/8-RNN_LSTM_Regressor_example.py){:target="_blank"}
  * 机器学习-简介系列 [RNN]({% link _tutorials/machine-learning/ML-intro/2-3-RNN.md %})
  * 机器学习-简介系列 [LSTM]({% link _tutorials/machine-learning/ML-intro/2-4-LSTM.md %})
  * Tensorflow [RNN教程]({% link _tutorials/machine-learning/tensorflow/5-08-RNN2.md %})

 {% include assign-heading.html %}

这次我们使用RNN来求解回归(Regression)问题.
首先生成序列`sin(x)`,对应输出数据为`cos(x)`,设置序列步长为20，每次训练的`BATCH_SIZE`为50.

```python
def get_batch():
    global BATCH_START, TIME_STEPS
    # xs shape (50batch, 20steps)
    xs = np.arange(BATCH_START, BATCH_START+TIME_STEPS*BATCH_SIZE).reshape((BATCH_SIZE, TIME_STEPS)) / (10*np.pi)
    seq = np.sin(xs)
    res = np.cos(xs)
    BATCH_START += TIME_STEPS
    return [seq[:, :, np.newaxis], res[:, :, np.newaxis], xs]
```

{% include tut-image.html image-name="2-5-1.png" %}

 {% include assign-heading.html %}

然后添加LSTM RNN层，输入为训练数据，输出数据大小由`CELL_SIZE`定义。因为每一个输入都对应一个输出，所以`return_sequences=True`。
每一个点的当前输出都受前面所有输出的影响，BATCH之间的参数也需要记忆，故`stateful=True`

```python
model.add(LSTM(
    batch_input_shape=(BATCH_SIZE, TIME_STEPS, INPUT_SIZE),       # Or: input_dim=INPUT_SIZE, input_length=TIME_STEPS,
    output_dim=CELL_SIZE,
    return_sequences=True,      # True: output at all steps. False: output as last step.
    stateful=True,              # True: the final state of batch1 is feed into the initial state of batch2
))
```

最后添加输出层，LSTM层的每一步都有输出，使用`TimeDistributed`函数。

```python
model.add(TimeDistributed(Dense(OUTPUT_SIZE)))
```

{% include google-in-article-ads.html %}

 {% include assign-heading.html %}

设置优化方法，`loss`函数和`metrics`方法之后就可以开始训练了。
训练501次，调用matplotlib函数采用动画的方式输出结果。

```python
for step in range(501):
    # data shape = (batch_num, steps, inputs/outputs)
    X_batch, Y_batch, xs = get_batch()
    cost = model.train_on_batch(X_batch, Y_batch)
    pred = model.predict(X_batch, BATCH_SIZE)
    plt.plot(xs[0, :], Y_batch[0].flatten(), 'r', xs[0, :], pred.flatten()[:TIME_STEPS], 'b--')
    plt.ylim((-1.2, 1.2))
    plt.draw()
    plt.pause(0.1)
    if step % 10 == 0:
        print('train cost: ', cost)
```
       
{% include tut-image.html image-name="2-5-2.png" %}


