---
youku_id: XMTc3OTA0NDc5Mg
youtube_id: FIZiuAM5kQo
bilibili_id: 16014640
title: 兼容 backend
description: "怎么样调整 keras 的 backend (Tensorflow, theano). 我们来介绍 Keras 的两个 Backend，也就是Keras基于什么东西来做运算。Keras 可以基于两个Backend，一个是 Theano，一个是 Tensorflow。如果我们选择Theano作为Keras的Backend，
那么Keras就用 Theano 在底层搭建你需要的神经网络；同样，如果选择 Tensorflow 的话呢，Keras 就使用 Tensorflow 在底层搭建神经网络。"
author: 刘思成
publish-date: 2016-10-29
chapter: 1
post-headings:
  - 如何看当前使用的是什么Backend
  - 如何修改Backend
---


学习资料:
  * backend [说明](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/3-backend.py){:target="_blank"}

我们来介绍 Keras 的两个 Backend，也就是Keras基于什么东西来做运算。Keras 可以基于两个Backend，一个是 Theano，一个是 Tensorflow。如果我们选择Theano作为Keras的Backend，
那么Keras就用 Theano 在底层搭建你需要的神经网络；同样，如果选择 Tensorflow 的话呢，Keras 就使用 Tensorflow 在底层搭建神经网络。

目前 Tensorflow 支持 Mac 和 Linux 系统，而 Theano 不但支持包括 Mac 和 Linux，还支持 Windows 系统，
所以我们就可以选择自己可以用的 Backend 就可以。

{% include assign-heading.html %}

每次当我们`import keras`的时候，就会看到屏幕显示当前使用的 Backend

```python
import keras
```

```python
Using Theano Backend
```

这就说明现在使用的是Theano在作Backend。

{% include assign-heading.html %}

```python
~/.keras/keras.json
```

文件内容：

```python
{
	"image_dim_ordering": "tf",
	"epsilon": 1e-07,
	"floatx": "float32",
	"backend": "theano"
}
```

每次`import`的时候，keras 就会检查这个 `keras.json` 文件。一般我们以为，如果需要把 Backend 改成 Tensorflow 的话，只需要改动最后一行"backend"对应的值，修改后的文件内容：

```python
{
	"image_dim_ordering": "tf",
	"epsilon": 1e-07,
	"floatx": "float32",
	"backend": "tensorflow"
}
```


{% include google-in-article-ads.html %}

但这样修改后，`import` 的时候会出现错误信息。

解决的方法有几种:

* 可以在其他文本编辑器内编辑好这段文本，然后整体拷贝到这个文件里。
* 还可以在terminal中直接输入临时环境变量执行

```python
# python2+输入:
KERAS_BACKEND=tensorflow python -c "from keras import backend"
```

```python
# python3+输入:
KERAS_BACKEND=tensorflow python3 -c "from keras import backend"
```

* 最好的解决方法，还是在python代码中`import keras`前加入一个环境变量修改的语句：

```python
import os
os.environ['KERAS_BACKEND']='theano'
```

这时`import keras`就会显示`Using Theano backend`。

如果语句改为：

```python
import os
os.environ['KERAS_BACKEND']='tensorflow'
```

这时`import keras`就会显示`Using Tensorflow backend`。
第三种修改影响的范围是仅这个脚本内，所以其他文件的执行Keras还是会去找`keras.json`配置文件来确定用什么`backend`。
