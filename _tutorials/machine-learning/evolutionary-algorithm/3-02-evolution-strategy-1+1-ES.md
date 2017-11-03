---
youku_id: XMjk5NDYxNTQ0OA
youtube_id: AcTeLqukgkA
bilibili_id: 15984779
title: (1+1)-ES
publish-date: 2017-08-28
thumbnail: "/static/thumbnail/evolutionary-algorithm/32es.jpg"
chapter: 3
description: "(1+1)-ES 是 ES 进化策略的一种形式, 也是众多形式中比较方便有效的一种. 接下来我们来细说他们的类别.
如果要我用一句话来概括 (1+1)-ES: 一个爸爸和一个孩子的战争"
post-headings:
  - 要点
  - ES的不同形式
  - 进化啦
---


学习资料:

* [本节的全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Evolution%20Strategy/(1%2B1){:target="_blank"}-ES.py)
* [我制作的 什么是进化策略 动画简介]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})

 {% include assign-heading.html %}

如果你想对进化策略有一个快速了解, [这个几分钟的短动画]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})是个很好的方式.

(1+1)-ES 是 ES 进化策略的一种形式, 也是众多形式中比较方便有效的一种. 接下来我们来细说他们的类别.
**如果要我用一句话来概括 (1+1)-ES: 一个爸爸和一个孩子的战争**

本节要实践的内容提前看:

{% include tut-image.html image-name="3-2-0.gif" %}


 {% include assign-heading.html %}

像上面看到的, 统一来说都是 (μ/ρ +, λ)-ES, (1+1)-ES 只是一种特殊形式.
这里的 μ 是 population 的数量, ρ 是从 population 中选取的个数, 用来生成宝宝的.
λ 是生成的宝宝数, 如果采用的是 "+" 形式的, 就是使用将 ρ + λ 混合起来进行适者生存,
如果是 "," 形式, 那么就是只使用 λ 进行适者生存.

形式多种多样有些头疼. 不过在这一节中,
我们考虑的只是一个爸爸, 生成一个宝宝,
然后在爸爸和宝宝中进行适者生存的游戏,
选择爸爸和宝宝中比较好的那个当做下一代的爸爸. (1+1)-ES 总结如下:

* 有一个爸爸;
* 根据爸爸变异出一个宝宝;
* 在爸爸和宝宝中选好的那个变成下一代爸爸.


 {% include assign-heading.html %}

同[上节]({% link _tutorials/machine-learning/evolutionary-algorithm/3-01-evolution-strategy.md %})一样,
这次我们还是两个功能, `make_kid` 和 `kill_bad`

```python
def make_kid(parent):
    # 根据 parent 正态分布生一个 kid

def kill_bad(parent, kid):
    # 杀了坏孩子或者坏爸爸
```

所以所有的操作都只有一个数量的 pop. 这时我们在 (1+1)-ES 中的策略是 parent DNA 中只有存平均值, 没有变异强度 (标准差). 这次的变异强度 MUT_STRENGTH
是一个 global variable. 一个标量表示它就好.

```python
def make_kid(parent):
    k = parent + MUT_STRENGTH * np.random.randn(DNA_SIZE)
    return k
```

在 `kill_bad` 中, 我们选择更为适合的, 不管是爸爸还是孩子, 只要是适合的就留下, 不适合的杀掉.
但是还有注意的一点是, 在这一步我们还要对 `MUT_STRENGTH` 进行一点改变. 改变的方法遵循了 1/5 successful rule.
这个方法是 ES 的开山鼻祖提出来的. 文献在这:

Rechenberg, I. 1973. Evolutionsstrategie – Optimierung technischer Systeme nach Prinzipien der biologischen Evolution, Frommann-Holzboog.

网上有个[课件"Tutorial: CMA-ES — Evolution Strategies and
Covariance Matrix Adaptation"](https://www.lri.fr/~hansen/gecco2011-CMA-ES-tutorial.pdf)里面一张图, 让你秒懂这个1/5的意思.

{% include tut-image.html image-name="3-2-1.png" %}

图中的意思是, 还没到收敛的时候(上面左图), 我们增大 `MUT_STRENGTH`, 如果已经快到收敛了(上右图), 我们就减小 `MUT_STRENGTH`.
那如何判断是否快到收敛没呢, 就是如果有1/5的变异比原始的 parent 好的话, 就是快收敛了(像上右图). 在上左图中, 有一半比原始 parent 好, 一半比较差, 所以还没到收敛.
在上面提到的课件中, 用一个公式就能概括这种1/5关系.

{% include tut-image.html image-name="3-2-2.png" %}

最后仿照上面的课件, 我写下了下面的 `kill_bad` 功能.

```python
def kill_bad(parent, kid):
    global MUT_STRENGTH
    fp = get_fitness(F(parent))[0]
    fk = get_fitness(F(kid))[0]
    p_target = 1/5
    if fp < fk:     # kid better than parent
        parent = kid
        ps = 1.     # kid win -> ps = 1 (successful offspring)
    else:
        ps = 0.
    # adjust global mutation strength
    MUT_STRENGTH *= np.exp(1/np.sqrt(DNA_SIZE+1) * (ps - p_target)/(1 - p_target))
    return parent
```


加上训练的主循环, 就大事告成.

```python
parent = 5 * np.random.rand(DNA_SIZE)   # parent DNA

for _ in range(N_GENERATIONS):
    kid = make_kid(parent)               # 生宝宝
    parent = kill_bad(parent, kid)       # 杀宝宝
```

下次我们来看看一种加入了[梯度下降原则的 ES 算法 Natural Evolution Strategy]({% link _tutorials/machine-learning/evolutionary-algorithm/3-03-evolution-strategy-natural-evolution-strategy.md %}).