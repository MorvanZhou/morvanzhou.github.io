---
youku_id: XMTYxMDk4OTk5Mg
youtube_id: GXHVyjGhFuc
description: 
chapter: 13
title: pickle 保存数据
date: 2016-11-3
post-headings:
  - pickle 保存
  - pickle 提取
---

学习资料:
* 全套[代码](https://github.com/MorvanZhou/tutorials/blob/master/basic/34_pickle.py){:target="_blank"}

{% include assign-heading.html %}

pickle 是一个 python 中, 压缩/保存/提取 文件的模块. 最一般的使用方式非常简单.
比如下面就是压缩并保存一个字典的方式. 字典和列表都是能被保存的.

```python
import pickle

a_dict = {'da': 111, 2: [23,1,4], '23': {1:2,'d':'sad'}}

# pickle a variable to a file
file = open('pickle_example.pickle', 'wb')
pickle.dump(a_dict, file)
file.close()
```

`wb` 是以写的形式打开 'pickle_example.pickle' 这个文件, 然后 `pickle.dump` 你要保存的东西去这个打开的 `file`.
最后关闭 `file` 你就会发现你的文件目录里多了一个 'pickle_example.pickle' 文件, 这就是那个字典了.


{% include assign-heading.html %}

提取的时候相对简单点, 同样我们以读的形式打开那个文件, 然后 load 进一个 python 的变量.

```python
# reload a file to a variable
with open('pickle_example.pickle', 'rb') as file:
    a_dict1 =pickle.load(file)

print(a_dict1)
```



