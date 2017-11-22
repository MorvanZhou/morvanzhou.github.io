---
youku_id:
youtube_id:
bilibili_id:
title: 从头开始做一个机器手臂4 加入强化学习算法
description: "在上节中,
我们的环境已经基本建设完成了, 现在我们需要的就是一个强化学习的学习方法. 学习方法有很多, 而且也分很多类型.
我们需要按照自己环境的要求挑选适合于这个环境的学习方法."
publish-date: 2017-11-22
thumbnail: "/static/thumbnail/ML-practice/arm4.jpg"
chapter: 1
post-headings:
  - 选择RL方法
  - 保存提取网络
  - 训练
---

学习资料:
  * [强化学习系列教程]({% link _tutorials/machine-learning/reinforcement-learning/1-1-A-RL.md %})
  * [本节学习代码](https://github.com/MorvanZhou/train-robot-arm-from-scratch/tree/master/part4){:target="_blank"}

在[上节]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch3.md %})中,
我们的环境已经基本建设完成了, 现在我们需要的就是一个强化学习的学习方法. 学习方法有很多, 而且也分很多类型.
我们需要按照自己环境的要求挑选适合于这个环境的学习方法.


{% include assign-heading.html %}

在我的 [强化学习教程系列](/tutorials/machine-learning/reinforcement-learning/) 中, 就囊括了非常多的强化学习方法.
而且我制作的 [这个动画视频]({% link _tutorials/machine-learning/reinforcement-learning/1-1-B-RL-methods.md %}) 也举例让大家对各种强化学习方法有了一些了解.
其中列举了当前比较流行的算法.

一般, 给你一个环境, 你最先要考虑到的问题是, 这个环境当中的机器人, 他的动作是连续(continuous)的还是离散(discrete)的? 因为这算是一个重大区别.
不是每种强化学习方法都能同时处理连续和离散动作的. 一般我们的选择方法可以是:

* 连续动作 (动作是一个连续值, 比如旋转角度)
  * [Policy gradient]({% link _tutorials/machine-learning/reinforcement-learning/5-1-policy-gradient-softmax1.md %})
  * [DDPG]({% link _tutorials/machine-learning/reinforcement-learning/6-2-DDPG.md %})
  * [A3C]({% link _tutorials/machine-learning/reinforcement-learning/6-3-A3C.md %})
  * [PPO]({% link _tutorials/machine-learning/reinforcement-learning/6-4-DPPO.md %})
* 离散动作 (动作是一个离散值, 比如向前,向后走)
  * [Q-learning]({% link _tutorials/machine-learning/reinforcement-learning/2-2-tabular-q1.md %})
  * [DQN]({% link _tutorials/machine-learning/reinforcement-learning/4-1-DQN1.md %})
  * [A3C]({% link _tutorials/machine-learning/reinforcement-learning/6-3-A3C.md %})
  * [PPO]({% link _tutorials/machine-learning/reinforcement-learning/6-4-DPPO.md %})

{% include tut-image.html image-name="arm4-1.png" %}

很多时候不限于上面的那些方法, 只不过是上面的那些方法都能在我的教程当中找到.
为了满足这个机械手臂的要求, 我选择了连续动作的 DDPG 来作为这次的 RL 算法.






{% include google-in-article-ads.html %}
{% include assign-heading.html %}

这里不会细说 DDPG 的算法, 因为在我[这个动画教程]({% link _tutorials/machine-learning/reinforcement-learning/6-2-A-DDPG.md %})
和[这个python教程]({% link _tutorials/machine-learning/reinforcement-learning/6-2-DDPG.md %})中已经详细阐述了一遍. 如果不关心 DDPG 的朋友们,
其实你最需要了解的就是这个网络是做连续动作的预测就行. 搭建的[全部代码在这里](https://github.com/MorvanZhou/train-robot-arm-from-scratch/blob/master/part4/rl.py){:target="_blank"}.
如果用 tensorboard 显示整个 DDPG 的计算流程图, 就是下面那样.

{% include tut-image.html global-path="/static/results/reinforcement-learning/6-2-2.png" %}

搭建这个图纸不会细说, 想要细说的是保存网络和提取网络的两个功能. 因为这两个功能在我的强化学习教程系列中是没有提到的. 已经有很多朋友在那个教程下面留言说不知道怎么保存提取.
首先我们使用的是 [tensorflow](https://www.tensorflow.org/){:target="_blank"}. 他的保存提取方式还是很简单的.

```python
# rl.py

class DDPG(object):
    def save(self):     # 保存功能
        saver = tf.train.Saver()
        saver.save(self.sess, 'params', write_meta_graph=False)

    def restore(self):  # 提取功能
        saver = tf.train.Saver()
        saver.restore(self.sess, 'params')
```

使用的时候我们可以对应上在 `main.py` 中的 training 和 test 时段分别进行. 比如 training 完了我们保存网络, 开始 test 的时候提取保存过的网络.
下面的过程有点省略, 具体的代码请查看[这里](https://github.com/MorvanZhou/train-robot-arm-from-scratch/blob/master/part4/main.py){:target="_blank"}.

```python
# main.py

ON_TRAIN = True     # 是否在 training
rl = DDPG(a_dim, s_dim, a_bound)

def train():
    ...
    # train 完了以后
    rl.save()

def eval():
    rl.restore()    # 提取网络

    # 开始测试循环
    ...

if ON_TRAIN:
    train()
else:
    eval()
```









{% include assign-heading.html %}

设置好了这些以后, 就是真正的 training 了.
在 [main.py](https://github.com/MorvanZhou/train-robot-arm-from-scratch/blob/master/part4/main.py){:target="_blank"} 中将 `ON_TRAIN = True`.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/ML-practice/arm4-2.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

看得出它已经不是在乱玩了, 但是还是有一些问题, 比如接触到蓝点就回合结束, 很多时候机器手臂都只是将手甩上去就结束了.
我们更希望是它能停在那个蓝色区域上一会再结束. 所以我总结了一下现在所面临的问题.

* 甩手结束
* 不太收敛

你看, 我们只有将这个学习过程可视化了, 才能便于我们发现潜在的问题, 这从侧面说明了做一个可视化的环境多重要.
发现问题这个过程肯定也是你在做强化学习项目会遇到的. 所以我们[下一节内容]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch5.md %})将会看我如何解决这些问题.




*实战:从头开始搭建训练机器人手臂*

* *[搭建结构]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})*
* *[写静态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch2.md %})*
* *[写动态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch3.md %})*
* *[加入强化学习算法]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch4.md %})*
* *[完善测试]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch5.md %})*