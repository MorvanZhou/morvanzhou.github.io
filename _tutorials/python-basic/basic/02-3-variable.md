---
youku_id: XMTU4Mjg3ODYzNg
youtube_id: hIbzfmdk2es
description: 
chapter: 2
title: 变量 variable
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - 自变量命名规则

---





{% include assign-heading.html %}

可以将一个数值，或者字符串串附值给自变量，如`apple=1` 中，`apple`为自变量的名称，`1`为自变量的值。 也可以将字符串赋值给自变量  `apple='iphone7 plus'`

```python
apple=1       #赋值 数字
print(apple)
""""
1
""""

apple='iphone 7 plus'   #赋值 字符串
print(apple)
""""
iphone 7 plus
""""

```

如果需要用多个单词来表示自变量，需要加下划线，如`apple_2016='iphone 7 plus'` 请看代码

```python
apple_2016='iphone 7 plus and new macbook'
print(apple_2016)
""""
iphone 7 plus and new macbook
""""
```

一次定义多个自变量  `a,b,c=1,2,3`。

```python
a,b,c=11,12,13
print(a,b,c)
""""
11 12 13
""""
```

