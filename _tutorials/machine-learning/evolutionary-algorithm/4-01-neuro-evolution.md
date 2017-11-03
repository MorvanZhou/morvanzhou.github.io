---
youku_id: XMzA0MDg2NTE5Mg
youtube_id: 0wWajjm9xj8
bilibili_id: 15985500
title: 神经进化
publish-date: 2017-09-23
thumbnail: "/static/thumbnail/evolutionary-algorithm/41es.jpg"
chapter: 4
description: "神经网络在当今是一种迅速发展的机器学习方式, 使用反向传播的神经网络更是被推向了一轮又一轮的高峰, 可是我们的视野请不要被反向传播的神经网络变得狭隘.
因为使用神经网络的机器学习方法还有这么一种叫做: 神经进化 (NeuroEvolution). 这种神经网络个人认为是更接近于生物的神经网络系统, 因为他和生物神经网络一样,
并没有反向传播这一步. 主导它解决问题的方式就是 进化, 而反向传播的神经网络解决问题的方式, 我们可以看作是 优化.
以下是我在 Youtube 中搜索看到大家都拿 Neuro Evolution 做的小实验. 看上去很高大上呀. 是不是又激情澎湃了."
post-headings:
  - 要点
  - 神经网络进化的方式
  - NEAT算法
  - 进化策略与神经网络
---


学习资料:
  * [我制作的 什么是神经进化 动画简介]({% link _tutorials/machine-learning/ML-intro/5-03-neuro-evolution.md %})
  * [什么是遗传算法]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %})
  * [什么是进化策略]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})
  * NEAT 论文 ([Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf){:target="_blank"})
  * OpenAI 的 [Evolution Strategies as a Scalable Alternative to Reinforcement Learning](https://blog.openai.com/evolution-strategies/){:target="_blank"}

 {% include assign-heading.html %}


神经网络在当今是一种迅速发展的机器学习方式, 使用反向传播的神经网络更是被推向了一轮又一轮的高峰, 可是我们的视野请不要被反向传播的神经网络变得狭隘.
因为使用神经网络的机器学习方法还有这么一种叫做: 神经进化 (NeuroEvolution). 这种神经网络个人认为是更接近于生物的神经网络系统, 因为他和生物神经网络一样,
并没有反向传播这一步. 主导它解决问题的方式就是 "进化", 而反向传播的神经网络解决问题的方式, 我们可以看作是 "优化".

以下是我在 Youtube 中搜索看到大家都拿 Neuro Evolution 做的小实验. 看上去很高大上呀. 是不是又激情澎湃了.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/evolutionary-algorithm/4-1-0.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

这些是上面实验的部分链接 ( [马里奥](https://www.youtube.com/watch?v=qv6UVOQ0F44){:target="_blank"}, [马里奥](https://www.youtube.com/watch?v=qv6UVOQ0F44){:target="_blank"},
 [微生物进化](https://www.youtube.com/watch?v=2kupe2ZKK58){:target="_blank"})

具体来说, Neuro Evolution 其实可以在很多方面来处理问题.
比如用它来做监督学习 (不过在这点上一般没有反向传播的神经网络学得快, 我们在下节内容里会做一个简单的监督学习例子),
还有可以拿它来做强化学习 (这和传统的强化学习 Reinforcement Learning 是有的一拼的,
在之后内容中我们使用 gym 模块来实现 NeuroEvolution 的强化学习).



 {% include assign-heading.html %}

说到进化, 我们之前看到了在遗传算法 (Genetic Algorithm) 中, 种群 `Population` 是通过不同的 DNA 配对, DNA 变异来实现物种的多样性,
然后通过自然选择 (Natural Selection), 繁衍下一代来实现 "适者生存, 不适者淘汰" 这条定律. 在神经网络中我们如何使用这种规律呢.

##### 尝试1: 固定神经网络形态 (Topology), 改变参数 (weight)

这种思路很简单, 我们有一个全连接神经网络, 像下图:

{% include tut-image.html image-name="4-1-1.png" %}

通过不断尝试变异, 修改链接中间的 weight, 改变神经网络的预测结果, 保留预测结果更准确的, 淘汰不那么准确的. 在这方面, OpenAI 在2017年做出了一个[有贡献的研究](https://blog.openai.com/evolution-strategies/){:target="_blank"}.
他们将进化策略 (Evolution Strategy) 衍生到神经网络, 然后不断进化神经网络中的参数. 他们的实验结果都能够媲美很多强化学习方法, 比如 [Q-learning]({% link _tutorials/machine-learning/ML-intro/4-03-q-learning.md %}),
[Policy Gradient]({% link _tutorials/machine-learning/ML-intro/4-07-PG.md %}).

##### 尝试2: 修改参数 和 形态

这种变化更多, 除了参数, 形态也是能够改变的. 我们待会要提到的 NEAT 算法就是这样一种. 因为能够变化形态, 所以在 NEAT 中, 并不存在神经层这种东西.

{% include tut-image.html image-name="4-1-2.jpg" %}


对比这两种不同的方式, 我们可以想象肯定是越能变化的, 结果会越好啦. 因为它能够探索的形态结构越多, 找到好方法的机会就越大.
而且还有一个优点就是, NEAT 可以最小化结构. 换句话说如果你拿一个 50 层的神经网络训练, 但是要解决的问题很简单, 并不会用到那么复杂的神经网络,
越多的层结构也是一种浪费, 所以用 NEAT 来自己探索需要使用多少链接, 他就能忽略那些没用的链接, 所以神经网络也就比较小, 而且小的神经网络运行也快嘛.


{% include google-in-article-ads.html %}

 {% include assign-heading.html %}

NEAT 是一种典型的[遗传算法]({% link _tutorials/machine-learning/evolutionary-algorithm/2-01-genetic-algorithm.md %}), 的算法详细解说可以参考这篇原始的 paper ([Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf){:target="_blank"}),
如果想偷懒, 这篇在 conference 上的浓缩版([Efficient evolution of neural network topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.cec02.pdf){:target="_blank"})也是很好的阅读材料.

简单来说, NEAT 有几个关键步骤,

* 使用 `创新号码 (Innovation ID)` 对神经网络的 `直接编码 (direct coding)`
* 根据 innovation ID 进行 `交叉配对 (crossover)`
* 对 `神经元 (node)`, `神经链接 (link)` 进行 `基因突变 (mutation)`
* 尽量保留 `生物多样性 (Speciation)` (有些不好的网络说不定突然变异成超厉害的)
* 通过初始化只有 input 连着 output 的神经网络来尽量减小神经网络的大小 (从最小的神经网络结构开始发展)

我们再来具体看看他是怎么 搭建/交叉/变异 神经网络的. 之后的用图都是上面提到的 paper 中的.


{% include tut-image.html image-name="4-1-3.png" %}


上面的图你可以想象成就是我们如何通过 DNA (图中的 Genome) 来编译出神经网络的. `Node genes` 很简单就是神经网络每个节点的定义.
哪些是输入, 哪些输出, 哪些是隐藏节点. `Connect. Genes` 则是对于每一个节点与节点的链接是什么样的形式, 从输入节点 (In) 到输出节点 (Out),
这个链接的参数 (weight) 是多少. 输出节点的值就是 `Out = In * weight`. 然后这条链接是要被使用 (Enabled) 还是不被使用 (DISAB). 最后就是这条链接专属的 创新号 (Innov)

通过上面的 Genome 我们就能搭建出那个神经网络了, 可以看出我们有一个 2-5 `DISAB` 的链接, 原因就是在2-5之间我们已经变异出了一个4节点.
所以2-5 是通过 4 相链接的, 这样我们就需要将原来的 2-5 链接 disable 掉.

{% include tut-image.html image-name="4-1-4.png" %}


关于变异呢. 我们可以有 `节点变异` 和 `链接变异`, 就和上图一样, 这个简单, 大家都看得出来. 但是要提的一点是,
如果新加的节点像 6 那样, 是在原有链接上的突变节点, 那么原来的 3-5 链接就要被 disable 掉.

{% include tut-image.html image-name="4-1-5.png" %}


再来就是 `crossover` 了, 两个神经网络 "交配" 啦. 这时你就发现原来 innovation number 在这里是这么重要.
两个父母通过 innovation number 对齐, 双方都有的 innovation, 我们就随机选一个, 如果双方有个方没有的 Innovation, 我们就直接全部遗传给后代.

之所以图上还出现了 "disjoint" 和 "excess" 的基因, 是因为在后面如果要区分种群不同度, 来选择要保留的种群的时候, 我们需要通过这个来计算, 计算方式我就不细提了,
大家知道有这么一回事就行.

好了, 通过上面的方式一步步进行, 好的神经网络被保留, 坏的杀掉. 我们的神经网络就能朝着正确的方形进化啦.

 {% include assign-heading.html %}

[Evolution Strategy]({% link _tutorials/machine-learning/evolutionary-algorithm/3-01-evolution-strategy.md %}) 相比较于 [Genetic Algorithm]({% link _tutorials/machine-learning/evolutionary-algorithm/2-01-genetic-algorithm.md %})
更加注重 mutation 的过程. 而且其中高度使用到了正态分布 (Normal distribution).

而 OpenAI 提出的能够替代强化学习的 ES 可以终结如下:

* 固定神经网络结构;
* 使用正态分布来扰动 (perturb) 神经网络链接参数;
* 使用扰动的网络在环境中收集奖励;
* 用奖励 (reward) 或者 效用 (utility) 来诱导参数更新幅度;

[下面的图](https://blog.openai.com/evolution-strategies/){:target="_blank"}是 OpenAI 用来诠释 ES 算法的精辟:

<a href="https://blog.openai.com/evolution-strategies/">
{% include tut-image.html image-name="4-1-6.png" %}
</a>

如果机器学习就是为了找到图中最红的地方, 那么 ES 就是在自己周围随机繁殖后代, 然后有些后代会靠近红色的地方, 有些不会.
那么我们就修改 ES 神经网络的参数, 让它更加像那些好后代的参数. 使用这种方式来越来越靠近红色.

接下来的内容我们就来用代码实现上述的两种途径.
