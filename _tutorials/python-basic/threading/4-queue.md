---
youku_id: XMTYwMjMxODc3Mg
youtube_id: DnTn3Yx-Nvg
description: "代码实现功能，将数据列表中的数据传入，使用四个线程处理，将结果保存在Queue中，线程执行完后，从Queue中获取存储的结果"
chapter: 1
title: 储存进程结果 Queue
date: 2016-11-3
author: Leoliao
post-headings:
  - 导入线程,队列的标准模块
  - 定义一个被多线程调用的函数
  - 定义一个多线程函数
  - 完整的代码
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/threadingTUT/thread4_queue.py){:target="_blank"}


代码实现功能，将数据列表中的数据传入，使用四个线程处理，将结果保存在`Queue`中，线程执行完后，从`Queue`中获取存储的结果


{% include assign-heading.html %}

```python
import threading
import time
from queue import Queue
```

{% include assign-heading.html %}

函数的参数是一个列表l和一个队列`q`，函数的功能是，对列表的每个元素进行平方计算，将结果保存在队列中

```python
def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)   #多线程调用的函数不能用return返回值
```


{% include assign-heading.html %}

在多线程函数中定义一个`Queue`，用来保存返回值，代替`return`，定义一个多线程列表，初始化一个多维数据列表，用来处理：

```python
def multithreading():
    q =Queue()    #q中存放返回值，代替return的返回值
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
```

在多线程函数中定义四个线程，启动线程，将每个线程添加到多线程的列表中

```python
for i in range(4):   #定义四个线程
    t = threading.Thread(target=job,args=(data[i],q)) #Thread首字母要大写，被调用的job函数没有括号，只是一个索引，参数在后面
    t.start()#开始线程
    threads.append(t) #把每个线程append到线程列表中
```

分别`join`四个线程到主线程

```python
for thread in threads:
    thread.join()
```

定义一个空的列表`results`，将四个线运行后保存在队列中的结果返回给空列表`results`

```python
results = []
for _ in range(4):
    results.append(q.get())  #q.get()按顺序从q中拿出一个值
print(results)
```

{% include assign-heading.html %}

```python
import threading
import time

from queue import Queue

def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)

def multithreading():
    q =Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    for i in range(4):
        t = threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name___=='__main__':
    multithreading()
```

最后运行结果为:

```python
[[1, 4, 9], [9, 16, 25], [16, 16, 16], [25, 25, 25]]
```