---
youku_id: XMjk3MDExOTUwNA
youtube_id: 9ExCPd918Yk
bilibili_id: 15983770
title: 遗传算法
description: 使用 Python 来实现遗传算法的简单教学. 如果让我用一句话概括遗传算法, 在程序里生宝宝, 杀死不乖的宝宝, 让乖宝宝继续生宝宝
publish-date: 2017-08-12
thumbnail: "/static/thumbnail/evolutionary-algorithm/21ga.jpg"
chapter: 2
post-headings:
  - 要点
  - 找一个好的fitness方程
  - DNA 编码
  - 进化啦
---



学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Genetic%20Algorithm%20Basic.py){:target="_blank"}
  * [我制作的 什么是遗传算法 动画简介]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %})

{% include assign-heading.html %}

如果对遗传算法有兴趣的朋友, 强烈推荐先看看我制作的动画短片 [什么是遗传算法]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %}), 在动画里有了基础的了解,
在接下来的内容中, 你就如鱼得水啦. **如果让我用一句话概括遗传算法: "在程序里生宝宝, 杀死不乖的宝宝, 让乖宝宝继续生宝宝".**

在这一节中, 我们的 "乖宝宝" 就是图中更高的点, 用遗传算法, 我们就能轻松找到 "最乖的宝宝".

{% include tut-image.html image-name="2-1-0.gif" %}



{% include assign-heading.html %}

所有的遗传算法 (Genetic Algorithm), 后面都简称 GA, 我们都需要一个评估好坏的方程,
这个方程通常被称为 fitness. 在今天的问题中, 我们找到下面这个曲线当中的最高点.
那么这个 fitness 方程就很好定, 越高的点, fitness 越高.

{% include tut-image.html image-name="2-1-1.png" %}

如果这个曲线上任一点的 y 值是 `pred` 的话, 我们的 fitness 就是下面这样:

```python
def get_fitness(pred):
    return pred
```

{% include assign-heading.html %}

在 GA 中有基因, 为了方便, 我们直接就称为 `DNA` 吧. GA 中第二重要的就是这 `DNA` 了, 如何编码和解码 `DNA`,
就是你使用 GA 首先要想到的问题. 传统的 GA 中, `DNA` 我们能用一串二进制来表示, 比如:

```python
DNA1 = [1, 1, 0, 1, 0, 0, 1]
DNA2 = [1, 0, 1, 1, 0, 1, 1]
```

为什么会要用二进制编码, 我们之后在下面的内容中详细说明这样编码的好处. 但是长成这样的 `DNA` 并不好使用.
如果要将它解码, 我们可以将二进制转换成十进制, 比如二进制的 `11` 就是十进制的 `3`. 这种转换的步骤在程序中很好执行.
但是有时候我们会需要精确到小数, 其实也很简单, 只要再将十进制的数浓缩一下就好. 比如我有 `1111` 这么长的 `DNA`, 我们产生的十进制数范围是 [0, 15],
而我需要的范围是 [-1, 1], 我们就将 [0, 15] 缩放到 [-1, 1] 这个范围就好.

```python
def translateDNA(pop):
    return pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2**DNA_SIZE-1) * X_BOUND[1]
```

注意, 这里的 `pop` 是一个储存二进制 `DNA` 的矩阵, 他的 shape 是这样 (pop_size, DNA_size).

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

进化分三步:

* 适者生存 (selection)
* DNA 交叉配对 (crossover)
* DNA 变异 (mutation)

我们用 python 的三个功能, 一个循环表示:

```python
# 种群 DNA
pop = np.random.randint(0, 2, (1, DNA_SIZE)).repeat(POP_SIZE, axis=0)

F_values = F(translateDNA(pop))
fitness = get_fitness(F_values)
pop = select(pop, fitness)      # 按适应度选 pop
pop_copy = pop.copy()           # 备个份
for parent in pop:
    child = croseeover(parent, pop_copy)
    child = mutate(child)
    parent[:] = child           # 宝宝变大人
```

适者生存的 `select()` 很简单, 我们只要按照适应程度 `fitness` 来选 `pop` 中的 `parent` 就好.
`fitness` 越大, 越有可能被选到.

```python
def select(pop, fitness):
    idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True,
                           p=fitness/fitness.sum()) # p 就是选它的比例
    return pop[idx]
```

接下来进行交叉配对. 方式很简单. 比如这两个 DNA, `Y` 的点我们取 `DNA1` 中的元素, `N` 的点取 `DNA2` 中的.
生成的 `DNA3` 就有来自父母的基因了.

```python
DNA1 = [1, 1, 0, 1, 0, 0, 1]
       [Y, N, Y, N, N, Y, N]
DNA2 = [1, 0, 1, 1, 0, 1, 1]

DNA3 = [1, 0, 0, 1, 0, 0, 1]
```

而 python 写出来也很方便, 从 `pop_copy` 中随便选一个当另一个父辈 和 `parent` 进行随机的 crossover:

```python
def crossover(parent, pop):
    if np.random.rand() < CROSS_RATE:
        i_ = np.random.randint(0, POP_SIZE, size=1)  # select another individual from pop
        cross_points = np.random.randint(0, 2, DNA_SIZE).astype(np.bool)  # choose crossover points
        parent[cross_points] = pop[i_, cross_points]  # mating and produce one child
    return parent
```

mutation 就更好写了, 将某些 DNA 中的 `0` 变成 `1`, `1` 变成 `0`.

```python
def mutate(child):
    for point in range(DNA_SIZE):
        if np.random.rand() < MUTATION_RATE:
            child[point] = 1 if child[point] == 0 else 0
    return child
```

有了这些规则, `select`, `crossover`, `mutate`, 我们就能在程序里上演进化论啦.
赶紧运行一下我在github的[这套全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Genetic%20Algorithm%20Basic.py){:target="_blank"}.

接下来几节内容, 我们就来看看在不同的情况中如何根据不同的标准选择 fitness 和 DNA 编码.