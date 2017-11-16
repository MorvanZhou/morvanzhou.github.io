---
youku_id: XMTYyOTg1MzE2OA
youtube_id: R6oAP8A2lNQ
bilibili_id: 16379172
title: Pandas 基本介绍
description: 我们说到了如果 numpy 是 python 中的列表的话, 那pandas 就是 python 中的字典. 我们还介绍了pandas 的基本用途,包括如何创建 pandas series 和 dataframe, 还有查看他们的一些属性
date: 2016-11-3
chapter: 3
author: 张能波
post-headings:
  - Numpy 和 Pandas 有什么不同
  - Series
  - DataFrame
  - DataFrame 的一些简单运用
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/numpy%26pandas/11_pandas_intro.py){:target="_blank"}
  
{% include assign-heading.html %}

如果用 python 的列表和字典来作比较, 那么可以说
Numpy 是列表形式的，没有数值标签，而 Pandas 就是字典形式。Pandas是基于Numpy构建的，让Numpy为中心的应用变得更加简单。

要使用pandas，首先需要了解他主要两个数据结构：Series和DataFrame。

{% include assign-heading.html %}

```python
import pandas as pd
import numpy as np
s = pd.Series([1,3,6,np.nan,44,1])

print(s)
"""
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64
"""

```

`Series`的字符串表现形式为：索引在左边，值在右边。由于我们没有为数据指定索引。于是会自动创建一个0到N-1（N为长度）的整数型索引。

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

```python
dates = pd.date_range('20160101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])

print(df)
"""
                   a         b         c         d
2016-01-01 -0.253065 -2.071051 -0.640515  0.613663
2016-01-02 -1.147178  1.532470  0.989255 -0.499761
2016-01-03  1.221656 -2.390171  1.862914  0.778070
2016-01-04  1.473877 -0.046419  0.610046  0.204672
2016-01-05 -1.584752 -0.700592  1.487264 -1.778293
2016-01-06  0.633675 -1.414157 -0.277066 -0.442545
"""
```

`DataFrame`是一个表格型的数据结构，它包含有一组有序的列，每列可以是不同的值类型（数值，字符串，布尔值等）。`DataFrame`既有行索引也有列索引，
它可以被看做由`Series`组成的大字典。

我们可以根据每一个不同的索引来挑选数据, 比如挑选 `b` 的元素:

{% include assign-heading.html %}

```python
print(df['b'])

"""
2016-01-01   -2.071051
2016-01-02    1.532470
2016-01-03   -2.390171
2016-01-04   -0.046419
2016-01-05   -0.700592
2016-01-06   -1.414157
Freq: D, Name: b, dtype: float64
"""
```

我们在创建一组没有给定行标签和列标签的数据 `df1`:

```python
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print(df1)

"""
   0  1   2   3
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11
"""
```

这样,他就会采取默认的从0开始 index. 还有一种生成 `df` 的方法, 如下 `df2`:
 
```python
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})
                    
print(df2)

"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""
```

这种方法能对每一列的数据进行特殊对待. 如果想要查看数据中的类型, 我们可以用 `dtype` 这个属性: 

```python
print(df2.dtypes)

"""
df2.dtypes
A           float64
B    datetime64[ns]
C           float32
D             int32
E          category
F            object
dtype: object
"""
```

如果想看对列的序号:

```python
print(df2.index)

# Int64Index([0, 1, 2, 3], dtype='int64')
```

同样, 每种数据的名称也能看到:

```python
print(df2.columns)

# Index(['A', 'B', 'C', 'D', 'E', 'F'], dtype='object')
```

如果只想看所有`df2`的值:
 
```python
print(df2.values)

"""
array([[1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'test', 'foo'],
       [1.0, Timestamp('2013-01-02 00:00:00'), 1.0, 3, 'train', 'foo']], dtype=object)
"""
```

想知道数据的总结, 可以用 `describe()`:

```python
df2.describe()

"""
         A    C    D
count  4.0  4.0  4.0
mean   1.0  1.0  3.0
std    0.0  0.0  0.0
min    1.0  1.0  3.0
25%    1.0  1.0  3.0
50%    1.0  1.0  3.0
75%    1.0  1.0  3.0
max    1.0  1.0  3.0
"""
```

如果想翻转数据, `transpose`:

```python
print(df2.T)

"""                   
0                    1                    2  \
A                    1                    1                    1   
B  2013-01-02 00:00:00  2013-01-02 00:00:00  2013-01-02 00:00:00   
C                    1                    1                    1   
D                    3                    3                    3   
E                 test                train                 test   
F                  foo                  foo                  foo   

                     3  
A                    1  
B  2013-01-02 00:00:00  
C                    1  
D                    3  
E                train  
F                  foo  

"""
```

如果想对数据的 `index` 进行排序并输出:

```python
print(df2.sort_index(axis=1, ascending=False))

"""
     F      E  D    C          B    A
0  foo   test  3  1.0 2013-01-02  1.0
1  foo  train  3  1.0 2013-01-02  1.0
2  foo   test  3  1.0 2013-01-02  1.0
3  foo  train  3  1.0 2013-01-02  1.0
"""
```

如果是对数据 值 排序输出:

```python
print(df2.sort_values(by='B'))

"""
     A          B    C  D      E    F
0  1.0 2013-01-02  1.0  3   test  foo
1  1.0 2013-01-02  1.0  3  train  foo
2  1.0 2013-01-02  1.0  3   test  foo
3  1.0 2013-01-02  1.0  3  train  foo
"""
```