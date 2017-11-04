---
youku_id: XMjc2MDUxNzUyOA
youtube_id: V7VgLkEgXVY
bilibili_id: 15999215
title: AutoEncoder (自编码/非监督学习)
publish-date: 2017-05-11
thumbnail: "/static/thumbnail/torch/4.4_autoencoder.jpg"
chapter: 4
description: "神经网络也能进行非监督学习, 只需要训练数据, 不需要标签数据. 自编码就是这样一种形式.
自编码能自动分类数据, 而且也能嵌套在半监督学习的上面, 用少量的有标签样本和大量的无标签样本学习.
这次我们还用 MNIST 手写数字数据来压缩再解压图片."
post-headings:
  - 要点
  - 训练数据
  - AutoEncoder
  - 训练
  - 画3D图
---


学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/PyTorch-Tutorial/blob/master/tutorial-contents/404_autoencoder.py){:target="_blank"}
  * [Tensorflow 的 50行 AutoEncoder 代码](https://github.com/MorvanZhou/Tensorflow-Tutorial/blob/master/tutorial-contents/404_AutoEncoder.py){:target="_blank"}
  * [我制作的 自编码 动画简介]({% link _tutorials/machine-learning/ML-intro/2-5-autoencoder.md %})
  * [PyTorch 官网](http://pytorch.org/){:target="_blank"}

{% include assign-heading.html %}

神经网络也能进行非监督学习, 只需要训练数据, 不需要标签数据. 自编码就是这样一种形式.
自编码能自动分类数据, 而且也能嵌套在半监督学习的上面, 用少量的有标签样本和大量的无标签样本学习.
如果对自编码还没有太多概念, 强烈推荐我的这个[动画短片]({% link _tutorials/machine-learning/ML-intro/2-5-autoencoder.md %}), 让你秒懂自编码.

这次我们还用 MNIST 手写数字数据来压缩再解压图片.

{% include tut-image.html image-name="4-4-1.gif" %}

然后用压缩的特征进行非监督分类.

{% include tut-image.html image-name="4-4-2.gif" %}






{% include assign-heading.html %}

自编码只用训练集就好了, 而且只需要训练 training data 的 image, 不用训练 labels.

```python
import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision

# 超参数
EPOCH = 10
BATCH_SIZE = 64
LR = 0.005
DOWNLOAD_MNIST = True   # 下过数据的话, 就可以设置成 False
N_TEST_IMG = 5          # 到时候显示 5张图片看效果, 如上图一

# Mnist digits dataset
train_data = torchvision.datasets.MNIST(
    root='./mnist/',
    train=True,                                     # this is training data
    transform=torchvision.transforms.ToTensor(),    # Converts a PIL.Image or numpy.ndarray to
                                                    # torch.FloatTensor of shape (C x H x W) and normalize in the range [0.0, 1.0]
    download=DOWNLOAD_MNIST,                        # download it if you don't have it
)
```

{% include tut-image.html image-name="4-4-3.png" %}

这就是一张我们要训练的手写数字 4.

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

AutoEncoder 形式很简单, 分别是 `encoder` 和 `decoder`, 压缩和解压, 压缩后得到压缩的特征值, 再从压缩的特征值解压成原图片.

```python
class AutoEncoder(nn.Module):
    def __init__(self):
        super(AutoEncoder, self).__init__()

        # 压缩
        self.encoder = nn.Sequential(
            nn.Linear(28*28, 128),
            nn.Tanh(),
            nn.Linear(128, 64),
            nn.Tanh(),
            nn.Linear(64, 12),
            nn.Tanh(),
            nn.Linear(12, 3),   # 压缩成3个特征, 进行 3D 图像可视化
        )
        # 解压
        self.decoder = nn.Sequential(
            nn.Linear(3, 12),
            nn.Tanh(),
            nn.Linear(12, 64),
            nn.Tanh(),
            nn.Linear(64, 128),
            nn.Tanh(),
            nn.Linear(128, 28*28),
            nn.Sigmoid(),       # 激励函数让输出值在 (0, 1)
        )

    def forward(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return encoded, decoded

autoencoder = AutoEncoder()
```

{% include assign-heading.html %}

训练, 并可视化训练的过程. 我们可以有效的利用 `encoder` 和 `decoder` 来做很多事,
比如这里我们用 `decoder` 的信息输出看和原图片的对比, 还能用 `encoder` 来看经过压缩后, 神经网络对原图片的理解.
`encoder` 能将不同图片数据大概的分离开来. 这样就是一个无监督学习的过程.

{% include tut-image.html image-name="4-4-1.gif" %}

```python
optimizer = torch.optim.Adam(autoencoder.parameters(), lr=LR)
loss_func = nn.MSELoss()

for epoch in range(EPOCH):
    for step, (x, y) in enumerate(train_loader):
        b_x = Variable(x.view(-1, 28*28))   # batch x, shape (batch, 28*28)
        b_y = Variable(x.view(-1, 28*28))   # batch y, shape (batch, 28*28)
        b_label = Variable(y)               # batch label

        encoded, decoded = autoencoder(b_x)

        loss = loss_func(decoded, b_y)      # mean square error
        optimizer.zero_grad()               # clear gradients for this training step
        loss.backward()                     # backpropagation, compute gradients
        optimizer.step()                    # apply gradients
```

{% include tut-image.html image-name="4-4-4.png" %}


{% include assign-heading.html %}

{% include tut-image.html image-name="4-4-2.gif" %}

3D 的可视化图挺有趣的, 还能挪动观看, 更加直观, 好理解.

```python
# 要观看的数据
view_data = Variable(train_data.train_data[:200].view(-1, 28*28).type(torch.FloatTensor)/255.)
encoded_data, _ = autoencoder(view_data)    # 提取压缩的特征值
fig = plt.figure(2)
ax = Axes3D(fig)    # 3D 图
# x, y, z 的数据值
X = encoded_data.data[:, 0].numpy()
Y = encoded_data.data[:, 1].numpy()
Z = encoded_data.data[:, 2].numpy()
values = train_data.train_labels[:200].numpy()  # 标签值
for x, y, z, s in zip(X, Y, Z, values):
    c = cm.rainbow(int(255*s/9))    # 上色
    ax.text(x, y, z, s, backgroundcolor=c)  # 标位子
ax.set_xlim(X.min(), X.max())
ax.set_ylim(Y.min(), Y.max())
ax.set_zlim(Z.min(), Z.max())
plt.show()
```

{% include tut-image.html image-name="4-4-5.png" %}


所以这也就是在我 [github 代码](https://github.com/MorvanZhou/PyTorch-Tutorial/blob/master/tutorial-contents/404_autoencoder.py){:target="_blank"} 中的每一步的意义啦.


