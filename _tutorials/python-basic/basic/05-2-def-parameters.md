---
youku_id: XMTU4NTA3Njk0MA
youtube_id: 9UhdrNHjHI8
description: 
chapter: 5
title: 函数参数
date: 2016-11-3

author-link: http://gaufung.info/
author: 高峰
post-headings:
  - 基本使用
  - 实例
---




我们在使用的调用函数的时候，想要指定一些变量的值在函数中使用，那么这些变量就是函数的参数，函数调用的时候，
传入即可。

{% include assign-heading.html %}

```python
def function_name(parameters):
    expressions
```

`parameters` 的位置就是函数的参数，在调用的时候传入即可。

{% include assign-heading.html %}

```python
def func(a, b):
    c = a+b
    print('the c is ', c)
```

在这里定义的一个函数，其参数就是两个数值，函数的功能就是把两个参数加起来。运行脚本后，在 Python 提示符内调用函数
`func`, 如果不指定参数 `func()`, 那么将会出错; 输出 `func(1, 2)`，将 `a=1, b=2` 传入函数，输出 `the c is 3` 。所以在调用函数时候，参数个数和位置一定要按照函数定义。如果我们忘记了函数的参数的位置，只知道各个参数的名字，可以在
函数调用的过程中给指明特定的参数 `func(a=1, b=2)`, 这样的话，参数的位置将不受影响，所以 `func(b=2,a=1)`是同样的
的效果。