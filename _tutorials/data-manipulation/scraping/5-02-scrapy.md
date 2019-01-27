---
youku_id: XMzM1MTA5Nzc3Mg
youtube_id: 0Uug1fDa8nw
b_av: 17920849
b_cid: 30515374
b_page: 13
title: "高级爬虫: 高效无忧的 Scrapy 爬虫库"
description: "前面的教程我们已经学会了如何写出自己的爬虫, 轻轻松松就能写出一个高性能的爬虫. 如果你想更高效的开发,
爬取网页, 记录数据库, Scrapy 是值得一推的. 它是一个爬虫的框架, 而不是一个简单的爬虫. 它整合了爬取, 处理数据, 存储数据的一条龙服务.
如果你只需要偶尔的一两次爬爬网页, 前面的教程已经够了, 如果你需要每天靠爬虫吃饭, Scrapy 还是有必要了解的."
publish-date: 2017-12-30
thumbnail: "/static/thumbnail-small/scraping/5-2 scrapy.jpg"
chapter: 5
post-headings:
  - Scrapy 的优势
  - Scrapy 爬虫
---

学习资料:
  * [本节学习代码](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/5-2-scrapy.ipynb){:target="_blank"}
  * Scrapy [官网](https://scrapy.org/){:target="_blank"}

前面的教程我们已经学会了如何写出自己的爬虫, 轻轻松松就能写出一个高性能的爬虫. 如果你想更高效的开发,
爬取网页, 记录数据库, Scrapy 是值得一推的. 它是一个爬虫的框架, 而不是一个简单的爬虫. 它整合了爬取, 处理数据, 存储数据的一条龙服务.
如果你只需要偶尔的一两次爬爬网页, 前面的教程已经够了, 如果你需要每天靠爬虫吃饭, Scrapy 还是有必要了解的.

{% include tut-image.html image-name="5-2-1.png" %}

这个教程教你写出一个 Scrapy 形式的爬虫, 带你入门 Scrapy, 但是 Scrapy 不仅仅只有爬虫, 你需要学习更多.
那学习 Scrapy 的地方, 当然是他们[自家网站](https://docs.scrapy.org/en/latest/){:target="_blank"}咯.








{% include assign-heading.html %}

Scrapy 是一个整合了的爬虫框架, 有着非常健全的管理系统. 而且它也是分布式爬虫,
但是比我们[之前写的]({% link _tutorials/data-manipulation/scraping/4-01-distributed-scraping.md %})那个分布式爬虫高级多了.
下面就是 Scrapy 的框架示意图([来源](https://docs.scrapy.org/en/latest/topics/architecture.html#topics-architecture){:target="_blank"}).
它的管理体系非常复杂. 但是特别高效. 让你又刷网页, 又下载, 同时能处理数据. 简直千手观音呀.

{% include tut-image.html image-name="5-2-2.png" %}

而且做 Scrapy 的项目, 绝对不是只需要写一个脚本就能解决的. 为了把你带入门, 这次我们只写一个脚本, 只涉及里面的爬虫(spider)部分.
其他的部分你可以在这里深入学习.

* 官网教程 [英文](https://docs.scrapy.org/en/latest/){:target="_blank"}, [中文](https://scrapy-chs.readthedocs.io/zh_CN/0.24/){:target="_blank"}
* JasonDing 的[学习Scrapy入门](https://www.jianshu.com/p/a8aad3bf4dc4){:target="_blank"}
* young-hz 的[Scrapy研究探索系列](http://blog.csdn.net/u012150179/article/details/32343635){:target="_blank"}




{% include assign-heading.html %}

好了, 我们开始今天的简单 Scrapy 教程吧. 首先你得安装 Scrapy. 在 terminal 或者 cmd
使用 pip 安装就好.

```shell
# python 2+
pip install scrapy

# python 3+
pip3 install scrapy
```

如果安装遇到任何问题, 它们家的[网站](https://docs.scrapy.org/en/latest/intro/install.html){:target="_blank"}是个好去处.

我们之前有做过爬取 [莫烦Python](/) 全网的信息. 用[多进程]({% link _tutorials/data-manipulation/scraping/4-01-distributed-scraping.md %})
和[异步爬取]({% link _tutorials/data-manipulation/scraping/4-02-asyncio.md %})都做过.
这次, 我们就用 Scrapy 来实现这样的一个爬虫. 剧透一下, 做前两个的时候, 代码行数差不多都是 50+ 行,
但是 scrapy 只需要用 20+ 行代码就解决的上面的事. 哈哈, 功能强大吧.

{% include google-in-article-ads.html %}


我们导入 scrapy 模块, 并创建一个 spider 的 class. 并继承 `scrapy.Spider`,
一定还要给这个 spider 一个名字, 我就用 `mofan` 好了, 因为是爬 莫烦Python 的.
给定一些初始爬取的网页, 写在 `start_urls` 里. 这里特别要提的是:
**之前我们用 python 的 set 来去除重复的 url, 在 scrapy 中, 这是不需要的, 因为它自动帮你去重**.
这可省心多了. 如果你想一次性看到全部代码, 请看到我的 [github](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/5-2-scrapy.ipynb){:target="_blank"}.

```python
import scrapy

class MofanSpider(scrapy.Spider):
    name = "mofan"
    start_urls = [
        'https://morvanzhou.github.io/',
    ]
    # unseen = set()
    # seen = set()      # 我们不在需要 set 了, 它自动去重
```


接着我们还要定义这个 class 中的一个功能就能完事了. 我们使用 python 的 `yield` 来返回搜集到的数据
(为什么是yield? 因为在 scrapy 中也有异步处理, 加速整体效率).
这些 title 和 url 的数据, 我们都是用 scrapy 中[抓取信息的方式](https://docs.scrapy.org/en/latest/intro/tutorial.html#extracting-data){:target="_blank"}.


```python
class MofanSpider(scrapy.Spider):
    ...
    def parse(self, response):
        yield {     # return some results
            'title': response.css('h1::text').extract_first(default='Missing').strip().replace('"', ""),
            'url': response.url,
        }

        urls = response.css('a::attr(href)').re(r'^/.+?/$')     # find all sub urls
        for url in urls:
            yield response.follow(url, callback=self.parse)     # it will filter duplication automatically
```

然后在这个response网页中筛选 `urls`, 这里我们也不需要使用 `urljoin()` 这种功能给 url 改变形式. 它在 `follow()` 这一步会自动检测 url 的格式.
(真是省心啊~), 然后对于每个找到的 url, 然后 yield 重新使用 `self.parse()` 来爬取, 这里又是自动去重!
Scrapy 仿佛知道你最不想做什么, 它自动帮你都做好了. 开心~

最后需要运行的时候有点不同, 你需要在 terminal 或 cmd 中运行这个爬虫. 而且还能帮你保存刚刚 yield 的 `{title:, url:}` 的结果.
`runspider 5-2-scrapy.py` 就是选择你要跑的这个 Python 文件.

```shell
$ scrapy runspider 5-2-scrapy.py -o res.json
```

`-o res.json` 这个 `-o` 就是输出的指令, 你可以在那个文件夹中找到一个名字叫 `res.json`
的文件, 里面存有所有找到的 `{title:, url:}`.

{% include tut-image.html image-name="5-2-3.png" %}


其实我们今天只做了 scrapy 中的爬虫, 一个正常的 scrapy 项目还包括有很多其他的内容(见下面).
这个教程就不会细说了, 因为学好 scrapy 还是比较麻烦的. 你可以在上面推荐给你的链接中, 继续深入学习 scrapy.

```
tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
```







*相关教程*

* *[简单的分布式爬虫]({% link _tutorials/data-manipulation/scraping/4-01-distributed-scraping.md %})*
* *[加速爬虫: 异步加载 Asyncio]({% link _tutorials/data-manipulation/scraping/4-02-asyncio.md %})*
* *[高级爬虫: 让 Selenium 控制你的浏览器帮你爬]({% link _tutorials/data-manipulation/scraping/5-01-selenium.md %})*
* *[高级爬虫: 高效无忧的 Scrapy 爬虫库]({% link _tutorials/data-manipulation/scraping/5-02-scrapy.md %})*
