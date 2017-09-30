---
youku_id: XMTU4NTE4OTA0OA
youtube_id: hkMQaooXkgs
description: 
chapter: 8
title: 读写文件 1
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - \n 换行命令
  - open 读文件方式
  - \t tab 对齐

---




{% include assign-heading.html %}

定义 `text` 为字符串, 并查看使用 `\n` 和不适用 `\n` 的区别:

```python
text='This is my first test. This is the second line. This the third '
print(text)  # 无换行命令

"""
This is my first test. This is the second line. This the third
"""

text='This is my first test.\nThis is the second line.\nThis the third line'
print(text)   # 输入换行命令\n，要注意斜杆的方向。注意换行的格式和c++一样

"""
This is my first test.
This is the second line.
This the third line
"""
```



{% include assign-heading.html %}

使用 `open` 能够打开一个文件, `open` 的第一个参数为文件名和路径 'my file.txt', 第二个参数为将要以什么方式打开它, 比如 `w` 为可写方式.
如果计算机没有找到 'my file.txt' 这个文件, `w` 方式能够创建一个新的文件, 并命名为 `my file.txt`

```python
my_file=open('my file.txt','w')   #用法: open('文件名','形式'), 其中形式有'w':write;'r':read.
my_file.write(text)               #该语句会写入先前定义好的 text
my_file.close()                   #关闭文件
```


{% include google-in-article-ads.html %}


{% include assign-heading.html %}

使用 `\t` 能够达到 `tab` 对齐的效果: 

```python
text='\tThis is my first test.\n\tThis is the second line.\n\tThis is the third line'
print(text)  #延伸 使用 \t 对齐

"""
	This is my first test.
	This is the second line.
	This is the third line
"""
```




