---
youku_id:
youtube_id:
bilibili_id:
title: 从头开始做一个机器手臂5 完善测试
description: "上节我们加上了强化学习的方法, 来测试了一下整个学习的流程.
不过也发现了一些问题, 而这种发现问题的方式也肯定会出现在你的强化学习项目中. 这次我们来看看我是怎么解决自己发现的问题的."
publish-date: 2017-11-22
thumbnail: "/static/thumbnail/ML-practice/arm5.jpg"
chapter: 1
post-headings:
  - 解决甩手问题
  - Reward Engineering
  - Feature Engineering
---

学习资料:
  * [强化学习系列教程]({% link _tutorials/machine-learning/reinforcement-learning/1-1-A-RL.md %})
  * [本节学习代码](https://github.com/MorvanZhou/train-robot-arm-from-scratch/tree/master/part5){:target="_blank"}

[上节]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch4.md %})我们加上了强化学习的方法, 来测试了一下整个学习的流程.
不过也发现了一些问题, 而这种发现问题的方式也肯定会出现在你的强化学习项目中. 这次我们来看看我是怎么解决自己发现的问题的.

首先我们来确认一下这几个问题是什么:

* 甩手结束 (需要改环境)
* 不太收敛 (引起这个问题的起因很多)
  * 网络性能不好?
  * 特征没选好?
  * reward 没设好?

当解决好这些问题以后, 我们的手臂大大提高了性能, 最后结果变成了这样:

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/ML-practice/arm5-1.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>





{% include assign-heading.html %}

甩手问题其实还是比较好解决的. 我们只要在 `ArmEnv` 限定手臂指尖需要在蓝色区域连续停留一段时间, 回合才结束.
这时我们在 `ArmEnv` 中多设置一个这样的计时器 `self.on_goal` 来记录停留了多久.

```python
# env.py

class ArmEnv(object):
    def __init__(self):
        ...
        self.on_goal = 0

    def step(action):
        ...
        # done and reward
        if self.goal['x'] - self.goal['l']/2 < finger[0] < self.goal['x'] + self.goal['l']/2:
            if self.goal['y'] - self.goal['l']/2 < finger[1] < self.goal['y'] + self.goal['l']/2:
                r += 1.
                self.on_goal += 1
                if self.on_goal > 50:
                    done = True
        else:
            self.on_goal = 0
        ...
```

接着我们在 `step()` 功能中写一个检查的判断, 如果 `finger` 掉落在蓝色 `goal` 区域, 再如果它是连续时间段掉落在这个区域,
`self.on_goal += 1`, 如果其中有一次移出了蓝色区域, `self.on_goal` 又变成 0. 如果保持在蓝色 goal 区域内50步,则回合结束
`done = True`. 这样就能很简单得把结束的条件提高了.








{% include google-in-article-ads.html %}
{% include assign-heading.html %}

在强化学习中, 我们很多时候都要手动设定一些比较好的 reward 形式, 这种方式叫做 reward engineering.
同样还有 feature engineering, 这个你可能有听过. feature engineering 被称作特征工程, 在很多监督学习上面都有用. 我们等等说这个手臂的特征工程怎么做.
先来说说 reward engineering 怎么做.

如果 reward 是连续提供的. 将会比不连续(sparse)提供的要好学. sparse reward 的问题已经一直困扰了 RL 很多年了.
打个比方, 下围棋, 下的过程中是没有任何 reward 的, 只有下到最后才会出现一个 reward 信号说谁赢了.
这是很不好学的. 这一个 reward 信号很容易就消失在了茫茫的数据中(没有 reward 的数据). 而如果时时刻刻都有一个 reward 信号,
而且这个 reward 信号有小有大, sparse 的问题就很容易解决了. 所以做出一个好的 reward function 在现阶段很重要.

而我们这个手臂的环境, reward 很好设置, 只要 finger 离 goal 近, reward 就大, 离越远越小.

```python
class ArmEnv(object):
    def step(self, action):
        ...
        # dist2 是 finger 离 goal 的 x,y方向的距离
        dist2 = [(self.goal['x'] - finger[0]) / 400, (self.goal['y'] - finger[1]) / 400]
        r = -np.sqrt(dist2[0]**2+dist2[1]**2)
        ...
```

而且只要 finger 在 goal 里, 我们的 reward `r += 1`. 这些 reward 的变化都能在[这里](https://github.com/MorvanZhou/train-robot-arm-from-scratch/tree/master/part5/env.py){:target="_blank"}看到.










{% include assign-heading.html %}

如果能做成连续的 reward 信号, 我们能将收敛性提升一个档次, 如果在 feature 上下一番功夫, 收敛性又可以提升,
好的 feature 起到了关键性的作用. 如果使用的 features 很完整的展示这个学习环境, 那手臂也能依据这些有价值的 feature 快速学习.
所以很多时候, 你会看到很多人直接使用图像当作输入, 因为图像就是已经包含了所有信息的 feature. 但是因为我的电脑没有 GPU 加速,
处理图片数据会非常的慢, 所以我还是选择了自己找找其他的好 features.

之前我们只用到了两个手臂的转动角度信息. 按学习情况来看, 这个信息不能提供全面的 state. 所以我们还需要再想想, 还有哪些是有价值的信息.
比如两截手臂的端点到 goal 的距离? 手臂端点离中心点的距离? 这些都是可以的. 我们将这两个补充进 state.

```python
# env.py

class ArmEnv(object):
    state_dim = 9       # state 的维度变到 9
    def step(self, action):
        ...
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy  # a1 end and a2 start (x1, y1)
        finger = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a1xy_  # a2 end (x2, y2)
        # normalize features
        dist1 = [(self.goal['x'] - a1xy_[0]) / 400, (self.goal['y'] - a1xy_[1]) / 400]
        dist2 = [(self.goal['x'] - finger[0]) / 400, (self.goal['y'] - finger[1]) / 400]
        ...
        # state
        s = np.concatenate((a1xy_/200, finger/200, dist1 + dist2, [1. if self.on_goal else 0.]))
        return s, r, done
```

现在的 state 拥有9个信息, 分别是两截手臂端点到中心 / goal 的 x,y 坐标 (共8个), 最后一个信息是 finger 是否在 goal 的区域内.
这一个 feature 我认为是有用的, 因为只要这个 feature 被激活, 手臂完全就可以根据这个不动了, 这在已经移动到了 goal 上的时候非常有用.

最后对程序进行 reward/feature engineering 之后, 效果的确好了很多.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/ML-practice/arm5-1.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

这个教程没有对神经网络方面进行讲解. 有时候神经网络也是需要好好测试的. [rl.py](https://github.com/MorvanZhou/train-robot-arm-from-scratch/tree/master/part5/rl.py){:target="_blank"}
中的几个全局参数, 还有神经网络的层数, 神经元数都是可以好好把玩的.

关于 RL 的神经网络, 我可以给大家提出几个在你硬件允许的情况下通用的方法.

* 增大记忆库 (MEMORY_CAPACITY)
* 减小学习率 (LR_A/LR_C)
* 增大神经网络规模

最后, 我想你还可以对这个程序进行加工, 比如随机初始化 goal 的位置, 让这个手臂更加 robust. 相应的, 你 training 这种 case 的时间肯定会更长.





*实战:从头开始搭建训练机器人手臂*

* *[搭建结构]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})*
* *[写静态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch2.md %})*
* *[写动态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch3.md %})*
* *[加入强化学习算法]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch4.md %})*
* *[完善测试]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch5.md %})*