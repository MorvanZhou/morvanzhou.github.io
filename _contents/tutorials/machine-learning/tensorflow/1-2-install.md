---
youku_id: XMTYxMzQzMjEyNA
youtube_id: pk6sAg2M-fU
description: 安装 Tensorflow 时需要注意的几点


chapter: 1
title: 安装
date: 2016-11-3
author: 张乐
---
* 学习资料:
  * 官方关于 Tensorflow 安装的 [说明](https://www.tensorflow.org/versions/master/get_started/os_setup.html)

安装 Tensorflow 时需要注意的几点:
1. 确保你的系统是 mac OS 或者是 Linux, (tensorflow 暂不支持 windows)
2. 确定你的 python 版本
3. 你的 GPU 是 NVIDIA, 就可以安装 GPU 版本的 Tensorflow; 你的 GPU 不是 NVIDIA 也没有关系, 安装 CPU 版本的就好了.

#### 安装 Tensorflow

Tensorflow 的安装方式很多. 比如:

* [Pip 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#pip-installation)
* [Virtualenv 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#virtualenv-installation)
* [Anaconda 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#anaconda-installation)
* [Docker 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#docker-installation)
* [从安装源 安装](https://www.tensorflow.org/versions/master/get_started/os_setup.html#installing-from-sources)

本文将提到第一种最简单的安装方式, pip 安装.
使用 pip 安装的时候要确保你的 pip 已经存在于你的电脑中. 如果还没有安装 pip. 你可以在 Terminal 窗口中运行这个

```shell
# Ubuntu/Linux 64-位 系统的执行代码:
$ sudo apt-get install python-pip python-dev

# Mac OS X 系统的执行代码:
$ sudo easy_install pip
$ sudo easy_install --upgrade six
```

接下来挑选一个适合你电脑 Tensorflow 版本, 复制并粘贴到 terminal 中运行:
**(注意: 以下链接是 Tensorflow 0.11.0 版本的, 如需更高版本, 请前往[官网](https://www.tensorflow.org/versions/master/get_started/os_setup.html))**

```
# Ubuntu/Linux 64-bit, CPU only, Python 2.7
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc2-cp27-none-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 2.7
# Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.11.0rc2-cp27-none-linux_x86_64.whl

# Mac OS X, CPU only, Python 2.7:
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc2-py2-none-any.whl

# Mac OS X, GPU enabled, Python 2.7:
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow-0.11.0rc2-py2-none-any.whl

# Ubuntu/Linux 64-bit, CPU only, Python 3.4
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc2-cp34-cp34m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 3.4
# Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.11.0rc2-cp34-cp34m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, CPU only, Python 3.5
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.11.0rc2-cp35-cp35m-linux_x86_64.whl

# Ubuntu/Linux 64-bit, GPU enabled, Python 3.5
# Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.11.0rc2-cp35-cp35m-linux_x86_64.whl

# Mac OS X, CPU only, Python 3.4 or 3.5:
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-0.11.0rc2-py3-none-any.whl

# Mac OS X, GPU enabled, Python 3.4 or 3.5:
(tensorflow)$ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/mac/gpu/tensorflow-0.11.0rc2-py3-none-any.whl
```

最后, 根据自己的 python 版本, 在 terminal 中执行以下语句:

```shell
# 如果你是 Python 2, 请复制下面
(tensorflow)$ pip install --ignore-installed --upgrade $TF_BINARY_URL

# 如果你是 Python 3, 请复制下面
(tensorflow)$ pip3 install --ignore-installed --upgrade $TF_BINARY_URL
```

然后打开你的 python 编辑器, 输入

```python
import tensorflow
```

运行脚本来检查一下是否有正确安装.

#### 更新 Tensorflow

最后, 如果你需要升级 Tensorflow 的版本, 推荐的方式是:

根据你的 python 版本, 在 terminal 中删除原有的版本

```shell
# 如果你是 Python 2, 请复制下面
pip uninstall tensorflow

# 如果你是 Python 3, 请复制下面
pip3 uninstall tensorflow
```

然后重复这个安装教程的步骤, 从头安装新版本.
