---
youku_id: XMTU4NTgwOTg4MA
youtube_id: GxMm82yy2Ds
description: 
chapter: 9
title: class 类 init 功能
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - init
  - 总结
---


{% include assign-heading.html %}

`__init__`可以理解成初始化`class`的变量，取自英文中`initial` 最初的意思.可以在运行时，给初始值附值，

运行`c=Calculator('bad calculator',18,17,16,15)`,然后调出每个初始值的值。看如下代码。

```python
class Calculator:
    name='good calculator'
    price=18
    def __init__(self,name,price,height,width,weight):   # 注意，这里的下划线是双下划线
        self.name=name
        self.price=price
        self.h=height
        self.wi=width
        self.we=weight
""""
>>> c=Calculator('bad calculator',18,17,16,15)
>>> c.name
'bad calculator'
>>> c.price
18
>>> c.h
17
>>> c.wi
16
>>> c.we
15
>>>
""""

```

如何设置属性的默认值, 直接在`def`里输入即可，如下:

`def __init__(self,name,price,height=10,width=14,weight=16):`查看运行结果，
三个有默认值的属性，可以直接输出默认值，这些默认值可以在`code`中更改,
比如`c.wi=17`再输出`c.wi`就会把`wi`属性值更改为`17`.同理可推其他属性的更改方法。

```python
class Calculator:
    name='good calculator'
    price=18
    def __init__(self,name,price,hight=10,width=14,weight=16): #后面三个属性设置默认值,查看运行
        self.name=name
        self.price=price
        self.h=hight
        self.wi=width
        self.we=weight

 """"
>>> c=Calculator('bad calculator',18)
>>> c.h
10
>>> c.wi
14
>>> c.we
16
>>> c.we=17
>>> c.we
17
""""
```


{% include assign-heading.html %}

`def __init__(self,name,price,height,width,weight):`  注意，这里的下划线是双下划线