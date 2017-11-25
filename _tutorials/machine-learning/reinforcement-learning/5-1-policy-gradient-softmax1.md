---
youku_id: XMjY1MzQ0MDI4NA
youtube_id: A54GU_WqLmQ
bilibili_id: 15990409
chapter: 5
title: Policy Gradients 算法更新 (Tensorflow)
thumbnail: "/static/thumbnail/rl/5.1_PG1.jpg"
publish-date: 2017-03-21
description: "Policy gradient 是 RL 中另外一个大家族, 他不像 Value-based 方法 (Q learning, Sarsa), 但他也要接受环境信息 (observation),
不同的是他要输出不是 action 的 value, 而是具体的那一个 action, 这样 policy gradient 就跳过了 value 这个阶段. 而且个人认为 Policy gradient
最大的一个优势是: 输出的这个 action 可以是一个连续的值, 之前我们说到的 value-based 方法输出的都是不连续的值, 然后再选择值最大的 action.
而 policy gradient 可以在一个连续分布上选取 action."
post-headings:
  - 要点
  - 算法
  - 算法代码形式
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/7_Policy_gradient_softmax){:target="_blank"}
  * [什么是 Policy Gradient 短视频]({% link _tutorials/machine-learning/ML-intro/4-07-PG.md %})
  * 本节内容的模拟视频效果:
    * CartPole: [Youtube](https://www.youtube.com/watch?v=z2-hn7iCjP0){:target="_blank"}, [优酷](http://v.youku.com/v_show/id_XMTg5NzgzNTk0NA==.html?f=27485743){:target="_blank"}
    * Mountain Car: [Youtube](https://www.youtube.com/watch?v=A8hXNykR0Fg){:target="_blank"}, [优酷](http://v.youku.com/v_show/id_XMTg5NzgzODQwNA==.html?f=27485743){:target="_blank"}
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 论文 [Policy gradient methods for reinforcement learning with function approximation.](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf){:target="_blank"}

{% include assign-heading.html %}

Policy gradient 是 RL 中另外一个大家族, 他不像 Value-based 方法 (Q learning, Sarsa), 但他也要接受环境信息 (observation),
不同的是他要输出不是 action 的 value, 而是具体的那一个 action, 这样 policy gradient 就跳过了 value 这个阶段. 而且个人认为 Policy gradient
最大的一个优势是: 输出的这个 action 可以是一个连续的值, 之前我们说到的 value-based 方法输出的都是不连续的值, 然后再选择值最大的 action.
而 policy gradient 可以在一个连续分布上选取 action.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/cartpole policy gradient softmax.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/mountaincar policy gradient softmax.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>




{% include assign-heading.html %}

我们介绍的 policy gradient 的第一个算法是一种基于 **整条回合数据** 的更新, 也叫 **REINFORCE** 方法.
这种方法是 policy gradient 的最基本方法, 有了这个的基础, 我们再来做更高级的.

{% include tut-image.html image-name="5-1-1.png" %}

`log(Policy(s,a))*V` 中的 `log(Policy(s,a))` 表示在 状态 `s` 对所选动作 `a` 的吃惊度,
如果 `Policy(s,a)` 概率越小, 反向的 `log(Policy(s,a))` (即 `-log(P)`) 反而越大. 如果在 `Policy(s,a)` 很小的情况下,
拿到了一个 大的 `R`, 也就是 大的 `V`, 那 `-log(Policy(s, a))*V` 就更大, 表示更吃惊, (我选了一个不常选的动作, 却发现原来它能得到了一个好的 reward,
那我就得对我这次的参数进行一个大幅修改). 这就是 `log(Policy)*V` 的物理意义啦.

{% include assign-heading.html %}

和以前类似, 我们先定义主更新的循环, 然后下节内容讲如何用 Tensorflow 定义 `PolicyGradient()` 的算法:

```python
import gym
from RL_brain import PolicyGradient
import matplotlib.pyplot as plt

RENDER = False  # 在屏幕上显示模拟窗口会拖慢运行速度, 我们等计算机学得差不多了再显示模拟
DISPLAY_REWARD_THRESHOLD = 400  # 当 回合总 reward 大于 400 时显示模拟窗口

env = gym.make('CartPole-v0')   # CartPole 这个模拟
env = env.unwrapped     # 取消限制
env.seed(1)     # 普通的 Policy gradient 方法, 使得回合的 variance 比较大, 所以我们选了一个好点的随机种子

print(env.action_space)     # 显示可用 action
print(env.observation_space)    # 显示可用 state 的 observation
print(env.observation_space.high)   # 显示 observation 最高值
print(env.observation_space.low)    # 显示 observation 最低值

# 定义
RL = PolicyGradient(
    n_actions=env.action_space.n,
    n_features=env.observation_space.shape[0],
    learning_rate=0.02,
    reward_decay=0.99,   # gamma
    # output_graph=True,    # 输出 tensorboard 文件
)
```

主循环在这, 这节介绍的内容是让计算机跑完一整个回合才更新一次. 之前的 Qleanring 等在回合中每一步都可以更新参数.

```python
for i_episode in range(3000):

    observation = env.reset()

    while True:
        if RENDER: env.render()

        action = RL.choose_action(observation)

        observation_, reward, done, info = env.step(action)

        RL.store_transition(observation, action, reward)    # 存储这一回合的 transition

        if done:
            ep_rs_sum = sum(RL.ep_rs)

            if 'running_reward' not in globals():
                running_reward = ep_rs_sum
            else:
                running_reward = running_reward * 0.99 + ep_rs_sum * 0.01
            if running_reward > DISPLAY_REWARD_THRESHOLD: RENDER = True     # 判断是否显示模拟
            print("episode:", i_episode, "  reward:", int(running_reward))

            vt = RL.learn() # 学习, 输出 vt, 我们下节课讲这个 vt 的作用

            if i_episode == 0:
                plt.plot(vt)    # plot 这个回合的 vt
                plt.xlabel('episode steps')
                plt.ylabel('normalized state-action value')
                plt.show()
            break

        observation = observation_
```

另外一个 'Mountain Car' 模拟代码在我的 [Github 中](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/7_Policy_gradient_softmax/run_MountainCar.py){:target="_blank"},
和上面那些代码类似, 只改动了一些大写的参数.