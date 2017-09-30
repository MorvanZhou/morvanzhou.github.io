---
youku_id: XMTU4NTc3NTE1Ng
youtube_id: PI9U3LKNCo4
description: 
chapter: 9
title: class 类
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - class 定义一个类
  - 总结
---




{% include assign-heading.html %}

`class` 定义一个类, 后面的类别首字母推荐以大写的形式定义，比如`Calculator`.
`class`可以先定义自己的属性，比如该属性的名称可以写为 `name='Good Calculator'`.
`class`后面还可以跟`def`, 定义一个函数.
比如`def add(self,x,y):` 加法, 输出`print(x+y)`.
其他的函数定义方法一样，注意这里的`self` 是默认值.

```python
class Calculator:       #首字母要大写，冒号不能缺
    name='Good Calculator'  #该行为class的属性
    price=18
    def add(self,x,y):
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result=x-y
        print(result)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)

""""
>>> cal=Calculator()  #注意这里运行class的时候要加"()",否则调用下面函数的时候会出现错误,导致无法调用.
>>> cal.name
'Good Calculator'
>>> cal.price
18
>>> cal.add(10,20)
Good Calculator
30
>>> cal.minus(10,20)
-10
>>> cal.times(10,20)
200
>>> cal.divide(10,20)
0.5
>>>
""""
```

{% include assign-heading.html %}

- 注意定义自变量`cal`等于`Calculator`要加括号“()” ,`cal=Calculator()`否则运行下面函数的时候会出现错误,导致无法调用.