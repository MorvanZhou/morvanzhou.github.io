---
youku_id: XMTY5MTk1NzIzMg
youtube_id: vBJ_XbRnzKE
bilibili_id: 16009245
title: 检验神经网络 (Evaluation)
description: 检验神经网络有没有学习到东西很重要. 应该如何来评价自己的神经网络, 从评价当中如何改进我们的神经网络. 其实评价神经网络的方法, 和评价其他机器学习的方法大同小异. 我们首先说说为什么要评价,检验学习到的神经网络. 
chapter: 3
post-headings:
  - Training and Test data
  - 误差曲线
  - 准确度曲线
  - 正规化
  - 交叉验证
---

学习资料:
  * Theano: l1 l2 regularization [教程]({% link _tutorials/machine-learning/theano/3-5-regularization.md %})
  * Scikit-learn: cross validation [教程1]({% link _tutorials/machine-learning/sklearn/3-2-cross-validation1.md %})
  * Scikit-learn: cross validation [教程2]({% link _tutorials/machine-learning/sklearn/3-3-cross-validation2.md %})
  * Scikit-learn: cross validation [教程3]({% link _tutorials/machine-learning/sklearn/3-4-cross-validation3.md %})
  * Tensorflow: dropout [教程]({% link _tutorials/machine-learning/tensorflow/5-02-dropout.md %})

今天我们会来聊聊在做好了属于自己的神经网络之后, 应该如何来评价自己的神经网络, 从评价当中如何改进我们的神经网络. 其实评价神经网络的方法, 和评价其他机器学习的方法大同小异. 我们首先说说为什么要评价,检验学习到的神经网络.

**注: 本文不会涉及数学推导. 大家可以在很多其他地方找到优秀的数学推导文章.**

{% include tut-image.html image-name="evaluate1.png" %}

在神经网络的训练当中, 神经网络可能会因为各种各样的问题,  出现学习的效率不高, 或者是因为干扰太多, 学到最后并没有很好的学到规律 . 而这其中的原因可能是多方面的, 可能是数据问题, 学习效率 等参数问题.


 {% include assign-heading.html %}

{% include tut-image.html image-name="evaluate2.png" %}

为了检验,评价神经网络, 避免和改善这些问题, 我们通常会把收集到的数据分为训练数据 和 测试数据,  一般用于训练的数据可以是所有数据的70%, 剩下的30%可以拿来测试学习结果.如果你想问为什么要分开成两批, 那就想想我们读书时的日子, 考试题和作业题大部分都是不一样的吧. 这也是同一个道理.

 {% include assign-heading.html %}

{% include tut-image.html image-name="evaluate3.png" %}

接着, 对于神经网络的评价基本上是基于这30%的测试数据. 想想期末考试虽然花的时间少, 但是占得总成绩肯定要比你平时作业的分多吧. 所以说这30%虽然少, 但是很重要.  然后, 我们就可以开始画图啦! 评价机器学习可以从误差这个值开始, 随着训练时间的变长, 优秀的神经网络能预测到更为精准的答案, 预测误差也会越少 . 到最后能够提升的空间变小, 曲线也趋于水平 . 班上的差生, 从不及格到80分已经不容易啦, 再往上冲刺100分, 就变成了更难的事了. 机器学习也一样. 所以, 如果你的机器学习的误差曲线是这样一条曲线, 那就已经是很不错的学习成果啦.

 {% include assign-heading.html %}

{% include tut-image.html image-name="evaluate4.png" %}

同样, 除了误差曲线, 我们可以看他的精确度曲线. 最好的精度是趋向于100%精确. 比如在神经网络的分类问题中, 100个样本中, 我有90张样本分类正确, 那就是说我的预测精确度是90%. 不过, 不知道大家有没有想过对于回归的问题呢? 怎样看预测值是连续数字的精确度? 这时, 我们可以引用 R2 分数在测量回归问题的精度 . R2给出的最大精度也是100%, 所以分类和回归就都有的统一的精度标准. 除了这些评分标准, 我们还有很多其他的标准, 比如 F1 分数 , 用于测量不均衡数据的精度. 由于时间有限, 我们会在今后的视频中继续详细讲解.

{% include google-in-article-ads.html %}

 {% include assign-heading.html %}

{% include tut-image.html image-name="evaluate5.png" %}

有时候, 意外是猝不及防的, 比如有时候我们明明每一道作业习题都会做, 可是考试分数为什么总是比作业分数低许多? 原来, 我们只复习了作业题,并没有深入, 拓展研究作业反映出来的知识. 这件事情发生在机器学习中, 我们就叫做过拟合. 我们在回到误差曲线, 不过这时我们也把训练误差画出来. 红色的是训练误差, 黑色的是测试误差. 训练时的误差比测试的误差小, 神经网络虽然学习到了知识, 但是对于平时作业太过依赖, 到了考试的时候, 却不能随机应变, 没有成功的把作业的知识扩展开来. 在机器学习中, 解决过拟合也有很多方法 , 比如 l1, l2 正规化, dropout 方法.

 {% include assign-heading.html %}

{% include tut-image.html image-name="evaluate6.png" %}

神经网络也有很多参数, 我们怎么确定哪样的参数能够更有效的解决现有的问题呢? 这时, 交叉验证 就是最好的途径了. 交叉验证不仅仅可以用于神经网络的调参, 还能用于其他机器学习方法的调参.  同样是选择你想观看的误差值或者是精确度, 不过横坐标不再是学习时间, 而是你要测试的某一参数 (比如说神经网络层数) . 我们逐渐增加神经层, 然后对于每一个不同层结构的神经网络求出最终的误差或精度, 画在图中. 我们知道, 神经层越多, 计算机所需要消耗的时间和资源就越多, 所以我们只需要找到那个能满足误差要求, 有节约资源的层结构. 比如说误差在0.005一下都能接受 , 那我们就可以采用30层的神经网络结构 .

