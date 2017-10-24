---
youku_id: XMTYwMjQ4Njk4OA
youtube_id: -q4txLdUMBM
description: "threading 中有线程锁, 我们能锁住变量的更新, 让它按预定的方式进行更新和交流"
chapter: 1
title: 线程锁 Lock
date: 2016-11-3
author: Leoliao
post-headings:
  - 不使用 Lock 的情况
  - 使用 Lock 的情况
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/threadingTUT/thread6_lock.py){:target="_blank"}


**导入线程标准模块**

```python
import threading
```

{% include assign-heading.html %}

函数一：全局变量A的值每次加1，循环10次，并打印

```python
def job1():
    global A
    for i in range(10):
        A+=1
        print('job1',A)
```
函数二：全局变量A的值每次加10，循环10次，并打印

```python
def job2():
    global A
    for i in range(10):
        A+=10
        print('job2',A)

```

主函数：定义两个线程，分别执行函数一和函数二

```python
if __name__== '__main__':
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

完整代码：

```python
import threading

def job1():
    global A
    for i in range(10):
        A+=1
        print('job1',A)

def job2():
    global A
    for i in range(10):
        A+=10
        print('job2',A)

if __name__== '__main__':
    lock=threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

运行结果（在spyder编译器下运行的打印结果）：

```python
job1job2 11
job2 21
job2 31
job2 41
job2 51
job2 61
job2 71
job2 81
job2 91
job2 101
 1
job1 102
job1 103
job1 104
job1 105
job1 106
job1 107
job1 108
job1 109
job1 110
```

可以看出，打印的结果非常混乱


{% include assign-heading.html %}

lock在不同线程使用同一共享内存时，能够确保线程之间互不影响，使用lock的方法是，
在每个线程执行运算修改共享内存之前，执行`lock.acquire()`将共享内存上锁，
确保当前线程执行时，内存不会被其他线程访问，执行运算完毕后，使用`lock.release()`将锁打开，
保证其他的线程可以使用该共享内存。

函数一和函数二加锁

```python
def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()
```

主函数中定义一个`Lock`

```python
if __name__== '__main__':
    lock=threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

完整的代码

```python
import threading

def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()

if __name__== '__main__':
    lock=threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
```

运行结果

```python
job1 1
job1 2
job1 3
job1 4
job1 5
job1 6
job1 7
job1 8
job1 9
job1 10
job2 20
job2 30
job2 40
job2 50
job2 60
job2 70
job2 80
job2 90
job2 100
job2 110
```

从打印结果来看，使用`lock`后，一个一个线程执行完。使用`lock`和不使用`lock`，最后打印输出的结果是不同的。
