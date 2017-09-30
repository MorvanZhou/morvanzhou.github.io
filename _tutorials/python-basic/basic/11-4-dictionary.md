---
youku_id: XMTU4NzUzNzI4NA
youtube_id: leAjEgeOppc
description: 
chapter: 11
title: dictionary 字典
date: 2016-11-3

author: Hao
post-headings:
  - 创建字典
  - 字典存储类型
---



{% include assign-heading.html %}

如果说`List`是有顺序地输出输入的话，那么字典的存档形式则是无需顺序的， 我们来看一个例子：

在字典中，有`key`和 `value`两种元素，每一个`key`对应一个`value`, `key`是名字, `value`是内容。数字和字符串都可以当做`key`或者`value`，
在同一个字典中, 并不需要所有的`key`或`value`有相同的形式。
这样说, `List` 可以说是一种`key`为有序数列的字典。

```python
a_list = [1,2,3,4,5,6,7,8]

d1 = {'apple':1, 'pear':2, 'orange':3}
d2 = {1:'a', 2:'b', 3:'c'}
d3 = {1:'a', 'b':2, 'c':3}

print(d1['apple'])  # 1
print(a_list[0])    # 1

del d1['pear']
print(d1)   # {'orange': 3, 'apple': 1}

d1['b'] = 20
print(d1)   # {'orange': 3, 'b': 20, 'pear': 2, 'apple': 1}
```


{% include assign-heading.html %}

以上的例子可以对列表中的元素进行增减。在打印出整个列表时，可以发现各个元素并没有按规律打印出来，进一步验证了字典是一个无序的容器。

```python
def func():
    return 0

d4 = {'apple':[1,2,3], 'pear':{1:3, 3:'a'}, 'orange':func}
print(d4['pear'][3])    # a
```

字典还可以以更多样的形式出现，例如字典的元素可以是一个List，或者再是一个列表，再或者是一个function。索引需要的项目时，只需要正确指定对应的`key`就可以了。