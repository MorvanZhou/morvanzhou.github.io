---
youku_id: XMzI4OTA1OTExMg
youtube_id: OfmmsxVSP0o
b_av: 17920849
b_cid: 29287894
b_page: 5
title: "BeautifulSoup 解析网页: 正则表达"
description: "正则表达式, 是处理文本信息的重要工具, 除了 Python, 在其他的程序语言中, 也有十分重要的地位.
如果将正则表达式 + BeautifulSoup, 岂不是完美中的完美, 哈哈. 我们今天就来看看, 在 BeautifulSoup 中如何使用正则表达式,
获取更有难度的信息."
publish-date: 2017-12-29
thumbnail: "/static/thumbnail-small/scraping/2-3 bs.jpg"
chapter: 2
post-headings:
  - 正则表达式
  - 正则匹配
---

学习资料:
  * [本节学习代码](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/2-3-beautifulsoup-regex.ipynb){:target="_blank"}
  * 本节使用的爬虫[测试网页](/static/scraping/table.html)
  * 我的完整[正则表达式教程]({% link _tutorials/python-basic/basic/13-10-regular-expression.md %})


正则表达式, 是处理文本信息的重要工具, 除了 Python, 在其他的程序语言中, 也有十分重要的地位.
如果将正则表达式 + BeautifulSoup, 岂不是完美中的完美, 哈哈. 我们今天就来看看, 在 BeautifulSoup 中如何使用正则表达式,
获取更有难度的信息.


{% include tut-image.html image-name="2-3-1.jpg" %}



{% include assign-heading.html %}

正则表达式很厉害, 它能用简单的规则匹配到多样化的文本信息. 在做爬虫教程之前,
我特地做了一个[正则表达式的教程]({% link _tutorials/python-basic/basic/13-10-regular-expression.md %}), 为爬虫做铺垫.
所以有兴趣了解使用正则表达式的朋友, 都可以看看这个非常全的正则教程.

{% include tut-image.html image-name="2-3-2.png" %}

这次的教程有一些表格形式的 HTML, 在表格中, 有一些信息的格式类似, 我们先用 BeautifulSoup 筛选一些,
然后完全可以用正则给匹配出来. 比如你想下载这个页面的图片, 我们就可以将图片形式的 url 个匹配出来.
之后再下载就简单多了.






{% include assign-heading.html %}

我们先读取这个[网页](/static/scraping/table.html). 导入正则模块 `re`.

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/table.html").read().decode('utf-8')
```

{% include google-in-article-ads.html %}

我们发现, 如果是图片, 它们都藏在这样一个 tag 中:

```html
<td>
    <img src="https://morvanzhou.github.io/static/img/course_cover/tf.jpg">
</td>
```

所以, 我们可以用 `soup` 将这些 `<img>` tag 全部找出来, 但是每一个 img 的链接(src)都可能不同.
或者每一个图片有的可能是 jpg 有的是 png, 如果我们只想挑选 jpg 形式的图片, 我们就可以用这样一个正则
`r'.*?\.jpg'` 来选取. 把正则的 compile 形式放到 BeautifulSoup 的功能中, 就能选到符合要求的图片链接了.

```python
soup = BeautifulSoup(html, features='lxml')

img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])

"""
https://morvanzhou.github.io/static/img/course_cover/tf.jpg
https://morvanzhou.github.io/static/img/course_cover/rl.jpg
https://morvanzhou.github.io/static/img/course_cover/scraping.jpg
"""
```

又或者我们发现, 我想选一些课程的链接, 而这些链接都有统一的形式, 就是开头都会有
`https://morvan.`, 那我就将这个定为一个正则的规则, 让 BeautifulSoup 帮我找到符合这个规则的链接.

```python
course_links = soup.find_all('a', {'href': re.compile('https://morvan.*')})
for link in course_links:
    print(link['href'])

"""
https://morvanzhou.github.io/
https://morvanzhou.github.io/tutorials/scraping
https://morvanzhou.github.io/tutorials/machine-learning/tensorflow/
https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/
https://morvanzhou.github.io/tutorials/data-manipulation/scraping/
"""
```


学习了这么多实用的方法, 我们[接下来]({% link _tutorials/data-manipulation/scraping/2-04-practice-baidu-baike.md %})就来做一个小实战,
让我们的爬虫在百度百科上自由爬行, 在各个百科网页上跳来跳去.






*相关教程*

* *[Why 爬虫?]({% link _tutorials/data-manipulation/scraping/1-00-why.md %})*
* *[了解网页结构]({% link _tutorials/data-manipulation/scraping/1-01-understand-website.md %})*
* *[BeautifulSoup 解析网页: 基础]({% link _tutorials/data-manipulation/scraping/2-01-beautifulsoup-basic.md %})*
* *[BeautifulSoup 解析网页: CSS]({% link _tutorials/data-manipulation/scraping/2-02-beautifulsoup-css.md %})*
* *[BeautifulSoup 解析网页: 正则表达]({% link _tutorials/data-manipulation/scraping/2-03-beautifulsoup-regex.md %})*
* *[小练习: 爬百度百科]({% link _tutorials/data-manipulation/scraping/2-04-practice-baidu-baike.md %})*