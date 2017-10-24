---
youku_id: XMTYxNjgwNjkxNg
youtube_id: 3GxT8n0ShsU
description: normalization 在数据跨度不一的情况下对机器学习有很重要的作用.特别是各种数据属性还会互相影响的情况之下. Scikit-learn 中标准化的语句是 preprocessing.scale() . scale 以后, model 就更能从标准化数据中学到东西.
chapter: 3
title: 正规化 Normalization
date: 2016-11-3
author: Bhan
post-headings:
  - 数据标准化
  - 数据标准化对机器学习成效的影响
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk7_normalization.py){:target="_blank"}
  * 机器学习-简介系列 [特征标准化]({% link _tutorials/machine-learning/ML-intro/3-02-normalization.md %})

由于资料的**偏差**与**跨度**会影响机器学习的成效，因此正规化(标准化)数据可以提升机器学习的成效。首先由例子来讲解:


{% include assign-heading.html %}


```python
from sklearn import preprocessing #标准化数据模块
import numpy as np

#建立Array
a = np.array([[10, 2.7, 3.6],
              [-100, 5, -2],
              [120, 20, 40]], dtype=np.float64)

#将normalized后的a打印出
print(preprocessing.scale(a))
# [[ 0.         -0.85170713 -0.55138018]
#  [-1.22474487 -0.55187146 -0.852133  ]
#  [ 1.22474487  1.40357859  1.40351318]]
```

{% include assign-heading.html %}

加载模块

```python
# 标准化数据模块
from sklearn import preprocessing 
import numpy as np

# 将资料分割成train与test的模块
from sklearn.model_selection import train_test_split

# 生成适合做classification资料的模块
from sklearn.datasets.samples_generator import make_classification 

# Support Vector Machine中的Support Vector Classifier
from sklearn.svm import SVC 

# 可视化数据的模块
import matplotlib.pyplot as plt 
```

{% include google-in-article-ads.html %}

生成适合做Classification数据

```python
#生成具有2种属性的300笔数据
X, y = make_classification(
    n_samples=300, n_features=2,
    n_redundant=0, n_informative=2, 
    random_state=22, n_clusters_per_class=1, 
    scale=100)

#可视化数据
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.show()
```

{% include tut-image.html image-name="3_1_1.png" %}

数据标准化前

标准化前的预测准确率只有`0.477777777778`

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
# 0.477777777778
```

数据标准化后

数据的单位发生了变化, `X` 数据也被压缩到差不多大小范围.

{% include tut-image.html image-name="3_1_2.png" %}

标准化后的预测准确率提升至`0.9`

```python
X = preprocessing.scale(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
clf = SVC()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
# 0.9
```