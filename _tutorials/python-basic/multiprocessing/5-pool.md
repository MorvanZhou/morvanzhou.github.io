---
youku_id: XMTYwNDMwMTU5Mg
youtube_id: w7SG9hhhwvI
description: "这次我们讲进程池Pool。 进程池就是我们将所要运行的东西，放到池子里，Python会自行解决多进程的问题"
chapter: 1
title: 进程池 Pool
date: 2016-11-3
author: Ryan Gao
post-headings:
  - 进程池 Pool() 和 map()
  - 自定义核数量
  - apply_async()
  - 用 apply_async() 输出多个结果
  - 总结
---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/multiprocessingTUT/multiprocessing5_pool.py){:target="_blank"}

这次我们讲进程池`Pool`。 进程池就是我们将所要运行的东西，放到池子里，Python会自行解决多进程的问题

首先`import multiprocessing`和定义`job()`

```python
import multiprocessing as mp

def job(x):
    return x*x
```

{% include assign-heading.html %}

然后我们定义一个`Pool`

```python
pool = mp.Pool()
```

有了池子之后，就可以让池子对应某一个函数，我们向池子里丢数据，池子就会返回函数返回的值。
`Pool`和之前的`Process`的不同点是丢向`Pool`的函数有返回值，而`Process`的没有返回值。

接下来用`map()`获取结果，在`map()`中需要放入函数和需要迭代运算的值，然后它会自动分配给CPU核，返回结果

```python
res = pool.map(job, range(10))
```

让我们来运行一下

```python
def multicore():
    pool = mp.Pool()
    res = pool.map(job, range(10))
    print(res)
    
if __name__ == '__main__':
    multicore()
```

运行结果：
```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

{% include assign-heading.html %}

我们怎么知道`Pool`是否真的调用了多个核呢？我们可以把迭代次数增大些，然后打开CPU负载看下CPU运行情况 

> 打开CPU负载(Mac)：活动监视器 > CPU > CPU负载(单击一下即可)

`Pool`默认大小是CPU的核数，我们也可以通过在`Pool`中传入`processes`参数即可自定义需要的核数量，

```python
def multicore():
    pool = mp.Pool(processes=3) # 定义CPU核数量为3
    res = pool.map(job, range(10))
    print(res)
```

{% include assign-heading.html %}

`Pool`除了`map()`外，还有可以返回结果的方式，那就是`apply_async()`.

`apply_async()`中只能传递一个值，它只会放入一个核进行运算，但是传入值时要注意是可迭代的，所以在传入值后需要加逗号, 同时需要用`get()`方法获取返回值

```python
def multicore():
    pool = mp.Pool() 
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    # 用get获得结果
    print(res.get())
```

运行结果；

```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]  # map()
4 # apply_async()
```

{% include assign-heading.html %}

那么如何用`apply_async()`输出多个迭代呢？

我们在`apply_async()`中多传入几个值试试

```python
res = pool.apply_async(job, (2,3,4,))
```

结果会报错：

```python
TypeError: job() takes exactly 1 argument (3 given)
```

即`apply_async()`只能输入一组参数。

在此我们将`apply_async()` 放入迭代器中，定义一个新的`multi_res`

```python
multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
```

同样在取出值时需要一个一个取出来

```python
print([res.get() for res in multi_res])
```

合并代码

```python
def multicore():
    pool = mp.Pool() 
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    # 用get获得结果
    print(res.get())
    # 迭代器，i=0时apply一次，i=1时apply一次等等
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    # 从迭代器中取出
    print([res.get() for res in multi_res])
```

运行结果

```python
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] # map()
4 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81] # multi_res
```

可以看出在apply用迭代器的得到的结果和用map得到的结果是一样的

{% include assign-heading.html %}

1. `Pool`默认调用是CPU的核数，传入`processes`参数可自定义CPU核数
2. `map()` 放入迭代参数，返回多个结果
3. `apply_async()`只能放入一组参数，并返回一个结果，如果想得到`map()`的效果需要通过迭代

   ​









