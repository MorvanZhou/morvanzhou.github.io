---
youku_id: XMjk0NzE0MjgxNg
youtube_id: BEquIwfEXes
bilibili_id: 15983143
title: 遗传算法 (Genetic Algorithm)
publish-date: 2017-08-05
chapter: 5
thumbnail: /static/thumbnail/ML-intro/genetic-algorithm.png
description: "这次我们尝试踏足机器学习中的另外一个领域, 用进化理论来解决复杂的问题. 遗传算法是进化算法的一个分支. 它将达尔文的进化理论搬进了计算机.
所以你会发现在程序中, 我们还时不时出现什么染色体, DNA, 遗传, DNA交叉, 变异 这些东西. 不过想想也能明白, 在自然界中, 优胜劣汰, 我们人类也是靠着这些手段一步步从猴子"
post-headings:
  - 进化算法
  - 猴子的进化
  - 种群的进化
  - 电脑里的 DNA
  - 别人的实验
---
学习资料:
* [进化算法教程系列]({% link _table-contents/machine-learning/evolutionary-algorithm.html %})
* [遗传算法Python教程]({% link _tutorials/machine-learning/evolutionary-algorithm/2-01-genetic-algorithm.md %})

欢迎观看有趣的机器学习系列视频, 这次我们尝试踏足机器学习中的另外一个领域, 用进化理论来解决复杂的问题. 遗传算法是进化算法的一个分支. 它将达尔文的进化理论搬进了计算机.


{% include assign-heading.html %}

{% include tut-image.html image-name="genetic-algorithm1.png" %}

所以你会发现在程序中, 我们还时不时出现什么染色体, DNA, 遗传, DNA交叉, 变异 这些东西. 不过想想也能明白, 在自然界中, 优胜劣汰, 我们人类也是靠着这些手段一步步从猴子

{% include tut-image.html image-name="genetic-algorithm2.png" %}

~变成会敲键盘, 会唱歌, 会读书, 会干坏事的猴子了. 哈哈. 重点不是这些. 我们应该正儿八经地想想, 我们是怎么样一步一步变成后面这些猴子的.


{% include assign-heading.html %}

{% include tut-image.html image-name="genetic-algorithm3.png" %}

想象我们的祖先是这么一群一直在树上的猴子. 某一天他们诞下了一只可能是因为某种变异而总喜欢呆在地上的猴子. 因为总喜欢在地上, 地上又有很多石头, 他开始用石头作为自己的工具, 比如砸开坚硬的果实或者做武器. 会使用石头的猴子变的比其他猴子更容易吃到东西, 也更有能力抵御外人. 所以这样的猴子活得越久, 繁衍得越多. 所以我们的祖先慢慢地变成了地上的猴子. 离变成人类也进了一步. 我们看到上面的线路, 可以总结一下这整套流程.



{% include google-in-article-ads.html %}

{% include assign-heading.html %}

{% include tut-image.html image-name="genetic-algorithm4.png" %}

首先有一整个种族, 然后种族里不断的繁衍后代, 有时候会突然间产生一些变异, 这些变异中有一些天生畸形, 一些有了新的能力, 不适应环境的人们, (包括畸形)被当下的环境淘汰掉了, 适应环境的人们, (包括哪些变异出新能力的人)被保留, 并且还能繁衍出更多这种新能力的人. 这就变成了我们下一代的种族. 接着继续这个循环. 其实计算机也能套用这一套体系, 这就有了我们的遗传算法.



{% include assign-heading.html %}

{% include tut-image.html image-name="genetic-algorithm5.png" %}

每个人都会有他独有的遗传信息比如 DNA, 种群的繁衍也就是这些 DNA 的传承, 所以遗传算法把握住了这一条定律. 我们就尝试着在电脑中用某些途径来代替这些生物形式的 DNA. 我们如果仔细看看这些 DNA, 就会发现, 他们其实是由一组组固定的结构构成, 如果你还没有忘记初高中学的生物, 这种小的结构就叫做碱基对. 在程序中, 我们也可以模拟这些结构, 将这些结构遗传给下一代或者变异一下. 最常用的一种替换方式是: 我们直接使用0和1来代替, 因为在电脑中, 所有东西都是01, 01 就是电脑的语言. 我们的手脚都是从这些最基本的 DNA 信息里翻译出来的, 那么我们也能用一定的规则将01这类信息用电脑翻译成其他的信息.

{% include tut-image.html image-name="genetic-algorithm6.png" %}

有了这些电脑能懂的 DNA 形式, 我们就能模拟生物中的繁衍后代了, 假设我们有两个来自父母的 DNA 信息. 我们只需要选取他们各自一段信息就能组成新的宝宝的DNA信息. 生物繁衍中, 还会存在时不时的变异, 我们也能从这套01 的系统中体现出来, 只要将某些地方将0变成1, 1变成0就好了. 有了这些遗传变异, 加上那一套适者生存,不适者淘汰的理论, 你的电脑里就能有一群渐渐成长壮大的小生物了.

{% include assign-heading.html %}

{% include tut-image.html image-name="genetic-algorithm7.png" %}

我们来看看别人都在拿电脑里喂养了哪些生物吧. 比如进化出会自己闯关的马里奥, 自动驾驶的汽车, 还能模拟微生物的行为. 看上去是不是真有那么一回事. 我会将这些视频的链接附在我”莫烦Python”的网页中, 有兴趣的朋友们可以观看一下.

视频里别人的实验: [马里奥](https://www.youtube.com/watch?v=qv6UVOQ0F44){:target="_blank"}
, [自动驾驶](https://www.youtube.com/watch?v=5lJuEW-5vr8&t=109s){:target="_blank"},
[微生物进化](https://www.youtube.com/watch?v=2kupe2ZKK58){:target="_blank"}.
