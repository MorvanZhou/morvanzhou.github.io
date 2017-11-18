---
youku_id: XMTU4ODcyODMwMA
youtube_id: o1j-biEc1Pc
bilibili_id: 16434440
title: Numpy array 分割
description: 关于 Numpy array 的分割运算, 包括横向和纵向分割的不同分割功能 (split).
author: Bhan
date: 2016-11-3
chapter: 2
post-headings:
  - 创建数据
  - 纵向分割
  - 横向分割
  - 错误的分割
  - 不等量的分割
  - 其他的分割方式
---


{% include assign-heading.html %}

首先 `import` 模块

```python
import numpy as np
```

建立3行4列的Array

```python
A = np.arange(12).reshape((3, 4))
print(A)
"""
array([[ 0,  1,  2,  3],
    [ 4,  5,  6,  7],
    [ 8,  9, 10, 11]])
"""
```

{% include assign-heading.html %}

```python
print(np.split(A, 2, axis=1))
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""
```

{% include assign-heading.html %}

```python
print(np.split(A, 3, axis=0))

# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
```

{% include assign-heading.html %}

范例的Array只有4列，只能等量对分，因此输入以上程序代码后Python就会报错。

```python
print(np.split(A, 3, axis=1))

# ValueError: array split does not result in an equal division
```

为了解决这种情况, 我们会有下面这种方式.

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

在机器学习时经常会需要将数据做不等量的分割，因此解决办法为`np.array_split()`

```python
print(np.array_split(A, 3, axis=1))
"""
[array([[0, 1],
        [4, 5],
        [8, 9]]), array([[ 2],
        [ 6],
        [10]]), array([[ 3],
        [ 7],
        [11]])]
"""
```

成功将Array不等量分割!

{% include assign-heading.html %}

在Numpy里还有`np.vsplit()`与横`np.hsplit()`方式可用。

```python
print(np.vsplit(A, 3)) #等于 print(np.split(A, 3, axis=0))

# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]


print(np.hsplit(A, 2)) #等于 print(np.split(A, 2, axis=1))
"""
[array([[0, 1],
       [4, 5],
       [8, 9]]), array([[ 2,  3],
        [ 6,  7],
        [10, 11]])]
"""
```
