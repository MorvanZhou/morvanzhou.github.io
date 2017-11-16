---
youku_id: XMTU4ODY3NTE2OA
youtube_id: 82Tva71Lm1E
bilibili_id: 16379074
title: Numpy 索引
description: 在 Numpy 中, 运用最多的, 还是方便的索引功能, 这里介绍了几种最基本的索引方法.
author: Sincejuly
date: 2016-11-3
chapter: 2
post-headings:
  - 一维索引
  - 二维索引
---



{% include assign-heading.html %}

我们都知道，在元素列表或者数组中，我们可以用如同`a[2]`一样的表示方法，同样的，在Numpy中也有相对应的表示方法：

```python
import numpy as np
A = np.arange(3,15)

# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
         
print(A[3])    # 6
```

让我们将矩阵转换为二维的，此时进行同样的操作：

```python
A = np.arange(3,15).reshape((3,4))
"""
array([[ 3,  4,  5,  6]
       [ 7,  8,  9, 10]
       [11, 12, 13, 14]])
"""
         
print(A[2])         
# [11 12 13 14]
```

实际上这时的`A[2]`对应的就是矩阵`A`中第三行(从0开始算第一行)的所有元素。

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

如果你想要表示具体的单个元素，可以仿照上述的例子：

```python
print(A[1][1])      # 8
```

此时对应的元素即`A[1][1]`，在`A`中即横纵坐标都为1，第二行第二列的元素，即8（因为计数从0开始）。同样的还有其他的表示方法：

```python
print(A[1, 1])      # 8
```

在Python的 list 中，我们可以利用`:`对一定范围内的元素进行切片操作，在Numpy中我们依然可以给出相应的方法：

```python
print(A[1, 1:3])    # [8 9]
```

这一表示形式即针对第二行中第2到第4列元素进行切片输出（不包含第4列）。
此时我们适当的利用for函数进行打印：

```python
for row in A:
    print(row)
"""    
[ 3,  4,  5, 6]
[ 7,  8,  9, 10]
[11, 12, 13, 14]
"""
```

此时它会逐行进行打印操作。如果想进行逐列打印，就需要稍稍变化一下：

```python
for column in A.T:
    print(column)
"""  
[ 3,  7,  11]
[ 4,  8,  12]
[ 5,  9,  13]
[ 6, 10,  14]
"""
```

上述表示方法即对A进行转置，再将得到的矩阵逐行输出即可得到原矩阵的逐列输出。

最后依然说一些关于迭代输出的问题：

```python
import numpy as np
A = np.arange(3,15).reshape((3,4))
         
print(A.flatten())   
# array([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])

for item in A.flat:
    print(item)
    
# 3
# 4
……
# 14
```

这一脚本中的`flatten`是一个展开性质的函数，将多维的矩阵进行展开成1行的数列。而`flat`是一个迭代器，本身是一个`object`属性。
