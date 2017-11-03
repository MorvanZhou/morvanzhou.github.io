---
youku_id: XMjk3MDg5OTk2NA
youtube_id: solxwZUtOQc
bilibili_id: 15983707
title: 例子 配对句子
description: "使用遗传算法的 Python 教学. 接着上节对遗传算法的基本应用,
在这一节中, 我们用通过不同的编码 DNA 方式, 不同的 fitness 定义方式来让程序生成出自己设定的句子来."
publish-date: 2017-08-12
thumbnail: "/static/thumbnail/evolutionary-algorithm/22ga.jpg"
chapter: 2
post-headings:
  - 要点
  - fitness 和 DNA
  - 进化啦
  - Python实践
---



学习资料:
  * [本节的全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Match%20Phrase.py){:target="_blank"}
  * [我制作的 什么是遗传算法 动画简介]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %})

{% include assign-heading.html %}

如果对遗传算法有兴趣的朋友, 强烈推荐先看看我制作的动画短片 [什么是遗传算法]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %}), 在动画里有了基础的了解,
在接下来的内容中, 你就如鱼得水啦.

接着[上节对遗传算法的基本应用]({% link _tutorials/machine-learning/evolutionary-algorithm/2-01-genetic-algorithm.md %}),
在这一节中, 我们用通过不同的编码 DNA 方式, 不同的 fitness 定义方式来让程序生成出自己设定的句子来.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/evolutionary-algorithm/2-2-0.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>



{% include assign-heading.html %}

上次我们提到过 GA 中最重要的就是怎么定义 fitness function, 怎么给 DNA 编码. 这次我们来句另一个例子.
比如我们有一个要生成的句子:

```python
Target:    You get it!
Generate:  YhtBget i@!
```

可以想象, 我们能够用这个句子长度的 DNA 来生成这个句子. 每个 DNA 代表一个字母. 如果对上的字母越多,
我的 fitness 就越高. 因为用一个 class 来代表 GA 会比较方便, 我们之后都用 class 来写.

```python
class GA:
    def get_fitness(self):             # count how many character matches
        match_count = (self.pop == TARGET_ASCII).sum(axis=1)
        return match_count
```

而 DNA 呢, 可以都用数字, 而且可以用 [ASCII 编码](http://www.asciitable.com/){:target="_blank"}.
将数字转化成字符, 或者字符转数字都可以, 我们为了统一, DNA 都用数字形式.

```python
class GA:
    def translateDNA(self, DNA):    # convert to readable string
        return DNA.tostring().decode('ascii')
```

而字符转数字可以用 numpy 的这个功能:

```python
>>> np.fromstring('dasd@', dtype=np.uint8)
# array([100,  97, 115, 100,  64], dtype=uint8)
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

如果 GA 用一个 class 代替, 那 select, mutate, crossover 都是 class 里的功能了.

```python
class GA:
    def select(self):

    def crossover(self, parent, pop):

    def mutate(self, child):
```

上面这三个功能的算法和[上节内容]({% link _tutorials/machine-learning/evolutionary-algorithm/2-01-genetic-algorithm.md %})差不多.
所以不会再详细说明了. 你也可以去我的 [github 看全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Match%20Phrase.py){:target="_blank"}.
但是这个 class 中还有一个功能来将上面的三个功能联系起来. 其实这就是上节内容里面的 forloop 中的内容.

```python
class GA:
    def evolve(self):
        pop = self.select()
        pop_copy = pop.copy()
        for parent in pop:  # for every parent
            child = self.crossover(parent, pop_copy)
            child = self.mutate(child)
            parent[:] = child
        self.pop = pop
```

有了上面定义的这些功能, 再将其他的[小部分](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Match%20Phrase.py){:target="_blank"}补全.
我们就能很容易的使用这个 `GA` class 了.

```python
ga = GA(DNA_size=DNA_SIZE, DNA_bound=ASCII_BOUND, cross_rate=CROSS_RATE,
            mutation_rate=MUTATION_RATE, pop_size=POP_SIZE)

for generation in range(N_GENERATIONS):
    fitness = ga.get_fitness()
    best_DNA = ga.pop[np.argmax(fitness)]
    best_phrase = ga.translateDNA(best_DNA)
    print('Gen', generation, ': ', best_phrase)
    if best_phrase == TARGET_PHRASE:
        break
    ga.evolve()

"""
Gen 0 :  !hT'ge0[px$
Gen 1 :  !n#'ged[p&!
Gen 2 :  YHJA(er6QM!
Gen 3 :  8=K@ge  "tZ
Gen 4 :  ThTVKet X7!
Gen 5 :  'oJ@ge06iM!
...
Gen 179 :  Youqget it!
Gen 180 :  You'get it!
Gen 181 :  You get it!
"""
```

赶紧试试这套github的[全部代码](https://github.com/MorvanZhou/Evolutionary-Algorithm/blob/master/tutorial-contents/Genetic%20Algorithm/Match%20Phrase.py){:target="_blank"}.

接下来几节内容, 我们就来看看在不同的情况中如何根据不同的标准选择 fitness 和 DNA 编码.