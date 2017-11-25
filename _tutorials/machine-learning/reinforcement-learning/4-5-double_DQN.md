---
youku_id: XMjYxMTA1NzkwOA
youtube_id: TjAEpfE8A64
bilibili_id: 16364954
chapter: 4
title: Double DQN (Tensorflow)
publish-date: 2017-03-07
thumbnail: "/static/thumbnail/rl/4.5_DDQN.jpg"
description: "接下来我们说说为什么会有 Double DQN 这种算法.
所以我们从 Double DQN 相对于 Natural DQN (传统 DQN) 的优势说起.
一句话概括, DQN 基于 Q-learning, Q-Learning 中有 Qmax, Qmax
会导致 Q现实 当中的过估计 (overestimate). 而 Double DQN 就是用来解决过估计的.
在实际问题中, 如果你输出你的 DQN 的 Q 值, 可能就会发现, Q 值都超级大. 这就是出现了 overestimate."
post-headings:
  - 要点
  - Double DQN 算法
  - 更新方法
  - 记录 Q 值
  - 对比结果
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/5.1_Double_DQN){:target="_blank"}
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 论文 [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461){:target="_blank"}

{% include assign-heading.html %}

**本篇教程是基于 Deep Q network (DQN) 的选学教程.
以下教程缩减了在 DQN 方面的介绍, 着重强调 Double DQN 和 DQN 在代码上不同的地方.
所以还没了解 DQN 的同学们, 有关于 DQN 的知识,
请从 [这个视频]({% link _tutorials/machine-learning/ML-intro/4-06-DQN.md %})
和 [这个Python教程]({% link _tutorials/machine-learning/reinforcement-learning/4-1-DQN1.md %}) 开始学习.**

接下来我们说说为什么会有 Double DQN 这种算法.
所以我们从 Double DQN 相对于 Natural DQN (传统 DQN) 的优势说起.

一句话概括, DQN 基于 Q-learning, Q-Learning 中有 `Qmax`, `Qmax`
会导致 `Q现实` 当中的过估计 (overestimate). 而 Double DQN 就是用来解决过估计的.
在实际问题中, 如果你输出你的 DQN 的 Q 值, 可能就会发现, Q 值都超级大. 这就是出现了 overestimate.

这次的 Double DQN 的算法基于的是 OpenAI Gym 中的 `Pendulum` 环境. 如果还不了解如何使用
OpenAI 的话, 这里有[我的一个教程]({% link _tutorials/machine-learning/reinforcement-learning/4-4-gym.md %}).
以下就是这次的结果, 先睹为快.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/Pendulum DQN.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>



{% include assign-heading.html %}

我们知道 DQN 的神经网络部分可以看成一个 `最新的神经网络` + `老神经网络`,
他们有相同的结构, 但内部的参数更新却有时差. 而它的 `Q现实` 部分是这样的:

{% include tut-image.html image-name="4-5-1.png" %}

因为我们的神经网络预测 `Qmax` 本来就有误差, 每次也向着最大误差的 `Q现实` 改进神经网络,
就是因为这个 `Qmax` 导致了 overestimate. 所以 Double DQN 的想法就是引入另一个神经网络来打消一些最大误差的影响.
而 DQN 中本来就有两个神经网络, 我们何不利用一下这个地理优势呢. 所以,
我们用 `Q估计` 的神经网络估计 `Q现实` 中 `Qmax(s', a')` 的最大动作值. 然后用这个被
`Q估计` 估计出来的动作来选择 `Q现实` 中的 `Q(s')`. 总结一下:

有两个神经网络: `Q_eval` (Q估计中的), `Q_next` (Q现实中的).

原本的 `Q_next = max(Q_next(s', a_all))`.

Double DQN 中的 `Q_next = Q_next(s', argmax(Q_eval(s', a_all)))`. 也可以表达成下面那样.


{% include tut-image.html image-name="4-5-2.png" %}




{% include assign-heading.html %}

好了, 有了理论, 我们就来用 Python 实现它吧.

这里的代码都是基于之前 DQN 教程中的代码 [(github)](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5.1_Double_DQN/RL_brain.py){:target="_blank"},
在 `RL_brain` 中, 我们将 class 的名字改成 `DoubleDQN`, 为了对比 Natural DQN,
我们也保留原来大部分的 DQN 的代码. 我们在 `__init__` 中加一个 `double_q` 参数来表示使用的是 Natural DQN 还是 Double DQN.
为了对比的需要, 我们的 `tf.Session()` 也单独传入. 并移除原本在 DQN 代码中的这一句:

`self.sess.run(tf.global_variables_initializer())`

```python
class DoubleDQN:
    def __init__(..., double_q=True, sess=None):
        ...
        self.double_q = double_q
        if sess is None:
            self.sess = tf.Session()
            self.sess.run(tf.global_variables_initializer())
        else:
            self.sess = sess
        ...
```

接着我们来修改 `learn()` 中的代码. 我们对比 Double DQN 和 Natural DQN 在 tensorboard 中的图,
发现他们的结构并没有不同, 但是在计算 `q_target` 的时候, 方法是不同的.

{% include tut-image.html image-name="4-5-3.png" %}


```python
class DoubleDQN:
    def learn(self):
        # 这一段和 DQN 一样:
        if self.learn_step_counter % self.replace_target_iter == 0:
            self.sess.run(self.replace_target_op)
            print('\ntarget_params_replaced\n')

        if self.memory_counter > self.memory_size:
            sample_index = np.random.choice(self.memory_size, size=self.batch_size)
        else:
            sample_index = np.random.choice(self.memory_counter, size=self.batch_size)
        batch_memory = self.memory[sample_index, :]

        # 这一段和 DQN 不一样
        q_next, q_eval4next = self.sess.run(
            [self.q_next, self.q_eval],
            feed_dict={self.s_: batch_memory[:, -self.n_features:],    # next observation
                       self.s: batch_memory[:, -self.n_features:]})    # next observation
        q_eval = self.sess.run(self.q_eval, {self.s: batch_memory[:, :self.n_features]})
        q_target = q_eval.copy()
        batch_index = np.arange(self.batch_size, dtype=np.int32)
        eval_act_index = batch_memory[:, self.n_features].astype(int)
        reward = batch_memory[:, self.n_features + 1]

        if self.double_q:   # 如果是 Double DQN
            max_act4next = np.argmax(q_eval4next, axis=1)        # q_eval 得出的最高奖励动作
            selected_q_next = q_next[batch_index, max_act4next]  # Double DQN 选择 q_next 依据 q_eval 选出的动作
        else:       # 如果是 Natural DQN
            selected_q_next = np.max(q_next, axis=1)    # natural DQN

        q_target[batch_index, eval_act_index] = reward + self.gamma * selected_q_next


        # 这下面和 DQN 一样:
        _, self.cost = self.sess.run([self._train_op, self.loss],
                                     feed_dict={self.s: batch_memory[:, :self.n_features],
                                                self.q_target: q_target})
        self.cost_his.append(self.cost)
        self.epsilon = self.epsilon + self.epsilon_increment if self.epsilon < self.epsilon_max else self.epsilon_max
        self.learn_step_counter += 1
```


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

为了记录下我们选择动作时的 Q 值, 接下来我们就修改 `choose_action()` 功能, 让它记录下每次选择的 Q 值.

```python
class DoubleDQN:
    def choose_action(self, observation):
        observation = observation[np.newaxis, :]
        actions_value = self.sess.run(self.q_eval, feed_dict={self.s: observation})
        action = np.argmax(actions_value)

        if not hasattr(self, 'q'):  # 记录选的 Qmax 值
            self.q = []
            self.running_q = 0
        self.running_q = self.running_q*0.99 + 0.01 * np.max(actions_value)
        self.q.append(self.running_q)

        if np.random.uniform() > self.epsilon:  # 随机选动作
            action = np.random.randint(0, self.n_actions)
        return action
```

{% include assign-heading.html %}

接着我们就来对比 Natural DQN 和 Double DQN 带来的不同结果啦. [代码在这](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5.1_Double_DQN/run_Pendulum.py){:target="_blank"}

```python
import gym
from RL_brain import DoubleDQN
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf


env = gym.make('Pendulum-v0')
env.seed(1) # 可重复实验
MEMORY_SIZE = 3000
ACTION_SPACE = 11    # 将原本的连续动作分离成 11 个动作

sess = tf.Session()
with tf.variable_scope('Natural_DQN'):
    natural_DQN = DoubleDQN(
        n_actions=ACTION_SPACE, n_features=3, memory_size=MEMORY_SIZE,
        e_greedy_increment=0.001, double_q=False, sess=sess
    )

with tf.variable_scope('Double_DQN'):
    double_DQN = DoubleDQN(
        n_actions=ACTION_SPACE, n_features=3, memory_size=MEMORY_SIZE,
        e_greedy_increment=0.001, double_q=True, sess=sess, output_graph=True)

sess.run(tf.global_variables_initializer())


def train(RL):
    total_steps = 0
    observation = env.reset()
    while True:
        # if total_steps - MEMORY_SIZE > 8000: env.render()

        action = RL.choose_action(observation)

        f_action = (action-(ACTION_SPACE-1)/2)/((ACTION_SPACE-1)/4)   # 在 [-2 ~ 2] 内离散化动作

        observation_, reward, done, info = env.step(np.array([f_action]))

        reward /= 10     # normalize 到这个区间 (-1, 0). 立起来的时候 reward = 0.
        # 立起来以后的 Q target 会变成 0, 因为 Q_target = r + gamma * Qmax(s', a') = 0 + gamma * 0
        # 所以这个状态时的 Q 值大于 0 时, 就出现了 overestimate.

        RL.store_transition(observation, action, reward, observation_)

        if total_steps > MEMORY_SIZE:   # learning
            RL.learn()

        if total_steps - MEMORY_SIZE > 20000:   # stop game
            break

        observation = observation_
        total_steps += 1
    return RL.q # 返回所有动作 Q 值

# train 两个不同的 DQN
q_natural = train(natural_DQN)
q_double = train(double_DQN)

# 出对比图
plt.plot(np.array(q_natural), c='r', label='natural')
plt.plot(np.array(q_double), c='b', label='double')
plt.legend(loc='best')
plt.ylabel('Q eval')
plt.xlabel('training steps')
plt.grid()
plt.show()
```

所以这个出来的图是这样:

{% include tut-image.html image-name="4-5-4.png" %}

可以看出, Natural DQN 学得差不多后, 在立起来时, 大部分时间都是 估计的 Q值 要大于0, 这时就出现了
overestimate, 而 Double DQN 的 Q值 就消除了一些 overestimate, 将估计值保持在 0 左右.