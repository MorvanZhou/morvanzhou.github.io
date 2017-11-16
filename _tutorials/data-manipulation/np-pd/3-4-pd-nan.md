---
youku_id: XMTYzMTUxNzgwOA
youtube_id: H9jqCR4z7Pw
bilibili_id: 16379234
title: Pandas 处理丢失数据 
description: 有时候我们导入或处理数据, 会产生一些空的或者是 NaN 数据,如何删除或者是填补这些 NaN 数据就是我们今天所要提到的内容.
author: 张能波
date: 2016-11-3
chapter: 3
post-headings:
  - 创建含 NaN 的矩阵
  - pd.dropna()
  - pd.fillna()
  - pd.isnull()

---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/numpy%26pandas/14_nan.py){:target="_blank"}

{% include assign-heading.html %}

有时候我们导入或处理数据, 会产生一些空的或者是 `NaN` 数据,如何删除或者是填补这些 `NaN` 数据就是我们今天所要提到的内容. 

建立了一个6X4的矩阵数据并且把两个位置置为空.

```python
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])
df.iloc[0,1] = np.nan
df.iloc[1,2] = np.nan
"""
             A     B     C   D
2013-01-01   0   NaN   2.0   3
2013-01-02   4   5.0   NaN   7
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
"""
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

如果想直接去掉有 `NaN` 的行或列, 可以使用 `dropna`

```python
df.dropna(
    axis=0,     # 0: 对行进行操作; 1: 对列进行操作
    how='any'   # 'any': 只要存在 NaN 就 drop 掉; 'all': 必须全部是 NaN 才 drop 
    ) 
"""
             A     B     C   D
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
"""
```

{% include assign-heading.html %}

如果是将 `NaN` 的值用其他值代替, 比如代替成 `0`:

```python
df.fillna(value=0)
"""
             A     B     C   D
2013-01-01   0   0.0   2.0   3
2013-01-02   4   5.0   0.0   7
2013-01-03   8   9.0  10.0  11
2013-01-04  12  13.0  14.0  15
2013-01-05  16  17.0  18.0  19
2013-01-06  20  21.0  22.0  23
"""
```

{% include assign-heading.html %}

判断是否有缺失数据 `NaN`, 为 `True` 表示缺失数据:

```python
df.isnull() 
"""
                A      B      C      D
2013-01-01  False   True  False  False
2013-01-02  False  False   True  False
2013-01-03  False  False  False  False
2013-01-04  False  False  False  False
2013-01-05  False  False  False  False
2013-01-06  False  False  False  False
"""
```

检测在数据中是否存在 `NaN`, 如果存在就返回 `True`:

```python
np.any(df.isnull()) == True  
# True
```
 
下次课会将pandas如何导入导出数据的过程。