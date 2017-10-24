---
youku_id: XMTY2NDI3ODc2NA
youtube_id: ho4ms9gVjKE
title: Classification 分类学习 
description: 这节我们说到了一很简单的神经网络,甚至还不能算是一个正规的神经网络,不过原理通了,大家就能应用自如啦.这个神经网络只有两层,一个输入,一个输出层,没有隐藏层,不过大家可以根据上次所讲的 Layer class 来自己做练习,加上隐藏层.
author: Alice
chapter: 3
post-headings:
  - 导入模块并创建数据
  - 建立模型
  - 激活模型
  - 训练模型
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/theanoTUT/theano11_classification_nn){:target="_blank"}





{% include assign-heading.html %}

引入需要使用的Python包：

``` python
import numpy as np
import theano
import theano.tensor as T
```


先定义一个功能，用来计算分类问题的准确率，即预测的类别中有多少是和实际类别一样的，计算出百分比。

``` python
def compute_accuracy(y_target, y_predict):
    correct_prediction = np.equal(y_predict, y_target)
    accuracy = np.sum(correct_prediction)/len(correct_prediction)
    return accuracy
```

用 `randn` 随机生成数据集。
`D` 中的 `input_values` 是 400 个样本，784 个feature。
`target_class` 是有两类，0 和 1。
要做的是，用神经网络训练数据学习哪些输入对应 0，哪些对应 1. 

``` python
rng = np.random

N = 400             # training 数据个数
feats = 784         # input 的 feature 数

# 生成随机数: D = (input_values, target_class)
D = (rng.randn(N, feats), rng.randint(size=N, low=0, high=2))
```



{% include google-in-article-ads.html %}

{% include assign-heading.html %}

接下来，定义神经网络。

先定义一个大的图片，编辑好图片的小部件，再把训练数据集放到图片中去自动地训练。

定义 `x` 和 `y`，相当于 placeholder。

``` python
# 定义 x y 容器
x = T.dmatrix("x")
y = T.dvector("y")
```

初始化 `weights` 和 `bias`。
有多少 features 就生成多少个 weights，
今天只是用最基本的 input 和 output 层的神经网络，如果想用 hidden layer 可以参考上一节课的例子。

``` python
# 初始化 weights and biases
W = theano.shared(rng.randn(feats), name="w")
b = theano.shared(0., name="b")
```

定义激活函数，交叉熵。
`p_1` 是用 `sigmoid` 求的概率，输入越小，则概率值越接近 0，越大则越接近 1，等于 0 则值为 0.5.
`p_1 > 0.5` 时，预测值为 True，即为 1。
然后计算针对每个 sample 的交叉熵 `xent`。
再计算整批数据的 `cost`，为了减小 `overfitting`，这里加入了 `L1-正则化`。
接下来可以计算 weights 和 bias 的梯度 `gW, gb`。


``` python
p_1 = T.nnet.sigmoid(T.dot(x, W) + b)   # sigmoid 激励函数
prediction = p_1 > 0.5                  
xent = -y * T.log(p_1) - (1-y) * T.log(1-p_1) # 交叉熵

# xent 也可以使用下面这个达到一样的效果
# xent = T.nnet.binary_crossentropy(p_1, y) 

cost = xent.mean() + 0.01 * (W ** 2).sum()  # l2 正则化
gW, gb = T.grad(cost, [W, b])             
```



{% include assign-heading.html %}


接下来激活网络。

学习率需要小于 1.
接下来定义两个函数 `train` 和 `predict`，方法和上一节课的类似。
`outputs` 可以输出两个 `prediction` 和交叉熵损失的平均值 `xent.mean`。


``` python
learning_rate = 0.1
train = theano.function(
          inputs=[x, y],
          outputs=[prediction, xent.mean()],
          updates=((W, W - learning_rate * gW), (b, b - learning_rate * gb)))
predict = theano.function(inputs=[x], outputs=prediction)

```


{% include assign-heading.html %}

接下来训练模型。
用训练集的 feature 和 target 训练模型，输出预测值和损失 `pred, err`。
每 50 步打印一次损失和准确率。

``` python
# Training
for i in range(500):
    pred, err = train(D[0], D[1])
    if i % 50 == 0:
        print('cost:', err)
        print("accuracy:", compute_accuracy(D[1], predict(D[0])))
```

最后打印出预测值与实际值进行比较。

``` python
print("target values for D:")
print(D[1])
print("prediction on D:")
print(predict(D[0]))

"""
cost: 11.677533008109728
accuracy: 0.52
cost: 6.1946164642562636
accuracy: 0.6175
cost: 3.012375762498935
accuracy: 0.725
cost: 1.3340537876600198
accuracy: 0.8275
cost: 0.4690120202455575
accuracy: 0.9075
...


target values for D:
[1 1 0 1 0 1 0 1 1 1 1 1 .....]

prediction on D:
[1 1 0 1 0 1 0 1 1 1 1 1 .....]
"""
```

