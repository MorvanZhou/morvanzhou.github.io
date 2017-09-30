---
youku_id: XMTU4NzI5NTYzMg
youtube_id: FCxiBnAOaJk
description: 
chapter: 11
title: list 列表
date: 2016-11-3

author: Hao
post-headings:
  - List 添加
  - List 移除
  - List 索引
  - List 排序
---



{% include assign-heading.html %}

列表是一系列有序的数列，有一系列自带的功能， 例如：

```python
a = [1,2,3,4,1,1,-1]
a.append(0)  # 在a的最后面追加一个0
print(a)
# [1, 2, 3, 4, 1, 1, -1, 0]
```

在指定的地方添加项：

```python
a = [1,2,3,4,1,1,-1]
a.insert(1,0) # 在位置1处添加0
print(a)
# [1, 0, 2, 3, 4, 1, 1, -1]
```


{% include assign-heading.html %}

删除项：

```python
a = [1,2,3,4,1,1,-1]
a.remove(2) # 删除列表中第一个出现的值为2的项
print(a)
# [1, 3, 4, 1, 1, -1]
```


{% include assign-heading.html %}

显示特定位：

```python
a = [1,2,3,4,1,1,-1]
print(a[0])  # 显示列表a的第0位的值
# 1

print(a[-1]) # 显示列表a的最末位的值
# -1

print(a[0:3]) # 显示列表a的从第0位 到 第2位(第3位之前) 的所有项的值
# [1, 2, 3]

print(a[5:])  # 显示列表a的第5位及以后的所有项的值
# [1, -1]

print(a[-3:]) # 显示列表a的倒数第3位及以后的所有项的值
# [1, 1, -1]
```

打印列表中的某个值的索引(index):

```python
a = [1,2,3,4,1,1,-1]
print(a.index(2)) # 显示列表a中第一次出现的值为2的项的索引
# 1
```

统计列表中某值出现的次数：

```python
a = [4,1,2,3,4,1,1,-1]
print(a.count(-1))
# 1
```


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

对列表的项排序：

```python
a = [4,1,2,3,4,1,1,-1]
a.sort() # 默认从小到大排序
print(a)
# [-1, 1, 1, 1, 2, 3, 4, 4]

a.sort(reverse=True) # 从大到小排序
print(a)
# [4, 4, 3, 2, 1, 1, 1, -1]
```