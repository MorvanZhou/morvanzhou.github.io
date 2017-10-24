---
youku_id: XMTYwMDE5MTQ4MA
youtube_id: EeoFahm8FOE
description: "本节我们来学习threading模块的一些基本操作，如获取线程数，添加线程等。首先别忘了导入模块："
chapter: 1
title: 添加线程 Thread
date: 2016-11-3
author: Jeff
post-headings:
  - 添加线程
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/threadingTUT/thread2_add_thread.py){:target="_blank"}

{% include assign-heading.html %}

本节我们来学习threading模块的一些基本操作，如获取线程数，添加线程等。首先别忘了导入模块：

```python
import threading
```

获取已激活的线程数

```python
threading.active_count()
# 2
```

查看所有线程信息

```python
threading.enumerate()
# [<_MainThread(MainThread, started 140736011932608)>, <Thread(SockThread, started daemon 123145376751616)>]
```

输出的结果是一个`<_MainThread(...)>`带多个`<Thread(...)>`。

查看现在正在运行的线程

```python
threading.current_thread()
# <_MainThread(MainThread, started 140736011932608)>
```

添加线程，`threading.Thread()`接收参数`target`代表这个线程要完成的任务，需自行定义

```python
def thread_job():
    print('This is a thread of %s' % threading.current_thread())

def main():
    thread = threading.Thread(target=thread_job,)   # 定义线程 
    thread.start()  # 让线程开始工作
    
if __name__ == '__main__':
    main()
```