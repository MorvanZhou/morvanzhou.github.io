---
youku_id: XMTU4ODc2ODUwOA
youtube_id: lXmiDyktnCA
bilibili_id: 16379143
title: Numpy copy & deep copy
description: 在 numpy 中的复制功能介绍. 如果直接把 numpy array 赋值给另一个变量, 改变任意的一个变量都会影响到其他变量.
author: Bhan
date: 2016-11-3
chapter: 2
post-headings:
  - = 的赋值方式会带有关联性
  - copy() 的赋值方式没有关联性
---




{% include assign-heading.html %}

首先 `import numpy` 并建立变量, 给变量赋值。

```python
import numpy as np

a = np.arange(4)
# array([0, 1, 2, 3])

b = a
c = a
d = b
```

改变`a`的第一个值，`b`、`c`、`d`的第一个值也会同时改变。

```python
a[0] = 11
print(a)
# array([11,  1,  2,  3])
```

确认`b`、`c`、`d`是否与`a`相同。

```python
b is a  # True
c is a  # True
d is a  # True
```

同样更改`d`的值，`a`、`b`、`c`也会改变。

```python
d[1:3] = [22, 33]   # array([11, 22, 33,  3])
print(a)            # array([11, 22, 33,  3])
print(b)            # array([11, 22, 33,  3])
print(c)            # array([11, 22, 33,  3])
```


{% include assign-heading.html %}

```python
b = a.copy()    # deep copy
print(b)        # array([11, 22, 33,  3])
a[3] = 44
print(a)        # array([11, 22, 33, 44])
print(b)        # array([11, 22, 33,  3])
```

此时`a`与`b`已经没有关联。
