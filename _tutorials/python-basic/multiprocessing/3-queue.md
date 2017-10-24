---
youku_id: XMTYwNDE4NTQ5Ng
youtube_id: _TNIlBlV5c0
description: "Queue的功能是将每个核或线程的运算结果放在队里中，
等到每个线程或核运行完毕后再从队列中取出结果，
继续加载运算。原因很简单, 多线程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果"
chapter: 1
title: 存储进程输出 Queue
date: 2016-11-3
author: Leoliao
post-headings:
  - 把结果放在 Queue 里
  - 主函数
  - 完整的代码
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/multiprocessingTUT/multiprocessing3_queue.py){:target="_blank"}

Queue的功能是将每个核或线程的运算结果放在队里中，
等到每个线程或核运行完毕后再从队列中取出结果，
继续加载运算。原因很简单, 多线程调用的函数不能有返回值, 所以使用Queue存储多个线程运算的结果

{% include assign-heading.html %}

定义一个被多线程调用的函数，`q` 就像一个队列，用来保存每次函数运行的结果

```python
#该函数没有返回值！！！
def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue
```

{% include assign-heading.html %}

定义一个多线程队列，用来存储结果

```python
if __name__=='__main__':
    q = mp.Queue()
```

定义两个线程函数，用来处理同一个任务,
`args` 的参数只要一个值的时候，参数后面需要加一个逗号，表示`args`是可迭代的，后面可能还有别的参数，不加逗号会出错

```python
p1 = mp.Process(target=job,args=(q,))
p2 = mp.Process(target=job,args=(q,))
```

分别启动、连接两个线程

```python
p1.start()
p2.start()
p1.join()
p2.join()
```

上面是分两批处理的，所以这里分两批输出，将结果分别保存

```python
res1 = q.get()
res2 = q.get()
```

打印最后的运算结果

```python
print(res1+res2)
```


{% include assign-heading.html %}

```python
import multiprocessing as mp

def job(q):
    res=0
    for i in range(1000):
        res+=i+i**2+i**3
    q.put(res)    #queue

if __name__=='__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))
    p2 = mp.Process(target=job,args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)
```

运行的时候还是要在terminal中，最后运行结果为

```python
499667166000
```