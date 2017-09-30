---
youku_id: XMTU4NTIwMjA2OA
youtube_id: TBemVnOITjk
description: 
chapter: 8
title: 读写文件 2
date: 2016-11-3

author: Huanyu Mao
post-headings:
  - 给文件增加内容
  - 总结
---




{% include assign-heading.html %}

我们先保存一个已经有3行文字的 "my file.txt" 文件, 文件的内容如下:

```
This is my first test. 
This is the second line.
This the third
```

然后使用添加文字的方式给这个文件添加一行 "This is appended file.", 并将这行文字储存在 `append_file` 里，注意`\n`的适用性:

```python
append_text='\nThis is appended file.'  # 为这行文字提前空行 "\n"
my_file=open('my file.txt','a')   # 'a'=append 以增加内容的形式打开
my_file.write(append_text)
my_file.close()

""""
This is my first test.
This is the second line.
This the third line.
This is appended file.
""""
#运行后再去打开文件，会发现会增加一行代码中定义的字符串
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

- 掌握 append 的用法 ：`open('my file.txt','a')` 打开类型为 `a` ，`a` 即表示 append
- 可以思考，如果用 `w` 形式打开，运行后会发生什么呢？

