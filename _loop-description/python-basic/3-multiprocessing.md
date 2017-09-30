---
title: 多进程 Multiprocessing
icon-dir: /static/img/icon/multiprocessing_icon.png
tut-dir: /tutorials/python-basic/multiprocessing/
---
我们在多线程 (Threading) 里提到过, 它是有劣势的, GIL 让它没能更有效率的处理一些分摊的任务. 
而现在的电脑大部分配备了多核处理器, <a href="{{page.tut-dir}}">多进程 Multiprocessing</a>
能让电脑更有效率的分配任务给每一个处理器, 这种做法解决了多线程的弊端. 也能很好的提升效率.

