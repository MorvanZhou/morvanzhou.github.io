---
youku_id: XMTYwNTMwMTcwOA
youtube_id: VJBSkVhHX3g
description: "这次我们讲进程锁的运用。让我们看看没有加进程锁时会产生什么样的结果。"
chapter: 1
title: 进程锁 Lock
date: 2016-11-3
author: Ryan Gao
post-headings:
  - 不加进程锁
  - 加进程锁
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/multiprocessingTUT/multiprocessing7_lock.py){:target="_blank"}

这次我们讲进程锁的运用。

{% include assign-heading.html %}

让我们看看没有加进程锁时会产生什么样的结果。

```python
import multiprocessing as mp
import time

def job(v, num):
    for _ in range(5):
        time.sleep(0.1) # 暂停0.1秒，让输出效果更明显
        v.value += num # v.value获取共享变量值
        print(v.value, end="")
        
def multicore():
    v = mp.Value('i', 0) # 定义共享变量
    p1 = mp.Process(target=job, args=(v,1))
    p2 = mp.Process(target=job, args=(v,3)) # 设定不同的number看如何抢夺内存
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
if __name__ == '__main__':
    multicore()
```

在上面的代码中，我们定义了一个共享变量`v`，两个进程都可以对它进行操作。
在`job()`中我们想让`v`每隔0.1秒输出一次累加`num`的结果，但是在两个进程`p1`和`p2` 
中设定了不同的累加值。所以接下来让我们来看下这两个进程是否会出现冲突。

运行一下：

```python
1
4
5
8
9
12
13
16
17
20
```

我们可以看到，进程1和进程2在相互抢着使用共享内存`v`。

{% include assign-heading.html %}

为了解决上述不同进程抢共享资源的问题，我们可以用加进程锁来解决。

首先需要定义一个进程锁

```python
    l = mp.Lock() # 定义一个进程锁
```

然后将进程锁的信息传入各个进程中

```python
    p1 = mp.Process(target=job, args=(v,1,l)) # 需要将Lock传入
    p2 = mp.Process(target=job, args=(v,3,l)) 
```

在`job()`中设置进程锁的使用，保证运行时一个进程的对锁内内容的独占

```python
def job(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1) 
        v.value += num # v.value获取共享内存
        print(v.value)
    l.release() # 释放
```

完整代码：

```python
def job(v, num, l):
    l.acquire() # 锁住
    for _ in range(5):
        time.sleep(0.1) 
        v.value += num # 获取共享内存
        print(v.value)
    l.release() # 释放

def multicore():
    l = mp.Lock() # 定义一个进程锁
    v = mp.Value('i', 0) # 定义共享内存
    p1 = mp.Process(target=job, args=(v,1,l)) # 需要将lock传入
    p2 = mp.Process(target=job, args=(v,3,l)) 
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ == '__main__':
    multicore()
```
运行一下，让我们看看是否还会出现抢占资源的情况：

```python
1
2
3
4
5
8
11
14
17
20
```

显然，进程锁保证了进程`p1`的完整运行，然后才进行了进程`p2`的运行