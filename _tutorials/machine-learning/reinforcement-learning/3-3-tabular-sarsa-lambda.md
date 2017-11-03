---
youku_id: XMjI2Nzg3MTgxNg
youtube_id: gXZ4AWgkrQE
bilibili_id: 15988888
chapter: 3
title: Sarsa-lambda
thumbnail: "/static/thumbnail/rl/3.3_sarsa_lambda.jpg"
publish-date: 2017-01-13
description: "Sarsa-lambda 是基于 Sarsa 方法的升级版, 他能更有效率地学习到怎么样获得好的 reward.
如果说 Sarsa 和 Qlearning 都是每次获取到 reward, 只更新获取到 reward 的前一步.
那 Sarsa-lambda 就是更新获取到 reward 的前 lambda 步. lambda 是在 [0, 1] 之间取值,
如果 lambda = 0, Sarsa-lambda 就是 Sarsa, 只更新获取到 reward 前经历的最后一步.
如果 lambda = 1, Sarsa-lambda 更新的是 获取到 reward 前所有经历的步.
这样解释起来有点抽象, 还是建议大家观看我制作的 什么是 Sarsa-lambda 短视频"
post-headings:
  - 要点
  - 代码主结构
  - 预设值
  - 检测 state 是否存在
  - 学习
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/4_Sarsa_lambda_maze){:target="_blank"}
  * [什么是 Sarsa-lambda 短视频]({% link _tutorials/machine-learning/ML-intro/4-05-sarsa-lambda.md %})
  * 本节内容的模拟视频效果[Youtube](https://www.youtube.com/watch?v=0-odgVLZ5EQ&index=3&list=PLXO45tsB95cLYyEsEylpPvTY-8ErPt2O_){:target="_blank"}, [Youtube](https://www.youtube.com/watch?v=0-odgVLZ5EQ&index=3&list=PLXO45tsB95cLYyEsEylpPvTY-8ErPt2O_){:target="_blank"}
  * 学习书籍 [Reinforcement learning: An introduction](http://ufal.mff.cuni.cz/~straka/courses/npfl114/2016/sutton-bookdraft2016sep.pdf){:target="_blank"}

{% include assign-heading.html %}



Sarsa-lambda 是基于 Sarsa 方法的升级版, 他能更有效率地学习到怎么样获得好的 reward.
如果说 Sarsa 和 Qlearning 都是每次获取到 reward, 只更新获取到 reward 的前一步.
那 Sarsa-lambda 就是更新获取到 reward 的前 lambda 步. lambda 是在 [0, 1] 之间取值,

如果 lambda = 0, Sarsa-lambda 就是 Sarsa, 只更新获取到 reward 前经历的最后一步.

如果 lambda = 1, Sarsa-lambda 更新的是 获取到 reward 前所有经历的步.

这样解释起来有点抽象, 还是建议大家观看我制作的 [什么是 Sarsa-lambda 短视频]({% link _tutorials/machine-learning/ML-intro/4-05-sarsa-lambda.md %}), 用动画展示具体的区别.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/maze sarsa_lambda.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>



{% include assign-heading.html %}


使用 `SarsaLambdaTable` 在算法更新迭代的部分, 是和之前的 `SarsaTable` 一样的, 所以这一节, 我们没有算法更新部分, 直接变成 思维决策部分.

```python
class SarsaLambdaTable:
    # 初始化 (有改变)
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9, trace_decay=0.9):

    # 选行为 (与之前一样)
    def choose_action(self, observation):

    # 学习更新参数 (有改变)
    def learn(self, s, a, r, s_):

    # 检测 state 是否存在 (有改变)
    def check_state_exist(self, state):
```

同样, 我们选择继承的方式, 将 `SarsaLambdaTable` 继承到 `RL`,
所以我们将之前的 `__init__`, `check_state_exist`, `choose_action`, `learn` 全部都放在这个主结构中, 之后根据不同的算法更改对应的内容就好了.
所以还没弄懂这些功能的朋友们, 请回到之前的教程再看一遍.

算法的相应更改请参考这个:

{% include tut-image.html image-name="3-3-1.png" %}

{% include assign-heading.html %}

在预设值当中, 我们添加了 `trace_decay=0.9` 这个就是 `lambda` 的值了. 这个值将会使得拿到 reward 前的每一步都有价值.
如果还不太明白其他预设值的意思, 请查看我的 [关于强化学习的短视频列表]({% link _table-contents/machine-learning/ML-intro.html %})

```python
class SarsaLambdaTable(RL): # 继承 RL class
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9, trace_decay=0.9):
        super(SarsaLambdaTable, self).__init__(actions, learning_rate, reward_decay, e_greedy)

        # 后向观测算法, eligibility trace.
        self.lambda_ = trace_decay
        self.eligibility_trace = self.q_table.copy()    # 空的 eligibility trace 表
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

`check_state_exist` 和之前的是高度相似的. 唯一不同的地方是我们考虑了 `eligibility_trace`,

```python
class SarsaLambdaTable(RL): # 继承 RL class
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9, trace_decay=0.9):
        ...
    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            to_be_append = pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            self.q_table = self.q_table.append(to_be_append)

            # also update eligibility trace
            self.eligibility_trace = self.eligibility_trace.append(to_be_append)
```

{% include assign-heading.html %}

有了父类的 `RL`, 我们这次的编写就很简单, 只需要编写 `SarsaLambdaTable` 中 `learn` 这个功能就完成了. 因为其他功能都和父类是一样的.
这就是我们所有的 `SarsaLambdaTable` 于父类 `RL` 不同之处的代码. 是不是很简单.

```python
class SarsaLambdaTable(RL): # 继承 RL class
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9, trace_decay=0.9):
        ...
    def check_state_exist(self, state):
        ...
    def learn(self, s, a, r, s_, a_):
        # 这部分和 Sarsa 一样
        self.check_state_exist(s_)
        q_predict = self.q_table.ix[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.ix[s_, a_]
        else:
            q_target = r
        error = q_target - q_predict

        # 这里开始不同:
        # 对于经历过的 state-action, 我们让他+1, 证明他是得到 reward 路途中不可或缺的一环
        self.eligibility_trace.ix[s, a] += 1

        # Q table 更新
        self.q_table += self.lr * error * self.eligibility_trace

        # 随着时间衰减 eligibility trace 的值, 离获取 reward 越远的步, 他的"不可或缺性"越小
        self.eligibility_trace *= self.gamma*self.lambda_
```

除了图中和上面代码这种更新方式, 还有一种会更加有效率. 我们可以将上面的这一步替换成下面这样:

```python
# 上面代码中的方式:
self.eligibility_trace.ix[s, a] += 1

# 更有效的方式:
self.eligibility_trace.ix[s, :] *= 0
self.eligibility_trace.ix[s, a] = 1
```

他们两的不同之处可以用这张图来概括:

{% include tut-image.html image-name="3-3-2.png" %}

这是针对于一个 state-action 值按经历次数的变化.
最上面是经历 state-action 的时间点, 第二张图是使用这种方式所带来的 "不可或缺性值":

`self.eligibility_trace.ix[s, a] += 1`

下面图是使用这种方法带来的 "不可或缺性值":

`self.eligibility_trace.ix[s, :] *= 0; self.eligibility_trace.ix[s, a] = 1`

实验证明选择下面这种方法会有更好的效果. 大家也可以自己玩一玩, 试试两种方法的不同表现.

最后不要忘了, eligibility trace 只是记录每个回合的每一步, 新回合开始的时候需要将 Trace 清零.

```python
for episode in range(100):
    ...

    # 新回合, 清零
    RL.eligibility_trace *= 0

    while True: # 开始回合
        ...
```

如果想一次性看到全部代码, 请去我的 [Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/4_Sarsa_lambda_maze){:target="_blank"}


