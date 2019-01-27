---
youku_id: XMzM1MDMwNjA4OA
youtube_id: rwI7bFXdOsk
b_av: 17920849
b_cid: 30504026
b_page: 9
title: "小练习: 下载美图"
description: "学会爬虫, 关键在于练习, 见多识广, 见多了网页的构造, 才知道怎么爬. 今天我们就来一个小实战,
结合之前学习的 requests 访问和下载功能, 还有 BeautifulSoup, 来下载一些国家地理杂志的美图."
publish-date: 2017-12-30
thumbnail: "/static/thumbnail-small/scraping/3-3 practice download.jpg"
chapter: 3
post-headings:
  - 找到图片位置
  - 下载图片
---

学习资料:
  * [本节学习代码](https://github.com/MorvanZhou/easy-scraping-tutorial/blob/master/notebook/3-3-practice-download-images.ipynb){:target="_blank"}
  * 国家地理杂志[爬取页面](http://www.nationalgeographic.com.cn/animals/){:target="_blank"}


学会爬虫, 关键在于练习, 见多识广, 见多了网页的构造, 才知道怎么爬. 今天我们就来一个小实战,
结合之前学习的 requests [访问]({% link _tutorials/data-manipulation/scraping/3-01-requests.md %})和
[下载]({% link _tutorials/data-manipulation/scraping/3-02-download.md %})功能,
还有 [BeautifulSoup]({% link _tutorials/data-manipulation/scraping/2-01-beautifulsoup-basic.md %}), 来下载一些国家地理杂志的美图.


{% include tut-image.html image-name="3-3-1.png" %}



{% include assign-heading.html %}

说白了, 每次的爬虫, 都是先分析一下这个网页要找的东西的位置, 然后怎么索引上这个位置, 最后用 python 找到它.
这次也是这个逻辑. 我们看看今天要爬的这个图片[网址](http://www.nationalgeographic.com.cn/animals/){:target="_blank"}.
定位到最新图片的位置,

{% include tut-image.html image-name="3-3-2.png" %}

找到这张图片的所在位置, 对比这类型的图片, 找到一种手段来筛选这些图片. 发现他们都存在于 `img_list` 的这种 `<ul>` 中.

{% include tut-image.html image-name="3-3-3.png" %}

而图片地址都是在 `<img>` 中.

```
<img src="http://image.nationalgeographic.com.cn/2017/1228/20171228030617696.jpg">
```

现在我们有了思路, 先找带有 `img_list` 的这种 `<ul>`, 然后在 `<ul>` 里面找 `<img>`.


{% include google-in-article-ads.html %}









{% include assign-heading.html %}

有了思路, 现在我们就用 python 来下图吧. import BeautifulSoup 和 requests. 定义爬取的 url.

```python
from bs4 import BeautifulSoup
import requests

URL = "http://www.nationalgeographic.com.cn/animals/"
```

用 BeautifulSoup 找到带有 `img_list` 的这种 `<ul>`,

```python
html = requests.get(URL).text
soup = BeautifulSoup(html, 'lxml')
img_ul = soup.find_all('ul', {"class": "img_list"})
```

从 ul 中找到所有的 `<img>`, 然后提取 `<img>` 的 `src` 属性, 里面的就是图片的网址啦.
接着, 就用之前在 requests 下载[那节内容]({% link _tutorials/data-manipulation/scraping/3-02-download.md %})里提到的一段段下载.

```python
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        url = img['src']
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]
        with open('./img/%s' % image_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)
        print('Saved %s' % image_name)

"""
Saved 20171227102206573.jpg
...
Saved 20171214020322682.jpg
"""
```

我从下载好的照片中抽了一张出来, 哈哈, 是张河马.

{% include tut-image.html image-name="3-3-4.png" %}

如果你只是偶尔爬一爬网页, 学到目前为止, 你已经入门了, 但是如果你想要继续深入, 你开始对爬虫的效率担忧,
觉得自己爬得太慢, 想要大规模爬取网页, 那么接下来的内容就再适合你不过了.
[接下来]({% link _tutorials/data-manipulation/scraping/4-01-distributed-scraping.md %})我们就会提到爬虫的提效方法.
而且现在我们爬取的都是静态网页 (莫烦python 就是静态网页), 如果你遇到 JavaScript 很多的动态加载网页 (淘宝等),
后面的 [selenium 教程]({% link _tutorials/data-manipulation/scraping/5-01-selenium.md %})就很适合你.

*相关教程*

* *[了解网页结构]({% link _tutorials/data-manipulation/scraping/1-01-understand-website.md %})*
* *[多功能的 Requests]({% link _tutorials/data-manipulation/scraping/3-01-requests.md %})*
* *[下载文件]({% link _tutorials/data-manipulation/scraping/3-02-download.md %})*
* *[小练习: 下载美图]({% link _tutorials/data-manipulation/scraping/3-03-practice-download-image.md %})*