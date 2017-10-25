---
youku_id: XMTU4NTEzMDIwOA
youtube_id: H7kIuKhtXHQ
description: 
chapter: 6
title: 全局 & 局部 变量
date: 2016-11-3
post-headings:
  - 局部变量
  - 全局变量
---


{% include assign-heading.html %}

在 `def` 中, 我们可以定义一个局部变量, 这个变量 `a` 只能在这个功能 `fun` 中有效, 出了这个功能,
`a` 这个变量就不是那个局部的 `a`.

```python
def fun():
    a = 10
    print(a)
    return a+100

print(fun())

"""
10
110
"""
```

下面这个例子就验证了如果在 `fun` 外面调用 `a`, 会报错, 这表明外面的这个 `print(a)` 不能找到那个局部的 `a`,
只有全局变量再能在外面被调用, 比如 `APPLE`.

```python
APPLY = 100 # 全局变量
def fun():
    a = 10  # 局部变量
    return a+100

print(APPLE)    # 100
print(a)    # 报错, 不能拿到一个局部变量的值
```





{% include assign-heading.html %}

那如何在外部也能调用一个在局部里修改了的全局变量呢. 首先我们在外部定义一个全局变量 `a=None`, 然后再 `fun()` 中声明
这个 `a` 是来自外部的 `a`. 声明方式就是 `global a`. 然后对这个外部的 `a` 修改后, 修改的效果会被施加到外部的 `a` 上.
所以我们将能看到运行完 `fun()`, `a` 的值从 `None` 变成了 `20`.


```python
APPLY = 100 # 全局变量
a = None
def fun():
    global a    # 使用之前在全局里定义的 a
    a = 20      # 现在的 a 是全局变量了
    return a+100

print(APPLE)    # 100
print('a past:', a)  # None
fun()
print('a now:', a)   # 20
```