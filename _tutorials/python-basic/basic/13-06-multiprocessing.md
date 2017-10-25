---
youku_id: XMTYwNDA2Mzg2NA
youtube_id: LIF4tn5KVu4
description: 
chapter: 13
title:  multiprocessing 什么是多进程
date: 2016-11-3

post-headings:
  - 多进程
---


学习资料
  * 全套[multiprocessing 教程](/tutorials/python-basic/multiprocessing/)

{% include assign-heading.html %}

我们在多线程 (Threading) 里提到过, 它是有劣势的, GIL 让它没能更有效率的处理一些分摊的任务.
而现在的电脑大部分配备了多核处理器, 多进程 Multiprocessing
能让电脑更有效率的分配任务给每一个处理器, 这种做法解决了多线程的弊端. 也能很好的提升效率.