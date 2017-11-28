---
youku_id: XMjcyMjMxNTI5Mg
youtube_id: TQE4OLSz2BE
bilibili_id: 15991621
chapter: 6
title: Deep Deterministic Policy Gradient (DDPG) (Tensorflow)
thumbnail: "/static/thumbnail/rl/6.2_DDPG.jpg"
publish-date: 2017-04-22
description: "一句话概括 DDPG:
Google DeepMind 提出的一种使用 Actor Critic 结构, 但是输出的不是行为的概率, 而是具体的行为,
用于连续动作 (continuous action) 的预测. DDPG 结合了之前获得成功的 DQN 结构, 提高了 Actor Critic 的稳定性和收敛性.
因为 DDPG 和 DQN 还有 Actor Critic 很相关,
所以最好这两者都了解下, 对于学习 DDPG 很有帮助. 我的教程链接都能在上面的学习资料中找到.
下面是这节内容的效果提前看:"
post-headings:
  - 要点
  - 算法
  - 主结构
  - Actor Critic
  - 记忆库 Memory
  - 每回合算法
  - 简化版代码(录完视频后发现了小错误, 重写了代码)
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py){:target="_blank"}
  * [修改版代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG_update.py){:target="_blank"}
  * [什么是 Deep Deterministic Policy Gradient 短视频]({% link _tutorials/machine-learning/ML-intro/4-09-DDPG.md %})
  * [什么是 Policy Gradient 短视频]({% link _tutorials/machine-learning/ML-intro/4-07-PG.md %})
  * 论文 [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971){:target="_blank"}
  * [我的 DQN 教程]({% link _tutorials/machine-learning/reinforcement-learning/4-1-DQN1.md %})
  * [我的 Actor Critic 教程]({% link _tutorials/machine-learning/reinforcement-learning/6-1-actor-critic.md %})
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})

{% include assign-heading.html %}

**一句话概括 DDPG:**
Google DeepMind 提出的一种使用 `Actor Critic` 结构, 但是输出的不是行为的概率, 而是具体的行为,
用于连续动作 (continuous action) 的预测. `DDPG` 结合了之前获得成功的 `DQN` 结构, 提高了 `Actor Critic` 的稳定性和收敛性.

因为 `DDPG` 和 `DQN` 还有 `Actor Critic` 很相关,
所以最好这两者都了解下, 对于学习 `DDPG` 很有帮助. 我的教程链接都能在上面的学习资料中找到.

下面是这节内容的效果提前看:

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/Pendulum DDPG.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>




{% include assign-heading.html %}

`DDPG` 的算法实际上就是一种 `Actor Critic`, 我在[上一篇]({% link _tutorials/machine-learning/reinforcement-learning/6-1-actor-critic.md %})中简短地介绍了 `Actor Critic` 的算法.
不太清楚的同学先去看看上一篇吧.

{% include tut-image.html image-name="6-2-0.png" %}

关于 `Actor` 部分, 他的参数更新同样会涉及到 `Critic`, 上面是关于 `Actor` 参数的更新,
它的前半部分 `grad[Q]` 是从 `Critic` 来的, 这是在说: **这次 `Actor` 的动作要怎么移动, 才能获得更大的 `Q`**,
而后半部分 `grad[u]` 是从 `Actor` 来的, 这是在说: **`Actor` 要怎么样修改自身参数, 使得 `Actor` 更有可能做这个动作**.
所以两者合起来就是在说: **`Actor` 要朝着更有可能获取大 `Q` 的方向修改动作参数了**.


{% include tut-image.html image-name="6-2-1.png" %}

上面这个是关于 `Critic` 的更新, 它借鉴了 `DQN` 和 `Double Q learning` 的方式,
有两个计算 `Q` 的神经网络, `Q_target` 中依据下一状态, 用 `Actor` 来选择动作, 而这时的 `Actor`
也是一个 `Actor_target` (有着 Actor 很久之前的参数). 使用这种方法获得的 `Q_target` 能像 `DQN`
那样切断相关性, 提高收敛性.


{% include assign-heading.html %}

**注意, 录视频的时候代码有个地方有小错误, 以下部分和视频中有些地方不同, 特别是计算 `Actor` 更新的时候.
 所以请以文字描述中的为准.**

我们用 Tensorflow 搭建神经网络, 主结构可以见这个 tensorboard 的出来的图.

{% include tut-image.html image-name="6-2-2.png" %}

看起来很复杂吧, 没关系, 我们一步步来, 拆开来看就容易了. 首先看看 `Actor`
和 `Critic` 中各有什么结构.

{% include tut-image.html image-name="6-2-3.png" %}

其搭建的代码部分在这 (如果想一次性看全部, 请去我的[Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py){:target="_blank"}):

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
            self.a = a  # 这个 a 是来自 Actor 的, 但是 self.a 在更新 Critic 的时候是之前选择的 a 而不是来自 Actor 的 a.
            self.q = self._build_net(S, self.a, 'eval_net', trainable=True)
            # 这个网络不及时更新参数, 用于给出 Actor 更新参数时的 Gradient ascent 强度
            self.q_ = self._build_net(S_, a_, 'target_net', trainable=False)
```



{% include google-in-article-ads.html %}

{% include assign-heading.html %}

有了对 `Actor Critic` 每个里面各两个神经网络结构的了解, 我们再来具体看看他们是如何进行交流,
传递信息的. 我们从 `Actor` 的学习更新方式开始说起.

{% include tut-image.html image-name="6-2-4.png" %}

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
    opt = tf.train.AdamOptimizer(-self.lr)  # 负的学习率为了使我们计算的梯度往上升, 和 Policy Gradient 中的方式一个性质
    self.train_op = opt.apply_gradients(zip(self.policy_grads, self.e_params)) # 对 eval_net 的参数更新
```

同时下面也提到的传送给 `Actor` 的 `a_grad` 应该用 Tensorflow 怎么计算. 这个 `a_grad`
是 `Critic` class 里面的, 这个 `a` 是来自 `Actor` 根据 `S` 计算而来的:

```python
with tf.variable_scope('a_grad'):
    self.a_grads = tf.gradients(self.q, a)[0]   # dQ/da
```


而在 `Critic` 中, 我们用的东西简单一点.

{% include tut-image.html image-name="6-2-5.png" %}

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
critic = Critic(..., actor.a, actor.a_)  # 将 actor 同它的 eval_net/target_net 产生的 a/a_ 传给 Critic
actor.add_grad_to_graph(critic.a_grads) # 将 critic 产出的 dQ/da 加入到 Actor 的 Graph 中去
```

同样, 如果你觉得只看部分代码不舒服, [这里有全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py){:target="_blank"}.

{% include assign-heading.html %}

以下是关于类似于 `DQN` 中的记忆库代码, 我们用一个 `class` 来建立.
关于 `Memory` 的详细算法, 请直接去我的 [Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py){:target="_blank"} 中看, 这样更简单.

```python
class Memory(object):
    def __init__(self, capacity, dims):
        """用 numpy 初始化记忆库"""

    def store_transition(self, s, a, r, s_):
        """保存每次记忆在 numpy array 里"""

    def sample(self, n):
        """随即从记忆库中抽取 n 个记忆进行学习"""
```

{% include assign-heading.html %}

这里的回合算法只提到了最重要的部分, 省掉了一些没必要的, 有助理解.
如果想一次性看到全部代码, 请去我的 [Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG.py){:target="_blank"}

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
            actor.learn(b_s)

        s = s_

        if j == MAX_EP_STEPS-1:
            break
```

我也用这套 DDPG 测试过自己写的机器手臂的环境, 发现效果也还行. 有兴趣的朋友可以[看到这里](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/experiments/Robot_arm){:target="_blank"}.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/experiment_arm.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

有很多人留言说想要我做一个关于这个机器手臂的教程, 不负众望, 你可以在[这里]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
看到我怎么从零开始, 手写环境, debug 测试, 来制作一个强化学习的机器手臂.

{% include assign-heading.html %}

后来我在回过头来看代码, 结果发现计算 `Actor` 更新时有点小问题, 所以就修改了之前的代码.
但是修改后我觉得.. 代码变得累赘了, 所以我觉得再重写一个, 简化所有流程.
能看到这一个板块的朋友们有没有感到绝望(MD 看了那么久上面的代码, 结果有个更简单的). 哈哈,没关系.
学习代码和技术不要嫌多. 所以[代码就直接看](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/9_Deep_Deterministic_Policy_Gradient_DDPG/DDPG_update.py){:target="_blank"}吧, 相信有了上面的了解, 看这份代码会比较容易.
