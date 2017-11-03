---
youku_id: XMzA0MTAzMTM4OA
youtube_id: uEzhTYiQdh8
bilibili_id: 15985487
title: NEAT 监督学习
publish-date: 2017-09-23
thumbnail: "/static/thumbnail/evolutionary-algorithm/42neat.jpg"
chapter: 4
description: "我们这次就来实现 NEAT 的算法. 因为 NEAT 相比普通的反向传播神经网络更加复杂.
我也尝试着纯手工编写 NEAT 算法. 可是... 尝试了几天过后, 因为太麻烦了, 我就放弃了. 我先总结下自己淌过的水, 如果你有能力解决下面提到的几点, 恭喜你, 你真的特别厉害.
难点 (1) 有效的储存编码的神经网络 (我用 numpy 解决了); (2) 有效的解码并生成一个可以正向传播的神经网络 (由于没有层结构, 不能方便地使用矩阵 dot 点乘.
我查了很多方法, 但是觉得那些方法都有点复杂, 有的也没效率); (3) 可视化网络结构 (当然要可视化啦, 不可视化出来, 你怎么知道自己的神经网络长什么样, 不好 debug 了呀); (4)
NEAT 的 Recurrent link/node 不是通常说的 RNN, 处理形式不同.
如果不能, 其实也没关系, 有高手已经写好了 NEAT 的 Python 模块, 我们直接调用就行.
下图就是使用 NEAT 模块生成的一个神经网络, 看起来很优雅吧."
post-headings:
  - 要点
  - 安装 neat-python
  - 例子
---

学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/tree/master/tutorial-contents/Using%20Neural%20Nets/NEAT){:target="_blank"}
  * [我制作的 什么是神经进化 动画简介]({% link _tutorials/machine-learning/ML-intro/5-03-neuro-evolution.md %})
  * [什么是遗传算法]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %})
  * [什么是进化策略]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})
  * NEAT 论文 ([Evolving Neural Networks through Augmenting Topologies](http://nn.cs.utexas.edu/downloads/papers/stanley.ec02.pdf){:target="_blank"})
  * NEAT [Python 模块](http://neat-python.readthedocs.io/en/latest/neat_overview.html){:target="_blank"}

 {% include assign-heading.html %}

接着[上节介绍了神经进化的内容]({% link _tutorials/machine-learning/evolutionary-algorithm/4-01-neuro-evolution.md %}),
我们这次就来实现 NEAT 的算法. 因为 NEAT 相比普通的反向传播神经网络更加复杂.
我也尝试着纯手工编写 NEAT 算法. 可是... 尝试了几天过后, 因为太麻烦了, 我就放弃了. 我先总结下自己淌过的水, 如果你有能力解决下面提到的几点, 恭喜你, 你真的特别厉害.
我想提一下,如果用 NEAT 或者遗传算法做监督学习, 这会比用梯度的神经网络慢, 所以如果你想做监督学习, 梯度神经网络是你的最爱. 不过这个教程只是为了学习如何使用 NEAT,
之后我们再那它来做强化学习. 在强化学习上, NEAT 还是有优势的.

难点 (1) 有效的储存编码的神经网络 (我用 numpy 解决了); (2) 有效的解码并生成一个可以正向传播的神经网络 (由于没有层结构, 不能方便地使用矩阵 dot 点乘.
我查了很多方法, 但是觉得那些方法都有点复杂, 有的也没效率); (3) 可视化网络结构 (当然要可视化啦, 不可视化出来, 你怎么知道自己的神经网络长什么样, 不好 debug 了呀); (4)
NEAT 的 Recurrent link/node 不是通常说的 RNN, 处理形式不同.

如果不能, 其实也没关系, 有高手已经写好了 NEAT 的 [Python 模块](http://neat-python.readthedocs.io/en/latest/neat_overview.html){:target="_blank"}, 我们直接调用就行.
下图就是使用 NEAT 模块生成的一个神经网络, 看起来很优雅吧.

{% include tut-image.html image-name="4-2-0.png" %}




 {% include assign-heading.html %}

我们可以直接在 terminal 中输入:

```shell
# python2+ 版本
$ pip install neat-python

# python3+ 版本
$ pip3 install neat-python
```

目前的 neat 版本是 0.92, 如果之后安装不成功, 或者有所变化, 请参考这个[网页](http://neat-python.readthedocs.io/en/latest/installation.html){:target="_blank"}.

好了, 这就安装好了主程序了, 接下来为了可视化的效果, 我们还要检查一下是否有安装 `graphviz` 模块. 如果在你电脑中没有这个模块, 如果是 MacOS, 请直接 同上面的步骤 使用 pip install 就好了.
如果是 Linux, 使用 `sudo apt-get install graphviz` 就好.

不过我在实际运行中发现了这个报错 "RuntimeError: Make sure the Graphviz executables are on your system's path", 简单搜索了一下,

我是 MacOS, python3.5, 所以我在 terminal 中执行了 `$ brew install graphviz` 然后再重新用 `$ pip3 install graphviz` 就好了.

最后确认你的有安装 `matplotlib` 和 `numpy` 就好了.

{% include google-in-article-ads.html %}

 {% include assign-heading.html %}

接着我们来说说 neat-python 网页上的一个使用例子, 用 neat 来进化出一个神经网络预测 XOR 判断. 什么是 XOR 呢, 简单来说就是 OR 判断的改版.

* 输入 True, True, 输出 False
* 输入 False, True, 输出 True
* 输入 True, False, 输出 True
* 输入 False, False 输出 False

在例子当中, 我们用这样的形式来代替要学习的 input 和 output:

```python
xor_inputs = [(0.0, 0.0), (0.0, 1.0), (1.0, 0.0), (1.0, 1.0)]
xor_outputs = [   (0.0,),     (1.0,),     (1.0,),     (0.0,)]
```

那怎么样来评价每个个体的适应度 (fitness), 或者说他的预测得分高低呢. 我们就对每个个体评分.
如果4个 xor 判断都预测对了就得4分, 用平方差来计算越策错的. 下面的 function 中就是根据每个 `genome` (DNA), 生成一个神经网络,
用这个神经网络预测, 再对这个 `genome` 打分, 并写入成它的 `fitness`.

```python
def eval_genomes(genomes, config):
    for genome_id, genome in genomes:   # for each individual
        genome.fitness = 4.0        # 4 xor evaluations
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        for xi, xo in zip(xor_inputs, xor_outputs):
            output = net.activate(xi)
            genome.fitness -= (output[0] - xo[0]) ** 2
```

每一个 neat 的程序里有需要有这样的评分标准. 接着我们创建一个 config 的文件, 用来给定所有运行参数.
这个 config 文件要分开存储, 而且文件里要有一下几个方面的参数预设. 对于每个方面具体的预设值请参考我在 github 中的[config-forward](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/NEAT/config-feedforward){:target="_blank"}这个文件.
对于每个方面的解释, 不太明白的话, 请参考[这里](http://neat-python.readthedocs.io/en/latest/config_file.html){:target="_blank"}

```shell
[NEAT]
[DefaultGenome]
[DefaultSpeciesSet]
[DefaultStagnation]
[DefaultReproduction]
```

现在我们就能使用这些预设的参数来生成一个 `config` 的值了 (上面的 `eval_genomes` 也用到了这个 `config`).

```python
local_dir = os.path.dirname(__file__)
config_file = os.path.join(local_dir, 'config-feedforward')     # 参数文件
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                     neat.DefaultSpeciesSet, neat.DefaultStagnation,
                     config_file)
```

有了这个 `config`, 我们就能拿它来生成我们整个 `population`, 使用这个初始的 `p` 来训练 300 次, 注意在 `config-forward` 中我们设置了一个参数 `fitness_threshold = 3.9`,
就是说, 只要有任何一个 fitness 达到了 3.9 (最大4), 我们就停止迭代更新 `population`. 所以有可能不到 300 次就学好了. 学好之后, 我们输出表现最好的 `winner`.

```python
p = neat.Population(config)
winner = p.run(eval_genomes, 300)   # 输入计算 fitness 的方式和 generation 的次数
```

最主要的过程就完啦, 简单吧. 在这个[例子脚本](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/NEAT/run_xor.py){:target="_blank"}中的其他代码都是现实结果的代码, 大家随便看看就知道了.

```python
print('\nOutput:')
winner_net = neat.nn.FeedForwardNetwork.create(winner, config)
for xi, xo in zip(xor_inputs, xor_outputs):
    output = winner_net.activate(xi)
    print("input {!r}, expected output {!r}, got {!r}".format(xi, xo, output))
```

我们通过这个来输出最后的 `winner` 神经网络预测结果, 不出意外, 你应该预测很准. 最后通过 `visualize.py` [文件的可视化功能](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Using%20Neural%20Nets/NEAT/visualize.py){:target="_blank"}, 我们就能生成几个图片,
使用浏览器打开 `speciation.svg` 看看不同种群的变化趋势, `avg_fitness.svg` 看看 fitness 的变化曲线, `Digraph.gv.svg` 看这个生成的神经网络长怎样.

{% include tut-image.html image-name="4-2-1.png" %}

{% include tut-image.html image-name="4-2-2.png" %}

{% include tut-image.html image-name="4-2-3.png" %}

关于最下面的那个神经网络图, 需要说明一下, 如果是实线, 如 B->1, B->2, 说明这个链接是 Enabled 的. 如果是虚线(点线), 如 B->A XOR B 就说明这个链接是 Disabled 的.
红色的线代表 weight <= 0, 绿色的线代表 weight > 0. 线的宽度和 weight 的大小有关.

下一次呢, 我们来点更厉害的, [使用 NEAT 进化出一个会立杆子的机器人]({% link _tutorials/machine-learning/evolutionary-algorithm/4-03-neat-reinforcement-learning.md %}).