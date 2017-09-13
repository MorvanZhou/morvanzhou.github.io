---
youku_id: XMTYwNDA2Mzg2NA
youtube_id: LIF4tn5KVu4
description: "多进程 Multiprocessing 和多线程 threading 类似, 他们都是在 python 中用来并行运算的.
不过既然有了 threading, 为什么 Python 还要出一个 multiprocessing 呢?
原因很简单, 就是用来弥补 threading 的一些劣势"
chapter: 1
title: 什么是 Multiprocessing
date: 2016-11-3
post-headings:
  - 和 threading 的比较
---
{% assign post-heading-count = -1 %}


{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>


多进程 Multiprocessing 和多线程 threading 类似, 他们都是在 python 中用来并行运算的.
不过既然有了 threading, 为什么 Python 还要出一个 multiprocessing 呢?
原因很简单, 就是用来弥补 threading 的一些劣势, 比如在 threading [教程中提到的GIL]({% link _contents/tutorials/python-basic/threading/5-GIL.md %}).

使用 multiprocessing 也非常简单, 如果对 threading 有一定了解的朋友, 你们的享受时间就到了.
因为 python 把 multiprocessing 和 threading 的使用方法做的几乎差不多. 这样我们就更容易上手.
也更容易发挥你电脑多核系统的威力了!