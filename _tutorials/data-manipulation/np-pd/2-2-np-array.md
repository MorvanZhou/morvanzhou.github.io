---
youku_id: XMTU4NzUzNDE0MA
youtube_id: 2TkMujKoDPI
bilibili_id: 16379006
title: Numpy 的创建 array
description:  Numpy array 数组的几种常用属性和功能介绍 (dtype, zeros, ones, empty, arrange, linspace)
author: abner
date: 2016-11-3
chapter: 2
post-headings:
  - 关键字
  - 创建数组
  - 指定数据 dtype
  - 创建特定数据
---


学习资料:
  * 创建 array 有很多 [形式](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html){:target="_blank"}

{% include assign-heading.html %}

- `array`：创建数组
- `dtype`：指定数据类型
- `zeros`：创建数据全为0
- `ones`：创建数据全为1
- `empty`：创建数据接近0
- `arrange`：按指定范围创建数据
- `linspace`：创建线段

{% include assign-heading.html %}

```python
a = np.array([2,23,4])  # list 1d
print(a)
# [2 23 4]
```

{% include assign-heading.html %}

```python
a = np.array([2,23,4],dtype=np.int)
print(a.dtype)
# int 64
```

```python
a = np.array([2,23,4],dtype=np.int32)
print(a.dtype)
# int32
```

```python
a = np.array([2,23,4],dtype=np.float)
print(a.dtype)
# float64
```

```python
a = np.array([2,23,4],dtype=np.float32)
print(a.dtype)
# float32
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

```python
a = np.array([[2,23,4],[2,32,4]])  # 2d 矩阵 2行3列
print(a)
"""
[[ 2 23  4]
 [ 2 32  4]]
"""
```

创建全零数组

```python
a = np.zeros((3,4)) # 数据全为0，3行4列
"""
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])
"""
```

创建全一数组, 同时也能指定这些特定数据的 `dtype`:

```python
a = np.ones((3,4),dtype = np.int)   # 数据为1，3行4列
"""
array([[1, 1, 1, 1],
       [1, 1, 1, 1],
       [1, 1, 1, 1]])
"""
```

创建全空数组, 其实每个值都是接近于零的数:

```python
a = np.empty((3,4)) # 数据为empty，3行4列
"""
array([[  0.00000000e+000,   4.94065646e-324,   9.88131292e-324,
          1.48219694e-323],
       [  1.97626258e-323,   2.47032823e-323,   2.96439388e-323,
          3.45845952e-323],
       [  3.95252517e-323,   4.44659081e-323,   4.94065646e-323,
          5.43472210e-323]])
"""
```

用 `arange` 创建连续数组:

```python
a = np.arange(10,20,2) # 10-19 的数据，2步长
"""
array([10, 12, 14, 16, 18])
"""
```

使用 `reshape` 改变数据的形状

```python
a = np.arange(12).reshape((3,4))    # 3行4列，0到11
"""
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
"""
```

用 `linspace` 创建线段型数据:

```python
a = np.linspace(1,10,20)    # 开始端1，结束端10，且分割成20个数据，生成线段
"""
array([  1.        ,   1.47368421,   1.94736842,   2.42105263,
         2.89473684,   3.36842105,   3.84210526,   4.31578947,
         4.78947368,   5.26315789,   5.73684211,   6.21052632,
         6.68421053,   7.15789474,   7.63157895,   8.10526316,
         8.57894737,   9.05263158,   9.52631579,  10.        ])
"""
```

同样也能进行 `reshape` 工作:

```python
a = np.linspace(1,10,20).reshape((5,4)) # 更改shape
"""
array([[  1.        ,   1.47368421,   1.94736842,   2.42105263],
       [  2.89473684,   3.36842105,   3.84210526,   4.31578947],
       [  4.78947368,   5.26315789,   5.73684211,   6.21052632],
       [  6.68421053,   7.15789474,   7.63157895,   8.10526316],
       [  8.57894737,   9.05263158,   9.52631579,  10.        ]])
"""
```










