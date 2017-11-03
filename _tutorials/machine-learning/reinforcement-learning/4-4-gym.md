---
youku_id: XMjUzMjA1NjY2NA
youtube_id: 9m3DN2dyi8I
bilibili_id: 15989806
chapter: 4
title: OpenAI gym 环境库
publish-date: 2017-02-26
thumbnail: "/static/thumbnail/rl/4.4_openai.jpg"
description: "手动编环境是一件很耗时间的事情, 所以如果有能力使用别人已经编好的环境, 可以节约我们很多时间. OpenAI gym 就是这样一个模块, 他提供了我们很多优秀的模拟环境.
我们的各种 RL 算法都能使用这些环境. 不过 OpenAI gym 暂时只支持 MacOS 和 Linux 系统. Windows 可能某一天就能支持了, 大家时不时查看下官网, 可能就有惊喜.
是在等不及更新了, 也行用 tkinter 来手动编写一下环境.
这里有我制作的很好的 tkinter 入门教程, 之前的 maze 环境也是用 tkinter
编出来的. 大家可以仿照这个文件编写就 ok 啦.
"
post-headings:
  - 要点
  - 安装 gym
  - CartPole 例子
  - MountainCar 例子
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/6_OpenAI_gym){:target="_blank"}
  * [什么是 DQN 短视频]({% link _tutorials/machine-learning/ML-intro/4-06-DQN.md %})
  * [OpenAI gym 官网](https://gym.openai.com/envs/){:target="_blank"}
  * 本节内容的模拟视频效果:
    * CartPole: [Youtube](https://www.youtube.com/watch?v=qlqqezju0xo){:target="_blank"}, [Youtube](https://www.youtube.com/watch?v=qlqqezju0xo){:target="_blank"}
    * Mountain Car: [Youtube](https://www.youtube.com/watch?v=r1mNIDN3zNM){:target="_blank"}, [Youtube](https://www.youtube.com/watch?v=r1mNIDN3zNM){:target="_blank"}

{% include assign-heading.html %}

手动编环境是一件很耗时间的事情, 所以如果有能力使用别人已经编好的环境, 可以节约我们很多时间. OpenAI gym 就是这样一个模块, 他提供了我们很多优秀的模拟环境.
我们的各种 RL 算法都能使用这些环境. 不过 OpenAI gym 暂时只支持 MacOS 和 Linux 系统. Windows 已经支持, 但是听说还没有全面支持, 大家时不时查看下官网, 可能就有惊喜.
是在等不及更新了, 也行用 tkinter 来手动编写一下环境.
这里有我制作的很好的 [tkinter 入门教程]({% link _table-contents/python-basic/tkinter.html %}), 之前的 maze 环境也是用 tkinter
编出来的. 大家可以仿照[这个文件](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5_Deep_Q_Network/maze_env.py){:target="_blank"}编写就 ok 啦.



{% include assign-heading.html %}

在 MacOS 和 Linux 系统下, 安装 gym 很方便, 首先确定你是 python 2.7 或者 python 3.5 版本.
然后在你的 terminal 中复制下面这些. 但是 gym 暂时还不完全支持 Windows, 不过有些虚拟环境已经的到了支持, 想立杆子那个已经支持了.
所以接下来要说的安装方法只有 MacOS 和 Linux 的. Windows 用户的安装方式应该也差不多, 如果 Windows 用户遇到了问题, 欢迎在留言区分享解决的方法.

```shell
# python 2.7, 复制下面
$ pip install gym

# python 3.5, 复制下面
$ pip3 install gym
```

如果没有报错, 恭喜你, 这样你就装好了 gym 的最基本款, 可以开始玩以下游戏啦:

* [algorithmic](https://gym.openai.com/envs#algorithmic){:target="_blank"}
* [toy_text](https://gym.openai.com/envs#toy_text){:target="_blank"}
* [classic_control](https://gym.openai.com/envs#classic_control){:target="_blank"} (这个需要 pyglet 模块)

如果在安装中遇到问题. 可能是缺少了一些必要模块, 可以使用下面语句来安装这些模块(安装时间可能有点久):

```shell
# MacOS:
$ brew install cmake boost boost-python sdl2 swig wget

# Ubuntu 14.04:
$ apt-get install -y python-numpy python-dev cmake zlib1g-dev libjpeg-dev xvfb libav-tools xorg-dev python-opengl libboost-all-dev libsdl2-dev swig
```

如果想要玩 gym 提供的全套游戏, 下面这几句就能满足你:

```shell
# python 2.7, 复制下面
$ pip install gym[all]

# python 3.5, 复制下面
$ pip3 install gym[all]
```



{% include google-in-article-ads.html %}

{% include assign-heading.html %}

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/cartpole dqn.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

之前我编写的 `maze_env` 基本上是按照 `gym` 环境格式写的, 所以你换成 `gym` 格式会很简单.

接下来我们对应上面的算法, 来实现主循环. 首先 import 所需模块.

```python
import gym
from RL_brain import DeepQNetwork

env = gym.make('CartPole-v0')   # 定义使用 gym 库中的那一个环境
env = env.unwrapped # 不做这个会有很多限制

print(env.action_space) # 查看这个环境中可用的 action 有多少个
print(env.observation_space)    # 查看这个环境中可用的 state 的 observation 有多少个
print(env.observation_space.high)   # 查看 observation 最高取值
print(env.observation_space.low)    # 查看 observation 最低取值
```

于之前使用 tkinter 定义的环境有点不一样, 我们可以不适用 `if __name__ == "__main__"` 的方式, 下面是一种类似, 却更简单的写法.
之中我们会用到里面的 reward, 但是 `env.step()` 说提供的 `reward` 不一定是最有效率的 `reward`, 我们大可对这些进行修改,
使 DQN 学得更有效率. 你可以自己对比一下不修改 reward 和 按我这样修改, 他们学习过程的不同.

```python
# 定义使用 DQN 的算法
RL = DeepQNetwork(n_actions=env.action_space.n,
                  n_features=env.observation_space.shape[0],
                  learning_rate=0.01, e_greedy=0.9,
                  replace_target_iter=100, memory_size=2000,
                  e_greedy_increment=0.0008,)

total_steps = 0 # 记录步数

for i_episode in range(100):

    # 获取回合 i_episode 第一个 observation
    observation = env.reset()
    ep_r = 0
    while True:
        env.render()    # 刷新环境

        action = RL.choose_action(observation)  # 选行为

        observation_, reward, done, info = env.step(action) # 获取下一个 state

        x, x_dot, theta, theta_dot = observation_   # 细分开, 为了修改原配的 reward

        # x 是车的水平位移, 所以 r1 是车越偏离中心, 分越少
        # theta 是棒子离垂直的角度, 角度越大, 越不垂直. 所以 r2 是棒越垂直, 分越高

        x, x_dot, theta, theta_dot = observation_
        r1 = (env.x_threshold - abs(x))/env.x_threshold - 0.8
        r2 = (env.theta_threshold_radians - abs(theta))/env.theta_threshold_radians - 0.5
        reward = r1 + r2   # 总 reward 是 r1 和 r2 的结合, 既考虑位置, 也考虑角度, 这样 DQN 学习更有效率

        # 保存这一组记忆
        RL.store_transition(observation, action, reward, observation_)

        if total_steps > 1000:
            RL.learn()  # 学习

        ep_r += reward
        if done:
            print('episode: ', i_episode,
                  'ep_r: ', round(ep_r, 2),
                  ' epsilon: ', round(RL.epsilon, 2))
            break

        observation = observation_
        total_steps += 1
# 最后输出 cost 曲线
RL.plot_cost()
```

这是更为典型的 RL cost 曲线:

{% include tut-image.html image-name="4-4-1.png" %}

{% include assign-heading.html %}

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/mountaincar dqn.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

代码基本和上述代码相同, 就只是在 reward 上动了下手脚.

```python
import gym
from RL_brain import DeepQNetwork

env = gym.make('MountainCar-v0')
env = env.unwrapped

print(env.action_space)
print(env.observation_space)
print(env.observation_space.high)
print(env.observation_space.low)

RL = DeepQNetwork(n_actions=3, n_features=2, learning_rate=0.001, e_greedy=0.9,
                  replace_target_iter=300, memory_size=3000,
                  e_greedy_increment=0.0001,)

total_steps = 0


for i_episode in range(10):

    observation = env.reset()
    ep_r = 0
    while True:
        env.render()

        action = RL.choose_action(observation)

        observation_, reward, done, info = env.step(action)

        position, velocity = observation_

        # 车开得越高 reward 越大
        reward = abs(position - (-0.5))

        RL.store_transition(observation, action, reward, observation_)

        if total_steps > 1000:
            RL.learn()

        ep_r += reward
        if done:
            get = '| Get' if observation_[0] >= env.unwrapped.goal_position else '| ----'
            print('Epi: ', i_episode,
                  get,
                  '| Ep_r: ', round(ep_r, 4),
                  '| Epsilon: ', round(RL.epsilon, 2))
            break

        observation = observation_
        total_steps += 1

RL.plot_cost()
```

出来的 cost 曲线是这样:

{% include tut-image.html image-name="4-4-2.png" %}

这两个都只是例子而已, 具体的实施你也可以大动手脚, 比如你的 reward 定义得更好, 你的神经网络结构更好, 使得他们学的更快.
这些都是自己定义的.