---
youku_id: XMjk3OTcyMTU1Mg
youtube_id: Etj_gclFFFo
bilibili_id: 15983100
title: 进化策略 (Evolution Strategy)
publish-date: 2017-08-19
chapter: 5
thumbnail: /static/thumbnail/ML-intro/ES_thumbnail.png
description: "进化是大自然赋予我们的礼物, 我们也能学习自然界的这份礼物, 将它放入计算机, 让计算机也能用进化来解决问题. 我们接着上回提到的遗传算法, 来说一说另一种使用进化理论的优化模式-进化策略 (Evolution Strategy).
遗传算法和进化策略共享着一些东西. 他们都用遗传信息, 比如 DNA 染色体, 一代代传承, 变异. 来获取上一代没有的东西."
post-headings:
  - 进化算法
  - 遗传算法
  - 进化策略
  - 总结
---
学习资料:
  * [进化算法教程系列](https://morvanzhou.github.io/tutorials/machine-learning/evolutionary-algorithm/){:target="_blank"}
  * [进化策略Python教程]({% link _tutorials/machine-learning/evolutionary-algorithm/3-01-evolution-strategy.md %})

Hello 大家好, 欢迎观看这一次的机器学习简介系列视频, 进化是大自然赋予我们的礼物, 我们也能学习自然界的这份礼物, 将它放入计算机, 让计算机也能用进化来解决问题. 我们接着上回提到的遗传算法, 来说一说另一种使用进化理论的优化模式-进化策略 (Evolution Strategy).


{% include assign-heading.html %}


{% include tut-image.html image-name="ES1.png" %}

[遗传算法]({% link _tutorials/machine-learning/ML-intro/5-01-genetic-algorithm.md %})和进化策略共享着一些东西. 他们都用遗传信息, 比如 DNA 染色体, 一代代传承, 变异. 来获取上一代没有的东西.

{% include tut-image.html image-name="ES2.png" %}

然后通过适者生存, 不适者淘汰的这一套理论不断进化着. 我们的祖先, 通过不断变异, 生存淘汰, 从猴子变成人也就是这么回事.既然进化策略或遗传算法都用到了进化的原则, 他们到底有哪些不同呢? 他们各自又适用于哪些问题呢?


{% include assign-heading.html %}


{% include tut-image.html image-name="ES3.png" %}

我们之前说到, 一般的遗传算法使用的 DNA 是二进制编码的, 爸妈的 DNA 通过交叉配对, 组成宝宝的 DNA, 宝宝也会通过一定的变异获得新的功能. 但一般的进化策略却有些不同.




{% include google-in-article-ads.html %}


{% include assign-heading.html %}

{% include tut-image.html image-name="ES4.png" %}

爸妈的 DNA 不用再是 01 的这种形式, 我们可以用实数来代替, 咋一看, 觉得牛逼了起来, 因为我们抛开了二进制的转换问题, 从而能解决实际生活中的很多由实数组成的真实问题. 比如我有一个关于 x 的公式, 而这个公式中其他参数, 我都能用 DNA 中的实数代替, 然后进化我的 DNA, 也就是优化这个公式啦. 这样用起来, 的确比遗传算法方便. 同样, 在制造宝宝的时候, 我们也能用到交叉配对, 一部分来自爸爸, 一部分来自妈妈. 可是我们应该如何变异呢? 遗传算法中简单的翻牌做法貌似在这里行不通. 不过进化策略中的另外一个因素起了决定性的作用. 这就是变异强度. 简单来说, 我们将爸妈遗传下来的值看做是正态分布的平均值, 再在这个平均值上附加一个标准差, 我们就能用正态分布产生一个相近的数了. 比如在这个8.8位置上的变异强度为1,  我们就按照1的标准差和8.8的均值产生一个离8.8的比较近的数, 比如8.7. 然后对宝宝每一位上的值进行同样的操作. 就能产生稍微不同的宝宝 DNA 啦. 所以, 变异强度也可以被当成一组遗传信息从爸妈的 DNA 里遗传下来. 甚至遗传给宝宝的变异强度基因也能变异. 进化策略的玩法也能多种多样.



 {% include assign-heading.html %}

{% include tut-image.html image-name="ES5.png" %}

我们总结一下, 在进化策略中, 可以有两种遗传性系被继承给后代, 一种是记录所有位置的均值, 一种是记录这个均值的变异强度, 有了这套体系, 我们就能更加轻松自在的在实数区间上进行变异了. 这种思路甚至还能被用在神经网络的参数优化上, 因为这些参数本来就是一些实数. 在之后的视频中我们会继续提到当今比较流行的将人工神经网络结合上遗传算法或者进化策略的方法.
