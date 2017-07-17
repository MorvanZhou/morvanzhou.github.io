---
youku_id:
youtube_id:
title: NEAT 强化学习
publish-date:
thumbnail: "/static/thumbnail/"
chapter: 3
---

* 学习资料:
  * [本节的全部代码](#)
  * [我制作的 什么是神经进化(即将制作) 动画简介](#)
  * NEAT 论文 ([Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf))
  * NEAT [Python 模块](http://neat-python.readthedocs.io/en/latest/neat_overview.html)

[上节内容]({% link _contents/tutorials/machine-learning/evolutionary-algorithm/3-02-neat-supervised-learning.md %}) 里,
我们见到了使用 NEAT 来进化出一个类似于监督学习中的神经网络, 这次我们用 NEAT 来做强化学习 (Reinforcement Learning), 这个强化学习可是没有反向传播的神经网络哦,
有的只是一个不断进化 (还可能进化到主宰人类) 的神经网络!! (哈哈, 骗你的, 因为每次提到在电脑里进化, 联想到科幻片, 我就激动!)

立杆子的机器人最后学习的效果提前看:

<div align="center">
<video width="500" controls loop autoplay muted>
  <source src="/static/results/evolutionary-algorithm/3-3-0.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>
</div>

这个机器人的神经网络长这样:

<img class="course-image" src="/static/results/evolutionary-algorithm/3-2-0.png">


#### 本节内容包括:

* [gym 模拟环境](#gym)
* [CartPole 进化吧](#cartpole)



<h4 class="tut-h4-pad" id="gym">gym 模拟环境</h4>

[OpenAI gym](https://gym.openai.com/) 应该算是当下最流行的 强化学习练手模块了吧. 它有超级多的虚拟环境可以让你 plugin 你的 python 脚本.

<img class="course-image" src="/static/results/evolutionary-algorithm/3-3-1.png">


安装 gym 的方式也很简单, 大家可以直接参考我在之前做 强化学习 Reinforcement learning 教程中的[这节内容]({% link _contents/tutorials/machine-learning/reinforcement-learning/4-4-gym.md %}),
简单的介绍了如何安装 Gym. 如果还是遇到了问题, [这里](https://github.com/openai/gym#installation)或许能够找到答案.


<h4 class="tut-h4-pad" id="cartpole">CartPole 进化吧</h4>

这次进化的框架系统大致是这样的:

```python
def eval_genomes(genomes, config):
    # 这是我们为每一个 genome 计算 fitness 的功能, 在 NEAT 中必备.

def run():
    # 这是我们生成 population, 不断适者生存的地方

def evaluation():
    # 我们挑选出最好的个体进行可视化测试
```

在 neat 的 `config` [文件](#)中, 我想提到的几个地方是:

```shell
fitness_criterion     = max     # 按照适应度最佳的模式选个体
# 为了一直立杆子下去, 这一个封顶值设置成永远达不到,
# 具体看我在 eval_genomes 中如何计算 fitness 的
fitness_threshold     = 2.

activation_default      = relu      # 我挑选的 激活函数
```

有了这个 `config` 文件里面的信息, 我们就能创建网络和评估网络了. 和上次一样, 下面的功能对每一个个体生成一个神经网络,
然后把这个网络放在立杆子游戏中玩, 一个 generation 中我们对每一个 `genome` 的 `net` 测试 `GENERATION_EP` 这么多回合,
然后最后挑选这么多回合中总 `reward` 最少的那个回合当成这个 `net` 的 `fitness` (你可以想象这是木桶效应, 整体的效应取决于最差的那个结果).
然后要注意的是, `net.activate()` 之后我们会使用一个 `softmax` 激励函数来激活最后 output 的值. 将 output 转换成施加动作的概率.
然后我们挑选一个概率最大的动作.

```python
softmax = lambda logits: np.exp(logits)/np.sum(np.exp(logits))   # softmax function for choosing action

def eval_genomes(genomes, config):
    for genome_id, genome in genomes:
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        ep_r = []
        for ep in range(GENERATION_EP): # run many episodes for the genome in case it's lucky
            accumulative_r = 0.         # stage longer to get a greater episode reward
            observation = env.reset()
            for t in range(EP_STEP):
                action_logits = net.activate(observation)
                action = np.argmax(softmax(action_logits))
                observation_, reward, done, _ = env.step(action)
                accumulative_r += reward
                if done:
                    break
                observation = observation_
            ep_r.append(accumulative_r)
        genome.fitness = np.min(ep_r)/float(EP_STEP)    # depends on the minimum episode reward
```

不知道大家看到这里有没有想过, 如果我们能并行运算该多好. 所以, 我亲测失败. 原因是, `gym` 的环境不支持 `multiprocessing`. 如果你想多线程的话, 可以考虑使用
`threading`, 不过不保证效率有提高. 想知道为什么的话, [请看这里]({% link _contents/tutorials/python-basic/multiprocessing/4-comparison.md %}).

接下来我们就开始写 `run` 里面的内容了, 创建种群, 繁衍后代, 适者生存, 不适者淘汰.

```python
def run():
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation, CONFIG)
    pop = neat.Population(config)
    pop.run(eval_genomes, 10)       # train 10 generations
```

那些可视化种群进化图的代码, 请在我的 [github](#) 中看全套代码吧.

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
            a = np.argmax(softmax(net.activate(s)))
            s, r, done, _ = env.step(a)
            if done: break
```

这串代码的结果就是这节内容最上面的那个视频效果啦. `winner` 的神经网络进化成这样了. 不过你的生成的神经网络可能并不是长这样.
是时候还可能某个 `input` 都没有使用到. 就说明这个 `input` 的效用可能并不大.

<img class="course-image" src="/static/results/evolutionary-algorithm/3-2-0.png">

如果是实线, 如 B->1, B->2, 说明这个链接是 Enabled 的. 如果是虚线(点线), 如 B->A XOR B 就说明这个链接是 Disabled 的.
红色的线代表 weight <= 0, 绿色的线代表 weight > 0. 线的宽度和 weight 的大小有关.
