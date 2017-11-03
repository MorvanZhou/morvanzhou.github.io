---
youku_id: XMjk3MDg3MDc5Ng
youtube_id: QuIHneWL8pw
bilibili_id: 15983670
title: 例子 旅行商人问题 (Travel Sales Problem)
publish-date: 2017-08-12
description: "我们在上几节内容中说道 遗传算法 (GA) 算法最主要的就是我们要想明白什么是他的 DNA 和怎么样对个体进行评估 (他们的 Fitness).
这次的旅行商人问题 (之后简称 TSP), 商人需要经过某几个城市, 但是城市之间的距离不一, 我们怎么规划路径, 成了一个复杂的问题.
如果计算每一条可行的路径, 就需要相当大的计算资源. 如果使用 GA, TSP 就能被当成一个非常典型的活学活用 GA 算法的问题.
他的 DNA 编码会有不一样的故事."
thumbnail: "/static/thumbnail/evolutionary-algorithm/23ga.jpg"
chapter: 2
post-headings:
  - 要点
  - fitness 和 DNA
  - 进化啦
  - 附加例子 寻找最近的路线
---



学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Travel%20Sales%20Person.py){:target="_blank"}
  * [我制作的 什么是遗传算法 动画简介]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %})

{% include assign-heading.html %}

如果对遗传算法有兴趣的朋友, 强烈推荐先看看我制作的动画短片 [什么是遗传算法]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %}), 在动画里有了基础的了解,
在接下来的内容中, 你就如鱼得水啦.

我们在上几节内容中说道 遗传算法 (GA) 算法最主要的就是我们要想明白什么是他的 DNA 和怎么样对个体进行评估 (他们的 Fitness).
这次的旅行商人问题 (之后简称 TSP), 商人需要经过某几个城市, 但是城市之间的距离不一, 我们怎么规划路径, 成了一个复杂的问题.
如果计算每一条可行的路径, 就需要相当大的计算资源. 如果使用 GA, TSP 就能被当成一个非常典型的活学活用 GA 算法的问题.
他的 DNA 编码会有不一样的故事.

{% include tut-image.html image-name="2-3-0.gif" %}



{% include assign-heading.html %}


这次的编码 DNA 方式又不一样, 我们可以尝试对每一个城市有一个 ID, 那经历的城市顺序就是按 ID 排序咯.
比如说商人要经过3个城市, 我们就有

* 0-1-2
* 0-2-1
* 1-0-2
* 1-2-0
* 2-0-1
* 2-1-0

这6种排列方式. 每一种排列方式我们就能把它当做一种 DNA 序列, 用 numpy
产生这种 DNA 序列的方式很简单.

```python
>>> np.random.permutation(3)
# array([1, 2, 0])
```

计算 fitness 的时候, 我们只要将 DNA 中这几个城市连成线, 计算一下总路径的长度, 根据长度,
我们定下规则, 越短的总路径越好, 下面的 `fitness0` 就用来计算 fitness 啦.
因为越短的路劲我们更要价大幅度选择, 所以这里我用到了 `fitness1` 这种方式.

```python
fitness0 = 1/total_distance
fitness1 = np.exp(1/total_distance)
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

同上次一样, 我们用一个 GA class 代替 GA 算法, 这个 class 里面有下面这几个主要功能.

```python
class GA:
    def select(self, fitness):

    def crossover(self, parent, pop):

    def mutate(self, child):

    def evolve(self):
```

上面这几个功能的算法在[这节内容]({% link _tutorials/machine-learning/evolutionary-algorithm/2-01-genetic-algorithm.md %})中有详细介绍.
所以不会再详细说明了. 你也可以去我的 [github 看全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Travel%20Sales%20Person.py){:target="_blank"}.
不过我们要注意的是在 `crossover` 和 `mutate` 的时候有一点点不一样, 因为对于路径点, 我们不能随意变化. 比如
如果按平时的 `crossover`, 可能会是这样的结果:

`p1=[0,1,2,3]`  (爸爸)

`p2=[3,2,1,0]`  (妈妈)

`cp=[m,b,m,b]`  (交叉点, m: 妈妈, b: 爸爸)

`c1=[3,1,1,3]`  (孩子)

那么这样的 `c1` 要经过两次城市 3, 两次城市1, 而没有经过 2, 0. 显然不行.
所以我们 `crossover` 以及 `mutation` 都要换一种方式进行. 其中一种可行的方式是这样.
同样是上面的例子.

`p1=[0,1,2,3]`  (爸爸)

`cp=[_,b,_,b]`  (选好来自爸爸的点)

`c1=[1,3,_,_]`  (先将爸爸的点填到孩子的前面)

此时除开来自爸爸的 1, 3. 还有0, 2 两个城市, 但是0,2 的顺序就按照妈妈 DNA 的先后顺序排列.
也就是 `p2=[3,2,1,0]` 的 0, 2 两城市在 p2 中是先有 2, 再有 0. 所以我们就按照这个顺序补去孩子的 DNA.

`c1=[1,3,2,0]`

按照这样的方式, 我们就能成功避免在 `crossover` 产生的问题: 访问多次通过城市的问题了.
用 Python 的写法很简单.

```python
if np.random.rand() < self.cross_rate:
    i_ = np.random.randint(0, self.pop_size, size=1)                        # select another individual from pop
    cross_points = np.random.randint(0, 2, self.DNA_size).astype(np.bool)   # choose crossover points
    keep_city = parent[~cross_points]                                       # find the city number
    swap_city = pop[i_, np.isin(pop[i_].ravel(), keep_city, invert=True)]   # 找到与爸爸不同的城市
    parent[:] = np.concatenate((keep_city, swap_city))
```

在 `mutate` 的时候, 也是找到两个不同的 DNA 点, 然后交换这两个点就好了.

```python
for point in range(self.DNA_size):
    if np.random.rand() < self.mutate_rate:
        swap_point = np.random.randint(0, self.DNA_size)
        swapA, swapB = child[point], child[swap_point]
        child[point], child[swap_point] = swapB, swapA
```

在 GA class 中, 其他的部分就和以前的例子非常相近了, 为了不显得累赘, 我也不会细说了, 可以参考我之前的教程,
也可以在我 [github](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Travel%20Sales%20Person.py){:target="_blank"} 中查看整套代码.

最后的循环主框架还是没变, 就像下面这么简单.

```python
ga = GA(...)

for generation in range(N_GENERATIONS):
    fitness = ga.get_fitness()
    ga.evolve(fitness)
```

{% include assign-heading.html %}

如果你还想多看一个例子, 我还有一个例子, 但是不会细说, 应为和上面的例子非常接近. 只要你懂了上面的, 就懂了接下来的例子了.

{% include tut-image.html image-name="2-3-1.gif" %}

这个例子中的 DNA 形式又不一样, 其实每条路线都是由 "左上, 右下, 右上..." 这样的移动顺序组成.
所以整个路线 DNA 就是一连串的移动方向. 在移动方向上变异和交配, 就能找到比较好的路线了. 详细[代码在这](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Find%20Path.py){:target="_blank"}.
