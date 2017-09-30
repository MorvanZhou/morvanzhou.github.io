---
youku_id: XMTU4Mjg4OTYzMg
youtube_id: Ul0ovDZOdgg
description: 
chapter: 4
title: if else 判断
date: 2016-11-3

author: 高峰
author-link: http://gaufung.info/
post-headings:
  - 基本使用
  - 实例
  - 高级主题
---



上一讲我们学习了 `if` 语句，这一样我们将要学习 `if else` 语句。


{% include assign-heading.html %}

```python
if condition:
    true_expressions
else:
    false_expressions
```

当 `if` 判断条件为 `True`,执行 `true_expressions` 语句; 如果为 `False`，将执行 `else` 的内部的
`false_expressions`。


{% include assign-heading.html %}

```python
x = 1
y = 2
z = 3
if x > y:
    print('x is greater than y')
else:
    print('x is less or equal to y')
```

在这个例子中，因为 `x > y` 将会返回 `False`, 那么将执行 `else` 的分支内容。输出 `x is less or equal to y`

```python
x = 4
y = 2
z = 3
if x > y:
    print('x is greater than y')
else:
    print('x is less or equal y')
```

在这里，因为 `condition` 条件为 `True`, 那么将会输出 `x is greater than y`。


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

对于从其他编程语言转过来的同学一定非常想知道 python 语言中的三目操作符怎么使用，很遗憾的是 python
中并没有类似 `condition ? value1 : value2 ` 三目操作符。然后现实中很多情况下我们只需要简单的判断
来确定返回值，但是冗长的 `if-else` 语句似乎与简单的 python 哲学不一致。别担心，python 可以通过
`if-else` 的行内表达式完成类似的功能。

```python
var = var1 if condition else var2
```

可以这么理解上面这段语句，如果 `condition` 的值为 `True`, 那么将 `var1` 的值赋给 `var`;如果为 `False`
则将 `var2` 的值赋给 `var`。

```python
worked = True
result = 'done' if worked else 'not yet'
print(result)
```

首先判断如果 `work` 为 `True`,那么将 `done` 字符串赋给 `result`，否则将 `not yet` 赋给 `result`。
结果将输出 `done`。