---
youku_id: XMjYxMTI2NTU2NA
youtube_id: OiEkaYpPHM0
bilibili_id: 15990095
chapter: 4
title: Dueling DQN (Tensorflow)
publish-date: 2017-03-08
thumbnail: "/static/thumbnail/rl/4.7_dueling_DQN.jpg"
description: "只要稍稍修改 DQN 中神经网络的结构, 就能大幅提升学习效果, 加速收敛. 这种新方法叫做
Dueling DQN. 用一句话来概括 Dueling DQN 就是. 它将每个动作的 Q 拆分成了 state 的 Value
加上 每个动作的 Advantage."
post-headings:
  - 要点
  - Dueling 算法
  - 更新方法
  - 对比结果
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/5.3_Dueling_DQN){:target="_blank"}
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 论文 [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581){:target="_blank"}

{% include assign-heading.html %}

**本篇教程是基于 Deep Q network (DQN) 的选学教程.
以下教程缩减了在 DQN 方面的介绍, 着重强调 Dueling DQN 和 DQN 在代码上不同的地方.
所以还没了解 DQN 的同学们, 有关于 DQN 的知识,
请从 [这个视频]({% link _tutorials/machine-learning/ML-intro/4-06-DQN.md %})
和 [这个Python教程]({% link _tutorials/machine-learning/reinforcement-learning/4-1-DQN1.md %}) 开始学习.**

只要稍稍修改 DQN 中神经网络的结构, 就能大幅提升学习效果, 加速收敛. 这种新方法叫做
Dueling DQN. 用一句话来概括 Dueling DQN 就是. 它将每个动作的 Q 拆分成了 state 的 Value
加上 每个动作的 Advantage.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/reinforcement-learning/Pendulum DQN.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>



{% include assign-heading.html %}

上一个 Paper 中的经典解释图片, 上者是一般的 DQN 的 Q值 神经网络.
下者就是 Dueling DQN 中的 Q值 神经网络了. 那具体是哪里不同了呢?

{% include tut-image.html image-name="4-7-1.png" %}

下面这个公式解释了不同之处. 原来 DQN 神经网络直接输出的是每种动作的 Q值,
而 Dueling DQN 每个动作的 Q值 是有下面的公式确定的.

{% include tut-image.html image-name="4-7-2.png" %}

它分成了这个 state 的值, 加上每个动作在这个 state 上的 advantage.
因为有时候在某种 state, 无论做什么动作, 对下一个 state 都没有多大影响. 比如 paper 中的这张图.


{% include tut-image.html image-name="4-7-3.png" %}

这是开车的游戏, 左边是 state value, 发红的部分证明了 state value 和前面的路线有关,
右边是 advantage, 发红的部分说明了 advantage 很在乎旁边要靠近的车子, 这时的动作会受更多
advantage 的影响. 发红的地方左右了自己车子的移动原则.






{% include assign-heading.html %}

下面的修改都是基于我之前写的 [DQN 代码](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5_Deep_Q_Network/RL_brain.py){:target="_blank"}.
这次修改的部分比较少. 我们把它们写在一块. 如果想直接看全部代码, [请戳这里](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/5.3_Dueling_DQN){:target="_blank"}.

{% include tut-image.html image-name="4-7-4.png" %}


```python
class DuelingDQN:
    def __init__(..., dueling=True, sess=None)
        ...
        self.dueling = dueling  # 会建立两个 DQN, 其中一个是 Dueling DQN
        ...
        if sess is None:    # 针对建立两个 DQN 的模式修改了 tf.Session() 的建立方式
            self.sess = tf.Session()
            self.sess.run(tf.global_variables_initializer())
        else:
            self.sess = sess
        ...

    def _build_net(self):
        def build_layers(s, c_names, n_l1, w_initializer, b_initializer):
            with tf.variable_scope('l1'):   # 第一层, 两种 DQN 都一样
                w1 = tf.get_variable('w1', [self.n_features, n_l1], initializer=w_initializer, collections=c_names)
                b1 = tf.get_variable('b1', [1, n_l1], initializer=b_initializer, collections=c_names)
                l1 = tf.nn.relu(tf.matmul(s, w1) + b1)

            if self.dueling:
                # Dueling DQN
                with tf.variable_scope('Value'):    # 专门分析 state 的 Value
                    w2 = tf.get_variable('w2', [n_l1, 1], initializer=w_initializer, collections=c_names)
                    b2 = tf.get_variable('b2', [1, 1], initializer=b_initializer, collections=c_names)
                    self.V = tf.matmul(l1, w2) + b2

                with tf.variable_scope('Advantage'):    # 专门分析每种动作的 Advantage
                    w2 = tf.get_variable('w2', [n_l1, self.n_actions], initializer=w_initializer, collections=c_names)
                    b2 = tf.get_variable('b2', [1, self.n_actions], initializer=b_initializer, collections=c_names)
                    self.A = tf.matmul(l1, w2) + b2

                with tf.variable_scope('Q'):    # 合并 V 和 A, 为了不让 A 直接学成了 Q, 我们减掉了 A 的均值
                    out = self.V + (self.A - tf.reduce_mean(self.A, axis=1, keep_dims=True))     # Q = V(s) + A(s,a)
            else:
                with tf.variable_scope('Q'):    # 普通的 DQN 第二层
                    w2 = tf.get_variable('w2', [n_l1, self.n_actions], initializer=w_initializer, collections=c_names)
                    b2 = tf.get_variable('b2', [1, self.n_actions], initializer=b_initializer, collections=c_names)
                    out = tf.matmul(l1, w2) + b2

            return out
        ...
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

对比的代码不在这里呈现, 如果想观看对比的详细代码, 请去往我的 [Github](https://github.com/MorvanZhou/tutorials/blob/master/Reinforcement_learning_TUT/5.3_Dueling_DQN/run_Pendulum.py){:target="_blank"}.

这次我们看看累积奖励 reward, 杆子立起来的时候奖励 = 0, 其他时候都是负值,
所以当累积奖励没有在降低时, 说明杆子已经被成功立了很久了.

{% include tut-image.html image-name="4-7-5.png" %}

我们发现当可用动作越高, 学习难度就越大, 不过 Dueling DQN 还是会比 Natural DQN 学习得更快. 收敛效果更好.

