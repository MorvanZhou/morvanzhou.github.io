---
youku_id: XMjc0NTk2NTgxNg
youtube_id: JIGkxYmLPPY
bilibili_id: 15997721
title: Pytorch 安装
publish-date: 2017-05-05
thumbnail: "/static/thumbnail/torch/1-2_install.jpg"
chapter: 1
description: "PyTorch 暂时只支持 MacOS, Linux.
暂不支持 Windows! (可怜的 Windows 同学们.. 又被抛弃了). 不过说不定像 Tensorflow 一样, 因为 Windows 用户的强烈要求, 他们在某天就突然支持了."
post-headings:
  - 支持的系统
  - 安装
---


学习资料:
  * [PyTorch 官网](http://pytorch.org/){:target="_blank"}


{% include assign-heading.html %}

PyTorch 暂时只支持 MacOS, Linux.
暂不支持 Windows! (可怜的 Windows 同学们.. 又被抛弃了). 不过说不定像 Tensorflow 一样, 因为 Windows 用户的强烈要求, 他们在某天就突然支持了.


{% include assign-heading.html %}

PyTorch 安装起来很简单, [它自家网页](http://pytorch.org/){:target="_blank"}上就有很方便的选择方式 (网页升级改版后可能和下图有点不同):

<a href="http://pytorch.org/">
{% include tut-image.html image-name="1-2-1.png" %}
</a>

所以根据你的情况选择适合你的安装方法, 我已自己为例, 我使用的是 MacOS, 想用 pip 安装, 我的 Python 是 3.5 版的, 我没有 GPU 加速, 那我就按上面的选:

然后根据上面的提示, 我只需要在我的 Terminal 当中输入以下指令就好了:

```shell
$ pip install http://download.pytorch.org/whl/torch-0.1.11.post5-cp35-cp35m-macosx_10_7_x86_64.whl
$ pip install torchvision
```

注意, 我安装的是0.1.11版本的 torch, 你需要去他们网站上看是否有新版本的.
安装 PyTorch 会安装两个模块, 一个是 torch, 一个 torchvision, torch 是主模块, 用来搭建神经网络的,
torchvision 是辅模块, 有数据库, 还有一些已经训练好的神经网络等着你直接用, 比如 ([VGG, AlexNet, ResNet](http://pytorch.org/docs/torchvision/models.html){:target="_blank"}).

