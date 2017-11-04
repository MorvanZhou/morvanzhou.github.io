---
youku_id: XMTc4MDI4NjIyNA
youtube_id: e-ICAuGXw7k
bilibili_id: 16014874
title: Save & reload 保存提取
description: "保存 Keras model 的时候需要安装h5py这个模块. 不然会不成功. 今天学习如何保存神经网络，这样以后想要用的时候直接提取就可以。"
author: Alice
publish-date: 2016-10-30
chapter: 3
thumbnail: "/static/thumbnail/keras/10save.jpg"
post-headings:
  - 训练模型
  - 保存模型
  - 导入模型并应用
---

学习资料:
  * [代码链接](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/10-save.py){:target="_blank"}
  
今天学习如何保存神经网络，这样以后想要用的时候直接提取就可以。


 {% include assign-heading.html %}

下面的导入数据和训练模型用的是之前讲过的回归模型的例子，今天要做的是如何保存这个模型。

``` python
import numpy as np
np.random.seed(1337)  # for reproducibility

from keras.models import Sequential
from keras.layers import Dense
from keras.models import load_model

# create some data
X = np.linspace(-1, 1, 200)
np.random.shuffle(X)    # randomize the data
Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200, ))
X_train, Y_train = X[:160], Y[:160]     # first 160 data points
X_test, Y_test = X[160:], Y[160:]       # last 40 data points
model = Sequential()
model.add(Dense(output_dim=1, input_dim=1))
model.compile(loss='mse', optimizer='sgd')
for step in range(301):
    cost = model.train_on_batch(X_train, Y_train)

```



 {% include assign-heading.html %}

训练完模型之后，可以打印一下预测的结果，接下来就保存模型。

保存的时候只需要一行代码 `model.save`，再给它加一个名字就可以用 `h5` 的格式保存起来。

这里注意，需要已经安装了 `HDF5` 这个模块。

保存完模型之后，删掉它，后面可以来比较是否成功的保存。

```python
# save
print('test before save: ', model.predict(X_test[0:2]))
model.save('my_model.h5')   # HDF5 file, you have to pip3 install h5py if don't have it
del model  # deletes the existing model

"""
test before save:  [[ 1.87243938] [ 2.20500779]]
"""
```

{% include google-in-article-ads.html %}

 {% include assign-heading.html %}

导入保存好的模型，再执行一遍预测，与之前预测的结果比较，可以发现结果是一样的。

```python
# load
model = load_model('my_model.h5')
print('test after load: ', model.predict(X_test[0:2]))

"""
test after load:  [[ 1.87243938] [ 2.20500779]]
"""
```


另外还有其他保存模型并调用的方式，第一种是只保存权重而不保存模型的结构。

```python
# save and load weights
model.save_weights('my_model_weights.h5')
model.load_weights('my_model_weights.h5')
```

第二种是用 `model.to_json` 保存完结构之后，然后再去加载这个`json_string`。 

```python
# save and load fresh network without trained weights
from keras.models import model_from_json
json_string = model.to_json()
model = model_from_json(json_string)
```