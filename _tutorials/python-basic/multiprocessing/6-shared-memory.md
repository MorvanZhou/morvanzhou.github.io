---
youku_id: XMTYwNDc3MjgxNg
youtube_id: EFjEPeYSlYY
description: "这节我们学习如何定义共享内存。只有用共享内存才能让CPU之间有交流。"
chapter: 1
title: 共享内存 shared memory
date: 2016-11-3
author: Ryan Gao
post-headings:
  - Shared Value
  - Shared Array
  - 参考数据形式
---

学习资料:
  * Python [C type code种类](https://docs.python.org/3.5/library/array.html){:target="_blank"}


这节我们学习如何定义共享内存。只有用共享内存才能让CPU之间有交流。

{% include assign-heading.html %}

我们可以通过使用`Value`数据存储在一个共享的内存表中。

```python
import multiprocessing as mp

value1 = mp.Value('i', 0) 
value2 = mp.Value('d', 3.14)
```

其中`d`和`i`参数用来设置数据类型的，`d`表示一个双精浮点类型，`i`表示一个带符号的整型。更多的形式请查看本页最后的表.

{% include assign-heading.html %}

在Python的`mutiprocessing`中，有还有一个`Array`类，可以和共享内存交互，来实现在进程之间共享数据。

```python
array = mp.Array('i', [1, 2, 3, 4])
```

这里的`Array`和numpy中的不同，它只能是一维的，不能是多维的。同样和`Value` 一样，需要定义数据形式，否则会报错。
我们会在后一节举例说明这两种的使用方法.

**错误形式**

```python
array = mp.Array('i', [[1, 2], [3, 4]]) # 2维list

"""
TypeError: an integer is required
"""
```


{% include assign-heading.html %}

各参数代表的数据类型

```
| Type code | C Type             | Python Type       | Minimum size in bytes |
| --------- | ------------------ | ----------------- | --------------------- |
| `'b'`     | signed char        | int               | 1                     |
| `'B'`     | unsigned char      | int               | 1                     |
| `'u'`     | Py_UNICODE         | Unicode character | 2                     |
| `'h'`     | signed short       | int               | 2                     |
| `'H'`     | unsigned short     | int               | 2                     |
| `'i'`     | signed int         | int               | 2                     |
| `'I'`     | unsigned int       | int               | 2                     |
| `'l'`     | signed long        | int               | 4                     |
| `'L'`     | unsigned long      | int               | 4                     |
| `'q'`     | signed long long   | int               | 8                     |
| `'Q'`     | unsigned long long | int               | 8                     |
| `'f'`     | float              | float             | 4                     |
| `'d'`     | double             | float             | 8                     |
```

(来源：[https://docs.python.org/3/library/array.html](https://docs.python.org/3/library/array.html){:target="_blank"}）