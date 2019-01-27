---
youku_id: XMzM3ODMzMTM2NA
youtube_id: fCEHdyLkjNE
b_av: 19120226
title: 迁移学习 Transfer Learning
chapter: 2
thumbnail: "/static/thumbnail-small/ML-intro/transfer_learning.png"
publish-date: 2018-02-03
description: "你会发现聪明人都喜欢偷懒, 因为这样的偷懒能帮我们节省大量的时间, 提高效率.
还有一种偷懒是站在巨人的肩膀上. 不仅能看得更远, 还能看到更多. 这也用来表达我们要善于学习先辈的经验, 一个人的成功往往还取决于先辈们累积的知识. 这句话, 放在机器学习中, 这就是今天要说的迁移学习了, transfer learning.
"
post-headings:
  - 机器学习发展
  - 怎么迁移
  - 还能怎么玩
---

学习资料:
  * 迁移学习 Tensorflow [教程]({% link _tutorials/machine-learning/tensorflow/5-16-transfer-learning.md %})
  * 斯坦福迁移学习[阅读](http://cs231n.github.io/transfer-learning/){:target="_blank"}
  
你会发现聪明人都喜欢”偷懒”, 因为这样的偷懒能帮我们节省大量的时间, 提高效率.
还有一种偷懒是 “站在巨人的肩膀上”. 不仅能看得更远, 还能看到更多. 这也用来表达我们要善于学习先辈的经验, 一个人的成功往往还取决于先辈们累积的知识. 这句话, 放在机器学习中, 这就是今天要说的迁移学习了, transfer learning.

{% include tut-image.html image-name="transfer_learning0.jpg" %}




{% include assign-heading.html %}

{% include tut-image.html image-name="transfer_learning1.jpg" %}

现在的机器人视觉已经非常先进了, 有些甚至超过了人类. 99.99%的识别准确率都不在话下. 这样的成功, 依赖于强大的机器学习技术, 其中, 神经网络成为了领军人物. 而 CNN 等, 像人一样拥有千千万万个神经联结的结构, 为这种成功贡献了巨大力量.
但是为了更厉害的 CNN, 我们的神经网络设计, 也从简单的几层网络,
变得越来越多, 越来越多, 越来越多… 为什么会越来越多?


因为计算机硬件, 比如 GPU 变得越来越强大, 能够更快速地处理庞大的信息. 在同样的时间内, 机器能学到更多东西. 可是, 不是所有人都拥有这么庞大的计算能力. 而且有时候面对类似的任务时, 我们希望能够借鉴已有的资源.






{% include assign-heading.html %}

{% include tut-image.html image-name="transfer_learning2.png" %}

这就好比, Google 和百度的关系, facebook 和人人的关系, KFC 和 麦当劳的关系, 同一类型的事业, 不用自己完全从头做, 借鉴对方的经验, 往往能节省很多时间. 有这样的思路, 我们也能偷偷懒, 不用花时间重新训练一个无比庞大的神经网络, 借鉴借鉴一个已经训练好的神经网络就行.


{% include tut-image.html image-name="transfer_learning3.png" %}


比如这样的一个神经网络, 我花了两天训练完之后, 它已经能正确区分图片中具体描述的是男人, 女人还是眼镜. 说明这个神经网络已经具备对图片信息一定的理解能力. 这些理解能力就以参数的形式存放在每一个神经节点中. 不巧, 领导下达了一个紧急任务,


{% include tut-image.html image-name="transfer_learning4.png" %}

要求今天之内训练出来一个预测图片里实物价值的模型. 我想这可完蛋了, 上一个图片模型都要花两天, 如果要再搭个模型重新训练, 今天肯定出不来呀. #这时, 迁移学习来拯救我了. 因为这个训练好的模型中已经有了一些对图片的理解能力, 而模型最后输出层的作用是分类之前的图片, 对于现在计算价值的任务是用不到的, #所以我将最后一层替换掉, 变为服务于现在这个任务的输出层. #接着只训练新加的输出层, 让理解力保持始终不变. 前面的神经层庞大的参数不用再训练, 节省了我很多时间, 我也在一天时间内, 将这个任务顺利完成.


{% include tut-image.html image-name="transfer_learning5.png" %}


但并不是所有时候我们都需要迁移学习. 比如神经网络很简单, 相比起计算机视觉中庞大的 CNN 或者语音识别的 RNN, 训练小的神经网络并不需要特别多的时间, 我们完全可以直接重头开始训练. 从头开始训练也是有好处的.

{% include tut-image.html image-name="transfer_learning6.png" %}

如果固定住之前的理解力, 或者使用更小的学习率来更新借鉴来的模型, 就变得有点像认识一个人时的第一印象, 如果迁移前的数据和迁移后的数据差距很大, 或者说我对于这个人的第一印象和后续印象差距很大, 我还不如不要管我的第一印象, 同理, 这时, 迁移来的模型并不会起多大作用, 还可能干扰我后续的决策.


{% include google-in-article-ads.html %}





{% include assign-heading.html %}

{% include tut-image.html image-name="transfer_learning7.png" %}

了解了一般的迁移学习玩法后, 我们看看前辈们还有哪些新玩法. [多任务学习](https://arxiv.org/abs/1706.05098){:target="_blank"}, 或者强化学习中的 [learning to learn](https://arxiv.org/abs/1706.09529){:target="_blank"}, 迁移机器人对运作形式的理解, 解决不同的任务. 炒个蔬菜, 红烧肉, 番茄蛋花汤虽然菜色不同, 但是做菜的原则是类似的.

{% include tut-image.html image-name="transfer_learning8.gif" %}

又或者 google 的[翻译模型](https://research.googleblog.com/2016/11/zero-shot-translation-with-googles.html){:target="_blank"}, 在某些语言上训练, 产生出对语言的理解模型, 将这个理解模型当做迁移模型在另外的语言上训练. 其实说白了, 那个迁移的模型就能看成机器自己发明的一种只有它自己才能看懂的语言. 然后用自己的这个语言模型当成翻译中转站, 将某种语言转成自己的语言, 然后再翻译成另外的语言. 迁移学习的脑洞还有很多, 相信这种站在巨人肩膀上继续学习的方法, 还会带来更多有趣的应用.
