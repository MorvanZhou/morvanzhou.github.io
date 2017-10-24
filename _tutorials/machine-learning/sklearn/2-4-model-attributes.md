---
youku_id: XMTYxNjU3MTQzMg
youtube_id: d2BMirIToF4
description: sklearn 的 model 属性和功能都是高度统一的. 你可以运用到这些属性查看 model 的参数和值等等.
chapter: 2
title: sklearn 常用属性与功能
author: Alice
date: 2016-11-3
post-headings:
  - 训练和预测
  - 参数和分数
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk6_model_attribute_method.py){:target="_blank"}
  
  
上次学了  `Sklearn` 中的 `data sets`，今天来看 Model 的属性和功能。

这里以 `LinearRegressor` 为例，所以先导入包，数据，还有模型。

```python
from sklearn import datasets
from sklearn.linear_model import LinearRegression

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_y = loaded_data.target

model = LinearRegression()
```


{% include assign-heading.html %}


接下来 `model.fit` 和 `model.predict` 就属于 Model 的功能，用来训练模型，用训练好的模型预测。

```python
model.fit(data_X, data_y)

print(model.predict(data_X[:4, :]))

"""
[ 30.00821269  25.0298606   30.5702317   28.60814055]
"""
```

{% include assign-heading.html %}

然后，`model.coef_` 和 `model.intercept_ ` 属于 Model 的属性，
例如对于 `LinearRegressor` 这个模型，这两个属性分别输出模型的斜率和截距（与y轴的交点）。

```python
print(model.coef_)
print(model.intercept_)


"""
[ -1.07170557e-01   4.63952195e-02   2.08602395e-02   2.68856140e+00
  -1.77957587e+01   3.80475246e+00   7.51061703e-04  -1.47575880e+00
   3.05655038e-01  -1.23293463e-02  -9.53463555e-01   9.39251272e-03
  -5.25466633e-01]
36.4911032804
"""
```

{% include google-in-article-ads.html %}

`model.get_params()` 也是功能，它可以取出之前定义的参数。

```python
print(model.get_params())


"""
{'copy_X': True, 'normalize': False, 'n_jobs': 1, 'fit_intercept': True}
"""
```

`model.score(data_X, data_y)` 它可以对 Model 用 `R^2` 的方式进行打分，输出精确度。关于 `R^2 coefficient of determination` 可以查看 [wiki](https://en.wikipedia.org/wiki/Coefficient_of_determination){:target="_blank"}

```python
print(model.score(data_X, data_y)) # R^2 coefficient of determination

"""
0.740607742865
"""
```

