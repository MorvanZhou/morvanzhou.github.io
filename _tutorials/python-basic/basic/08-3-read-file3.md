---
youku_id: XMTU4NTIxODg3Ng
youtube_id: pz3I-9MgxGo
description: 
chapter: 8
title: 读写文件 3
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - 读取文件内容 file.read()
  - 按行读取 file.readline()
  - 读取所有行 file.readlines()
---




{% include assign-heading.html %}

使用 `file.read()` 能够读取到文本的所有内容.

```python
file= open('my file.txt','r') 
content=file.read()  
print(content)

""""
This is my first test.
This is the second line.
This the third line.
This is appended file.    
""""
```

{% include assign-heading.html %}

如果想在文本中一行行的读取文本, 可以使用 `file.readline()`, `file.readline()` 读取的内容和你使用的次数有关,
使用第二次的时候, 读取到的是文本的第二行, 并可以以此类推:

```python
file= open('my file.txt','r') 
content=file.readline()  # 读取第一行
print(content)

""""
This is my first test.
""""

second_read_time=file.readline()  # 读取第二行
print(second_read_time)

"""
This is the second line.
"""
```


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

如果想要读取所有行, 并可以使用像 `for` 一样的迭代器迭代这些行结果, 我们可以使用 `file.readlines()`, 将每一行的结果存储在 `list` 中, 方便以后迭代.

```python
file= open('my file.txt','r') 
content=file.readlines() # python_list 形式
print(content)

""""
['This is my first test.\n', 'This is the second line.\n', 'This the third line.\n', 'This is appended file.']
""""

# 之后如果使用 for 来迭代输出:
for item in content:
    print(item)
    
"""
This is my first test.

This is the second line.

This the third line.

This is appended file.
"""
```



