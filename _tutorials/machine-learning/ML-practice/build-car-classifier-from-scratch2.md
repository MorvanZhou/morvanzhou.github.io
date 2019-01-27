---
youku_id: XMzIzNjMxNTE5Mg
youtube_id: 0AjtDFUzteM
b_av: 17310310
b_cid: 28284907
b_page: 2
b-cid: 28283745
title: "从头开始做一个汽车状态分类器2: 搭建模型"
description: "上次我们已经处理好了需要用到的数据, 这就已经解决了一大堆问题了. 在机器学习/深度学习中, 其实花时间最多的不是训练, 而是数据的预处理.
大多数人都感叹, 如果搭建模型训练花了10分钟, 那处理数据就得花一天. 哈哈哈. 你已经攻克了最难的地方了. 这节内容, 就是非常容易, 我们搭建一个模型, 训练, 并可视化它."
publish-date: 2017-12-14
thumbnail: "/static/thumbnail-small/ML-practice/car_classifier2.jpg"
chapter: 2
post-headings:
  - 导入数据
  - 搭建网络
  - 训练网络
  - 可视化学习过程
---

学习资料:
  * [Tensorflow 教程]({% link _tutorials/machine-learning/tensorflow/1-1-A-ANN-and-NN.md %})
  * [Pytorch 神经网络教程]({% link _tutorials/machine-learning/torch/1-1-A-ANN-and-NN.md %})
  * [本节学习代码](https://github.com/MorvanZhou/train-classifier-from-scratch){:target="_blank"}
  * 用到的[UCI数据](http://archive.ics.uci.edu/ml/datasets/Car+Evaluation){:target="_blank"}



[上次]({% link _tutorials/machine-learning/ML-practice/build-car-classifier-from-scratch1.md %})
我们已经处理好了需要用到的数据, 这就已经解决了一大堆问题了. 在机器学习/深度学习中, 其实花时间最多的不是训练, 而是数据的预处理.
大多数人都感叹, 如果搭建模型训练花了10分钟, 那处理数据就得花一天. 哈哈哈. 你已经攻克了最难的地方了. 这节内容, 就是非常容易,
我们搭建一个模型, 训练, 并可视化它.





{% include assign-heading.html %}

我们使用 tensorflow 搭建神经网络 ([Tensorflow 教程]({% link _tutorials/machine-learning/tensorflow/1-1-why.md %})),
其实你也可以按我的 [Pytorch 教程]({% link _tutorials/machine-learning/torch/1-1-why.md %})
使用 Pytorch 来编写这个网络, 没太多差别. 然后使用 matplotlib 可视化学习过程, 使用之前写好的 data_processing 来导入, 加工数据.
因为我们的数据都是类别数据, 所以我们将要使用的数据都是 onehot 形式的数据.

```python
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import data_processing

data = data_processing.load_data(download=True)
new_data = data_processing.convert2onehot(data)
```

加工好数据以后, 为了比较严谨地测试模型的准确率, 我们首先打乱数据的顺序, 然后将训练和测试数据以 7/3 比例分开.

```python
# prepare training data
new_data = new_data.values.astype(np.float32)       # change to numpy array and float32
np.random.shuffle(new_data)
sep = int(0.7*len(new_data))
train_data = new_data[:sep]                         # training data (70%)
test_data = new_data[sep:]                          # test data (30%)
```






{% include assign-heading.html %}

接着我们就搭建神经网络, `input` 数据的后面4个是真实数据的4类型的 onehot 形式.
我们添加两层隐藏层, 用 softmax 来输出每种类型的概率. 使用 tensorflow 的功能计算 loss 和 accuracy.

```python
# build network
tf_input = tf.placeholder(tf.float32, [None, 25], "input")
tfx = tf_input[:, :21]
tfy = tf_input[:, 21:]

l1 = tf.layers.dense(tfx, 128, tf.nn.relu, name="l1")
l2 = tf.layers.dense(l1, 128, tf.nn.relu, name="l2")
out = tf.layers.dense(l2, 4, name="l3")
prediction = tf.nn.softmax(out, name="pred")

loss = tf.losses.softmax_cross_entropy(onehot_labels=tfy, logits=out)
accuracy = tf.metrics.accuracy(          # return (acc, update_op), and create 2 local variables
    labels=tf.argmax(tfy, axis=1), predictions=tf.argmax(out, axis=1),)[1]
opt = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train_op = opt.minimize(loss)

sess = tf.Session()
sess.run(tf.group(tf.global_variables_initializer(), tf.local_variables_initializer()))
```

{% include tut-image.html image-name="car_classifier2-1.png" %}




{% include google-in-article-ads.html %}

{% include assign-heading.html %}

搭建好图, 然后通过 tensorboard 检查一下有没有错误, 最后就能开始训练啦.
通过4000次循环, 这里我们使用 Mini-batch update, 先随机生成 batch 的索引, 然后在 train_data 中选择数据当作这次的 batch.
这样运算起来比较快. 还有更快的方式, 比如使用 epoch 在每次 epoch 的时候 shuffle 一次数据, 然后在这个 shuffle 完的数据中按先后索引 batch 数据.
这都是使用 numpy 进行 mini-batch 运行速度上的经验之谈了.

```python
for t in range(4000):
    # training
    batch_index = np.random.randint(len(train_data), size=32)
    sess.run(train_op, {tf_input: train_data[batch_index]})

    if t % 50 == 0:
        # testing
        acc_, pred_, loss_ = sess.run([accuracy, prediction, loss], {tf_input: test_data})
        print("Step: %i" % t,"| Accurate: %.2f" % acc_,"| Loss: %.2f" % loss_,)
```






{% include assign-heading.html %}

可视化的代码, 我不在这里呈现了, 想看代码的朋友来我的 [github](https://github.com/MorvanZhou/train-classifier-from-scratch/blob/master/model.py){:target="_blank"}.
这个可视化展示的是在整个训练过程中, 原本 target 有多少这种类型的数据, 我们发现, 其实每种车状况的数据量还是不同的,
虽然有点 [imbalance 的问题]({% link _tutorials/machine-learning/ML-intro/3-07-imbalanced-data.md %}),
但是貌似模型没有被这种 imbalance 问题给带偏. 这是好事. 要不然, 我们还要对这套模型或者数据做手脚, 来解决 imbalance 问题.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/ML-practice/car_classifier1-1.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

{% include google-in-article-ads.html %}

好啦, 我们现在就已经成功的走过了一遍分类器的实践. 我们发现, 在机器学习中, 搭建模型和训练并不一定是最难的地方,
很多时候处理和分析数据也是很麻烦很繁琐的. 我们需要把握数据的规律, 寻找数据的正确表达形式. 好让神经网络比较容易接受.






*实战:从头开始做一个汽车状态分类器*

* *[分析数据]({% link _tutorials/machine-learning/ML-practice/build-car-classifier-from-scratch1.md %})*
* *[搭建模型]({% link _tutorials/machine-learning/ML-practice/build-car-classifier-from-scratch2.md %})*