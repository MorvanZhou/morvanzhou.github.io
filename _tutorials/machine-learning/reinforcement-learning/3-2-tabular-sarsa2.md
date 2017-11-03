---
youku_id: XMjI2NjIxODcyMA
youtube_id: sqpuf7hCC4c
bilibili_id: 15988485
chapter: 3
title: Sarsa 思维决策
thumbnail: "/static/thumbnail/rl/3.2_sarsa2.jpg"
publish-date: 2017-01-13
description: "接着上节内容, 我们来实现 RL_brain 的 SarsaTable 部分, 这也是 RL 的大脑部分, 负责决策和思考.
和之前定义 Qlearning 中的 QLearningTable 一样, 因为使用 tabular 方式的 Sarsa 和 Qlearning 的相似度极高,"
post-headings:
  - 代码主结构
  - 学习
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/3_Sarsa_maze){:target="_blank"}
  * [什么是 Sarsa 短视频]({% link _tutorials/machine-learning/ML-intro/4-04-sarsa.md %})
  * 本节内容的模拟视频效果[Youtube](https://www.youtube.com/watch?v=UKlQmGTNEo0){:target="_blank"}, [Youtube](https://www.youtube.com/watch?v=UKlQmGTNEo0){:target="_blank"}
  * 学习书籍 [Reinforcement learning: An introduction](http://ufal.mff.cuni.cz/~straka/courses/npfl114/2016/sutton-bookdraft2016sep.pdf){:target="_blank"}

接着上节内容, 我们来实现 `RL_brain` 的 `SarsaTable` 部分, 这也是 RL 的大脑部分, 负责决策和思考.



{% include assign-heading.html %}


和之前定义 Qlearning 中的 `QLearningTable` 一样, 因为使用 tabular 方式的 `Sarsa` 和 `Qlearning` 的相似度极高,

```python
class SarsaTable:
    # 初始化 (与之前一样)
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):

    # 选行为 (与之前一样)
    def choose_action(self, observation):

    # 学习更新参数 (有改变)
    def learn(self, s, a, r, s_):

    # 检测 state 是否存在 (与之前一样)
    def check_state_exist(self, state):
```

我们甚至可以定义一个 主class `RL`, 然后将 `QLearningTable` 和 `SarsaTable` 作为 主class `RL` 的衍生, 这个主 `RL` 可以这样定义.
所以我们将之前的 `__init__`, `check_state_exist`, `choose_action`, `learn` 全部都放在这个主结构中, 之后根据不同的算法更改对应的内容就好了.
所以还没弄懂这些功能的朋友们, 请回到之前的教程再看一遍.

```python
import numpy as np
import pandas as pd


class RL(object):
    def __init__(self, action_space, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        ... # 和 QLearningTable 中的代码一样

    def check_state_exist(self, state):
        ... # 和 QLearningTable 中的代码一样

    def choose_action(self, observation):
        ... # 和 QLearningTable 中的代码一样

    def learn(self, *args):
        pass # 每种的都有点不同, 所以用 pass
```

如果是这样定义父类的 `RL` class, 通过继承关系, 那之子类 `QLearningTable` class 就能简化成这样:

```python
class QLearningTable(RL):   # 继承了父类 RL
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(QLearningTable, self).__init__(actions, learning_rate, reward_decay, e_greedy)    # 表示继承关系

    def learn(self, s, a, r, s_):   # learn 的方法在每种类型中有不一样, 需重新定义
        self.check_state_exist(s_)
        q_predict = self.q_table.ix[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.ix[s_, :].max()
        else:
            q_target = r
        self.q_table.ix[s, a] += self.lr * (q_target - q_predict)
```

{% include assign-heading.html %}


有了父类的 `RL`, 我们这次的编写就很简单, 只需要编写 `SarsaTable` 中 `learn` 这个功能就完成了. 因为其他功能都和父类是一样的.
这就是我们所有的 `SarsaTable` 于父类 `RL` 不同之处的代码. 是不是很简单.

```python
class SarsaTable(RL):   # 继承 RL class

    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(SarsaTable, self).__init__(actions, learning_rate, reward_decay, e_greedy)    # 表示继承关系

    def learn(self, s, a, r, s_, a_):
        self.check_state_exist(s_)
        q_predict = self.q_table.ix[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.ix[s_, a_]  # q_target 基于选好的 a_ 而不是 Q(s_) 的最大值
        else:
            q_target = r  # 如果 s_ 是终止符
        self.q_table.ix[s, a] += self.lr * (q_target - q_predict)  # 更新 q_table
```

如果想一次性看到全部代码, 请去我的 [Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/3_Sarsa_maze){:target="_blank"}

