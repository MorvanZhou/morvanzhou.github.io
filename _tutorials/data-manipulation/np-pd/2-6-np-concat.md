---
youku_id: XMTU4ODcwNjI1Ng
youtube_id: ttSUtDTjDyI
bilibili_id: 16433457
title: Numpy array 合并
description: 关于 Numpy 多个的 array 的合并介绍. (stack, concatenate等)
author: Sincejuly
date: 2016-11-3
chapter: 2
post-headings:
  - np.vstack()
  - np.hstack()
  - np.newaxis()
  - np.concatenate()
---



{% include assign-heading.html %}

对于一个`array`的合并，我们可以想到按行、按列等多种方式进行合并。首先先看一个例子：

```python
import numpy as np
A = np.array([1,1,1])
B = np.array([2,2,2])
         
print(np.vstack((A,B)))    # vertical stack
"""
[[1,1,1]
 [2,2,2]]
"""
```

`vertical stack`本身属于一种上下合并，即对括号中的两个整体进行对应操作。此时我们对组合而成的矩阵进行属性探究：

```python
C = np.vstack((A,B))      
print(A.shape,C.shape)

# (3,) (2,3)
```

{% include assign-heading.html %}

利用`shape`函数可以让我们很容易地知道`A`和`C`的属性，从打印出的结果来看，`A`仅仅是一个拥有3项元素的数组（数列），而合并后得到的`C`是一个2行3列的矩阵。

介绍完了上下合并，我们来说说左右合并：

```python
D = np.hstack((A,B))       # horizontal stack

print(D)
# [1,1,1,2,2,2]

print(A.shape,D.shape)
# (3,) (6,)
```

通过打印出的结果可以看出：`D`本身来源于`A`，`B`两个数列的左右合并，而且新生成的`D`本身也是一个含有6项元素的序列。

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

说完了`array`的合并，我们稍稍提及一下前一节中转置操作，如果面对如同前文所述的`A`序列，
转置操作便很有可能无法对其进行转置（因为`A`并不是矩阵的属性），此时就需要我们借助其他的函数操作进行转置：

```python
print(A[np.newaxis,:])
# [[1 1 1]]

print(A[np.newaxis,:].shape)
# (1,3)

print(A[:,np.newaxis])
"""
[[1]
[1]
[1]]
"""

print(A[:,np.newaxis].shape)
# (3,1)
```

此时我们便将具有3个元素的`array`转换为了1行3列以及3行1列的矩阵了。

结合着上面的知识，我们把它综合起来：

```python
import numpy as np
A = np.array([1,1,1])[:,np.newaxis]
B = np.array([2,2,2])[:,np.newaxis]
         
C = np.vstack((A,B))   # vertical stack
D = np.hstack((A,B))   # horizontal stack

print(D)
"""
[[1 2]
[1 2]
[1 2]]
"""

print(A.shape,D.shape)
# (3,1) (3,2)
```

{% include assign-heading.html %}

当你的合并操作需要针对多个矩阵或序列时，借助`concatenate`函数可能会让你使用起来比前述的函数更加方便：

```python
C = np.concatenate((A,B,B,A),axis=0)

print(C)
"""
array([[1],
       [1],
       [1],
       [2],
       [2],
       [2],
       [2],
       [2],
       [2],
       [1],
       [1],
       [1]])
"""

D = np.concatenate((A,B,B,A),axis=1)

print(D)
"""
array([[1, 2, 2, 1],
       [1, 2, 2, 1],
       [1, 2, 2, 1]])
"""
```

`axis`参数很好的控制了矩阵的纵向或是横向打印，相比较`vstack`和`hstack`函数显得更加方便。