---
youku_id: XMjk5NDUzNTc0OA
youtube_id: 9yuL-vuiOO0
bilibili_id: 15984678
title: 进化策略
publish-date: 2017-08-28
thumbnail: "/static/thumbnail/evolutionary-algorithm/31es.jpg"
chapter: 3
description: "进化策略 (Evolution Strategy) 后面都简称 ES. 它和 遗传算法 GA 是好兄弟. 步骤和流程都非常相似.
如果你对遗传算法也感兴趣, 前面几节内容都是有关于遗传算法的.
要我用一句话概括ES: 在程序里生宝宝, 杀死不乖的宝宝, 让乖宝宝继续生宝宝. 乍一听, 怎么和 GA 是完全一样的逻辑呢?
没关系, 我们在接下来的内容中揭晓他们的不同."
post-headings:
  - 要点
  - 和遗传算法的异同
  - 进化啦
---

学习资料:

* [本节的全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Evolution%20Strategy/Evolution%20Strategy%20Basic.py){:target="_blank"}
* [我制作的 什么是进化策略 动画简介]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %})

 {% include assign-heading.html %}

如果你想对进化策略有一个快速了解, [这个几分钟的短动画]({% link _tutorials/machine-learning/ML-intro/5-02-evolution-strategy.md %}Fƒ)是个很好的方式.

进化策略 (Evolution Strategy) 后面都简称 ES. 它和 遗传算法 GA 是好兄弟. 步骤和流程都非常相似.
如果你对遗传算法也感兴趣, [前面几节内容]({% link _tutorials/machine-learning/evolutionary-algorithm/2-01-genetic-algorithm.md %})都是有关于遗传算法的.
**要我用一句话概括ES: 在程序里生宝宝, 杀死不乖的宝宝, 让乖宝宝继续生宝宝**. 乍一听, 怎么和 GA 是完全一样的逻辑呢?
没关系, 我们在接下来的内容中揭晓他们的不同.

本节要实践的内容提前看:

{% include tut-image.html image-name="3-1-0.gif" %}



 {% include assign-heading.html %}

遗传算法 (后面简称 GA) 和 ES 真 TM 差不多. 导致很多朋友学习的时候, 都傻傻分不清.
不过我具体的列出来, 方便看清楚.

* 选好父母进行繁殖 (`GA`); 先繁殖, 选好的孩子 (`ES`)
* 通常用二进制编码 DNA (`GA`); 通常 DNA 就是实数, 比如 1.221 (`ES`)
* 通过随机让 1 变成 0 这样变异 DNA (`GA`); 通过正态分布(Normal distribution)变异 DNA (`ES`)

具体来说, 传统的 GA 的 DNA 形式是这样:

DNA=`11010010`

而传统的 ES DNA 形式分两种, 它有两条 DNA. 一个 DNA 是控制数值的, 第二个 DNA 是控制这个数值的变异强度.
比如一个问题有4个变量. 那一个 DNA 中就有4个位置存放这4个变量的值 (这就是我们要得到的答案值).
第二个 DNA 中就存放4个变量的变动幅度值.

DNA1=`1.23, -0.13, 2.35, 112.5` 可以理解为4个正态分布的4个平均值.

DNA2=`0.1, 2.44, 5.112, 2.144`  可以理解为4个正态分布的4个标准差.

所以这两条 DNA 都需要被 `crossover` 和 `mutate`.


 {% include assign-heading.html %}

写基础的 ES 算法其实很简单. 我总结起来, 其实就两个功能, `make_kid` 和 `kill_bad`

```python
def make_kid(pop, n_kid):
    # 根据正态分布生孩子

def kill_bad(pop, kids):
    # 杀了那些坏孩子和坏父母
```

对于今天的问题, 我们就是要找这张图中的最高点.

{% include tut-image.html image-name="2-1-1.png" %}

而这个点只有一个, 所以我们的 DNA 的长度就只有一个. 我们用一个 python 字典来存这两种 DNA 的信息.
这里 `DNA` 存的是均值, `mut_strength` 存的是标准差.

```python
pop = dict(DNA=5 * np.random.rand(1, DNA_SIZE).repeat(POP_SIZE, axis=0),   # initialize the pop DNA values
           mut_strength=np.random.rand(POP_SIZE, DNA_SIZE))
```

训练的主循环, (生死循环... 觉得血腥味很重..为什么我的遗传算法教程就没这么重血腥味呢..) 如下:

```python
for _ in range(N_GENERATIONS):
    kids = make_kid(pop, N_KID)     # 生宝宝
    pop = kill_bad(pop, kids)       # 杀宝宝
```

首先的 `make_kid` 功能. 我们随机找到一对父母, 然后将父母的 `DNA` 和 `mut_strength` 基因都 crossover 给 kid.
然后再根据 `mut_strength` mutate 一下 kid 的 DNA. 也就是用正态分布抽一个 DNA sample. 而且 `mut_strength` 也能变异.
将变异强度变异以后, 他就能在快收敛的时候很自觉的逐渐减小变异强度, 方便收敛.

```python
def make_kid(pop, n_kid):
    # generate empty kid holder
    kids = {'DNA': np.empty((n_kid, DNA_SIZE))}
    kids['mut_strength'] = np.empty_like(kids['DNA'])
    for kv, ks in zip(kids['DNA'], kids['mut_strength']):
        # crossover (roughly half p1 and half p2)
        p1, p2 = np.random.choice(np.arange(POP_SIZE), size=2, replace=False)
        cp = np.random.randint(0, 2, DNA_SIZE, dtype=np.bool)  # crossover points
        kv[cp] = pop['DNA'][p1, cp]
        kv[~cp] = pop['DNA'][p2, ~cp]
        ks[cp] = pop['mut_strength'][p1, cp]
        ks[~cp] = pop['mut_strength'][p2, ~cp]

        # mutate (change DNA based on normal distribution)
        ks[:] = np.maximum(ks + (np.random.rand(*ks.shape)-0.5), 0.)    # must > 0
        kv += ks * np.random.randn(*kv.shape)
        kv[:] = np.clip(kv, *DNA_BOUND)    # clip the mutated value
    return kids
```


{% include google-in-article-ads.html %}

接下来到了惊心动魄的杀人时间. 根据适应度 `fitness` 选择适应度最靠前的一些人,
抛弃掉那些适应度不佳的人. 这个很简单.

```python
def kill_bad(pop, kids):
    # put pop and kids together
    for key in ['DNA', 'mut_strength']:
        pop[key] = np.vstack((pop[key], kids[key]))

    fitness = get_fitness(F(pop['DNA']))            # calculate global fitness
    idx = np.arange(pop['DNA'].shape[0])
    good_idx = idx[fitness.argsort()][-POP_SIZE:]   # selected by fitness ranking (not value)
    for key in ['DNA', 'mut_strength']:
        pop[key] = pop[key][good_idx]
    return pop
```

这样我们就完成了最一般的 ES 算法的主体. 还有一些零散的, 可视化的代码都可以在我的 [github](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Evolution%20Strategy/Evolution%20Strategy%20Basic.py){:target="_blank"} 中找到.
这里就不细说了.

[下次]({% link _tutorials/machine-learning/evolutionary-algorithm/3-02-evolution-strategy-1+1-ES.md %})我们会总结基础的 ES 算法类型. 并且看看一种比较流行的 ES 算法.