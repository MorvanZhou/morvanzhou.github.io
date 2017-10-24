---
youku_id: XMTYxMjg5MTYyOA
youtube_id: FG3W1_8ogBE
description: 安装 Scikit-learn (sklearn) 最简单的方法就是使用 pip 安装它.在你的终端上执行 (pip install scikit-learn) 就好啦~ 注意 python3.x版本的用户要使用 (pip3 install scikit-learn). 还有要确保你有安装过 numpy 和 scipy这两个模块.
chapter: 1
title: Sklearn 安装
date: 2016-11-3
post-headings:
  - pip 安装
  - Windows 注意事项
---


学习资料:
  * 官方安装 [教程](http://scikit-learn.org/stable/install.html){:target="_blank"}
  * Windows 使用 [Anaconda](https://www.continuum.io/downloads){:target="_blank"} 安装

{% include assign-heading.html %}

安装 Scikit-learn (sklearn) 最简单的方法就是使用 pip 安装它.

首先确认自己电脑中有安装

* Python (>=2.6 或 >=3.3 版本)
* Numpy (>=1.6.1)
* Scipy (>=0.9)

如果还不确定如何安装 Numpy 请查看这个 [安装 Numpy]({% link _tutorials/data-manipulation/np-pd/1-2-install.md %})
教程. 如果能顺利安装 Numpy 那 Scipy 的安装就没有问题了.

然后找到你的 Terminal (MacOS or Linux), 或者 CMD (Windows).
输入以下语句:

```shell
# python 2+ 版本复制:
pip install -U scikit-learn

# python 3+ 版本复制:
pip3 install -U scikit-learn
```

{% include assign-heading.html %}

如果你是 Windows 用户, 你也可以选择使用 `Anaconda` 来安装所有 python 的科学计算模块.
[Anaconda的相关资料在这](https://www.continuum.io/downloads){:target="_blank"}

