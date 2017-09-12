---
youku_id: XMTcxNjAxMDAxNg
youtube_id: F2K5hqLiBi0
description: 对于 Windows, MacOS, Linux, matplotlib 的安装方式各不相同, 我们看看如何安装 matplotlib 吧.
chapter: 1
title: 安装
date: 2016-11-3
post-headings:
  - Linux
  - MacOS
  - Windows
---
{% assign post-heading-count = -1 %}
学习资料:
  * Windows 安装文件 [网址](https://pypi.python.org/pypi/matplotlib/)

对于 [Linux](#linux), [MacOS](#mac), [Windows](#windows) 的安装方式各不相同. 

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>


打开 Terminal 窗口, 输入以下内容

```python
# python 3+ 请复制以下在 terminal 中执行
$ sudo apt-get install python3-matplotlib

# python 2+ 请复制以下在 terminal 中执行
$ sudo apt-get install python-matplotlib
```

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>


打开 Terminal 窗口, 输入以下内容

```python
# python 3+ 请复制以下在 terminal 中执行
$ pip3 install matplotlib

# python 2+ 请复制以下在 terminal 中执行
$ pip install matplotlib
```

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>


Windows 的安装最麻烦. 我们一步步来:

* 确保你有安装 Visual Studio;
* 去这个网址: [https://pypi.python.org/pypi/matplotlib/](https://pypi.python.org/pypi/matplotlib/)
* 找到一个适合你自己 python 版本的 wheel (.whl) 文件. (如下图) 

<img class= "course-image" src="/static/results/plt/1_2_1.png">

```
    matplotlib-1.5.3-cp35-cp35m-win32.whl (md5)
    1.5.3 : plt版本
    cp35  : python 版本
    win32 : Windows 32位系统
    whl   : wheel 文件 
```

* 用 CMD 找到这个 .whl 文件目录, 然后 pip 安装. 以 `matplotlib-1.4.3-cp35-none-win32.whl`文件为例:

```shell
$ cd python_work   # 用 cd 去到你下载的文件目录

# 如果是 python 3+ 版本, 像下面一样
python_work$ python -m pip3 install matplotlib-1.4.3-cp35-none-win32.whl
```

* 如果安装不成功, 还有一种方法可以简便安装所有科学运算模块. 可以搜索一下 `Anaconda python` 