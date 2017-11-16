---
youku_id: XMTYzMDE5ODc2OA
youtube_id: BRps4z_EJO0
bilibili_id: 16379192
title: Pandas 选择数据
description: pandas 中选择数据或索引的方法有很多种,一般我们会用到这几种 (loc, iloc, ix).
author: 张能波
date: 2016-11-3
chapter: 3
post-headings:
  - 简单的筛选
  - 根据标签 loc
  - 根据序列 iloc
  - 根据混合的这两种 ix
  - 通过判断的筛选
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/numpy%26pandas/12_selection.py){:target="_blank"}



我们建立了一个 6X4 的矩阵数据。

```python
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])

"""
             A   B   C   D
2013-01-01   0   1   2   3
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
"""
```

{% include assign-heading.html %}

如果我们想选取`DataFrame`中的数据，下面描述了两种途径, 他们都能达到同一个目的：

```python
print(df['A'])
print(df.A)

"""
2013-01-01     0
2013-01-02     4
2013-01-03     8
2013-01-04    12
2013-01-05    16
2013-01-06    20
Freq: D, Name: A, dtype: int64
"""
```

让选择跨越多行或多列: 

```python
print(df[0:3])
 
"""
            A  B   C   D
2013-01-01  0  1   2   3
2013-01-02  4  5   6   7
2013-01-03  8  9  10  11
"""

print(df['20130102':'20130104'])

"""
A   B   C   D
2013-01-02   4   5   6   7
2013-01-03   8   9  10  11
2013-01-04  12  13  14  15
"""
```

如果`df[3:3]`将会是一个空对象。后者选择`20130102`到`20130104`标签之间的数据，并且包括这两个标签。

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

同样我们可以使用标签来选择数据 `loc`, 本例子主要通过标签名字选择某一行数据，
或者通过选择某行或者所有行（`:`代表所有行）然后选其中某一列或几列数据。:

```python
print(df.loc['20130102'])
"""
A    4
B    5
C    6
D    7
Name: 2013-01-02 00:00:00, dtype: int64
"""

print(df.loc[:,['A','B']]) 
"""
             A   B
2013-01-01   0   1
2013-01-02   4   5
2013-01-03   8   9
2013-01-04  12  13
2013-01-05  16  17
2013-01-06  20  21
"""

print(df.loc['20130102',['A','B']])
"""
A    4
B    5
Name: 2013-01-02 00:00:00, dtype: int64
"""
```

{% include assign-heading.html %}

另外我们可以采用位置进行选择 `iloc`, 在这里我们可以通过位置选择在不同情况下所需要的数据例如选某一个，连续选或者跨行选等操作。

```python
print(df.iloc[3,1])
# 13

print(df.iloc[3:5,1:3])
"""
             B   C
2013-01-04  13  14
2013-01-05  17  18
"""

print(df.iloc[[1,3,5],1:3])
"""
             B   C
2013-01-02   5   6
2013-01-04  13  14
2013-01-06  21  22

"""
```

在这里我们可以通过位置选择在不同情况下所需要的数据, 例如选某一个，连续选或者跨行选等操作。

{% include assign-heading.html %}

当然我们可以采用混合选择 `ix`, 其中选择'A'和'C'的两列，并选择前三行的数据。

```python
print(df.ix[:3,['A','C']])
"""
            A   C
2013-01-01  0   2
2013-01-02  4   6
2013-01-03  8  10
"""
```

{% include assign-heading.html %}

最后我们可以采用判断指令 (Boolean indexing) 进行选择. 我们可以约束某项条件然后选择出当前所有数据.

```python
print(df[df.A>8])
"""
             A   B   C   D
2013-01-04  12  13  14  15
2013-01-05  16  17  18  19
2013-01-06  20  21  22  23
"""
```

下节我们将会讲到Pandas中如何设置值。