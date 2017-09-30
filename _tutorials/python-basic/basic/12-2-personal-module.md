---
youku_id: XMTU5MjI5MTI1Ng
youtube_id: oYheNUtZpFw
description: 
chapter: 12
title: 自己的模块
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - 自建一个模块
  - 调用自己的模块
  - 模块存储路径说明
---






{% include assign-heading.html %}

这里和视频有点差别，我自己写了另外一个模块，是计算五年复利本息的模块,代码如下：模块写好后保存在默认文件夹：`balance.py`

```python
d=float(input('Please enter what is your initial balance: \n'))
p=float(input('Please input what is the interest rate (as a number): \n'))
d=float(d+d*(p/100))
year=1
while year<=5:
    d=float(d+d*p/100)
    print('Your new balance after year:',year,'is',d)
    year=year+1
print('your final year is',d)
```


{% include assign-heading.html %}

新开一个脚本，`import balance`

```python
import balance

""""
Please enter what is your initial balance:
50000  # 手动输入我的本金
Please input what is the interest rate (as a number):
2.3  #手动输入我的银行利息
Your new balance after year: 1 is 52326.45
Your new balance after year: 2 is 53529.95834999999
Your new balance after year: 3 is 54761.14739204999
Your new balance after year: 4 is 56020.653782067144
Your new balance after year: 5 is 57309.12881905469
your final year is 57309.12881905469
""""
```


{% include assign-heading.html %}

在Mac系统中，下载的python模块会被存储到外部路径`site-packages`，同样，我们自己建的模块也可以放到这个路径，最后不会影响到自建模块的调用。