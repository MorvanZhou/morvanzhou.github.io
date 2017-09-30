---
youku_id: XMTU4Mjg4MTI1Ng
youtube_id: F9Ptmo9CZl4
description: 
chapter: 3
title: while 循环
date: 2016-11-3

author: 高峰
author-link: http://gaufung.info/
post-headings:
  - 基本使用
  - 实例
  - 注意点
  - 高级主题
---




在 Python 语言中用来控制循环的主要有两个句法，`while` 和 `for` 语句，本讲将简单介绍 `while` 句法的使用。

{% include assign-heading.html %}

while 语句同其他编程语言中 while 的使用方式大同小异，主要结构如下

```python
while condition:
    expressions
```

其中 `condition` 为判断条件，在 Python 中就是 `True` 和 `False` 其中的一个，如果为 `True`，
那么将执行 `exexpressions` 语句,否则将跳过该 while 语句块接着往下执行。


{% include assign-heading.html %}

比如要打印出 0 - 9 的所有数据,

```python
condition = 0
while condition < 10:
    print(condition)
    condition = condition + 1
```

输出的结果将是 `0, 1, 2, 3, 4, 5, 6, 7, 8, 9`, 第一行设置 `condition` 的
初始值为 0，在进行 while 判断的时候 `0 < 10` 为 `True`, 将会执行 while 内部
的代码，首先先打印出该值，然后将 `condition` 值加 1，至此将完成一次循环；再
`condition` 的值与 `10` 进行比较，仍然为 `True`, 重复如上过程，至到 `condiiton`
等于 10 后，不满足 `condition < 10` 的条件（`False`），将不执行 while 内部的内容
所以 `10` 不会被打印。

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

在使用 while 句法的时候一定要注意在循环内部一定要修改判断条件的值，否则程序的 while 部分
将**永远执行下去**。

```python
while True:
    print("I'm True")
```

如果这样做的话，程序将一直打印出 `I'm True`, 要停止程序，使用 `ctrl` + `c` 终止程序。


{% include assign-heading.html %}

在 Python 中除了常规比较操作
+ 小于（<)
+ 大于 (>)
+ 不大于 (<=)
+ 不大于 (>=)
+ 等于 (==)
+ 不等于 (!=)

会返回 `True` 和 `False`值，例如其他也会返回 `True` 和 `False`

##### 1 数字

整数和浮点数也能进行 `Boolean` 数据操作, 具体规则，如果该值等于 `0` 或者 `0.0` 将会返回 `False`
其余的返回 `True`

```python
condiiton = 10
while condiiton:
    print(condiiton)
    condiiton -= 1
```

输出的结果将会是 `10, 9, 8, 7, 6, 5, 4, 3, 2, 1`, 在这里 `condition` 在 while 语句中，如果该值
大于0，那么将会返回为 `True`,执行循环内部语句，直至 `condition` 等于0，返回 `False`。

##### 2 None 类型

如果 while 后面接着的语句数据类型 `None`, 将会返回 `False`。

##### 3 集合类型

在 Python 中集合类型有 `list`、 `tuple` 、`dict` 和 `set` 等，如果该集合对象作为 while 判断语句，
如果集合中的元素数量为 0，那么将会返回 `False`, 否则返回 `True`。

```python
a = range(10)
while a:
    print(a[-1])
    a = a[:len(a)-1]
```

上述程序将会返回 `9, 8, 7, 6, 5, 4, 3, 2, 1, 0`, 程序首先判断列表是否空，如果不为空，则
打印出最后一个内容，然后使用`切片`操作去掉最后一个元素，并更新列表；如此重复，直至列表为空。
