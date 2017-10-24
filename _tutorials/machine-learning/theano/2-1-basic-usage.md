---
youku_id: XMTY2MTY1NDY1Ng
youtube_id: je2oHCX5m74
title: 基本用法
description: 在theano 中学会定义矩阵 matrix 和功能 function 是一个比较重要的事, 我们在这里简单的提及了一下在 theano 将要运用到的东西.  
author: 缘
chapter: 2
post-headings:
  - Theano 的基本用法
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/theanoTUT/theano4_basic_usage.py){:target="_blank"}

{% include assign-heading.html %}

在 theano 中学会定义矩阵 `matrix` 和功能 `function` 是一个比较重要的事, 我们在这里简单的提及了一下在 theano 将要运用到的东西.  

theano 和 tensorflow 类似，都是基于建立神经网络每个组件，在组件联系起来，数据放入组件，得到结果。

首先, 我们这次需要加载 theano 和 numpy 两个模块, 并且使用 theano 来创建 `function`.

```python
import numpy as np
import theano.tensor as T
from theano import function
```

定义`X`和`Y`两个常量 (scalar)，把结构建立好之后，把结构放在`function`，在把数据放在`function`。

```python
# basic
x = T.dscalar('x')  # 建立 x 的容器
y = T.dscalar('y')  # 建立 y 的容器
z = x+y     #  建立方程

# 使用 function 定义 theano 的方程, 
# 将输入值 x, y 放在 [] 里,  输出值 z 放在后面
f = function([x, y], z)  

print(f(2,3))  # 将确切的 x, y 值放入方程中
# 5.0
```

使用 theano 中 的 `pp` (pretty-print) 能够打印出原始方程:

```python
from theano import pp
print(pp(z)) 
# (x + y)
```

定义矩阵，以及利用矩阵做相关运算:

```python
x = T.dmatrix('x')  # 矩阵 x 的容器
y = T.dmatrix('y')  # 矩阵 y 的容器
z = x + y   # 定义矩阵加法
f = function([x, y], z) # 定义方程

print(f(
        np.arange(12).reshape((3,4)), 
        10*np.ones((3,4))
        )
      )
"""
[[ 10.  11.  12.  13.]
 [ 14.  15.  16.  17.]
 [ 18.  19.  20.  21.]]
"""
```