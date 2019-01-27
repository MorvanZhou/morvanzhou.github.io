---
b_av: 16944429
b_cid: 27699353
b_page: 5
youku_id: XMTYwMjQyMDAzNg
youtube_id: 2511-7VR4nQ
description: 
chapter: 1
title: GIL 不一定有效率
date: 2016-11-3
post-headings:
  - 测试 GIL
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/threadingTUT/thread5_GIL.py){:target="_blank"}
  * 多进程 [教程](/tutorials/python-basic/multiprocessing/)


这次我们来看看为什么说 python 的多线程 threading 有时候并不是特别理想.
最主要的原因是就是, Python 的设计上, 有一个必要的环节, 就是 Global Interpreter Lock (GIL).
这个东西让 Python 还是一次性只能处理一个东西.

我从[这里](http://python3-cookbook.readthedocs.io/zh_CN/latest/c12/p09_dealing_with_gil_stop_worring_about_it.html){:target="_blank"}摘抄了一段对于 GIL 的解释.

> 尽管Python完全支持多线程编程， 但是解释器的C语言实现部分在完全并行执行时并不是线程安全的。 实际上，解释器被一个全局解释器锁保护着，它确保任何时候都只有一个Python线程执行。 GIL最大的问题就是Python的多线程程序并不能利用多核CPU的优势 （比如一个使用了多个线程的计算密集型程序只会在一个单CPU上面运行）。

> 在讨论普通的GIL之前，有一点要强调的是GIL只会影响到那些严重依赖CPU的程序（比如计算型的）。 如果你的程序大部分只会涉及到I/O，比如网络交互，那么使用多线程就很合适， 因为它们大部分时间都在等待。实际上，你完全可以放心的创建几千个Python线程， 现代操作系统运行这么多线程没有任何压力，没啥可担心的。



{% include assign-heading.html %}

我们创建一个 `job`, 分别用 threading 和 一般的方式执行这段程序.
并且创建一个 list 来存放我们要处理的数据. 在 Normal 的时候, 我们这个 list 扩展4倍,
在 threading 的时候, 我们建立4个线程, 并对运行时间进行对比.

```python
import threading
from queue import Queue
import copy
import time

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)
```

如果你成功运行整套程序, 你大概会有这样的输出. 我们的运算结果没错, 所以程序 threading 和 Normal 运行了一样多次的运算.
但是我们发现 threading 却没有快多少, 按理来说, 我们预期会要快3-4倍, 因为有建立4个线程, 但是并没有.
这就是其中的 GIL 在作怪.

```
1999998000000
normal:  0.10034608840942383
1999998000000
multithreading:  0.08421492576599121
```