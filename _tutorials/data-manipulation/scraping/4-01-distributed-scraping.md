---
youku_id: MzM1MDQ3ODE2MA
youtube_id: QRJdEdgpTos
b_av: 17920849
b_cid: 30506095
b_page: 10
title: "加速爬虫: 多进程分布式"
description: "当你看到这里的时候, 说明你已经不满足于自己的爬虫速度, 你想要最求更快, 更便捷的爬虫方法.
你常常会听到用爬虫的人说分布式爬虫. 这就是为了体现便捷和效率而出现的方法. 这一节内容,
我们简单地介绍一下我使用的分布式爬虫方法, 并且用 python 的 multiprocessing 模块编写一个分布式爬虫."
publish-date: 2017-12-30
thumbnail: "/static/thumbnail-small/scraping/4-1 distributed.jpg"
chapter: 4
post-headings:
  - 什么是分布式爬虫
  - 我们的分布式爬虫
  - 测试普通爬法
  - 测试分布式爬法
---

学习资料:
  * [本节学习代码](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/4-1-distributed-scraping.ipynb){:target="_blank"}
  * 英文分布式爬虫[扩展阅读](https://blog.scrapinghub.com/2015/08/05/distributed-frontera-web-crawling-at-large-scale/){:target="_blank"}
  * 中文分布式爬虫[扩展阅读](http://bittiger.blogspot.com.au/2016/02/blog-post_3.html){:target="_blank"}
  * Python 的 [Multiprocessing 教程](/tutorials/python-basic/multiprocessing/)

当你看到这里的时候, 说明你已经不满足于自己的爬虫速度, 你想要最求更快, 更便捷的爬虫方法.
你常常会听到用爬虫的人说分布式爬虫. 这就是为了体现便捷和效率而出现的方法. 这一节内容,
我们简单地介绍一下我使用的分布式爬虫方法, 并且用 python 的 multiprocessing 模块编写一个分布式爬虫.

{% include tut-image.html image-name="1-1-00.jpg" %}




{% include assign-heading.html %}

分布式爬虫主要是为了非常有效率的抓取网页, 我们的程序一般是单线程跑的, 指令也是一条条处理的,
每执行完一条指令才能跳到下一条. 那么在爬虫的世界里, 这里存在着一个问题.

如果你已经顺利地执行过了前几节的爬虫代码, 你会发现, 有时候代码运行的时间大部分都花在了下载网页上.
有时候不到一秒能下载好一张网页的 HTML, 有时候却要几十秒. 而且非要等到 HTML 下载好了以后, 才能执行网页分析等步骤.
这非常浪费时间.

如果我们能合理利用计算资源, 在下载一部分网页的时候就已经开始分析另一部分网页了. 这将会大大节省整个程序的运行时间.
又或者, 我们能同时下载多个网页, 同时分析多个网页, 这样就有种事倍功半的效用.
分布式爬虫的体系有很多种, 处理优化的问题也是多样的. 这里有[一篇博客](http://bittiger.blogspot.com.au/2016/02/blog-post_3.html){:target="_blank"}可以当做扩展阅读,
来了解当今比较流行的分布式爬虫框架.





{% include assign-heading.html %}

而今天我们想搭建的这一个爬虫, 就是同时下载, 同时分析的这一种类型的分布式爬虫. 虽然算不上特别优化的框架, 但是概念理解起来比较容易.
我有尝试过徒手写高级一点的分布式爬虫, 但是写起来非常麻烦. 我琢磨了一下, 打算给大家介绍的这种分布式爬虫代码也较好写,
而且效率比普通爬虫快了3.5倍. 我也特地画了张图给大家解释一下要搭建的分布式爬虫.

{% include tut-image.html image-name="4-1-1.png" %}

主要来说, 我们最开始有一个网页, 比如说是莫烦Python的[首页](/), 然后首页中有很多 url, 我们使用多进程 ([Python多进程教程](/tutorials/python-basic/multiprocessing/))
同时开始下载这些 url, 得到这些 url 的 HTML 以后, 同时开始解析 (比如 BeautifulSoup) 网页内容. 在网页中寻找这个网站还没有爬过的链接.
最终爬完整个 莫烦 Python 网站所有页面.

有了这种思路, 我们就可以开始写代码了. 你可以在[我的 Github](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/4-1-distributed-scraping.ipynb){:target="_blank"}
一次性观看全部代码.

首先 import 全部要用的模块, 并规定一个主页. **注意, 我用这份代码测试我内网的网站(速度不受外网影响)**
所以使用的 `base_url` 是 "http://127.0.0.1:4000/", 如果你要爬 莫烦Python, 你的 `base_url`
要是 "https://morvanzhou.github.io/" (下载速度会受外网影响).

```python
import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import re

# base_url = "http://127.0.0.1:4000/"
base_url = 'https://morvanzhou.github.io/'
```

我们定义两个功能, 一个是用来爬取网页的(crawl), 一个是解析网页的(parse). 有了前几节内容的铺垫,
你应该能一言看懂下面的代码. `crawl()` 用 urlopen 来打开网页, 我用的内网测试, 所以为了体现下载网页的延迟,
添加了一个 `time.sleep(0.1)` 的下载延迟. 返回原始的 HTML 页面, `parse()` 就是在这个 HTML 页面中找到需要的信息,
我们用 BeautifulSoup 找 ([BeautifulSoup 教程]({% link _tutorials/data-manipulation/scraping/2-01-beautifulsoup-basic.md %})).
返回找到的信息.

```python
def crawl(url):
    response = urlopen(url)
    # time.sleep(0.1)             # slightly delay for downloading
    return response.read().decode()


def parse(html):
    soup = BeautifulSoup(html, 'lxml')
    urls = soup.find_all('a', {"href": re.compile('^/.+?/$')})
    title = soup.find('h1').get_text().strip()
    page_urls = set([urljoin(base_url, url['href']) for url in urls])   # 去重
    url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls, url
```

网页中爬取中, 肯定会爬到重复的网址, 为了去除掉这些重复, 我们使用 python 的 [set]({% link _tutorials/python-basic/basic/13-09-set.md %}) 功能.
定义两个 set, 用来搜集爬过的网页和没爬过的.

```python
unseen = set([base_url,])
seen = set()
```


{% include google-in-article-ads.html %}







{% include assign-heading.html %}

为了对比效果, 我们将在下面对比普通的爬虫和这种分布式的效果. 如果是普通爬虫,
我简化了一下接下来的代码, 将一些不影响的代码去除掉了, 如果你想看全部的代码, 请来到我的 [Github](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/4-1-distributed-scraping.ipynb){:target="_blank"}.
我们用循环一个个 `crawl` `unseen` 里面的 url, 爬出来的 HTML 放到 `parse` 里面去分析得到结果.
接着就是更新 `seen` 和 `unseen` 这两个集合了.

**特别注意: 任何网站都是有一个服务器压力的, 如果你爬的过于频繁, 特别是使用多进程爬取或异步爬取, 一次性提交请求给服务器太多次,
这将可能会使得服务器瘫痪, 你可能再也看不到莫烦 Python 了. 所以为了安全起见, 我限制了爬取数量(restricted_crawl=True).** 因为我测试使用的是内网 "http://127.0.0.1:4000/" 所以不会有这种压力.
你在以后的爬网页中, 会经常遇到这样的爬取次数的限制 (甚至被封号). 我以前爬 github 时就被限制成一小时只能爬60页.

```python
# DON'T OVER CRAWL THE WEBSITE OR YOU MAY NEVER VISIT AGAIN
if base_url != "http://127.0.0.1:4000/":
    restricted_crawl = True
else:
    restricted_crawl = False

while len(unseen) != 0:                 # still get some url to visit
    if restricted_crawl and len(seen) >= 20:
        break
    htmls = [crawl(url) for url in unseen]
    results = [parse(html) for html in htmls]

    seen.update(unseen)         # seen the crawled
    unseen.clear()              # nothing unseen

    for title, page_urls, url in results:
        unseen.update(page_urls - seen)     # get new url to crawl
```

使用这种单线程的方法, 在我的内网上面爬, 爬完整个 莫烦Python, 一共消耗 **52.3秒**.
接着我们把它改成多进程分布式.


{% include assign-heading.html %}

还是上一个 `while` 循环, 首先我们创建一个进程池(Pool). 不太懂进程池的朋友[看过来]({% link _tutorials/python-basic/multiprocessing/5-pool.md %}).
然后我们修改得到 `htmls` 和 `results` 的两句代码. 其他都不变, 只将这两个功能给并行了.
我在这里写的都是简化代码, 你可以在[这里](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/4-1-distributed-scraping.ipynb){:target="_blank"}
看到完整代码.

```python
pool = mp.Pool(4)
while len(unseen) != 0:
    # htmls = [crawl(url) for url in unseen]
    # --->
    crawl_jobs = [pool.apply_async(crawl, args=(url,)) for url in unseen]
    htmls = [j.get() for j in crawl_jobs]

    # results = [parse(html) for html in htmls]
    # --->
    parse_jobs = [pool.apply_async(parse, args=(html,)) for html in htmls]
    results = [j.get() for j in parse_jobs]

    ...
```

还是在内网测试, 只用了 **16.3秒**!! 这可比上面的单线程爬虫快了3.5倍. 而且我还不是在外网测试的.
如果在外网, 爬取一张网页的时间更长, 使用多进程会更加有效率, 节省的时间更多.

看到这里, 你一定觉得多线程是爬虫的救星. 其实不然, 要不然我们的教程为什么还能继续. 哈哈.
[下一节]({% link _tutorials/data-manipulation/scraping/4-02-asyncio.md %}),
我们会讲到比多进程更加厉害的一种方法. 叫做异步爬取 (asyncio 模块).





*相关教程*

* *[简单的分布式爬虫]({% link _tutorials/data-manipulation/scraping/4-01-distributed-scraping.md %})*
* *[加速爬虫: 异步加载 Asyncio]({% link _tutorials/data-manipulation/scraping/4-02-asyncio.md %})*
* *[高级爬虫: 让 Selenium 控制你的浏览器帮你爬]({% link _tutorials/data-manipulation/scraping/5-01-selenium.md %})*
* *[高级爬虫: 高效无忧的 Scrapy 爬虫库]({% link _tutorials/data-manipulation/scraping/5-02-scrapy.md %})*
