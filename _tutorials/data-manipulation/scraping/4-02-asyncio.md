---
youku_id: XMzM1MDYyOTYyOA
youtube_id: Wa2K7sB7BZE
b_av: 17920849
b_cid: 30507993
b_page: 11
title: "加速爬虫: 异步加载 Asyncio"
description: "之前我一直在想如何用 multiprocessing 或者 threading 加速我的爬虫,
也做过了一些小实验, 确实, 我们看到了不小的效率提升. 但是当我更加深入的时候, 我发现, Python 还提供了一个有力的工具,
叫做 asyncio."
publish-date: 2017-12-30
thumbnail: "/static/thumbnail-small/scraping/4-2 asyncio.jpg"
chapter: 4
post-headings:
  - Asyncio 库
  - 基本用法
  - aiohttp
  - 和多进程分布式爬虫对比
---

学习资料:
  * [本节学习代码](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/4-2-asyncio.ipynb){:target="_blank"}
  * 一个很详细的[英文教学](https://hackernoon.com/asyncio-for-the-working-python-developer-5c468e6e2e8e){:target="_blank"}
  * Python 官网的 [Asyncio 介绍](https://docs.python.org/3/library/asyncio.html){:target="_blank"}
  * 异步加载网页 Python 包 [aiohttp](https://aiohttp.readthedocs.io/en/stable/index.html){:target="_blank"}



之前我一直在想如何用 [multiprocessing](https://docs.python.org/3.6/library/multiprocessing.html){:target="_blank"}
或者 [threading](https://docs.python.org/3.6/library/threading.html#module-threading){:target="_blank"} 加速我的爬虫,
也做过了一些[小实验]({% link _tutorials/data-manipulation/scraping/4-01-distributed-scraping.md %}),
确实, 我们看到了不小的效率提升. 但是当我更加深入的时候, 我发现, Python 还提供了一个有力的工具,
叫做 [asyncio](https://docs.python.org/3/library/asyncio.html){:target="_blank"}. 这是一个仅仅使用单线程, 就能达到多线程/进程的效果的工具.
它的原理, 简单说就是: **在单线程里使用异步计算, 下载网页的时候和处理网页的时候是不连续的, 更有效利用了等待下载的这段时间.**

传统的单线程下载处理网页可能就像下图([来源](https://www.nginx.com/blog/thread-pools-boost-performance-9x/){:target="_blank"})左边蓝色那样,
计算机执行一些代码, 然后等待下载网页, 下好以后, 再执行一些代码... 或者在等待的时候, 用另外一个线程执行其他的代码, 这是多线程的手段. 那么 asyncio 就像右边,
只使用一个线程, 但是将这些等待时间统统掐掉, 下载应该都调到了后台, 这个时间里, 执行其他异步的功能, 下载好了之后, 再调回来接着往下执行.

{% include tut-image.html image-name="4-2-1.png" %}

如果换一张 Python 自家解释 asyncio 的图([来源](https://docs.python.org/3/library/asyncio-task.html){:target="_blank"}), 虽然稍微复杂一点, 但是就是和上图想要表达的是一个意思.


{% include tut-image.html image-name="4-2-2.png" %}

那么, 我们今天就来尝试使用 asyncio 来替换掉 multiprocessing 或者 threading, 看看效果如何.



{% include assign-heading.html %}

[Asyncio](https://docs.python.org/3/library/asyncio.html){:target="_blank"} 库是 Python 的原装库, 但是是在 Python 3 的时候提出来的,
Python 2 和 Python 3.3- 是没有的. 而且 Python 3.5 之后, 和 Python 3.4 前在语法上还是有些不同,
比如 "await" 和 "yield" 的使用, 下面的教程都是基于 Python 3.5+, 使用 Python3.4 的可能会执行有点问题. 调整一下就好.

在 3.5+ 版本中, asyncio 有两样语法非常重要, `async`, `await`. 弄懂了它们是如何协同工作的, 我们就完全能发挥出这个库的功能了.
剧透一下, 等会使用单线程爬网页的 asyncio 和[之前多进程]({% link _tutorials/data-manipulation/scraping/4-01-distributed-scraping.md %})写的爬网页效果差不多,
而且当并行的进程数少的时候, asyncio 效果还会比多进程快.










{% include assign-heading.html %}

接着我们来举例介绍 asyncio, 像之前画的图那样, 我们要时刻记住, asyncio 不是多进程, 也不是多线程, 单单是一个线程, 但是是在 Python 的功能间切换着执行.
切换的点用 `await` 来标记, 能够异步的功能用 `async` 标记, 比如 `async def function():`. 首先我们看一下, 不使用 `async` 完成的一份代码, 然后我们将这份代码改成 `async` 版的.
这些代码我都会放在我的 github 中, 如果想一次性看全部, 请来[这里](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/4-2-asyncio.ipynb){:target="_blank"}.

```python
# 不是异步的
import time


def job(t):
    print('Start job ', t)
    time.sleep(t)               # wait for "t" seconds
    print('Job ', t, ' takes ', t, ' s')


def main():
    [job(t) for t in range(1, 3)]


t1 = time.time()
main()
print("NO async total time : ", time.time() - t1)

"""
Start job  1
Job  1  takes  1  s
Start job  2
Job  2  takes  2  s
NO async total time :  3.008603096008301
"""
```

从上面可以看出, 我们的 job 是按顺序执行的, 必须执行完 `job 1` 才能开始执行 `job 2`, 而且 `job 1` 需要1秒的执行时间,
而 `job 2` 需要2秒. 所以总时间是 **3 秒多**. 而如果我们使用 asyncio 的形式, `job 1` 在等待 `time.sleep(t)` 结束的时候,
比如是等待一个网页的下载成功, 在这个地方是可以切换给 `job 2`, 让它开始执行.

```python
import asyncio


async def job(t):                   # async 形式的功能
    print('Start job ', t)
    await asyncio.sleep(t)          # 等待 "t" 秒, 期间切换其他任务
    print('Job ', t, ' takes ', t, ' s')


async def main(loop):                       # async 形式的功能
    tasks = [
    loop.create_task(job(t)) for t in range(1, 3)
    ]                                       # 创建任务, 但是不执行
    await asyncio.wait(tasks)               # 执行并等待所有任务完成

t1 = time.time()
loop = asyncio.get_event_loop()             # 建立 loop
loop.run_until_complete(main(loop))         # 执行 loop
loop.close()                                # 关闭 loop
print("Async total time : ", time.time() - t1)

"""
Start job  1
Start job  2
Job  1  takes  1  s
Job  2  takes  2  s
Async total time :  2.001495838165283
"""
```

从结果可以看出, 我们没有等待 `job 1` 的结束才开始 `job 2`, 而是 `job 1` 触发了 `await` 的时候就切换到了 `job 2` 了.
这时, `job 1` 和 `job 2` 同时在等待 `await asyncio.sleep(t)`, 所以最终的程序完成时间, 取决于等待最长的 `t`, 也就是 **2秒**.
这和上面用普通形式的代码相比(3秒), 的确快了很多.






{% include google-in-article-ads.html %}
{% include assign-heading.html %}

有了对 asyncio 的基本了解, 我们就来看怎么把它用在爬虫. 这个功能对于爬虫非常的理想, 原因很简单, 我们在等待一个网页下载的时候, 完全可以切换到其它代码,
事半功倍. 但是 asycio 自己还是没办法完成这项任务的, 我们还需要安装另一个牛逼的模块将 `requests` 模块代替成一个异步的 `requests`, 这个牛逼的模块叫作
`aiohttp` ([官网在这](https://aiohttp.readthedocs.io/en/stable/index.html){:target="_blank"}). 下载安装特别简单.
直接在你的 terminal 或者 cmd 里面输入 "pip3 install aiohttp".

接着我们来看看我们怎么用最一般的 requests 模块爬网页, 和我们怎么将 requests 替换成 aiohttp.

```python
import requests

URL = 'https://morvanzhou.github.io/'


def normal():
    for i in range(2):
        r = requests.get(URL)
        url = r.url
        print(url)

t1 = time.time()
normal()
print("Normal total time:", time.time()-t1)

"""
https://morvanzhou.github.io/
https://morvanzhou.github.io/
Normal total time: 0.3869960308074951
"""
```

用 requests 用久了以后, 这样的代码真是信手拈来. 很好, 我们打开 [莫烦 Python](/) 的首页**两次**只花了 **0.38秒**.
然后我们在用 [aiohttp](https://aiohttp.readthedocs.io/en/stable/index.html){:target="_blank"} 来实现一样的功能.
结果 asyncio 的方式只用了 **0.11秒**! 大获全胜.

```python
import aiohttp


async def job(session):
    response = await session.get(URL)       # 等待并切换
    return str(response.url)


async def main(loop):
    async with aiohttp.ClientSession() as session:      # 官网推荐建立 Session 的形式
        tasks = [loop.create_task(job(session)) for _ in range(2)]
        finished, unfinished = await asyncio.wait(tasks)
        all_results = [r.result() for r in finished]    # 获取所有结果
        print(all_results)

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()
print("Async total time:", time.time() - t1)

"""
['https://morvanzhou.github.io/', 'https://morvanzhou.github.io/']
Async total time: 0.11447715759277344
"""
```

我们刚刚创建了一个 Session, 这是官网推荐的方式, 但是我觉得也可以直接用 request 形式, 细节请参考[官方说明](https://aiohttp.readthedocs.io/en/stable/client.html#make-a-request){:target="_blank"}.
如果要获取网页返回的结果, 我们可以在 `job()` 中 return 个结果出来, 然后再在 `finished, unfinished = await asyncio.wait(tasks)` 收集完成的结果,
这里它会返回完成的和没完成的, 我们关心的都是完成的, 而且 `await` 也确实是等待都完成了才返回. 真正的结果被存放在了 `result()` 里面.




{% include google-in-article-ads.html %}
{% include assign-heading.html %}

有了这些基础, 我们就可以来玩点高级的了, 之前我们用 multiprocessing 写过了一个[简单的分布式爬虫]({% link _tutorials/data-manipulation/scraping/4-01-distributed-scraping.md %}), 现在我们就来拿过来 PK 一下 asyncio 的方法.
首先我们对比一下这次写的结构和上次写的简单分布式爬虫的区别. 分布式我们完全依赖的是 multiprocessing 这个模块. 不了解的可以快速过一遍这个[教程](/tutorials/python-basic/multiprocessing).
使用 python 强大的并行处理运算来下载我们要处理的 urls, 然后解析网页也是一件耗时的事, 特别是网页量多的时候. 所以我们也将网页解析给并行了.
这样大大节省了下载和运算时间. 再看右边的这个 asyncio 的例子, 我们解析网页还是用的和 multiprocessing 那边一样的并行处理, 因为 asyncio 好像不支持解析网页的异步,
毕竟是计算密集型工序. 然后不一样的地方是, 我们在下载网页时, 不用 multiprocessing, 改用 asyncio, 用一个单线程的东西挑战多进程.

{% include tut-image.html image-name="4-2-3.png" %}

**特别注意: 任何网站都是有一个服务器压力的, 如果你爬的过于频繁, 特别是使用多进程爬取或异步爬取, 一次性提交请求给服务器太多次,
这将可能会使得服务器瘫痪, 你可能再也看不到莫烦 Python 了. 所以为了安全起见, 我限制了爬取数量(restricted_crawl=True).** 因为我测试使用的是内网 "http://127.0.0.1:4000/" 所以不会有这种压力.
你在以后的爬网页中, 会经常遇到这样的爬取次数的限制 (甚至被封号). 我以前爬 github 时就被限制成一小时只能爬60页.

具体的代码可以在[这里](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/4-2-asyncio.ipynb){:target="_blank"}详细观看, 需要注意的是, 我使用的内网进行测试(外网的下载速度变动太大),
在下载网页的地方, 我使用 `sleep(0.1)` 的功能模拟了网页下载的延迟. 一共下载了我 莫烦 Python 的快400个网页.
因为代码表达的内容我已经用上图展示给大家了, [每一个代码](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/4-2-asyncio.ipynb){:target="_blank"}都有50-60行, 我就不粘贴在这里了.
具体的结果, 我们可以总结一下.

| Number of Process| Multiprocessing | Asyncio |
|:----------------:|:---------------:|:-------:|
|         2        |       25.5s     |   7.5s  |
|         4        |       15.4s     |   7.0s  |
|         8        |       11.5s     |   7.2s  |

我们发现, 如果 `Pool(n)` 里面的这个 n 越大, 多进程才能越快, 但是 asyncio 却不会特别受进程数的影响.
一个单线程的东西居然战胜了多进程. 可见异步 asyncio 下载网页的重要性.

上面介绍的还只是 asyncio 的一小部分功能, 如果想了解更多有关于 asyncio 的使用方法, 请看到 Python 的[官方介绍](https://docs.python.org/3/library/asyncio.html){:target="_blank"}.


*相关教程*

* *[简单的分布式爬虫]({% link _tutorials/data-manipulation/scraping/4-01-distributed-scraping.md %})*
* *[加速爬虫: 异步加载 Asyncio]({% link _tutorials/data-manipulation/scraping/4-02-asyncio.md %})*
* *[高级爬虫: 让 Selenium 控制你的浏览器帮你爬]({% link _tutorials/data-manipulation/scraping/5-01-selenium.md %})*
* *[高级爬虫: 高效无忧的 Scrapy 爬虫库]({% link _tutorials/data-manipulation/scraping/5-02-scrapy.md %})*