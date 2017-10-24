---
youku_id: XMTYwNDIyNzk2MA
youtube_id: In5ye-JXj-w
description: "上篇讲了多进程/多核的运算，这次我们来对比下多进程，多线程和什么都不做时的消耗时间，看看哪种方式更有效率。"
chapter: 1
title: 效率对比 threading & multiprocessing
date: 2016-11-3
author: Ryan Gao
post-headings:
  - 创建多进程 multiprocessing
  - 创建多线程 multithread
  - 创建普通函数
  - 运行时间
  - 结果对比
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/multiprocessingTUT/multiprocessing4_efficiency_comparison.py){:target="_blank"}


上篇讲了多进程/多核的运算，这次我们来对比下多进程，多线程和什么都不做时的消耗时间，看看哪种方式更有效率。

{% include assign-heading.html %}

和上节一样，首先`import multiprocessing`并定义要实现的`job()`，同时为了容易比较，我们将计算的次数增加到1000000

```python
import multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000000):
        res += i + i**2 + i**3
    q.put(res) # queue
```

因为多进程是多核运算，所以我们将上节的多进程代码命名为`multicore()`

```python
def multicore():
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print('multicore:',res1 + res2)
```


{% include assign-heading.html %}

接下来创建多线程程序，创建多线程和多进程有很多相似的地方。首先`import threading`然后定义`multithread()`完成同样的任务

```python
import threading as td

def multithread():
    q = mp.Queue() # thread可放入process同样的queue中
    t1 = td.Thread(target=job, args=(q,))
    t2 = td.Thread(target=job, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print('multithread:', res1 + res2)
```

{% include assign-heading.html %}

最后我们定义最普通的函数。注意，在上面例子中我们建立了两个进程或线程，均对`job()`进行了两次运算，所以在`normal()`中我们也让它循环两次

```python
def normal():
    res = 0
    for _ in range(2):
        for i in range(1000000):
            res += i + i**2 + i**3
    print('normal:', res)
```

{% include assign-heading.html %}

最后，为了对比各函数运行时间，我们需要`import time`， 然后依次运行定义好函数：

```python
import time

if __name__ == '__main__':
    st = time.time()
    normal()
    st1 = time.time()
    print('normal time:', st1 - st)
    multithread()
    st2 = time.time()
    print('multithread time:', st2 - st1)
    multicore()
    print('multicore time:', time.time() - st2)
```

大功告成，下面我们来看下实际运行对比。

{% include assign-heading.html %}

```python
"""
# range(1000000)
('normal:', 499999666667166666000000L)
('normal time:', 1.1306169033050537)
('thread:', 499999666667166666000000L)
('multithread time:', 1.3054230213165283)
('multicore:', 499999666667166666000000L)
('multicore time:', 0.646507978439331)
"""
```

普通/多线程/多进程的运行时间分别是`1.13`，`1.3`和`0.64`秒。
我们发现多核/多进程最快，说明在同时间运行了多个任务。
而多线程的运行时间居然比什么都不做的程序还要慢一点，说明多线程还是有一定的短板的。
戳[这里]({% link _tutorials/python-basic/threading/5-GIL.md %})查看“多线程的短板是什么”。

我们将运算次数加十倍，再来看看三种方法的运行时间：

```python
"""
# range(10000000)
('normal:', 4999999666666716666660000000L)
('normal time:', 40.041773080825806)
('thread:', 4999999666666716666660000000L)
('multithread time:', 41.777158975601196)
('multicore:', 4999999666666716666660000000L)
('multicore time:', 22.4337899684906)
"""
```

这次运行时间依然是 多进程 < 普通 < 多线程，由此我们可以清晰地看出哪种方法更有效率。

