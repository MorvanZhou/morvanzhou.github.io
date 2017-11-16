---
youku_id: XMTU4NjU0MzE4NA
youtube_id: mf7ktBLwaJs
bilibili_id: 16378984
title: Numpy 属性
description: Numpy 的几种常用属性介绍 (shape, size, ndim).
author: abner
date: 2016-11-3
chapter: 2
post-headings:
  - numpy 的几种属性
---


这次我们会介绍几种 numpy 的属性:

- `ndim`：维度
- `shape`：行数和列数
- `size`：元素个数

使用`numpy`首先要导入模块

```python
import numpy as np #为了方便使用numpy 采用np简写
```

列表转化为矩阵：
```python
array = np.array([[1,2,3],[2,3,4]])  #列表转化为矩阵
print(array)
"""
array([[1, 2, 3],
       [2, 3, 4]])
"""
```

{% include assign-heading.html %}

接着我们看看这几种属性的结果:

```python
print('number of dim:',array.ndim)  # 维度
# number of dim: 2

print('shape :',array.shape)    # 行数和列数
# shape : (2, 3)

print('size:',array.size)   # 元素个数
# size: 6
```
