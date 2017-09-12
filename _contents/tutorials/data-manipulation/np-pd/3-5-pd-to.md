---
youku_id: XMTYzODIxMTg3Mg
youtube_id: Vb2aR_t957E
title: Pandas 导入导出
description: 使用 pandas 进行文件的导入导出是一件非常简单的事情 (csv, pickle等).
author: Bhan
date: 2016-11-3
chapter: 3
post-headings:
  - 要点
  - 读取csv
  - 将资料存取成pickle

---
{% assign post-heading-count = -1 %}
学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/numpy%26pandas/15_read_to)

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

`pandas`可以读取与存取的资料格式有很多种，像`csv`、`excel`、`json`、`html`与`pickle`等…，
详细请看[官方说明文件](http://pandas.pydata.org/pandas-docs/stable/io.html)

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

示范档案下载 - [student.csv](https://github.com/MorvanZhou/tutorials/blob/master/numpy%26pandas/15_read_to/student.csv)

```python
import pandas as pd #加载模块

#读取csv
data = pd.read_csv('students.csv')

#打印出data
print(data)
```

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

```python
data.to_pickle('student.pickle')
```