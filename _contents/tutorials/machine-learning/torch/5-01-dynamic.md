---
youku_id:
youtube_id:
title: 为什么 Torch 是动态的
publish-date:
thumbnail: "/static/thumbnail/torch/5.1 dynamic.jpg"
chapter: 5
---

* 学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/tutorials/blob/master/pytorchTUT/12_why_torch_dynamic_graph.py)
  * [PyTorch 官网](http://pytorch.org/)

听说过 Torch 的人都听说了 torch 是动态的, 那他的动态到底是什么呢? 我们用一个 RNN 的例子来展示一下动态计算到底长什么样.


#### 本节内容包括:

* [动态?静态?](#dynamic)
* [动态RNN](#RNN)



<h4 class="tut-h4-pad" id="dynamic">动态?静态?</h4>

对比静态动态, 我们就得知道谁是静态的. 在流行的神经网络模块中, Tensorflow 就是最典型的静态计算模块.
下图是一种我在[强化学习教程](https://morvanzhou.github.io/tutorials/machine-learning/reinforcement-learning/)中的 Tensorflow 计算图.
也就是说, Tensorflow 是先搭建好这样一个计算系统, 一旦搭建好了, 就不能改动了, 所有的计算都会在这种图中流动, 当然很多情况, 这样就够了, 我们不需要改动什么结构.
不动结构当然可以提高效率. 但是一旦计算流程不是静态的, 计算图要变动. 最典型的例子就是 RNN, 有时候 RNN 的 time step 不会一样, 或者在 training 和 testing 的时候,
步长也不一样, 这时, Tensorflow 就头疼了, Tensorflow 的人也头疼了. 哈哈, 如果用一个动态计算图的 Torch, 我们就好理解多了.

<img class="course-image" src="/static/results/rl/6-2-2.png">



<h4 class="tut-h4-pad" id="RNN">动态RNN</h4>

我们拿 [这一节内容的 RNN]({% link _contents/tutorials/machine-learning/torch/4-03-RNN-regression.md %})
来解释动态计算图. 那节内容的[代码在这](https://github.com/MorvanZhou/tutorials/blob/master/pytorchTUT/11_RNN_regressor.py).

```python
...

######################## 前面代码都一样, 下面开始不同 #########################

################ 那节内容的代码结构 (静态 time step) ##########
for step in range(60):
    start, end = step * np.pi, (step+1)*np.pi   # time steps 都是一样长的
    # use sin predicts cos
    steps = np.linspace(start, end, 10, dtype=np.float32)
    ...


################ 这节内容修改代码 (动态 time step) #########
step = 0
for i in range(60):
    dynamic_steps = np.random.randint(1, 4)  # 随机 time step 长度
    start, end = step * np.pi, (step + dynamic_steps) * np.pi  # different time steps length
    step += dynamic_steps

    # use sin predicts cos
    steps = np.linspace(start, end, 10 * dynamic_steps, dtype=np.float32)

#######################  这下面又一样了 ###########################
    print(len(steps))   # print how many time step feed to RNN

    x_np = np.sin(steps)    # float32 for converting torch FloatTensor
    y_np = np.cos(steps)
    ...

"""
输出的动态time step 长
30
30
10
30
20
30
"""
```

进过这样的折腾, torch 还能 handle 住, 已经很不容易啦. 所以当你想要处理这些动态计算图的时候, Torch 还是你首选的神经网络模块.

所以这也就是在我 [github 代码](https://github.com/MorvanZhou/tutorials/blob/master/pytorchTUT/12_why_torch_dynamic_graph.py) 中的每一步的意义啦.


