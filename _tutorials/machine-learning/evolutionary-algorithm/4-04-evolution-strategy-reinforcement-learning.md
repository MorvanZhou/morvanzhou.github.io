---
youku_id: XMzA0MTMxNDcyOA
youtube_id: x-svcNmIMBs
bilibili_id: 15986593
title: Evolution Strategy 强化学习
publish-date: 2017-09-23
thumbnail: "/static/thumbnail/evolutionary-algorithm/44es.jpg"
chapter: 4
description: "上节内容里,
我们见到了使用 NEAT 来进化出一个会立杆子的机器人. 这次, 我们使用另一种进化算法 Evolution Strategy (后面都用简称 ES 代替) 来实现大规模强化学习.
如果你的计算机是多核的, 我们还能将模拟程序并行到你多个核上去. 如果我用一句话概括强化学习上的 ES : 在自己附近生宝宝, 让自己更像那些表现好的宝宝
本节内容提前看:"
post-headings:
  - 要点
  - 算法介绍
  - gym模拟环境
  - Python实践
---


学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/Evolution%20Strategy%20with%20Neural%20Nets.py){:target="_blank"}
  * [我制作的 什么是神经进化 动画简介]({% link _tutorials/machine-learning/ML-intro/5-03-neuro-evolution.md %})
  * [什么是遗传算法]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %})
  * [什么是进化策略]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})
  * 论文 [Evolution Strategies as a Scalable Alternative to Reinforcement Learning](https://arxiv.org/abs/1703.03864){:target="_blank"}

 {% include assign-heading.html %}

[上节内容]({% link _tutorials/machine-learning/evolutionary-algorithm/4-03-neat-reinforcement-learning.md %}) 里,
我们见到了使用 NEAT 来进化出一个会立杆子的机器人. 这次, 我们使用另一种进化算法 Evolution Strategy (后面都用简称 ES 代替) 来实现大规模强化学习.
如果你的计算机是多核的, 我们还能将模拟程序并行到你多个核上去. **如果我用一句话概括强化学习上的 ES : 在自己附近生宝宝, 让自己更像那些表现好的宝宝**

本节内容提前看:

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/evolutionary-algorithm/4-4-0.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>



 {% include assign-heading.html %}

{% include tut-image.html image-name="4-4-1.png" %}

简单来说, 这个算法就是在不断地试错, 然后每一次试错后, 让自己更靠近到那些返回更多奖励的尝试点. 如果大家对[强化学习的 Policy Gradient]({% link _tutorials/machine-learning/reinforcement-learning/5-1-policy-gradient-softmax1.md %})
有了解的话, 我们就来在这里说说 Policy Gradient (PG) 和 Evolution Strategy (ES) 的不同之处.

PG 和 ES 是一对双胞胎兄弟, 他们非常像, 不过他们最重要的一点差别就是. **PG 需要进行误差反向传播, 而 ES 不用**. 在行为的策略上, **PG 是扰动 Action**, 不同的 action 带来不同的 reward,
通过 reward 大小对应上 action 来计算 gradient, 再反向传递 gradient. 但是 **ES 是扰动 神经网络中的 Parameters**, 不同的 parameters 带来不同的 reward,
通过 reward 大小对应上 parameters 来按比例更新原始的 parameters.

[OpenAI 官网](https://blog.openai.com/evolution-strategies/){:target="_blank"}上对这种算法的最简单 Python 诠释:

```python
# 最简单的诠释: 找到 solution 中的值
import numpy as np
solution = np.array([0.5, 0.1, -0.3])
def f(w): return -np.sum((w - solution)**2)

npop = 50      # 种群数
sigma = 0.1    # 噪点标准差
alpha = 0.001  # 学习率
w = np.random.randn(3) # 对 solution 的初始猜测
for i in range(300):
  N = np.random.randn(npop, 3)  # 产生噪点
  R = np.zeros(npop)
  for j in range(npop):
    w_try = w + sigma*N[j]
    R[j] = f(w_try)             # 得到环境奖励
  A = (R - np.mean(R)) / np.std(R)  # 归一化奖励
  w = w + alpha/(npop*sigma) * np.dot(N.T, A)   # 更新参数
```






 {% include assign-heading.html %}

[OpenAI gym](https://gym.openai.com/){:target="_blank"} 应该算是当下最流行的 强化学习练手模块了吧. 它有超级多的虚拟环境可以让你 plugin 你的 python 脚本.

{% include tut-image.html image-name="4-3-1.png" %}
安装 gym 的方式也很简单, 大家可以直接参考我在之前做 强化学习 Reinforcement learning 教程中的[这节内容]({% link _tutorials/machine-learning/reinforcement-learning/4-4-gym.md %}),
简单的介绍了如何安装 Gym. 如果还是遇到了问题, [这里](https://github.com/openai/gym#installation){:target="_blank"}或许能够找到答案.


{% include google-in-article-ads.html %}


 {% include assign-heading.html %}

这次进化的框架系统大致是这样的:

```python
def get_reward():
    # 机器人在环境中玩, 我们会通过 CPU 并行计算这个功能

def build_net():
    # 建网络

def train():
    # 让儿孙们尽情在平行世界玩耍
    rewards = [get_reward() for i in range(N_KID)]
    # 再用 rewards 更新 net

build_net()
for g in range(N_GENERATION):
    train()
```

接下来我们将会往这个框架上加很多东西. 如果觉得我太啰嗦了, 你也可以直接跳到[这份完整代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/Evolution%20Strategy%20with%20Neural%20Nets.py){:target="_blank"}
研究. 相比这份代码, 我下面说的要简单一点(为了方便理解). 首先, 我们使用 `numpy` 来搭建神经网络.
其实我发现, 用 `tensorflow` 这种模块来建网络可能比较麻烦, 所以为了更直观, 我就用 `numpy` 好了.

```python
def build_net():
    def linear(n_in, n_out):  # network linear layer
        w = np.random.randn(n_in * n_out).astype(np.float32) * .1
        b = np.random.randn(n_out).astype(np.float32) * .1
        return (n_in, n_out), np.concatenate((w, b))
    s0, p0 = linear(CONFIG['n_feature'], 30)
    s1, p1 = linear(30, 20)
    s2, p2 = linear(20, CONFIG['n_action'])
    return [s0, s1, s2], np.concatenate((p0, p1, p2))
```

这里我们搭建了3层网络, 注意我并没有让 `w` 和 `b` 变成矩阵, 因为在 ES 中, 我觉得1维的参数比较好进行加噪点处理.
之后我们在并行的时候再将参数变成矩阵形式. 所以这个地方, 我也 `return` 了各层的 `shape` 为了之后变矩阵.

我们将使用 `multiprocessing` 这个模块来实现 CPU 的并行, 有兴趣了解 python 并行的朋友, 我有一个非常简单的 `multiprocessing` 的[教程](https://morvanzhou.github.io/tutorials/python-basic/multiprocessing/){:target="_blank"}. 并行的时候传给每个 CPU 的数据越少, 运行越快,
所以与其将像这样的 `np.random.randn(noise.size)` array 噪点数据传入其他 CPU, 还不如在其他 CPU 运算的时候在组装这些噪点就好.
因为我们只需要给 CPU 传入一个数 `noise seed` 来代替庞大的 `array`, 用 `seed` 来伪随机生成 `array`, 这样能加速你的运算.
在更新网络的时候再用同样的 `seed` 伪随机构造同样的 `array` 更新就行. 虽然创建了两遍 `array`, 但是这还是比将 `noise array` 传入其他 CPU 快.

```python
def train(net_shapes, net_params, pool):
    # 生成噪点的 seed
    noise_seed = np.random.randint(0, 2 ** 32 - 1, size=N_KID, dtype=np.uint32) # 限制 seed 的范围.

    # 用多进程完成 get_reward 功能
    jobs = [pool.apply_async(get_reward, (这里是get_reward需要的数据, 比如 seed))
            for k_id in range(N_KID)]
    rewards = np.array([j.get() for j in jobs])

    cumulative_update = np.zeros_like(net_params)       # initialize update values
    for k_id in range(N_KID):
        np.random.seed(noise_seed[k_id])                # reconstruct noise using seed
        cumulative_update += rewards[k_id] * np.random.randn(net_params.size)

    net_params = net_params + LR/(N_KID*SIGMA) * cumulative_update
    return net_params
```

上面的这个 `pool` 是我们用了 `multiprocessing.Pool` 生成的多进程池. 在[这个教程]({% link _tutorials/python-basic/multiprocessing/5-pool.md %})中有介绍.
拿到每个 `kid` 的 `reward` 后, 我们重新按照之前的 `seed` 组装 `noise`, 在进行 `net_params` 的更新.
但是你看到的这个版本的 `train()`  和我 [github](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/Evolution%20Strategy%20with%20Neural%20Nets.py){:target="_blank"}
中的不太一样, 因为 github 中使用的不是完完全全的 `reward` 来诱导更新.
而是使用了 `utility` 这个东西. 简单来说, 就是将 `reward` 排序, `reward` 最大的那个, 对应上 `utility` 的第一个,
反之, `reward` 最小的对应上 `utility` 最后一位. 而我们的 `utility` 长这样:

{% include tut-image.html image-name="4-4-2.png" %}

OpenAI 的 paper 当中提到这样会促进学习, 我想这样的效果应该和 normalize reward 的效果差不多. 我们就按 OpenAI 提到的方法来.

接下来要开始定义在平行的 CPU 中怎么样玩啦 `get_reward()`.

```python
def get_reward(shapes, params, env, ep_max_step, seed,):
    np.random.seed(seed)    # 使用 seed 按规律伪随机生成噪点
    params += SIGMA * np.random.randn(params.size)

    # 将 params 变成矩阵形式
    p = params_reshape(shapes, params)
    # 开始用 gym 模拟
    s = env.reset()
    ep_r = 0.
    for step in range(ep_max_step):
        a = get_action(p, s)    # 神经网络选择行为
        s, r, done, _ = env.step(a)
        ep_r += r
        if done: break
    return ep_r     # 返回回合奖励
```

同样, 上面的 `get_reward()` 也是简单版本的, 我 [github](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/Evolution%20Strategy%20with%20Neural%20Nets.py){:target="_blank"}
当中, 用了论文中提到的 `mirrored sampling` 这种方法 (论文名: [Mirrored Sampling and Sequential Selection for
Evolution Strategies](https://hal.inria.fr/inria-00530202/document)). 下面是这个论文中的图.

{% include tut-image.html image-name="4-4-3.png" %}

简单说, 我们会生成很多噪点, 与其完全随机, 还不如生成一些镜像的噪点. 那这些镜像噪点中,
大多数情况都是其中一个比另一个好, 所以总会有比较好的那个一个噪点, 我们就利用镜像中比较好的噪点, 加大幅度更新.

上面的就是 ES 的核心功能了, 其他的小功能, 我想, 只要你运行一下[我写的那个文件](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/Evolution%20Strategy%20with%20Neural%20Nets.py){:target="_blank"},
自己折腾一下, 就能轻松理解.
你在这里挑选不同的模拟环境:

```python
CONFIG = [
    dict(game="CartPole-v0", ......),
    dict(game="MountainCar-v0", ......),
    dict(game="Pendulum-v0", ......)
][2]        # 这里选择要运行的游戏
```

然后试试不同的参数:

```python
N_KID = 10                  # half of the training population
N_GENERATION = 5000         # training step
LR = .05                    # learning rate
SIGMA = .05                 # mutation strength or step size
```

你就能对 ES 有个大概的了解了. 注意, 每个游戏环境的运行时间长短, 取决于你的硬件, 比如你有2核, 像 `MountainCar` 可能运行5-10分钟吧.
`CartPole` 是最简单一个环境了, 学会的时间最短. 我用 MacBook 两核, 跑了不到30秒就能立起杆子了.
最终的效果也就和你在教程最开头看到的一样.

看好 OpenAI 的这种算法, 这套算法还比较原始和死板, 之后应该会有很多基于他的算法改进版. 我们拭目以待吧.