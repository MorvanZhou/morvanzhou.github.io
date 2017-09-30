---
youku_id: XMTU4Mjg3Mjc4MA
youtube_id: JxsBd6dniXc
description: 
chapter: 2
title: print 功能
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - print 字符串
  - print 字符串叠加
  - 简单运算
---






{% include assign-heading.html %}

`python` 中 `print` 字符串 要加`''`或者`""`

```python
>>> print('hello world')
'''
hello world
'''
>>> print("hello world 2")
'''
hello world 2
'''
```

{% include assign-heading.html %}

可以使用 `+` 将两个字符串链接起来, 如以下代码.

```python
>>> print('Hello world'+' Hello Hong Kong')
"""
Hello world Hello Hong Kong
"""
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

可以直接`print` 加法`+`,减法`-`,乘法`*`,除法`/`.  注意：字符串不可以直接和数字相加，否则出现错误。

```python
>>> print(1+1)
"""
2
"""
>>> print(3-1)
"""
2
"""
>>> print(3*4)
"""
12
"""
>>> print(12/4)
"""
3.0
"""
>>> print('iphone'+4) #字符串不可以直接和数字相加
"""
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print('iphone'+4)
TypeError: Can't convert 'int' object to str implicitly
"""
```

`int()` 和 `float()`；当`int()`一个浮点型数时，`int`会保留整数部分,比如 `int(1.9)`,会输出`1`,而不是四舍五入。

```python
>>> print(int('2')+3) #int为定义整数型
"""
5
"""
>>> print(int(1.9))  #当int一个浮点型数时，int会保留整数部分
"""
1
"""
>>> print(float('1.2')+3) #float()是浮点型，可以把字符串转换成小数
""""
4.2
""""
```



