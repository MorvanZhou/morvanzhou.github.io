---
youku_id: XMTYwNDExNTQ3Ng
youtube_id: ECb8WKVepGw
description: "本节包括的内容有: 线程、进程的创建和使用"
chapter: 1
title: 添加进程 Process
date: 2016-11-3
author: Leoliao
post-headings:
  - 导入线程进程标准模块
  - 定义一个被线程和进程调用的函数
  - 创建线程和进程
  - 完整的线程和进程创建使用对比代码
  - 运用
---




{% include assign-heading.html %}

```python
import multiprocessing as mp
import threading as td
```


{% include assign-heading.html %}

```python
def job(a,d):
    print('aaaaa')
```

{% include assign-heading.html %}


```python
t1 = td.Thread(target=job,args=(1,2))
p1 = mp.Process(target=job,args=(1,2))
```

注意：Thread和Process的首字母都要大写，被调用的函数没有括号，被调用的函数的参数放在args(...)中

分别启动线程和进程

```python
t1.start()
p1.start()
```

分别连接线程和进程

```python
t1.join()
p1.join()
```

{% include assign-heading.html %}

```python
import multiprocessing as mp
import threading as td

def job(a,d):
    print('aaaaa')

t1 = td.Thread(target=job,args=(1,2))
p1 = mp.Process(target=job,args=(1,2))
t1.start()
p1.start()
t1.join()
p1.join()
```
从上面的使用对比代码可以看出，线程和进程的使用方法相似


{% include assign-heading.html %}

在运用时需要添加上一个定义main函数的语句

```python
if __name__=='__main__':
```

完整的应用代码：

```python
import multiprocessing as mp

def job(a,d):
    print('aaaaa')

if __name__=='__main__':
    p1 = mp.Process(target=job,args=(1,2))
    p1.start()
    p1.join()
```

运行环境要在terminal环境下，可能其他的编辑工具会出现运行结束后没有打印结果，在terminal中的运行后打印的结果为：

```python
aaaaa
```