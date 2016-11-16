---
youku_id: XMTYxMzg0NzE5Mg
youtube_id: EvV99YhSsJU
description: 我们用 sklearn 自己的 iris 的例子实现了一次 KNeighborsClassifier 学习. 说明了所有 sklearn的编程结构和过程都是极度类似的.所以只需要先定义 用什么model学习,然后再 model.fit(数据), 这样 model 就能从数据中学到东西. 最后还可以用 model.predict() 来预测值.
chapter: 2
title: 通用学习模式
date: 2016-11-3
---
* 学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk4_learning_pattern.py)
  
我们用 sklearn 自己的 iris 的例子实现了一次 KNeighborsClassifier 学习. 
说明了所有 sklearn的编程结构和过程都是极度类似的.所以只需要先定义
用什么model学习,然后再 model.fit(数据), 这样 model 就能从数据中学到东西. 最后还可以用 model.predict() 来预测值.