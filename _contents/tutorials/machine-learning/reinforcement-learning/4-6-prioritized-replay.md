---
youku_id: XMjYxMTE2NTEzNg
youtube_id: 9gQl-TkmA80
chapter: 4
title: Prioritized Experience Replay (DQN) (Tensorflow)
publish-date: 2017-03-07
thumbnail: "/static/thumbnail/rl/12_2 prioritized replay.jpg"
---

* 学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/5.2_Prioritized_Replay_DQN)
  * [什么是 Prioritized Replay 短视频(即将制作)](#)
  * 论文 [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952)

**本篇教程是基于 Deep Q network (DQN) 的选学教程.
以下教程缩减了在 DQN 方面的介绍, 着重强调 DQN with Prioritized Replay 和 DQN 在代码上不同的地方.
所以还没了解 DQN 的同学们, 有关于 DQN 的知识,
请从 [这个视频]({% link _contents/tutorials/machine-learning/ML-intro/4-06-DQN.md %})
和 [这个Python教程]({% link _contents/tutorials/machine-learning/reinforcement-learning/4-1-DQN1.md %}) 开始学习.**

这一次还是使用 MountainCar 来进行实验, 因为这次我们不需要重度改变他的 reward 了.
所以只要是没有拿到小旗子, reward=-1, 拿到小旗子时, 我们定义它获得了 +10 的 reward.
比起之前 DQN 中, 这个 reward 定义更加准确. 如果使用这种 reward 定义方式,
可以想象 Natural DQN 会花很久的时间学习, 因为记忆库中只有很少很少的 +10 reward 可以学习. 正负样本不一样.
而使用 Prioritized replay, 就会重视这种少量的, 但值得学习的样本.

<div align="center">
<video width="500" controls loop autoplay muted>
  <source src="/static/results/rl/mountaincar dqn.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
</div>

#### 本节内容包括:

* [Prioritized replay 算法](#algorithm)
* [SumTree 有效抽样](#sumtree)
* [Memory 类](#memory)
* [更新方法](#learn)
* [对比结果](#result)

<h4 class="tut-h4-pad" id="algorithm">Prioritized replay 算法</h4>

<img class="course-image" src="/static/results/rl/4-6-1.png">

这一套算法重点就在我们 batch 抽样的时候并不是随机抽样, 而是按照 Memory 中的样本优先级来抽.
所以这能更有效地找到我们需要学习的样本.

那么样本的优先级是怎么定的呢? 原来我们可以用到 `TD-error`, 也就是 `Q现实 - Q估计` 来规定优先学习的程度.
如果 `TD-error` 越大, 就代表我们的预测精度还有很多上升空间, 那么这个样本就越需要被学习, 也就是优先级 `p` 越高.

有了 `TD-error` 就有了优先级 `p`, 那我们如何有效地根据 `p` 来抽样呢?
如果每次抽样都需要针对 `p` 对所有样本排序, 这将会是一件非常消耗计算能力的事.
好在我们还有其他方法, 这种方法不会对得到的样本进行排序. 这就是这篇 [paper](https://arxiv.org/abs/1511.05952)
中提到的 `SumTree`.

SumTree 是一种树形结构, 每片树叶存储每个样本的优先级 `p`, 每个树枝节点只有两个分叉, 节点的值是两个分叉的合,
所以 SumTree 的顶端就是所有 `p` 的合. 正如下面[图片(来自Jaromír Janisch)](https://jaromiru.com/2016/11/07/lets-make-a-dqn-double-learning-and-prioritized-experience-replay/),
最下面一层树叶存储样本的 `p`, 叶子上一层最左边的 13 = 3 + 10, 按这个规律相加, 顶层的 root 就是全部 `p` 的合了.

<a href="https://jaromiru.com/2016/11/07/lets-make-a-dqn-double-learning-and-prioritized-experience-replay/">
<img class="course-image" src="/static/results/rl/4-6-2.png">
</a>

抽样时, 我们会将 `p` 的总合 除以 batch size, 分成 batch size 那么多区间, (n=sum(p)/batch_size).
然后在每个区间里随机选取一个数.

比如上面的叶子中抽取 2 个 samples, 先将 42 / 2 = 21.
然后在 (0-21) 这个优先度区间中随机选数, 比如选到 2. 再从 root 开始向下根据 2 来抽样, 具体怎么抽, 请看下面的代码好懂一点.
然后在 (21-42) 这个优先度区间随机抽数, 比如选到 24, 再从 root 开始向下根据 24 来抽样. 这样我们就根据优先度抽取到了 2 个样本.


<h4 class="tut-h4-pad" id="sumtree">SumTree 有效抽样</h4>

首先要提的是, 这个 SumTree 的算法是对于 [Jaromír Janisch 写的 Sumtree](https://github.com/jaara/AI-blog/blob/master/SumTree.py) 的修改版.

```python
class SumTree(object):
    # 建立 tree 和 data,
    # 因为 SumTree 有特殊的数据结构,
    # 所以两者都能用一个一维 np.array 来存储
    def __init__(self, capacity):

    # 当有新 sample 时, 添加进 tree 和 data
    def add_new_priority(self, p, data):

    # 当 sample 被 train, 有了新的 TD-error, 就在 tree 中更新
    def update(self, tree_idx, p):

    # update 和 add_new_priority 时会调用这个功能
    def _propagate_change(self, tree_idx, change):

    # 抽取样本
    def get_leaf(self, lower_bound):

    # get_leaf 时调用这个
    def _retrieve(self, lower_bound, parent_idx=0):

    # 获取 sum(p)
    @property
    def root_priority(self):
```

具体的代码在这里呈现的话比较累赘, 详细代码请去往我的 [Github对应的位置](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5.2_Prioritized_Replay_DQN/RL_brain.py#L18-L93)





<h4 class="tut-h4-pad" id="memory">Memory 类</h4>

这个 Memory 类也是基于 [Jaromír Janisch 所写的 Memory](https://github.com/jaara/AI-blog/blob/master/Seaquest-DDQN-PER.py) 进行了修改.

```python
class Memory(object):
    # 建立 SumTree 和各种参数
    def __init__(self, capacity):

    # 存储 sample
    def store(self, error, transition):

    # 抽取 sample
    def sample(self, n):

    # train 完被抽取的 samples 后更新在 tree 中的 samples
    def update(self, idx, error):

    # update 和 store 都会用到
    def _get_priority(self, error):
```

具体的代码在这里呈现的话比较累赘, 详细代码请去往我的 [Github对应的位置](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5.2_Prioritized_Replay_DQN/RL_brain.py#L96-L136)





<h4 class="tut-h4-pad" id="learn">更新方法</h4>


基于之前的 [DQN 代码](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5.1_Double_DQN/RL_brain.py),
我们做出以下修改. 我们将 class 的名字改成 `DQNPrioritiedReplay`, 为了对比 Natural DQN,
我们也保留原来大部分的 DQN 的代码. 我们在 `__init__` 中加一个 `prioritized` 参数来表示 DQN 是否具备 prioritized 能力.
为了对比的需要, 我们的 `tf.Session()` 也单独传入. 并移除原本在 DQN 代码中的这一句:

`self.sess.run(tf.global_variables_initializer())`

```python
class DQNPrioritiedReplay:
    def __init__(..., prioritized=True, sess=None)
        self.prioritized = prioritized
        ...
        if self.prioritized:
            self.memory = Memory(capacity=memory_size)
        else:
            self.memory = np.zeros((self.memory_size, n_features*2+2))

        if sess is None:
            self.sess = tf.Session()
            self.sess.run(tf.global_variables_initializer())
        else:
            self.sess = sess
```

<a href="/static/results/rl/4-6-3.png">
<img class="course-image" src="/static/results/rl/4-6-3.png">
</a>

搭建神经网络时, 我们发现 DQN with Prioritized replay 只多了一个 `ISWeights`, 这个正是[刚刚算法中](/tutorials/machine-learning/reinforcement-learning/4-6-prioritized-replay/#algorithm)提到的
`Importance-Sampling Weights`, 用来恢复被 Prioritized replay 打乱的抽样概率分布.

```python
class DQNPrioritizedReplay:
    def _build_net(self)
        ...
        # self.prioritized 时 eval net 的 input 多加了一个 ISWeights
        self.s = tf.placeholder(tf.float32, [None, self.n_features], name='s')  # input
        self.q_target = tf.placeholder(tf.float32, [None, self.n_actions], name='Q_target')  # for calculating loss
        if self.prioritized:
            self.ISWeights = tf.placeholder(tf.float32, [None, 1], name='IS_weights')

        ...
        # 为了得到 abs 的 TD error 并用于修改这些 sample 的 priority, 我们修改如下
        with tf.variable_scope('loss'):
            if self.prioritized:
                self.abs_errors = tf.reduce_sum(tf.abs(self.q_target - self.q_eval), axis=1)    # for updating Sumtree
                self.loss = tf.reduce_mean(self.ISWeights * tf.squared_difference(self.q_target, self.q_eval))
            else:
                self.loss = tf.reduce_mean(tf.squared_difference(self.q_target, self.q_eval))
```

因为和 Natural DQN 使用的 Memory 不一样, 所以在存储 transition 的时候方式也略不相同.

```python
class DQNPrioritizedReplay:
    def store_transition(self, s, a, r, s_):
        if self.prioritized:    # prioritized replay
            transition = np.hstack((s, [a, r], s_))
            max_p = np.max(self.memory.tree.tree[-self.memory.tree.capacity:])
            self.memory.store(max_p, transition)    # 新记忆优先度也高
        else:       # random replay
            if not hasattr(self, 'memory_counter'):
                self.memory_counter = 0
            transition = np.hstack((s, [a, r], s_))
            index = self.memory_counter % self.memory_size
            self.memory[index, :] = transition
            self.memory_counter += 1
```

接下来是相对于 [Natural DQN 代码](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5_Deep_Q_Network/RL_brain.py),
我们在 `learn()` 改变的部分也在如下展示.

```python
class DQNPrioritizedReplay:
    def learn(self):
        ...
        # 相对于 DQN 代码, 改变的部分
        if self.prioritized:
            tree_idx, batch_memory, ISWeights = self.memory.sample(self.batch_size)
        else:
            sample_index = np.random.choice(self.memory_size, size=self.batch_size)
            batch_memory = self.memory[sample_index, :]

        ...

        if self.prioritized:
            _, abs_errors, self.cost = self.sess.run([self._train_op, self.abs_errors, self.loss],
                                         feed_dict={self.s: batch_memory[:, :self.n_features],
                                                    self.q_target: q_target,
                                                    self.ISWeights: ISWeights})
            for i in range(len(tree_idx)):  # update priority
                idx = tree_idx[i]
                self.memory.update(idx, abs_errors[i])
        else:
            _, self.cost = self.sess.run([self._train_op, self.loss],
                                         feed_dict={self.s: batch_memory[:, :self.n_features],
                                                    self.q_target: q_target})

        ...
```




<h4 class="tut-h4-pad" id="result">对比结果</h4>

<img class="course-image" src="/static/results/rl/4-6-4.png">

运行我 Github 中的这个 [MountainCar 脚本](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5.2_Prioritized_Replay_DQN/run_MountainCar.py),
我们就不难发现, 我们都从两种方法最初拿到第一个 `R=+10` 奖励的时候算起, 看看经历过一次 `R=+10` 后, 他们有没有好好利用这次的奖励,
可以看出, 有 Prioritized replay 的可以高效的利用这些不常拿到的奖励, 并好好学习他们. 所以 Prioritized replay 会更快结束每个 episode, 很快就到达了小旗子.


