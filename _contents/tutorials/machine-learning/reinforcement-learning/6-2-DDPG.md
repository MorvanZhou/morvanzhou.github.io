---
youku_id: XMjcyMjMxNTI5Mg
youtube_id: TQE4OLSz2BE
chapter: 6
title: Deep Deterministic Policy Gradient (DDPG) (Tensorflow)
thumbnail: "/static/thumbnail/rl/16 DDPG.jpg"
publish-date: 2017-04-22
---

* 学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py)
  * [什么是 Deep Deterministic Policy Gradient 短视频]({% link _contents/tutorials/machine-learning/ML-intro/4-09-DDPG.md %})
  * [什么是 Policy Gradient 短视频]({% link _contents/tutorials/machine-learning/ML-intro/4-07-PG.md %})
  * 论文 [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971)
  * [我的 DQN 教程]({% link _contents/tutorials/machine-learning/reinforcement-learning/4-1-DQN1.md %})
  * [我的 Actor Critic 教程]({% link _contents/tutorials/machine-learning/reinforcement-learning/6-1-actor-critic.md %})

**一句话概括 DDPG:**
Google DeepMind 提出的一种使用 `Actor Critic` 结构, 但是输出的不是行为的概率, 而是具体的行为,
用于连续动作 (continuous action) 的预测. `DDPG` 结合了之前获得成功的 `DQN` 结构, 提高了 `Actor Critic` 的稳定性和收敛性.

因为 `DDPG` 和 `DQN` 还有 `Actor Critic` 很相关,
所以最好这两者都了解下, 对于学习 `DDPG` 很有帮助. 我的教程链接都能在上面的学习资料中找到.

下面是这节内容的效果提前看:

<div align="center">
<video width="500" controls loop autoplay muted>
  <source src="/static/results/rl/Pendulum DDPG.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
</div>


#### 本节内容包括:

* [算法](#algorithm)
* [主结构](#main-structure)
* [Actor Critic](#AC)
* [记忆库 Memory](#memory)
* [每回合算法](#episode)


<h4 class="tut-h4-pad" id="algorithm">算法</h4>

`DDPG` 的算法实际上就是一种 `Actor Critic`, 我在[上一篇]({% link _contents/tutorials/machine-learning/reinforcement-learning/6-1-actor-critic.md %})中简短地介绍了 `Actor Critic` 的算法.
不太清楚的同学先去看看上一篇吧.

<img class="course-image" src="/static/results/rl/6-2-0.png">

关于 `Actor` 部分, 他的参数更新同样会涉及到 `Critic`, 上面是关于 `Actor` 参数的更新,
它的前半部分 `grad[Q]` 是从 `Critic` 来的, 这是在说: **这次 `Actor` 的动作要怎么移动, 才能获得更大的 `Q`**,
而后半部分 `grad[u]` 是从 `Actor` 来的, 这是在说: **`Actor` 要怎么样修改自身参数, 使得 `Actor` 更有可能做这个动作**.
所以两者合起来就是在说: **`Actor` 要朝着更有可能获取大 `Q` 的方向修改动作参数了**.


<img class="course-image" src="/static/results/rl/6-2-1.png">

上面这个是关于 `Critic` 的更新, 它借鉴了 `DQN` 和 `Double Q learning` 的方式,
有两个计算 `Q` 的神经网络, `Q_target` 中依据下一状态, 用 `Actor` 来选择动作, 而这时的 `Actor`
也是一个 `Actor_target` (有着 Actor 很久之前的参数). 使用这种方法获得的 `Q_target` 能像 `DQN`
那样切断相关性, 提高收敛性.


<h4 class="tut-h4-pad" id="main-structure">主结构</h4>

我们用 Tensorflow 搭建神经网络, 主结构可以见这个 tensorboard 的出来的图.

<img class="course-image" src="/static/results/rl/6-2-2.png">

看起来很复制吧, 没关系, 我们一步步来, 拆开来看就容易了. 首先看看 `Actor`
和 `Critic` 中各有什么结构.

<img class="course-image" src="/static/results/rl/6-2-3.png">

其搭建的代码部分在这 (如果想一次性看全部, 请去我的[Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py)):

```python
class Actor(object):
    def __init__(self):
        ...
        with tf.variable_scope('Actor'):
            # 这个网络用于及时更新参数
            self.a = self._build_net(S, scope='eval_net', trainable=True)
            # 这个网络不及时更新参数, 用于预测 Critic 的 Q_target 中的 action
            self.a_ = self._build_net(S_, scope='target_net', trainable=False)
        ...

class Critic(object):
    def __init__(self):
        with tf.variable_scope('Critic'):
            # 这个网络是用于及时更新参数
            self.q = self._build_net(S, A, 'eval_net', trainable=True)
            # 这个网络不及时更新参数, 用于给出 Actor 更新参数时的 Gradient ascent 强度
            self.q_ = self._build_net(S_, a_, 'target_net', trainable=False)
```



<h4 class="tut-h4-pad" id="AC">Actor Critic</h4>

有了对 `Actor Critic` 每个里面各两个神经网络结构的了解, 我们再来具体看看他们是如何进行交流,
传递信息的. 我们从 `Actor` 的学习更新方式开始说起.

<img class="course-image" src="/static/results/rl/6-2-4.png">

这张图我们就能一眼看穿 `Actor` 的更新到底基于了哪些东西. 可以看出, 它使用了两个
`eval_net`, 所以 `Actor` class 中用于 train 的代码我们这样写:

```python
with tf.variable_scope('policy_grads'):
    # 这是在计算 (dQ/da) * (da/dparams)
    self.policy_grads = tf.gradients(
        ys=self.a, xs=self.e_params, # 计算 ys 对于 xs 的梯度
        grad_ys=a_grads # 这是从 Critic 来的 dQ/da
    )
with tf.variable_scope('A_train'):
    opt = tf.train.AdamOptimizer(-self.lr/BATCH_SIZE)  # 负的学习率为了使我们计算的梯度往上升, 和 Policy Gradient 中的方式一个性质
    self.train_op = opt.apply_gradients(zip(self.policy_grads, self.e_params)) # 对 eval_net 的参数更新
```

同时下面也提到的传送给 `Actor` 的 `a_grad` 应该用 Tensorflow 怎么计算. 这个 `a_grad`
是 `Critic` class 里面的:

```python
with tf.variable_scope('a_grad'):
    self.a_grads = tf.gradients(self.q, A)[0]   # dQ/da
```


而在 `Critic` 中, 我们用的东西简单一点.

<img class="course-image" src="/static/results/rl/6-2-5.png">

下面就是 `Critic` 更新时的代码了.

```python
# 计算 target Q
with tf.variable_scope('target_q'):
    self.target_q = R + self.gamma * self.q_    # self.q_ 根据 Actor 的 target_net 来的
# 计算误差并反向传递误差
with tf.variable_scope('TD_error'):
    self.loss = tf.reduce_mean(tf.squared_difference(self.target_q, self.q))  # self.q 又基于 Actor 的 target_net
with tf.variable_scope('C_train'):
    self.train_op = tf.train.AdamOptimizer(self.lr).minimize(self.loss)
```

最后我们建立并把 `Actor` 和 `Critic` 融合在一起的时候是这样写的.

```python
actor = Actor(...)
critic = Critic(..., actor.a_)  # 将 actor 同它的 target_net 产生的 a_ 传给 Critic
actor.add_grad_to_graph(critic.a_grads) # 将 critic 产出的 dQ/da 加入到 Actor 的 Graph 中去
```

同样, 如果你觉得只看部分代码不舒服, [这里有全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py).

<h4 class="tut-h4-pad" id="memory">记忆库 Memory</h4>

以下是关于类似于 `DQN` 中的记忆库代码, 我们用一个 `class` 来建立.
关于 `Memory` 的详细算法, 请直接去我的 [Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py) 中看, 这样更简单.

```python
class Memory(object):
    def __init__(self, capacity, dims):
        """用 numpy 初始化记忆库"""

    def store_transition(self, s, a, r, s_):
        """保存每次记忆在 numpy array 里"""

    def sample(self, n):
        """随即从记忆库中抽取 n 个记忆进行学习"""
```

<h4 class="tut-h4-pad" id="episode">每回合算法</h4>

这里的回合算法只提到了最重要的部分, 省掉了一些没必要的, 有助理解.
如果想一次性看到全部代码, 请去我的 [Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py)

```python
var = 3  # 这里初始化一个方差用于增强 actor 的探索性

for i in range(MAX_EPISODES):
    ...
    for j in range(MAX_EP_STEPS):
        ...

        a = actor.choose_action(s)
        a = np.clip(np.random.normal(a, var), -2, 2) # 增强探索性
        s_, r, done, info = env.step(a)

        M.store_transition(s, a, r / 10, s_)   # 记忆库

        if M.pointer > MEMORY_CAPACITY: # 记忆库头一次满了以后
            var *= .9998    # 逐渐降低探索性
            b_M = M.sample(BATCH_SIZE)
            ...   # 将 b_M 拆分成下面的输入信息
            critic.learn(b_s, b_a, b_r, b_s_)
            actor.learn(b_s, b_a)

        s = s_

        if j == MAX_EP_STEPS-1:
            break
```




