---
youku_id:
youtube_id:
bilibili_id:
title: 从头开始做一个机器手臂1 搭建结构
description: "做这个实践的主要目的就是让我们活学活用, 从0开始搭建一个强化学习框架. 之前我们在强化学习系列教程中学习到了很多强化学习的知识,
了解了各种算法应该怎样运用, 从最简单的 Q-Learning 到结合神经网络的 DQN, 再到做连续动作的DDPG以及分布式训练的 A3C 和 DPPO. 但是我们却没有真正意义上的实践过一次, 因为在那个系列中大多数时候我们只关注了算法本身.
但是搭建模拟环境, 调整参数也同样重要. 所以我们在这个系列中将会做到这些, 让你真正意义上入门了强化学习."
publish-date: 2017-11-22
thumbnail: "/static/thumbnail/ML-practice/arm1.jpg"
chapter: 1
post-headings:
  - 为什么做这个实践
  - 要做成怎样
  - 代码主结构
---

学习资料:
  * [强化学习系列教程]({% link _tutorials/machine-learning/reinforcement-learning/1-1-A-RL.md %})
  * [本节学习代码](https://github.com/MorvanZhou/train-robot-arm-from-scratch/tree/master/part1){:target="_blank"}



{% include assign-heading.html %}

做这个实践的主要目的就是让我们活学活用, 从0开始搭建一个强化学习框架. 之前我们在[强化学习系列教程](/tutorials/machine-learning/reinforcement-learning/)中学习到了很多强化学习的知识,
了解了各种算法应该怎样运用, 从最简单的 [Q-Learning]({% link _tutorials/machine-learning/reinforcement-learning/2-2-A-q-learning.md %}) 到结合神经网络的
[DQN]({% link _tutorials/machine-learning/reinforcement-learning/4-1-A-DQN.md %}), 再到做连续动作的 [DDPG]({% link _tutorials/machine-learning/reinforcement-learning/6-2-A-DDPG.md %}) 以及分布式训练的 [A3C]({% link _tutorials/machine-learning/reinforcement-learning/6-3-A1-A3C.md %})
和 [DPPO]({% link _tutorials/machine-learning/reinforcement-learning/6-4-DPPO.md %}). **但是我们却没有真正意义上的实践过一次**, 因为在那个系列中大多数时候我们只关注了算法本身.
但是搭建模拟环境, 调整参数也同样重要. 所以我们在这个系列中将会做到这些, 让你真正意义上入门了强化学习.




{% include assign-heading.html %}

这个实践很简单, 我使用的是我自己一年前编写的[训练代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/experiments/Robot_arm){:target="_blank"},
让机器人手臂学会到达某一个预设点.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/experiment_arm.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

不过这次, 我优化了代码结构, 将这个自己做过的练习给大家呈现一遍, 让你也能一步步知道在做强化学习的时候要考量些什么, 怎么样做一个合理的环境.
所以我将从下面几个方面来阐述这些.






{% include google-in-article-ads.html %}

{% include assign-heading.html %}

在做每一个强化学习的时候, 我们最好先规划好要怎么分解这一个 task. 一般来说我们尽量不要把所有代码 (环境, 强化学习算法, 学习主循环) 放在一个脚本中.
拆分成三个脚本分开管理将会更有效率, 更加方便管理, 而且眼睛也不会花了. 这也是我在自己[强化学习系列教程]({% link _tutorials/machine-learning/reinforcement-learning/1-1-A-RL.md %})中一直给大家呈现的方式.

具体来说, 这三方面的脚本可以是这样:

* 环境脚本 (env.py)
* 强化学习脚本 (rl.py)
* 主循环脚本 (main.py)

我们在主循环脚本中将会 import 环境和强化学习方法, 所以主循环脚本将上面两者给串联了起来.
如果你看到这次教学的[代码](https://github.com/MorvanZhou/train-robot-arm-from-scratch/){:target="_blank"},
你会发现我将每一步分别打包, part1, part2... 中都有上述三个脚本文件. 我们将在每个 part 中一一添加必要的部分.

这一节, 我们从最基本的 main.py 开始说. 这里涉及了程序的主循环, 也是学习的部分. 怎个学习的框架可以被简化成下面这样,
我采取了 [gym](https://gym.openai.com/docs/){:target="_blank"} 模块的形式. 所以如果使用过 gym 的朋友, 你会发现无比的熟悉.

```python
# main.py

# 导入环境和学习方法
from part1.env import ArmEnv
from part1.rl import DDPG

# 设置全局变量
MAX_EPISODES = 500
MAX_EP_STEPS = 200

# 设置环境
env = ArmEnv()
s_dim = env.state_dim
a_dim = env.action_dim
a_bound = env.action_bound

# 设置学习方法 (这里使用 DDPG)
rl = DDPG(a_dim, s_dim, a_bound)

# 开始训练
for i in range(MAX_EPISODES):
    s = env.reset()                 # 初始化回合设置
    for j in range(MAX_EP_STEPS):
        env.render()                # 环境的渲染
        a = rl.choose_action(s)     # RL 选择动作
        s_, r, done = env.step(a)   # 在环境中施加动作

        # DDPG 这种强化学习需要存放记忆库
        rl.store_transition(s, a, r, s_)

        if rl.memory_full:
            rl.learn()              # 记忆库满了, 开始学习

        s = s_                      # 变为下一回合
```

写到这个时候, 我们明白了, 在 rl.py 和 env.py 中, 我们必须有这样几个 function 和 attribute.

* rl.py
  * `rl.choose_action(s)`
  * `rl.store_transition(s, a, r, s_)`
  * `rl.learn()`
  * `rl.memory_full`
* env.py
  * `env.reset()`
  * `env.render()`
  * `env.step(a)`
  * `env.state_dim`
  * `env.action_dim`
  * `env.action_bound`

有了这些准则, 我们就能在 rl.py 和 env.py 中进行前期规划了. 所以你可以另外创建一个 env.py 的脚本,
先写好下面这个 `ArmEnv` 的 class. 然后给他加上上面提到的功能.

```python
# env.py

class ArmEnv(object):
    def __init__(self):
        pass
    def step(self, action):
        pass
    def reset(self):
        pass
    def render(self):
        pass
```

然后再创建一个 rl.py 脚本, 用来存放你要使用的 RL 的方法. 因为我想要将这个手臂环境设置成一个连续动作的环境(机器人旋转手臂时的角度是一个连续值),
所以我会选用 DDPG 的算法. 但是如果你想设置的环境是一个离散动作(比如机器人只能选上下左右4个键), 你可能需要选择不同的 RL 算法, 对环境也要有不同的应对方式.

```python
# rl.py

class DDPG(object):
    def __init__(self, a_dim, s_dim, a_bound,):
        pass
    def choose_action(self, s):
        pass
    def learn(self):
        pass
    def store_transition(self, s, a, r, s_):
        pass
```

有了这些框架, 我们的主结构就大功告成了, 接着我们就开始继续往下面添砖加瓦吧. 看看如何[搭建一个模拟环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch2.md %}).

*实战:从头开始搭建训练机器人手臂*

* *[搭建结构]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})*
* *[写静态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch2.md %})*
* *[写动态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch3.md %})*
* *[加入强化学习算法]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch4.md %})*
* *[完善测试]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch5.md %})*
