---
youku_id: XMTY2NTAyNTM0MA
youtube_id: sj9BGXGyLho
title: Save 保存 提取
description: 我们肯定需要保存学习好的 model, 毕竟不能浪费学习的时间和资源. 所以这里讲到了如何保存和提取出已经学习好的 model 参数.
author: Alice
chapter: 3
date: 2016-11-3
post-headings:
  - 要点
  - 导入模块
  - 创建数据－建立模型－激活－训练
  - 保存模型
  - 提取模型
---


学习资料:
  * [代码链接](https://github.com/MorvanZhou/tutorials/tree/master/theanoTUT/theano13_save){:target="_blank"}

{% include assign-heading.html %}

今天学习如何保存神经网络，以方便日后可以直接提取使用。

保存的方式是我们可以先把神经网络的参数，比如说 weights 还有 bias 保存起来，再重新定义神经网络的结构，使用模型的时候需要把参数 set 到结构中去。

保存和提取的方法是利用 shared 变量的 get 功能，拿出变量值保存到文件中去，
下一次再定义 weights 和 bias 的时候，可以直接把保存好的值放到 shared variable 中去。


本文以 [Classification 分类学习](https://morvanzhou.github.io/tutorials/machine-learning/theano/3-4-classification/){:target="_blank"} 那节的代码为例。




{% include assign-heading.html %}

在引入相关包时，需要用到 pickle， 这是 python 中用来储存文件的一个模块。

```python
import numpy as np
import theano
import theano.tensor as T
import pickle
```

{% include assign-heading.html %}

接下来的 创建数据－建立模型－激活模型－训练模型 都和分类那节课的内容是一样的。

```python
def compute_accuracy(y_target, y_predict):
    correct_prediction = np.equal(y_predict, y_target)
    accuracy = np.sum(correct_prediction)/len(correct_prediction)
    return accuracy

rng = np.random

# set random seed
np.random.seed(100)

N = 400
feats = 784

# generate a dataset: D = (input_values, target_class)
D = (rng.randn(N, feats), rng.randint(size=N, low=0, high=2))

# Declare Theano symbolic variables
x = T.dmatrix("x")
y = T.dvector("y")

# initialize the weights and biases
w = theano.shared(rng.randn(feats), name="w")
b = theano.shared(0., name="b")

# Construct Theano expression graph
p_1 = 1 / (1 + T.exp(-T.dot(x, w) - b))
prediction = p_1 > 0.5
xent = -y * T.log(p_1) - (1-y) * T.log(1-p_1)
cost = xent.mean() + 0.01 * (w ** 2).sum()
gw, gb = T.grad(cost, [w, b])

# Compile
learning_rate = 0.1
train = theano.function(
          inputs=[x, y],
          updates=((w, w - learning_rate * gw), (b, b - learning_rate * gb)))
predict = theano.function(inputs=[x], outputs=prediction)

# Training
for i in range(500):
    train(D[0], D[1])
```

今天重点放在保存和提取模型的部分：

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

把所有的参数放入 `save` 文件夹中，命名文件为 `model.pickle`，以 `wb` 的形式打开并把参数写入进去。

定义 `model＝[]` 用来保存 `weights` 和 `bias`，这里用的是 list 结构保存，也可以用字典结构保存，提取值时用 `get_value()` 命令。

再用 `pickle.dump` 把 `model` 保存在 `file` 中。

可以通过 `print(model[0][:10])` 打印出保存的 `weights` 的前 10 个数，方便后面提取模型时检查是否保存成功。还可以打印 `accuracy` 看准确率是否一样。


```python
# save model
with open('save/model.pickle', 'wb') as file:
    model = [w.get_value(), b.get_value()]
    pickle.dump(model, file)
    print(model[0][:10])
    print("accuracy:", compute_accuracy(D[1], predict(D[0])))

"""
[-0.15707296  0.14590665 -0.08451091 -0.12594476 -0.13424085 -0.33887753
  0.12650858  0.20702686  0.0549835   0.29920542]
accuracy: 1.0
"""
```

执行上述代码后可以看到 `save` 文件夹中生成了一个 `model.pickle` 的文件。


{% include assign-heading.html %}

接下来提取模型时，提前把代码中 `# Training` 和 `# save model` 两部分注释掉，即相当于只是通过 创建数据－建立模型－激活模型 构建好了新的模型结构，下面要通过调用存好的参数来进行预测。

以 `rb` 的形式读取 `model.pickle` 文件加载到 `model` 变量中去，

然后用 `set_value` 命令把 `model` 的第 0 位存进 `w`，第 1 位存进 `b` 中。

同样可以打印出 `weights` 的前 10 位和 `accuracy`，来对比之前的结果，可以发现结果完全一样。


```python
# load model
with open('save/model.pickle', 'rb') as file:
    model = pickle.load(file)
    w.set_value(model[0])
    b.set_value(model[1])
    print(w.get_value()[:10])
    print("accuracy:", compute_accuracy(D[1], predict(D[0])))
    
"""
[-0.15707296  0.14590665 -0.08451091 -0.12594476 -0.13424085 -0.33887753
  0.12650858  0.20702686  0.0549835   0.29920542]
accuracy: 1.0
"""
```

以上就是保存和提取的过程。