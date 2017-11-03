---
youku_id: XMTk2OTg5NDE0MA
youtube_id: lfMICa9sEQE
bilibili_id: 15987893
chapter: 2
title: Q-learning 算法更新
thumbnail: "/static/thumbnail/rl/2.2_qlearning1.jpg"
publish-date: 2017-01-09
description: "上次我们知道了 RL 之中的 Q-learning 方法是在做什么事, 今天我们就来说说一个更具体的例子. 让探索者学会走迷宫. 黄色的是天堂 (reward 1),
黑色的地狱 (reward -1). 大多数 RL 是由 reward 导向的, 所以定义 reward 是 RL 中比较重要的一点.整个算法就是一直不断更新 Q table 里的值, 然后再根据新的值来判断要在某个 state 采取怎样的 action.
Qlearning 是一个 off-policy 的算法, 因为里面的 max action 让 Q table 的更新可以不基于正在经历的经验(可以是现在学习着很久以前的经验,甚至是学习他人的经验).
不过这一次的例子, 我们没有运用到 off-policy, 而是把 Qlearning 用在了 on-policy 上, 也就是现学现卖, 将现在经历的直接当场学习并运用."
post-headings:
  - 要点
  - 算法
  - 算法的代码形式
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/2_Q_Learning_maze){:target="_blank"}
  * [什么是 Q Learning 短视频]({% link _tutorials/machine-learning/ML-intro/4-03-q-learning.md %})
  * 本节内容的模拟视频效果[Youtube](https://www.youtube.com/watch?v=G5BDgzxfLvA){:target="_blank"}, [Youtube](https://www.youtube.com/watch?v=G5BDgzxfLvA){:target="_blank"}
  * 学习书籍 [Reinforcement learning: An introduction](http://ufal.mff.cuni.cz/~straka/courses/npfl114/2016/sutton-bookdraft2016sep.pdf){:target="_blank"}


{% include assign-heading.html %}

上次我们知道了 RL 之中的 Q-learning 方法是在做什么事, 今天我们就来说说一个更具体的例子. 让探索者学会走迷宫. 黄色的是天堂 (reward 1),
黑色的地狱 (reward -1). 大多数 RL 是由 reward 导向的, 所以定义 reward 是 RL 中比较重要的一点.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/maze q.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>



{% include assign-heading.html %}

{% include tut-image.html image-name="2-1-1.png" %}

整个算法就是一直不断更新 Q table 里的值, 然后再根据新的值来判断要在某个 state 采取怎样的 action.
Qlearning 是一个 off-policy 的算法, 因为里面的 `max` action 让 Q table 的更新可以不基于正在经历的经验(可以是现在学习着很久以前的经验,甚至是学习他人的经验).
不过这一次的例子, 我们没有运用到 off-policy, 而是把 Qlearning 用在了 on-policy 上, 也就是现学现卖, 将现在经历的直接当场学习并运用.
On-policy 和 off-policy 的差别我们会在之后的 [Deep Q network (off-policy)]({% link _tutorials/machine-learning/reinforcement-learning/4-1-DQN1.md %}) 学习中见识到. 而之后的教程也会讲到一个 on-policy (Sarsa) 的形式, 我们之后再对比.

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

首先我们先 import 两个模块,  `maze_env` 是我们的环境模块, 已经编写好了, 大家可以直接在[这里下载](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/2_Q_Learning_maze/maze_env.py){:target="_blank"},
`maze_env` 模块我们可以不深入研究, 如果你对编辑环境感兴趣, 可以去看看如何使用 python 自带的简单 GUI 模块 `tkinter` 来编写虚拟环境.
我也有[对应的教程](/tutorials/python-basic/tkinter/). `maze_env` 就是用 `tkinter` 编写的. 而 `RL_brain` 这个模块是 RL 的大脑部分, 我们下节会讲.

```python
from maze_env import Maze
from RL_brain import QLearningTable
```

下面的代码, 我们可以根据上面的图片中的算法对应起来, 这就是整个 Qlearning 最重要的迭代更新部分啦.

```python
def update():
    # 学习 100 回合
    for episode in range(100):
        # 初始化 state 的观测值
        observation = env.reset()

        while True:
            # 更新可视化环境
            env.render()

            # RL 大脑根据 state 的观测值挑选 action
            action = RL.choose_action(str(observation))

            # 探索者在环境中实施这个 action, 并得到环境返回的下一个 state 观测值, reward 和 done (是否是掉下地狱或者升上天堂)
            observation_, reward, done = env.step(action)

            # RL 从这个序列 (state, action, reward, state_) 中学习
            RL.learn(str(observation), action, reward, str(observation_))

            # 将下一个 state 的值传到下一次循环
            observation = observation_

            # 如果掉下地狱或者升上天堂, 这回合就结束了
            if done:
                break

    # 结束游戏并关闭窗口
    print('game over')
    env.destroy()

if __name__ == "__main__":
    # 定义环境 env 和 RL 方式
    env = Maze()
    RL = QLearningTable(actions=list(range(env.n_actions)))

    # 开始可视化环境 env
    env.after(100, update)
    env.mainloop()
```

如果想一次性看到全部代码, 请去我的 [Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/2_Q_Learning_maze){:target="_blank"}
