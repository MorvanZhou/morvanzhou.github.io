---
youku_id: XMzIzNjE5OTE3Mg
youtube_id: 7__jPfjFuR4
b_av: 17310310
b_cid: 28283745
b_page: 1
b-cid: 28283745
title: "从头开始做一个汽车状态分类器1: 分析数据"
description: "大家都喜欢看实践, 因为即使学了很多机器学习的知识(比如说在莫烦Python上的很多教程), 我们大多数时候碰到真正的问题却束手无策.
理论与实践结合还是太少太少了. 做这个教程的主要目的就是为了均衡你的这种学习的不平衡. 让你也能真正动手实战. 让你在实战中收获更多."
publish-date: 2017-12-14
thumbnail: "/static/thumbnail-small/ML-practice/car_classifier1.jpg"
chapter: 2
post-headings:
  - 为什么做这个实践
  - 要做成怎样
  - 我们的数据
  - 数据预处理
---

学习资料:
  * [Tensorflow 教程]({% link _tutorials/machine-learning/tensorflow/1-1-A-ANN-and-NN.md %})
  * [Pytorch 神经网络教程]({% link _tutorials/machine-learning/torch/1-1-A-ANN-and-NN.md %})
  * [本节学习代码](https://github.com/MorvanZhou/train-classifier-from-scratch){:target="_blank"}
  * 用到的[UCI数据](http://archive.ics.uci.edu/ml/datasets/Car+Evaluation){:target="_blank"}



{% include assign-heading.html %}

大家都喜欢看实践, 因为即使学了很多机器学习的知识(比如说在[莫烦Python](/)上的很多教程), 我们大多数时候碰到真正的问题却束手无策.
理论与实践结合还是太少太少了. 做这个教程的主要目的就是为了均衡你的这种学习的不平衡. 让你也能真正动手实战. 让你在实战中收获更多.

首先, 这一个汽车状态的分类器需要用到的知识有:

* 数据的预处理 (你可以学习我的 [Numpy & Pandas](/tutorials/data-manipulation/np-pd/) 来快速入门)
* 画图可视化 (你可以通过我的 [Matplotlib](/tutorials/data-manipulation/plt/) 来了解 Python 的这个画图神器)
* 神经网络 (你可以学习我的 [Tensorflow](/tutorials/machine-learning/tensorflow/) 或者 [Pytorch](/tutorials/machine-learning/torch/) 这两个主流 Python 框架的教程)

有了这些预备知识的储备, 你做完这个实战练习绝对是一件小菜一碟的事. 如果你对上面的知识还不是特别熟, 你也可以选择边往下走, 边挑着看不懂的 google 百度.






{% include assign-heading.html %}

这个实践很简单, 我们需要训练出来一个神经网络的分类器,
用来对数据中的类别进行分类. 其实在现实生活中, 我们有很多形式的数据, 纯数字或文本的数据是最多的.
所以我选择了这样一个分类的练习来做实战. 这种类型的分类器非常常见, 特别是在工业界,
比如通过对一个工业零件的压力等测试, 判断一个这个零件是否要更换了. 这样来最小化故障的损失.
而这个练习, 则是通过一些评估的数据来判断这辆车的状态.

最后我们的结果展示成这样.
通过对数据的分析, 加工, 然后放入神经网络学习, 让它在 test data 的识别准确率上达到 95% 以上.


<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/ML-practice/car_classifier1-1.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>








{% include google-in-article-ads.html %}

{% include assign-heading.html %}

{% include tut-image.html image-name="car_classifier1-2.png" %}

首先我们需要了解一下这一次所要用到的数据是什么. 这个车辆状况的数据是我在网上一个[数据库](http://archive.ics.uci.edu/ml/datasets/Car+Evaluation){:target="_blank"}找到的.
具体的数据描述也能在那个网页找到. 下面我来简单的说明一下.

车辆的状态分为四类:
* unacc (Unacceptable 状况很差)
* acc   (Acceptable 状况一般)
* good  (Good 状况好)
* vgood (Very good 状况非常好)

那我们又是通过什么来判断这辆车的状态好坏呢?
* buying (购买价: vhigh, high, med, low)
* maint  (维护价: vhigh, high, med, low)
* doors  (几个门: 2, 3, 4, 5more)
* persons (载人量: 2, 4, more)
* lug_boot (贮存空间: small, med, big)
* safety  (安全性: low, med, high)

如果展示出这些数据, 我们就能清楚的看到这些数据的表示形式了.

|buying|maint|doors|persons|lug_boot|safety|condition|
| --- | --- | --- | --- | --- | ---|
|vhigh|vhigh|2|2|small|low|unacc|
|vhigh|vhigh|2|2|small|med|unacc|
|vhigh|vhigh|2|2|small|high|unacc|


好了, 第一个问题来了, 我们能不能直接这样喂给神经网络让它学习呢?
如果你有过一些处理神经网络的经历, 你就会察觉到, 这里的数据有很多都是文字形式的,
比如 `vhigh`, `small` 等.
而神经网络能够读取的数据形式都是数字. 这可怎么办? 或者说, 我们要通过什么样的途径,
将这些文字数据转换成数字呢?

接下来我介绍两种途径, 然后谈谈每一种的优缺点.

**途径一**

我们观察到这些文字描述不超过几个类别, 比如在 buying 下面, 总共也就这几种情况 (vhigh, high, med, low),
那我们能不能直接将每种情况给它一个数字代替呢? 比如 (vhigh=0, high=1, med=2, low=3).

**途径二**

同样是类别, 如果你听说过那个手写数字 MNIST 的数据集 (可以看看这个[教程]({% link _tutorials/machine-learning/tensorflow/5-01-classifier.md %})),
你会发现, 0/1/2/3/4/5/6/7/8/9 这十个数字不是直传入神经网络, 而是进行了一次 onehot 的处理. 也就是将数字变成只有 0/1 的形式, 比如下面:

* 0 -> [1,0,0,0,0,0,0,0,0,0]
* 1 -> [0,1,0,0,0,0,0,0,0,0]
* 2 -> [0,0,1,0,0,0,0,0,0,0]
* ...
* 9 -> [0,0,0,0,0,0,0,0,0,1]

转换的途径一般有这两种, 那我们选哪个? 途径一非常简单, 不同的类别变成不同的数字, 但是试想这样的情况,
如果现在是红色, 蓝色, 黄色这三个类别需要转换, 如果红色=0, 蓝色=1, 黄色=2,
红色到蓝色差了1, 红色到黄色差了2, 但是在真实的世界中, 各种颜色之间真的有数量差? 红色到蓝色的差别真的比红色到黄色大?
显然不是, 所以这样的类别转换数字的途径还是存在一定的问题.

而途径二, 我们如果转换成 onehot 形式, 红黄蓝它们就没有这种距离上的差距概念, 而是每个类别都是独立, 特别的, 不能互相比较的.
这才是比较好的类别转换形式. 我觉得有必要提的是, 像(vhigh=0, high=1, med=2, low=3)这样的类别, 可能还是存在一些从高到底的顺序,
这样的类别, 理论上也是可以使用途径一. 大家到了最后可以测试一下途径一和途径二的差别. 这个实战练习, 我是基于途径二的转换.






{% include assign-heading.html %}

了解了我们的数据, 也知道要怎么样处理数据, 我们现在用开始用 python 来处理这些数据吧.
因为网上的数据是现成的, 我们可以直接[下载](http://archive.ics.uci.edu/ml/machine-learning-databases/car/){:target="_blank"}这个数据,
或者是通过 Python 代码来实现下载这个功能. 按耐不住, 想一次性看到所有处理数据代码的朋友点[这里](https://github.com/MorvanZhou/train-classifier-from-scratch/blob/master/data_processing.py){:target="_blank"}.

```python
import pandas as pd
from urllib.request import urlretrieve

def load_data(download=True):
    # download data from : http://archive.ics.uci.edu/ml/datasets/Car+Evaluation
    if download:
        data_path, _ = urlretrieve("http://archive.ics.uci.edu/ml/machine-learning-databases/car/car.data", "car.csv")
        print("Downloaded to car.csv")

    # use pandas to view the data structure
    col_names = ["buying", "maint", "doors", "persons", "lug_boot", "safety", "class"]
    data = pd.read_csv("car.csv", names=col_names)
    return data
```

这个功能, 让我们可以选择下载网上的数据 (大概51KB), 这个文件将会以 "car.csv" 文件名保存, 或者你已经下载好了, 将 `download=False` 直接载入本地数据.

{% include tut-image.html image-name="car_classifier1-3.png" %}

我们同样可以输出一下每类数据类型有多少, 检验一下是否和网上的描述一致.

{% include tut-image.html image-name="car_classifier1-4.png" %}

确认无误之后, 我们就开始使用上面提到的途径二来对这些类别数据做 onehot 预处理. 好在如果你使用 pandas,
它有一个很 handy 的功能 `pd.get_dummies()`, 来帮你实现 onehot 形式的数据转化.

```python
def convert2onehot(data):
    # covert data to onehot representation
    return pd.get_dummies(data, prefix=data.columns)
```

{% include tut-image.html image-name="car_classifier1-5.png" %}

因为转换成 onehot 之后, 屏幕放不下, 所以上面的图只显示了一部分的结果. 不过我们已经清楚地看到,
它将类别项上的 class 标记成了1, 而其他的是0. 有了这些处理好的数据, 我们就能在下一节开始训练了.

接着我们就开始继续往下面添砖加瓦吧. 看看如何[搭建模型]({% link _tutorials/machine-learning/ML-practice/build-car-classifier-from-scratch2.md %}), 并且测试我们的模型.

*实战:从头开始做一个汽车状态分类器*

* *[分析数据]({% link _tutorials/machine-learning/ML-practice/build-car-classifier-from-scratch1.md %})*
* *[搭建模型]({% link _tutorials/machine-learning/ML-practice/build-car-classifier-from-scratch2.md %})*

