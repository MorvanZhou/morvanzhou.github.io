---
youku_id: XMzM3ODUxNzc4OA
youtube_id: HWHBCsUR-58
b_av: 16001891
b_cid: 31193840
b_page: 44
chapter: 5
title: 迁移学习 Transfer Learning
publish-date: 2018-02-03
thumbnail: "/static/thumbnail-small/tf/tf26_transfer_learning.jpg"
description: "在上次的动画简介中,
我们大概了解了一些迁移学习的原理和为什么要使用迁移学习. 如果用一句话来概括迁移学习, 那务必就是:
为了偷懒, 在训练好了的模型上接着训练其他内容, 充分使用原模型的理解力.
有时候也是为了避免再次花费特别长的时间重复训练大型模型."
post-headings:
  - 下载数据
  - 迁移 VGG
  - 训练
  - 测试
---


学习资料:
  * [本节代码](https://github.com/MorvanZhou/Tensorflow-Tutorial/blob/master/tutorial-contents/407_transfer_learning.py){:target="_blank"}
  * [什么是迁移学习短视频]({% link _tutorials/machine-learning/ML-intro/2-9-transfer-learning.md %})
  * Stanford 迁移学习[阅读](http://cs231n.github.io/transfer-learning/){:target="_blank"}


在上次的[动画简介]({% link _tutorials/machine-learning/tensorflow/5-16-A-tranfer-learning.md %})中,
我们大概了解了一些迁移学习的原理和为什么要使用迁移学习. 如果用一句话来概括迁移学习, 那务必就是:
**"为了偷懒, 在训练好了的模型上接着训练其他内容, 充分使用原模型的理解力".**
有时候也是为了避免再次花费特别长的时间重复训练大型模型.

{% include tut-image.html image-name="5_16_01.png" %}

CNN 通常都是大型模型, 下面我们拿 CNN 来举个例子. 我训练好了一个区分男人和女人的 CNN.
接着来了个任务, 说我下个任务是区分照片中人的年龄. 这看似完全不相干的两个模型, 但是我们却可以运用到迁移学习,
让之前那个 CNN 当我们的初始模型, 因为区分男女的 CNN 已经对人类有了理解.
基于这个理解开始训练, 总比完全重新开始训练强. 但是如果你下一个任务是区分飞机和大象.
这个 CNN 可能就没那么有用了, 因为这个 CNN 可能并没有对飞机大象有任何的理解.

这一次, 我们就来迁移一个图片分类的 CNN ([VGG](https://arxiv.org/abs/1409.1556){:target="_blank"}).
这个 VGG 在[1000个类别](http://imagenet.stanford.edu/synset){:target="_blank"}中训练过.
我们提取这个 VGG 前面的 Conv layers, 重新组建后面的 fully connected layers, 让它做一个和分类完全不相干的事.
我们在网上下载那1000个分类数据中的猫和老虎的图片, 然后伪造一些猫和老虎长度的数据.
最后做到让迁移后的网络分辨出猫和老虎的长度 (regressor).



{% include assign-heading.html %}

为了达到这次的目的, 我们不需要下载所有的1000个分类的所有图片, 只要找到自己感兴趣的类就好 (老虎和猫).
我选老虎和猫的目的就是因为他们是近亲, 还是有点像的, 可以增加点难度. 如果是飞机和大象的话, 学习难度就被降低了.

{% include tut-image.html image-name="5_16_02.png" %}

上图是这个[网址](http://imagenet.stanford.edu/synset?wnid=n02123394#){:target="_blank"},
你能在 Download 的那个 tag 中, 找到所有图片的 urls, 我将所有老虎和猫的 urls 文件给大家放在下面:

* 老虎 Tiger: [imagenet_tiger.txt](/static/results/tensorflow/imagenet_tiger.txt)
* 猫 Kitty cat: [imagenet_kittycat.txt](/static/results/tensorflow/imagenet_kittycat.txt)

我们可以编一个 [Python功能](https://github.com/MorvanZhou/Tensorflow-Tutorial/blob/master/tutorial-contents/407_transfer_learning.py){:target="_blank"}
逐个下载里面的图片. 这个功能我定义成 `download()`. 下载好后就会被放在 data 这个文件夹中了.

{% include tut-image.html image-name="5_16_03.png" %}

因为有些图片url已经过期了, 所以我自己也手动过滤了一遍, 将不是图片的和404的图片给清理掉了. 因为只有两个类,
图片不是很多, 比较好清理. 有网友说一些很多链接和图片已经"失联", 我把我收集到的图片数据打包放在[我的百度云](https://pan.baidu.com/s/1weg_hw-F9wVjK0J7ldjNZw){:target="_blank"},
如果用代码下图片感到有困难的同学们, 请直接在我[百度云](https://pan.baidu.com/s/1weg_hw-F9wVjK0J7ldjNZw){:target="_blank"}下载吧.

因为现在我们不是预测分类结果了, 所以我伪造了一些体长的数据. 老虎通常要比猫长, 所以它们的 distribution 就差不多是下面这种结构(单位cm).

{% include tut-image.html image-name="5_16_05.png" %}


{% include assign-heading.html %}

处理好图片后, 我们可以开始弄 VGG 的 pre-trained model. 我使用的是[machrisaa](https://github.com/machrisaa/tensorflow-vgg){:target="_blank"} 改写的
[VGG16 的代码](https://github.com/machrisaa/tensorflow-vgg/blob/master/vgg16.py){:target="_blank"}.
和他提供的 VGG16 train 好了的 model parameters, 你可以在[这里下载](https://mega.nz/#!YU1FWJrA!O1ywiCS2IiOlUCtCpI6HTJOMrneN-Qdv3ywQP5poecM){:target="_blank"} 这些 parameters
(有网友说这个文件下载不了，我把它放在了[百度云共享](https://pan.baidu.com/s/1Dnz11zVrpWhKmUIAOm33-w){:target="_blank"}了).
做好准备, 这个 parameter 文件有500+MB.
可见一般 CNN 的 model 有多大.

{% include tut-image.html image-name="5_16_04.png" %}

为了做迁移学习, 我对他的 tensorflow VGG16 代码进行了[改写](https://github.com/MorvanZhou/Tensorflow-Tutorial/blob/master/tutorial-contents/407_transfer_learning.py).
保留了所有 Conv 和 pooling 层, 将后面的所有 fc 层拆了, 改成可以被 train 的两层, 输出一个数字, 这个数字代表了这只猫或老虎的长度.

```python
class Vgg16:
    def __init__():
        # ...前面的层
        pool5 = self.max_pool(conv5_3, 'pool5')

        # pool5 是最后的 conv 出来的结果
        self.flatten = tf.reshape(pool5, [-1, 7*7*512])
        self.fc6 = tf.layers.dense(self.flatten, 256, tf.nn.relu, name='fc6')
        self.out = tf.layers.dense(self.fc6, 1, name='out')
```

在 `self.flatten` 之前的 layers, 都是不能被 train 的. 而 `tf.layers.dense()` 建立的 layers 是可以被 train 的.
到时候我们 train 好了, 再定义一个 Saver 来保存由 `tf.layers.dense()` 建立的 parameters.

```python
class Vgg16:
    ...
    def save(self, path='./for_transfer_learning/model/transfer_learn'):
        saver = tf.train.Saver()
        saver.save(self.sess, path, write_meta_graph=False)
```






{% include google-in-article-ads.html %}

{% include assign-heading.html %}

因为有了训练好了的 VGG16, 你就能将 VGG16 的 Conv 层想象成是一个 feature extractor, 提取或压缩图片中的特征.
和 Autoencoder 中的 encoder 类似.
用这些提取的特征来训练后面的 regressor. 具体代码[在这](https://github.com/MorvanZhou/Tensorflow-Tutorial/blob/master/tutorial-contents/407_transfer_learning.py){:target="_blank"},
下面是简写版.

```python
def train():
    xs, ys = ...

    vgg = Vgg16(vgg16_npy_path='./for_transfer_learning/vgg16.npy')
    print('Net built')
    for i in range(100):
        b_idx = np.random.randint(0, len(xs), 6)
        train_loss = vgg.train(xs[b_idx], ys[b_idx])
        print(i, 'train loss: ', train_loss)

    vgg.save('./for_transfer_learning/model/transfer_learn')
```

这里我只 train 了 100次, 如果是重新开始 train 一个 CNN, 100次绝对少了. 而且我使用的是只有 CPU 的电脑,
不好意思, 我暂时没有合适的 GPU... 所以你暂时在 莫烦Python 中基本找不到关于图像处理的教程... 不过!
正因为 transfer learning 让我不用从头 train CNN, 所以我做了这个教程!
否则, 我想用我的 CPU, 估计得一周才能 train 出来这个 VGG 吧.





{% include assign-heading.html %}

我们现在已经迁移好了, train 好了后面的 fc layers, 也保存了后面的 fc 参数. 接着我们提取原始的 VGG16 前半部分参数和 train 好的后半部分参数.
进行测试.

```python
def eval():
    vgg = Vgg16(vgg16_npy_path='./for_transfer_learning/vgg16.npy',
                restore_from='./for_transfer_learning/model/transfer_learn')
    vgg.predict(
        ['./for_transfer_learning/data/kittycat/000129037.jpg',
        './for_transfer_learning/data/tiger/391412.jpg'])
```

我输入了一张猫, 一张老虎的图, 这个 VGG 给我预测除了他们的长度.

{% include tut-image.html image-name="5_16_06.png" %}

可以想象, 要让 VGG 达到这个目的, VGG必须懂得区分哪些是猫, 哪些是老虎, 而这个认知, 在原始的 VGG conv 层中就已经学出来了.
所以如果我们拆了后面的层, 将后面的 classifier 变成 regressor, 花费相当少的时间就能训练好.

迁移学习的玩法除了这样, 还有很多种其他的玩法, 我在这个[短视频]({% link _tutorials/machine-learning/ML-intro/2-9-transfer-learning.md %})中介绍了一些.
迁移学习还有一些细节的地方也可以在[这里](http://cs231n.github.io/transfer-learning/){:target="_blank"}关注一下,
比如什么时候要稍微 train 一下前面的 conv layers, 什么时候要完全固定住前面的 conv layers.
