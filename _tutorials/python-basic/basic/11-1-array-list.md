---
youku_id: XMTU4NzI2ODI0OA
youtube_id: tjIDFuyMuhc
description: 
chapter: 11
title: 元组 列表
date: 2016-11-3

author: Hao
post-headings:
  - Tuple
  - List
  - 两者对比
---



{% include assign-heading.html %}

叫做 `tuple`，用小括号、或者无括号来表述，是一连串有顺序的数字。

```python
a_tuple = (12, 3, 5, 15 , 6)
another_tuple = 12, 3, 5, 15 , 6
```


{% include assign-heading.html %}

而`list`是以中括号来命名的:

```python
a_list = [12, 3, 67, 7, 82]
```


{% include assign-heading.html %}

他们的元素可以一个一个地被迭代、输出、运用、定位取值:

```python
for content in a_list:
    print(content)
"""
12
3
67
7
82
"""

for content_tuple in a_tuple:
    print(content_tuple)
"""
12
3
5
15
6
"""
```

下一个例子，依次输出`a_tuple`和`a_list`中的各个元素：

```python
for index in range(len(a_list)):
    print("index = ", index, ", number in list = ", a_list[index])
"""
index =  0 , number in list =  12
index =  1 , number in list =  3
index =  2 , number in list =  67
index =  3 , number in list =  7
index =  4 , number in list =  82
"""

for index in range(len(a_tuple)):
    print("index = ", index, ", number in tuple = ", a_tuple[index])
"""
index =  0 , number in tuple =  12
index =  1 , number in tuple =  3
index =  2 , number in tuple =  5
index =  3 , number in tuple =  15
index =  4 , number in tuple =  6
"""
```
