---
youku_id: XMjY4NTE1MDY3Mg
youtube_id: tvMu5oPYpsw
bilibili_id: 15990821
chapter: 6
title: Actor Critic (Tensorflow)
thumbnail: "/static/thumbnail/rl/6.1_actor_critic.jpg"
publish-date: 2017-04-03
description: "一句话概括 Actor Critic 方法:
结合了 Policy Gradient (Actor) 和 Function Approximation (Critic) 的方法.
Actor 基于概率选行为, Critic 基于 Actor 的行为评判行为的得分,
Actor 根据 Critic 的评分修改选行为的概率.
Actor Critic 方法的优势:
可以进行单步更新, 比传统的 Policy Gradient 要快.
Actor Critic 方法的劣势:
取决于 Critic 的价值判断, 但是 Critic 难收敛, 再加上 Actor 的更新, 就更难收敛.
为了解决收敛问题, Google Deepmind 提出了 Actor Critic 升级版 Deep Deterministic Policy Gradient."
post-headings:
  - 要点
  - 算法
  - 代码主结构
  - 两者学习方式
  - 每回合算法
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/8_Actor_Critic_Advantage){:target="_blank"}
  * [什么是 Actor Critic 短视频]({% link _tutorials/machine-learning/ML-intro/4-08-AC.md %})
  * [什么是 Policy Gradient 短视频]({% link _tutorials/machine-learning/ML-intro/4-07-PG.md %})
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 学习书籍 [Reinforcement learning: An introduction](http://ufal.mff.cuni.cz/~straka/courses/npfl114/2016/sutton-bookdraft2016sep.pdf){:target="_blank"}

{% include assign-heading.html %}

**一句话概括 Actor Critic 方法**:

结合了 Policy Gradient (Actor) 和 Function Approximation (Critic) 的方法.
`Actor` 基于概率选行为, `Critic` 基于 `Actor` 的行为评判行为的得分,
`Actor` 根据 `Critic` 的评分修改选行为的概率.

**Actor Critic 方法的优势**:
可以进行单步更新, 比传统的 Policy Gradient 要快.

**Actor Critic 方法的劣势**:
取决于 Critic 的价值判断, 但是 Critic 难收敛, 再加上 Actor 的更新, 就更难收敛.
为了解决收敛问题, Google Deepmind 提出了 `Actor Critic` 升级版 `Deep Deterministic Policy Gradient`.
后者融合了 DQN 的优势, 解决了收敛难的问题. 我们之后也会要讲到 [Deep Deterministic Policy Gradient]({% link _tutorials/machine-learning/reinforcement-learning/6-2-DDPG.md %}).
不过那个是要以 `Actor Critic` 为基础, 懂了 `Actor Critic`, 后面那个就好懂了.

下面是基于 Actor Critic 的 Gym Cartpole 实验:

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/cartpole actor critic.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>




{% include assign-heading.html %}

这套算法是在普通的 Policy gradient 算法上面修改的, 如果对 Policy Gradient
算法还不是很了解, 欢迎[戳这里]({% link _tutorials/machine-learning/reinforcement-learning/5-1-policy-gradient-softmax1.md %}).
对这套算法打个比方如下:

**`Actor` 修改行为时就像蒙着眼睛一直向前开车, `Critic` 就是那个扶方向盘改变 `Actor`
开车方向的.**

{% include tut-image.html image-name="6-1-1.png" %}

或者说详细点, 就是 `Actor` 在运用 Policy Gradient 的方法进行 Gradient ascent 的时候, 由
`Critic` 来告诉他, 这次的 Gradient ascent 是不是一次正确的 ascent, 如果这次的得分不好,
那么就不要 ascent 那么多.

{% include assign-heading.html %}

有了点理解, 我们来代码 (如果想一次性看所有代码, 请来我的 [Github](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/8_Actor_Critic_Advantage/AC_CartPole.py){:target="_blank"}):

{% include tut-image.html image-name="6-1-2.png" %}

上图是 `Actor` 的神经网络结果, 代码结构在下面:

```python
class Actor(object):
    def __init__(self, sess, n_features, n_actions, lr=0.001):
        # 用 tensorflow 建立 Actor 神经网络,
        # 搭建好训练的 Graph.

    def learn(self, s, a, td):
        # s, a 用于产生 Gradient ascent 的方向,
        # td 来自 Critic, 用于告诉 Actor 这方向对不对.

    def choose_action(self, s):
        # 根据 s 选 行为 a
```


{% include tut-image.html image-name="6-1-3.png" %}

上图是 `Critic` 的神经网络结果, 代码结构在下面:

```python
class Critic(object):
    def __init__(self, sess, n_features, lr=0.01):
        # 用 tensorflow 建立 Critic 神经网络,
        # 搭建好训练的 Graph.

    def learn(self, s, r, s_):
        # 学习 状态的价值 (state value), 不是行为的价值 (action value),
        # 计算 TD_error = (r + v_) - v,
        # 用 TD_error 评判这一步的行为有没有带来比平时更好的结果,
        # 可以把它看做 Advantage
        return # 学习时产生的 TD_error
```



{% include google-in-article-ads.html %}

{% include assign-heading.html %}

`Actor` 想要最大化期望的 `reward`, 在 `Actor Critic` 算法中, 我们用 "比平时好多少"
(`TD error`) 来当做 `reward`, 所以就是:

```python
with tf.variable_scope('exp_v'):
    log_prob = tf.log(self.acts_prob[0, self.a])    # log 动作概率
    self.exp_v = tf.reduce_mean(log_prob * self.td_error)   # log 概率 * TD 方向
with tf.variable_scope('train'):
    # 因为我们想不断增加这个 exp_v (动作带来的额外价值),
    # 所以我们用过 minimize(-exp_v) 的方式达到
    # maximize(exp_v) 的目的
    self.train_op = tf.train.AdamOptimizer(lr).minimize(-self.exp_v)
```

`Critic` 的更新很简单, 就是像 Q learning 那样更新现实和估计的误差 (TD error) 就好了.

```python
with tf.variable_scope('squared_TD_error'):
    self.td_error = self.r + GAMMA * self.v_ - self.v
    self.loss = tf.square(self.td_error)    # TD_error = (r+gamma*V_next) - V_eval
with tf.variable_scope('train'):
    self.train_op = tf.train.AdamOptimizer(lr).minimize(self.loss)
```



{% include assign-heading.html %}

```python
for i_episode in range(MAX_EPISODE):
    s = env.reset()
    t = 0
    track_r = []    # 每回合的所有奖励
    while True:
        if RENDER: env.render()

        a = actor.choose_action(s)

        s_, r, done, info = env.step(a)

        if done: r = -20    # 回合结束的惩罚

        track_r.append(r)

        td_error = critic.learn(s, r, s_)  # Critic 学习
        actor.learn(s, a, td_error)     # Actor 学习

        s = s_
        t += 1

        if done or t >= MAX_EP_STEPS:
            # 回合结束, 打印回合累积奖励
            ep_rs_sum = sum(track_r)
            if 'running_reward' not in globals():
                running_reward = ep_rs_sum
            else:
                running_reward = running_reward * 0.95 + ep_rs_sum * 0.05
            if running_reward > DISPLAY_REWARD_THRESHOLD: RENDER = True  # rendering
            print("episode:", i_episode, "  reward:", int(running_reward))
            break
```

建立神经网络的详细流程请直接看代码更直观, 其他方面的代码也不是重点, 所以直接看代码很好懂.
一次性看到全部代码, 请去我的 [Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/blob/master/contents/8_Actor_Critic_Advantage/AC_CartPole.py){:target="_blank"}

由于更新时的 网络相关性, state 相关性, Actor Critic 很难收敛. 如果同学们对这份代码做过修改,
并且达到了好的收敛性, 欢迎在下面分享~
