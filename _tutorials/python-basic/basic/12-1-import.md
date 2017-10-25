---
youku_id: XMTU5MTI1MzY5Ng
youtube_id: K5azzbPxV5M
description: 
chapter: 12
title: import 模块
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - import 的各种方法
---


学习资料:
* 全套[代码](https://github.com/MorvanZhou/tutorials/blob/master/basic/25_import.py){:target="_blank"}





{% include assign-heading.html %}

`import time`  指 import `time`  模块，这个模块可以python自带，也可以是自己安装的，比如以后会用到`numpy`这些模块,需要自己安装。

```python
import time
print(time.localtime())  #这样就可以print 当地时间了
""""
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=23, tm_hour=14, tm_min=12, tm_sec=48, tm_wday=4, tm_yday=358, tm_isdst=0)
""""
```

方法二：`import time as __`,`__`下划线缩写部分可以自己定义，在代码中把time 定义成 `t`.

```python
import time as t
print(t.localtime()) # 需要加t.前缀来引出功能

""""
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=23, tm_hour=14, tm_min=12, tm_sec=48, tm_wday=4, tm_yday=358, tm_isdst=0)
""""

```

方法三：`from time import time,localtime` ,只`import`自己想要的功能.

```python
from time import time, localtime
print(localtime())
print(time())
""""
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=23, tm_hour=14, tm_min=41, tm_sec=38, tm_wday=4, tm_yday=358, tm_isdst=0)

1482475298.709855
""""
```

方法四：`from time import *`  输入模块的所有功能

```python
from time import *
print(localtime())
""""
time.struct_time(tm_year=2016, tm_mon=12, tm_mday=23, tm_hour=14, tm_min=41, tm_sec=38, tm_wday=4, tm_yday=358, tm_isdst=0)
""""

```

