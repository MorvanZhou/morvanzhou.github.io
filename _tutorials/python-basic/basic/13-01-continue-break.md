---
youku_id: XMTU5MjY2MTg3Mg
youtube_id: vfUjqt9r04o
description: 
chapter: 13
title: continue & break
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - 跳出循环
  - break
  - continue
---





{% include assign-heading.html %}

`True` and `False` ,当输入`1`时，`a=False`时，会执行接下来的语句后再跳出这个循环。

```python
a=True
while a:
    b= input('type somesthing')
    if b=='1':
        a= False
    else:
        pass
print ('finish run')

''''
type somesthing:2
still in while
type somesthing:3
still in while
type somesthing:1
still in while    #会执行下面的语句再跳出
finish run
''''
```




{% include assign-heading.html %}

`break`用法，在循环语句中，使用 `break`, 当符合跳出条件时，会直接结束循环，这是 `break` 和 `True False` 的区别。

```python
while True:
    b= input('type somesthing:')
    if b=='1':
        break
    else:
        pass
    print('still in while')
print ('finish run')

"""
type somesthing:4
still in while
type somesthing:5
still in while
type somesthing:1
finish run
"""
```




{% include google-in-article-ads.html %}

{% include assign-heading.html %}

在代码中，满足`b=1`的条件时，因为使用了 `continue` , `python` 不会执行 `else` 后面的代码，而会直接进入下一次循环。

```python
while True:
    b=input('input somesthing:')
    if b=='1':
       continue
    else:
        pass
    print('still in while' )

print ('finish run')
"""
input somesthing:3
still in while
input somesthing:1  # 没有"still in while"。直接进入下一次循环
input somesthing:4
still in while
input somesthing:
"""

```

