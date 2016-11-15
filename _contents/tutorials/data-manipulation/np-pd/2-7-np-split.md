---
youku_id: XMTU4ODcyODMwMA
youtube_id: o1j-biEc1Pc
title: Numpy array 分割
description: 


date: 2016-11-3
chapter: 2
---
* 学习资料:
  * [相关代码]()

numpy array 同样是可以进行分割的,
包括横向和纵向分割:
A = np.arange(12).reshape((3,4))

print(np.split(A, 4, axis=1))
print(np.vsplit(A,3))
print(np.array_split(A, 3, axis=1))   # 不等分割