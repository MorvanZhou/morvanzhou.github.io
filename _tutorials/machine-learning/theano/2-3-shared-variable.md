---
youku_id: XMTY2Mjc3NTU4NA
youtube_id: GbYWEOjjsAI
title: Shared 变量
description: theano 中的 shared 基本上是用于定义神经网络的 weights 和 biases 的工具. 其中还有 get_value() 和 set_value()的功能.使用这些功能我们可以查看, 导入,导出我们的这些 model 的参数.
author: Alice
chapter: 2
date: 2016-11-3
post-headings:
  - 定义 Shared 变量
  - 提取 使用
  - 临时使用

---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/theanoTUT/theano6_shared_variable.py){:target="_blank"}

今天讲 `Shared 变量`，意思是这些变量可以在运算过程中，不停地进行交换和更新值。
在定义 `weights 和 bias` 的情况下，会需要用到这样的变量。

今天会学习如何定义和使用它。


{% include assign-heading.html %}


我们会用累加器来定义 `Shared 变量`，每一次向上面加一个值，每一次基于上面的变化，再加上另一个值，就这样不断地更新并保存这样的值。

首先引用需要的包：

```python
import numpy as np
import theano
import theano.tensor as T
```

用下面一行来定义 `Shared 变量`，要用 `np.array` 给它赋予初始值，初始值是 `0`，并且它的数据类型要规定好。
数据类型是很重要的，在后面要定义 `vector 或者 matrix` 的时候，一定要统一，否则就会报错。
这个例子中，我们定义它为 `float64`，所以在后面定义其他结构的时候，也要保证这样的数据类型。
最后一个参数就是它的名字 `'state'`。

```python
state = theano.shared(np.array(0,dtype=np.float64), 'state') # inital state = 0
```

下面是累加值，定义它的名字为 `inc`，还有它的数据类型，调用 `state.dtype`，而不是写 `dtype=np.float64`， 否则会报错。

```python
inc = T.scalar('inc', dtype=state.dtype)
```

接下来是要定义一个 `accumulator` 函数，它的输入参数为 `inc`，结果就是输出 `state`，累加的过程叫做 `updates`，就是要把现在的 `state` 变成 `state+inc` 。

```python
accumulator = theano.function([inc], state, updates=[(state, state+inc)])
```

{% include assign-heading.html %}

打印：
不能直接用 `print(accumulator(10))`，因为这样输出的，第一次就是初始值 0，只能到下一次输出的时候，才会出现 10.
下面这个更科学，它可以取出 `state` 的当前值，我们可以先后 ＋1， ＋10， 打印结果看看如何：

```python
# to get variable value
print(state.get_value())
# 0.0

accumulator(1)   # return previous value, 0 in here
print(state.get_value())
# 1.0

accumulator(10)  # return previous value, 1 in here
print(state.get_value())
# 11.0
```

`get_value` 可以用来提取参数的值。

而 `set_value` 可以用来重新设置参数，例如 把 11 变成了 －1，那么再 ＋3 之后就是 2，而不是 11+3=14.


```python
# to set variable value
state.set_value(-1)
accumulator(3)
print(state.get_value())
# 2.0
```

`get_value， set_value` 这两种只能在 `Shared 变量` 的时候调用。


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

有时只是想暂时使用 `Shared 变量`，并不需要把它更新：
这时我们可以定义一个 `a` 来临时代替 `state`，注意定义 `a` 的时候也要统一 `dtype`。

```
a = T.scalar(dtype=state.dtype)
```


然后忽略掉 `Shared 变量` 的运算，输入值是 `[inc, a]`，相当于把 `a` 代入 `state`，输出是 `tmp_func`，`givens` 就是想把什么替换成什么。
这样的话，在调用 `skip_shared` 函数后，`state` 并没有被改变。


```python
# temporarily replace shared variable with another value in another function
tmp_func = state * 2 + inc
a = T.scalar(dtype=state.dtype)
skip_shared = theano.function([inc, a], tmp_func, givens=[(state, a)]) # temporarily use a's value for the state
print(skip_shared(2, 3))
# 8.0

print(state.get_value()) # old state value
# 2.0
```

最后输出 `print(skip_shared(2, 3))` 时，就得到 3*2 + 2 = 8.
`state` 只是被暂时地替换成 `a`，但是在调用它的时候，仍然是原来的值 2，而不是 3（a的值）。

