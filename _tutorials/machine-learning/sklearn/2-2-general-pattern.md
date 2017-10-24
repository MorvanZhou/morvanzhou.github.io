---
youku_id: XMTYxMzg0NzE5Mg
youtube_id: EvV99YhSsJU
description: 我们用 sklearn 自己的 iris 的例子实现了一次 KNeighborsClassifier 学习. 说明了所有 sklearn的编程结构和过程都是极度类似的.所以只需要先定义 用什么model学习,然后再 model.fit(数据), 这样 model 就能从数据中学到东西. 最后还可以用 model.predict() 来预测值.
chapter: 2
author: Alice
title: 通用学习模式
date: 2016-11-3
post-headings:
  - 要点
  - 导入模块
  - 创建数据
  - 建立模型－训练－预测
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk4_learning_pattern.py){:target="_blank"}
  

{% include assign-heading.html %}


Sklearn 把所有机器学习的模式整合统一起来了，学会了一个模式就可以通吃其他不同类型的学习模式。

例如，分类器，

Sklearn 本身就有很多数据库，可以用来练习。
以 Iris 的数据为例，这种花有四个属性，花瓣的长宽，茎的长宽，根据这些属性把花分为三类。

我们要用 分类器 去把四种类型的花分开。

{% include tut-image.html image-name="2_2_1.png" %}

今天用 `KNN classifier`，就是选择几个临近点，综合它们做个平均来作为预测值。



{% include assign-heading.html %}


```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}


加载 `iris` 的数据，把属性存在 `X`，类别标签存在 `y`：

```python
iris = datasets.load_iris()
iris_X = iris.data
iris_y = iris.target
```

观察一下数据集，`X` 有四个属性，`y` 有 0，1，2 三类：

```python
print(iris_X[:2, :])
print(iris_y)

"""
[[ 5.1  3.5  1.4  0.2]
 [ 4.9  3.   1.4  0.2]]
[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2 2 2 2 2 2 2
 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
 2 2]
 """
```

把数据集分为训练集和测试集，其中 `test_size=0.3`，即测试集占总数据的 30%：

```python
X_train, X_test, y_train, y_test = train_test_split(
    iris_X, iris_y, test_size=0.3)
```

可以看到分开后的数据集，顺序也被打乱，这样更有利于学习模型：

```python
print(y_train)

"""
[2 1 0 1 0 0 1 1 1 1 0 0 1 2 1 1 1 0 2 2 1 1 1 1 0 2 2 0 2 2 2 2 2 0 1 2 2
 2 2 2 2 0 1 2 2 1 1 1 0 0 1 2 0 1 0 1 0 1 2 2 0 1 2 2 2 1 1 1 1 2 2 2 1 0
 1 1 0 0 0 2 0 1 0 0 1 2 0 2 2 0 0 2 2 2 1 2 0 0 2 1 2 0 0 1 2]
 """
```

{% include assign-heading.html %}


定义模块方式 `KNeighborsClassifier()`，
用 `fit` 来训练 `training data`，这一步就完成了训练的所有步骤，
后面的 `knn` 就已经是训练好的模型，可以直接用来 `predict` 测试集的数据，
对比用模型预测的值与真实的值，可以看到大概模拟出了数据，但是有误差，是不会完完全全预测正确的。

```python
knn = KNeighborsClassifier()
knn.fit(X_train, y_train)
print(knn.predict(X_test))
print(y_test)

"""
[2 0 0 1 2 2 0 0 0 1 2 2 1 1 2 1 2 1 0 0 0 2 1 2 0 0 0 0 1 0 2 0 0 2 1 0 1
 0 0 1 0 1 2 0 1]
[2 0 0 1 2 1 0 0 0 1 2 2 1 1 2 1 2 1 0 0 0 2 1 2 0 0 0 0 1 0 2 0 0 2 1 0 1
 0 0 1 0 1 2 0 1]
 """
```