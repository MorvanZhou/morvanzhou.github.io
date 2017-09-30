---
youku_id: XMTU4NzIzNDI0NA
youtube_id: g_o8y-LTqos
description: 
chapter: 10
title: input 输入
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - input
  - input扩展
---




{% include assign-heading.html %}

`variable=input()`  表示运行后，可以在屏幕中输入一个数字，该数字会赋值给自变量。看代码：

```python
a_input=input('please input a number:')
print('this number is:',a_input)

''''
please input a number:12 #12 是我在硬盘中输入的数字
this number is: 12
''''
```

 `input()`应用在`if`语句中.

在下面代码中，需要将`input()` 定义成整型，因为在`if`语句中自变量 `a_input` 对应的是`1` and `2` 整数型。输入的内容和判断句中对应的内容格式应该一致。

也可以将`if`语句中的`1and2` 定义成字符串，其中区别请读者自定写入代码查看。

```python
a_input=int(input('please input a number:'))#注意这里要定义一个整数型
if a_input==1:
    print('This is a good one')
elif a_input==2:
    print('See you next time')
else:
    print('Good luck')

""""
please input a number:1   #input 1
This is a good one

please input a number:2   #input 2
See you next time

please input a number:3   #input 3 or other number
Good luck
""""
```


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

用`input()`来判断成绩

```python
score=int(input('Please input your score: \n'))
if score>=90:
   print('Congradulation, you get an A')
elif score >=80:
    print('You get a B')
elif score >=70:
    print('You get a C')
elif score >=60:
    print('You get a D')
else:
    print('Sorry, You are failed ')

""""
Please input your score:
100   #手动输入
Congradulation, you get an A
""""

```

