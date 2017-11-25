---
youku_id: XMjY1MzU2NTc2NA
youtube_id: DwrGHh9Nkvg
bilibili_id: 15990645
chapter: 5
title: Policy Gradients 思维决策 (Tensorflow)
thumbnail: "/static/thumbnail/rl/5.2_PG2.jpg"
publish-date: 2017-03-21
description: "接着上节内容, 我们来实现 RL_brain 的 PolicyGradient 部分, 这也是 RL 的大脑部分, 负责决策和思考."
post-headings:
  - 要代码主结构
  - 初始化
  - 建立 Policy 神经网络
  - 选行为
  - 存储回合
  - 学习
---


学习资料:
  * [全部代码](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/7_Policy_gradient_softmax){:target="_blank"}
  * [什么是 Policy Gradient 短视频]({% link _tutorials/machine-learning/ML-intro/4-07-PG.md %})
  * 本节内容的模拟视频效果:
    * CartPole: [Youtube](https://www.youtube.com/watch?v=z2-hn7iCjP0){:target="_blank"}, [优酷](http://v.youku.com/v_show/id_XMTg5NzgzNTk0NA==.html?f=27485743){:target="_blank"}
    * Mountain Car: [Youtube](https://www.youtube.com/watch?v=A8hXNykR0Fg){:target="_blank"}, [优酷](http://v.youku.com/v_show/id_XMTg5NzgzODQwNA==.html?f=27485743){:target="_blank"}
  * [强化学习实战]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})
  * 论文 [Policy gradient methods for reinforcement learning with function approximation.](https://papers.nips.cc/paper/1713-policy-gradient-methods-for-reinforcement-learning-with-function-approximation.pdf){:target="_blank"}


接着上节内容, 我们来实现 `RL_brain` 的 `PolicyGradient` 部分, 这也是 RL 的大脑部分, 负责决策和思考.




{% include assign-heading.html %}

用基本的 Policy gradient 算法, 和之前的 value-based 算法看上去很类似.

```python
class PolicyGradient:
    # 初始化 (有改变)
    def __init__(self, n_actions, n_features, learning_rate=0.01, reward_decay=0.95, output_graph=False):

    # 建立 policy gradient 神经网络 (有改变)
    def _build_net(self):

    # 选行为 (有改变)
    def choose_action(self, observation):

    # 存储回合 transition (有改变)
    def store_transition(self, s, a, r):

    # 学习更新参数 (有改变)
    def learn(self, s, a, r, s_):

    # 衰减回合的 reward (新内容)
    def _discount_and_norm_rewards(self):
```

{% include assign-heading.html %}

初始化时, 我们需要给出这些参数, 并创建一个神经网络.

```python
class PolicyGradient:
    def __init__(self, n_actions, n_features, learning_rate=0.01, reward_decay=0.95, output_graph=False):
        self.n_actions = n_actions
        self.n_features = n_features
        self.lr = learning_rate     # 学习率
        self.gamma = reward_decay   # reward 递减率

        self.ep_obs, self.ep_as, self.ep_rs = [], [], []    # 这是我们存储 回合信息的 list

        self._build_net()   # 建立 policy 神经网络

        self.sess = tf.Session()

        if output_graph:    # 是否输出 tensorboard 文件
            # $ tensorboard --logdir=logs
            # http://0.0.0.0:6006/
            # tf.train.SummaryWriter soon be deprecated, use following
            tf.summary.FileWriter("logs/", self.sess.graph)

        self.sess.run(tf.global_variables_initializer())

```


{% include assign-heading.html %}

这次我们要建立的神经网络是这样的:

{% include tut-image.html image-name="5-2-1.png" %}

因为这是强化学习, 所以神经网络中并没有我们熟知的监督学习中的 y label. 取而代之的是我们选的 action.

```python
class PolicyGradient:
    def __init__(self, n_actions, n_features, learning_rate=0.01, reward_decay=0.95, output_graph=False):
        ...
    def _build_net(self):
        with tf.name_scope('inputs'):
            self.tf_obs = tf.placeholder(tf.float32, [None, self.n_features], name="observations")  # 接收 observation
            self.tf_acts = tf.placeholder(tf.int32, [None, ], name="actions_num")   # 接收我们在这个回合中选过的 actions
            self.tf_vt = tf.placeholder(tf.float32, [None, ], name="actions_value") # 接收每个 state-action 所对应的 value (通过 reward 计算)

        # fc1
        layer = tf.layers.dense(
            inputs=self.tf_obs,
            units=10,   # 输出个数
            activation=tf.nn.tanh,  # 激励函数
            kernel_initializer=tf.random_normal_initializer(mean=0, stddev=0.3),
            bias_initializer=tf.constant_initializer(0.1),
            name='fc1'
        )
        # fc2
        all_act = tf.layers.dense(
            inputs=layer,
            units=self.n_actions,   # 输出个数
            activation=None,    # 之后再加 Softmax
            kernel_initializer=tf.random_normal_initializer(mean=0, stddev=0.3),
            bias_initializer=tf.constant_initializer(0.1),
            name='fc2'
        )

        self.all_act_prob = tf.nn.softmax(all_act, name='act_prob')  # 激励函数 softmax 出概率

        with tf.name_scope('loss'):
            # 最大化 总体 reward (log_p * R) 就是在最小化 -(log_p * R), 而 tf 的功能里只有最小化 loss
            neg_log_prob = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=all_act, labels=self.tf_acts) # 所选 action 的概率 -log 值
            # 下面的方式是一样的:
            # neg_log_prob = tf.reduce_sum(-tf.log(self.all_act_prob)*tf.one_hot(self.tf_acts, self.n_actions), axis=1)
            loss = tf.reduce_mean(neg_log_prob * self.tf_vt)  # (vt = 本reward + 衰减的未来reward) 引导参数的梯度下降

        with tf.name_scope('train'):
            self.train_op = tf.train.AdamOptimizer(self.lr).minimize(loss)
```

这里有必要解释一下为什么我们使用的 `loss= -log(prob)*vt` 当做 loss,
因为下面有很多评论说这里不理解.
简单来说, 上面提到了两种形式来计算 `neg_log_prob`, 这两种形式是一模一样的, 只是第二个是第一个的展开形式. 如果你仔细看第一个形式, 这不就是在神经网络分类问题中的 cross-entropy 嘛!
使用 softmax 和神经网络的最后一层 logits 输出和真实标签 (`self.tf_acts`) 对比的误差. 并将神经网络的参数按照这个真实标签改进.
这显然和一个分类问题没有太多区别. 我们能将这个 `neg_log_prob` 理解成 cross-entropy 的分类误差. 分类问题中的标签是真实 x 对应的 y,
而我们 Policy gradient 中, x 是 state, y 就是它按照这个 x 所做的动作号码. 所以也可以理解成, 它按照 x 做的动作永远是对的 (出来的动作永远是正确标签),
它也永远会按照这个 "正确标签" 修改自己的参数. 可是事实却不是这样, 他的动作不一定都是 "正确标签", 这就是强化学习(Policy gradient)和监督学习(classification)的不同.

为了确保这个动作真的是 "正确标签", 我们的 loss 在原本的 cross-entropy 形式上乘以 `vt`, 用 `vt` 来告诉这个 cross-entropy 算出来的梯度是不是一个值得信任的梯度.
如果 `vt` 小, 或者是负的, 就说明这个梯度下降是一个错误的方向, 我们应该向着另一个方向更新参数, 如果这个 `vt` 是正的, 或很大, `vt` 就会称赞 cross-entropy 出来的梯度,
并朝着这个方向梯度下降. 下面有一张从 [karpathy 大神](http://karpathy.github.io/2016/05/31/rl/){:target="_blank"} 网页上扣下来的图, 也正是阐述的这个思想.


{% include tut-image.html image-name="5-2-4.png" %}

而不明白为什么是 `loss=-log(prob)*vt` 而不是 `loss=-prob*vt` 的朋友们, 下面留言有很多问道这个问题.
原因是这里的 `prob` 是从 softmax 出来的, 而计算神经网络里的所有参数梯度, 使用到的就是 cross-entropy,
然后将这个梯度乘以 `vt` 来控制梯度下降的方向和力度. 而我上面使用 `neg_log_prob` 这个名字只是为了区分这不是真正意义上的 cross-entropy, 因为标签不是真标签.
我在下面提供一些扩展链接.

* [Loss 的定义](http://cs231n.github.io/neural-networks-2/#losses){:target="_blank"}
* [karpathy 大神的 PG 算法说明](http://karpathy.github.io/2016/05/31/rl/){:target="_blank"}
* [David Silver 的 PG 课件](http://www0.cs.ucl.ac.uk/staff/D.Silver/web/Teaching_files/pg.pdf){:target="_blank"}












{% include assign-heading.html %}

这个行为不再是用 Q value 来选定的, 而是用概率来选定. 即使不用 epsilon-greedy, 也具有一定的随机性.

```python
class PolicyGradient:
    def __init__(self, n_actions, n_features, learning_rate=0.01, reward_decay=0.95, output_graph=False):
        ...
    def _build_net(self):
        ...
    def choose_action(self, observation):
        prob_weights = self.sess.run(self.all_act_prob, feed_dict={self.tf_obs: observation[np.newaxis, :]})    # 所有 action 的概率
        action = np.random.choice(range(prob_weights.shape[1]), p=prob_weights.ravel())  # 根据概率来选 action
        return action
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

这一部很简单, 就是将这一步的 `observation`, `action`, `reward` 加到列表中去.
因为本回合完毕之后要清空列表, 然后存储下一回合的数据, 所以我们会在 `learn()` 当中进行清空列表的动作.

```python
class PolicyGradient:
    def __init__(self, n_actions, n_features, learning_rate=0.01, reward_decay=0.95, output_graph=False):
        ...
    def _build_net(self):
        ...
    def choose_action(self, observation):
        ...
    def store_transition(self, s, a, r):
        self.ep_obs.append(s)
        self.ep_as.append(a)
        self.ep_rs.append(r)
```

{% include assign-heading.html %}

本节的 `learn()` 很简单, 首先我们要对这回合的所有 `reward` 动动手脚, 使他变得更适合被学习.
第一就是随着时间推进, 用 `gamma` 衰减未来的 `reward`, 然后为了一定程度上减小 policy gradient 回合 variance,
我们标准化回合的 state-action value [依据在 Andrej Karpathy 的 blog](http://karpathy.github.io/2016/05/31/rl/){:target="_blank"}.

```python
class PolicyGradient:
    def __init__(self, n_actions, n_features, learning_rate=0.01, reward_decay=0.95, output_graph=False):
        ...
    def _build_net(self):
        ...
    def choose_action(self, observation):
        ...
    def store_transition(self, s, a, r):
        ...
    def learn(self):
        # 衰减, 并标准化这回合的 reward
        discounted_ep_rs_norm = self._discount_and_norm_rewards()   # 功能再面

        # train on episode
        self.sess.run(self.train_op, feed_dict={
             self.tf_obs: np.vstack(self.ep_obs),  # shape=[None, n_obs]
             self.tf_acts: np.array(self.ep_as),  # shape=[None, ]
             self.tf_vt: discounted_ep_rs_norm,  # shape=[None, ]
        })

        self.ep_obs, self.ep_as, self.ep_rs = [], [], []    # 清空回合 data
        return discounted_ep_rs_norm    # 返回这一回合的 state-action value
```

我们再来看看这个 `discounted_ep_rs_norm` 到底长什么样, 不知道大家还记不记得上节内容的这一段:

```python
vt = RL.learn() # 学习, 输出 vt, 我们下节课讲这个 vt 的作用

if i_episode == 0:
    plt.plot(vt)    # plot 这个回合的 vt
    plt.xlabel('episode steps')
    plt.ylabel('normalized state-action value')
    plt.show()
```

我们看看这一段的输出, `vt` 也就是 `discounted_ep_rs_norm`, 看他是怎么样诱导我们的 gradient descent.

{% include tut-image.html image-name="5-2-2.png" %}

可以看出, 左边一段的 `vt` 有较高的值, 右边较低, 这就是 `vt` 在说:

**"请重视我这回合开始时的一系列动作, 因为前面一段时间杆子还没有掉下来.
而且请惩罚我之后的一系列动作, 因为后面的动作让杆子掉下来了"** 或者是

**"我每次都想让这个动作在下一次增加被做的可能性 (`grad(log(Policy))`),
但是增加可能性的这种做法是好还是坏呢?
这就要由 `vt` 告诉我了, 所以后段时间的 `增加可能性` 做法并没有被提倡, 而前段时间的
 `增加可能性` 做法是被提倡的."**

这样 `vt` 就能在这里 `loss = tf.reduce_mean(log_prob * self.tf_vt)`
诱导 gradient descent 朝着正确的方向发展了.

如果你玩了下 `MountainCar` 的模拟程序, 你会发现 `MountainCar` 模拟程序中的 `vt` 长这样:

{% include tut-image.html image-name="5-2-3.png" %}

这张图在说: **"请重视我这回合最后的一系列动作, 因为这一系列动作让我爬上了山.
而且请惩罚我开始的一系列动作, 因为这些动作没能让我爬上山".**

也是通过这些 `vt` 来诱导梯度下降的方向.

最后是如何用算法实现对未来 reward 的衰减.

```python
class PolicyGradient:
    def __init__(self, n_actions, n_features, learning_rate=0.01, reward_decay=0.95, output_graph=False):
        ...
    def _build_net(self):
        ...
    def choose_action(self, observation):
        ...
    def store_transition(self, s, a, r):
        ...
    def learn(self):
        ...
    def _discount_and_norm_rewards(self):
        # discount episode rewards
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in reversed(range(0, len(self.ep_rs))):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add

        # normalize episode rewards
        discounted_ep_rs -= np.mean(discounted_ep_rs)
        discounted_ep_rs /= np.std(discounted_ep_rs)
        return discounted_ep_rs
```

如果想一次性看到全部代码, 请去我的 [Github](https://github.com/MorvanZhou/Reinforcement-learning-with-tensorflow/tree/master/contents/7_Policy_gradient_softmax){:target="_blank"}

