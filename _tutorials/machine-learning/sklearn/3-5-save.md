---
youku_id: XMTYyOTkwNzA2OA
youtube_id: 8sMZkhWtdaI
description: 总算到了最后一次的课程了, 我们练习好了一个 model 以后总需要保存和再次预测, 所以保存和读取我们的 sklearn model 也是同样重要的一步.
chapter: 3
title: 保存模型
author: Bhan
date: 2016-11-3
post-headings:
  - 使用 pickle 保存
  - 使用 joblib 保存
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk11_save.py){:target="_blank"}


总算到了最后一次的课程了,我们训练好了一个Model 以后总需要保存和再次预测,
所以保存和读取我们的sklearn model也是同样重要的一步。这次主要介绍两种保存Model的模块`pickle`与`joblib`。


{% include assign-heading.html %}

首先简单建立与训练一个`SVC`Model。

```python
from sklearn import svm
from sklearn import datasets

clf = svm.SVC()
iris = datasets.load_iris()
X, y = iris.data, iris.target
clf.fit(X,y)
```

使用`pickle`来**保存**与**读取**训练好的Model。
(若忘记什么是`pickle`，可以回顾[13.8 pickle 保存数据]({% link _tutorials/python-basic/basic/13-08-pickle.md %})视频。)

```python
import pickle #pickle模块

#保存Model(注:save文件夹要预先建立，否则会报错)
with open('save/clf.pickle', 'wb') as f:
    pickle.dump(clf, f)

#读取Model
with open('save/clf.pickle', 'rb') as f:
    clf2 = pickle.load(f)
    #测试读取后的Model
    print(clf2.predict(X[0:1]))

# [0]
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}


`joblib`是`sklearn`的外部模块。

```python
from sklearn.externals import joblib #jbolib模块

#保存Model(注:save文件夹要预先建立，否则会报错)
joblib.dump(clf, 'save/clf.pkl')

#读取Model
clf3 = joblib.load('save/clf.pkl')

#测试读取后的Model
print(clf3.predict(X[0:1]))

# [0]
```

最后可以知道`joblib`在使用上比较容易，读取速度也相对`pickle`快。
