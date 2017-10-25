---
youku_id: XMTU4NTE2NDk4OA
youtube_id: D0-8urP2b5Y
description: 
chapter: 7
title: 模块安装
date: 2016-11-3
post-headings:
  - 什么是外部模块
  - 安装 Numpy
  - 更新外部模块
---

安装外部的模块有很多种方式, 不同的系统安装形式也不同. 比如在 Windows 上安装 Python 的一些包,
可能还会要了你的老命. 哈哈.

{% include assign-heading.html %}

外部模块就是在你 `import` 什么东西去python 脚本的时候会用到的.

```python
import numpy as np
import matplotlib.pyplot as plt
```

这里的 Numpy 和 matplotlib 都是外部模块, 需要安装以后才会有的. 他不属于 python 自带的模块.




{% include assign-heading.html %}

这里我们举例说明,
对于一些科学运算的模块, 比如 [numpy](http://www.numpy.org/){:target="_blank"}, 他的安装方式就有很多.
在 Windows 上, 最简单的方式就安装 [Anaconda](https://www.anaconda.com/download/){:target="_blank"} 这种平台, 他会自带很多必要的外部模块.
安装一个, 省去安装其它的烦恼.

不过我这里要讲的是下载安装包的方式在 Windows 安装. 比如
在 [Numpy 安装包](https://sourceforge.net/projects/numpy/files/NumPy/){:target="_blank"}的网站中, 你能找到 numpy 的各种版本的安装包.

{% include tut-image.html image-name="07-01-01.png" %}

在 [NumPy 1.10.2](https://sourceforge.net/projects/numpy/files/NumPy/1.10.2/){:target="_blank"}
这个版本中, 我们能找到适合 Windows 的安装包, 新版中目前还没添加 Windows 的安装包.
然后根据你的系统和 python 版本选择合适的 "exe" 安装包. 下载安装.

{% include tut-image.html image-name="07-01-02.png" %}



如果你是 MacOS 或者 Linux, 这种外部模块, 安装起来就方便多了.
在你的电脑 Terminal 上输入一句话, 就能轻松安装. Windows 好像要经过特殊设置才能实现一样的功能, 具体忘记了... 你可能要查一下.
在我电脑中, Terminal 长这样.

{% include tut-image.html image-name="07-01-03.png" %}

然后只要你在里面输入这种形式就可以安装了.

```shell
$ pip install 你要的模块名
```

比如

```shell
$ pip install numpy   # 这是 python2+ 版本的用法
$ pip3 install numpy   # 这是 python3+ 版本的用法
```







{% include assign-heading.html %}

使用 pip 更新外部模块会十分简单. 主需要在 Terminal 中输入下面的指令就行.
这里的 `-U` 就是 update 意思.

```shell
$ pip install -U numpy   # 这是 python2+ 版本的用法
$ pip3 install -U numpy   # 这是 python3+ 版本的用法
```




