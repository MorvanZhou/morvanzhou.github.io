---
youku_id: XMzA0MTEzNzAzNg
youtube_id: ZgFzC7uBShM
bilibili_id: 15986215
title: NEAT 强化学习
publish-date: 2017-09-23
thumbnail: "/static/thumbnail/evolutionary-algorithm/43neat.jpg"
chapter: 4
description: "我们见到了使用 NEAT 来进化出一个类似于监督学习中的神经网络, 这次我们用 NEAT 来做强化学习 (Reinforcement Learning), 这个强化学习可是没有反向传播的神经网络哦,
有的只是一个不断进化 (还可能进化到主宰人类) 的神经网络!! (哈哈, 骗你的, 因为每次提到在电脑里进化, 联想到科幻片, 我就激动!)
立杆子的机器人最后学习的效果提前看"
post-headings:
  - 要点
  - gym 模拟环境
  - CartPole 进化吧
  - Recurrent link 和 node
---

学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/tree/master/tutorial-contents/Using%20Neural%20Nets/NEAT_gym){:target="_blank"}
  * [我制作的 什么是神经进化 动画简介]({% link _tutorials/machine-learning/ML-intro/5-03-neuro-evolution.md %})
  * [什么是遗传算法]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %})
  * [什么是进化策略]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})
  * NEAT 论文 ([Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf){:target="_blank"})
  * NEAT [Python 模块](http://neat-python.readthedocs.io/en/latest/neat_overview.html){:target="_blank"}

 {% include assign-heading.html %}

[上节内容]({% link _tutorials/machine-learning/evolutionary-algorithm/4-02-neat-supervised-learning.md %}) 里,
我们见到了使用 NEAT 来进化出一个类似于监督学习中的神经网络, 这次我们用 NEAT 来做强化学习 (Reinforcement Learning), 这个强化学习可是没有反向传播的神经网络哦,
有的只是一个不断进化 (还可能进化到主宰人类) 的神经网络!! (哈哈, 骗你的, 因为每次提到在电脑里进化, 联想到科幻片, 我就激动!)

立杆子的机器人最后学习的效果提前看:

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/evolutionary-algorithm/4-3-0.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

这个机器人的神经网络长这样:

{% include tut-image.html image-name="4-2-0.png" %}



 {% include assign-heading.html %}

[OpenAI gym](https://gym.openai.com/){:target="_blank"} 应该算是当下最流行的 强化学习练手模块了吧. 它有超级多的虚拟环境可以让你 plugin 你的 python 脚本.

{% include tut-image.html image-name="4-3-1.png" %}


安装 gym 的方式也很简单, 大家可以直接参考我在之前做 强化学习 Reinforcement learning 教程中的[这节内容]({% link _tutorials/machine-learning/reinforcement-learning/4-4-gym.md %}),
简单的介绍了如何安装 Gym. 如果还是遇到了问题, [这里](https://github.com/openai/gym#installation){:target="_blank"}或许能够找到答案.

{% include google-in-article-ads.html %}

 {% include assign-heading.html %}

这次进化的框架系统大致是这样的:

```python
def eval_genomes(genomes, config):
    # 这是我们为每一个 genome 计算 fitness 的功能, 在 NEAT 中必备.

def run():
    # 这是我们生成 population, 不断适者生存的地方

def evaluation():
    # 我们挑选出最好的个体进行可视化测试
```

在 neat 的 `config` [文件](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/NEAT_gym/config){:target="_blank"}中, 我想提到的几个地方是:

```shell
fitness_criterion     = max     # 按照适应度最佳的模式选个体
# 为了一直立杆子下去, 这一个封顶值设置成永远达不到,
# 具体看我在 eval_genomes 中如何计算 fitness 的
fitness_threshold     = 2.

activation_default      = relu      # 我挑选的 激活函数

# network 输入输出个数
num_hidden              = 0
num_inputs              = 4
num_outputs             = 2
```

有了这个 `config` 文件里面的信息, 我们就能创建网络和评估网络了. 和上次一样, 下面的功能对每一个个体生成一个神经网络,
然后把这个网络放在立杆子游戏中玩, 一个 generation 中我们对每一个 `genome` 的 `net` 测试 `GENERATION_EP` 这么多回合,
然后最后挑选这么多回合中总 `reward` 最少的那个回合当成这个 `net` 的 `fitness` (你可以想象这是木桶效应, 整体的效应取决于最差的那个结果).
然后要注意的是, `net.activate()` output 的是动作的值.
然后我们挑选一个值最大的动作.

```python
def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        ep_r = []
        for ep in range(GENERATION_EP): # run many episodes for the genome in case it's lucky
            accumulative_r = 0.         # stage longer to get a greater episode reward
            observation = env.reset()
            for t in range(EP_STEP):
                action_values = net.activate(observation)
                action = np.argmax(action_values)
                observation_, reward, done, _ = env.step(action)
                accumulative_r += reward
                if done:
                    break
                observation = observation_
            ep_r.append(accumulative_r)
        genome.fitness = np.min(ep_r)/float(EP_STEP)    # depends on the minimum episode reward
```

不知道大家看到这里有没有想过, 如果我们能并行运算该多好. 所以, 我亲测失败. 原因是, `gym` + `neat` 的环境不方便运行 `multiprocessing`. 如果你想多线程的话, 可以考虑使用
`threading`, 不过不保证效率有提高. 想知道为什么的话, [请看这里]({% link _tutorials/python-basic/multiprocessing/4-comparison.md %}).

接下来我们就开始写 `run` 里面的内容了, 创建种群, 繁衍后代, 适者生存, 不适者淘汰.

```python
def run():
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation, CONFIG)
    pop = neat.Population(config)
    pop.run(eval_genomes, 10)       # train 10 generations
```

那些可视化种群进化图的代码, 请在我的 [github](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/NEAT_gym/run_cartpole.py){:target="_blank"} 中看全套代码吧.

最后我们挑选一下保存的 `checkpoint` 文件, 展示出最强神经网络的样子吧.

```python
def evaluation():
    p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-%i' % CHECKPOINT)
    winner = p.run(eval_genomes, 1)     # find the winner in restored population
    net = neat.nn.FeedForwardNetwork.create(winner, p.config)
    while True:
        s = env.reset()
        while True:
            env.render()
            a = np.argmax(net.activate(s))
            s, r, done, _ = env.step(a)
            if done: break
```

这串代码的结果就是这节内容最上面的那个视频效果啦. `winner` 的神经网络进化成这样了. 不过你的生成的神经网络可能并不是长这样.
有时候还可能某个 `input` 都没有使用到. 就说明这个 `input` 的效用可能并不大.

{% include tut-image.html image-name="4-2-0.png" %}

如果是实线, 如 B->1, B->2, 说明这个链接是 Enabled 的. 如果是虚线(点线), 如 B->A XOR B 就说明这个链接是 Disabled 的.
红色的线代表 weight <= 0, 绿色的线代表 weight > 0. 线的宽度和 weight 的大小有关.

 {% include assign-heading.html %}

如果修改一下 `config` [文件](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/NEAT_gym/config){:target="_blank"}里面的参数, 比如下面的 `feed_forward = True` 改成 `False`, 我们就允许网络能产生 recurrent 节点或者链接.
这样的设置能使网络产生记忆功能. 就像循环神经网络那样. 神经网络的形式结构就能更加多种多样. 不过这里的 recurrent 貌似是和我们一般见到的 Recurrent Neural Network 有所不同,
我们通常说的 RNN 是通过一个 hidden state 来传递记忆, 而 NEAT 中的 Recurrent 是通过一种 "延迟刷新的形式" (不知道这样说对不对, 我是细看了一遍 NEAT-python 的底层代码发现的),
每一个时间点每个节点只接收这一时刻传来的信息. 比如下面第一张图中, 现在所有节点都为0, 如果我先更新 `node3`, 由于接收到了 `act2=0`,  `node3` 还是会为0. 但是如果是先更新 `act2`, 等 `act2` 有值了再更新 `node3`,
那 `node3` 这时刻也会有值. 如果这是一个 feedforward net, 更新 link/node 的顺序十分重要, 上述情况肯定会出问题的. 不过在这种版本中的 recurrent, 程序不知道顺序,
所以每次都 copy 一份所有 node 的值, 用上一步的 node 的值进行这一步的操作, 这样进行 recurrent 的操作.

```shell
feed_forward            = False
```

将所有原来的 `net = neat.nn.FeedForwardNetwork` 改成 `neat.nn.RecurrentNetwork`, 就能按上面所说的方式进行 recurrent 操作了.

```python
# net = neat.nn.FeedForwardNetwork.create(winner, p.config)
net = neat.nn.RecurrentNetwork.create(genome, config)
```

这样我们就能发现, 产生的网络还能是这样, 注意箭头的方向和位置.

{% include tut-image.html image-name="4-3-2.png" %}

{% include tut-image.html image-name="4-3-3.png" %}


最后, 在这里提一下, 还有一些根据 NEAT 改良的算法. 比如
* [HyperNEAT (A Hypercube-Based Encoding for Evolving Large-Scale Neural Networks)](http://axon.cs.byu.edu/Dan/778/papers/NeuroEvolution/stanley3**.pdf){:target="_blank"}, 使用 NEAT 形式生成 CPPN 的网络, 用 CPPN 进行 indirect encoding 生成更大更复杂的神经网络, 但是后者的网络结构的 capacity 不能改变;
* [ES-HyperNEAT (An Enhanced Hypercube-Based Encoding for Evolving the Placement, Density and Connectivity of Neurons)](http://eplex.cs.ucf.edu/papers/risi_alife12.pdf){:target="_blank"}, 解决上面提到的网络结构 capacity 不可变问题.

[下一节]({% link _tutorials/machine-learning/evolutionary-algorithm/4-04-evolution-strategy-reinforcement-learning.md %})我们会关注使用 Evolution Strategy 来做大规模强化学习.