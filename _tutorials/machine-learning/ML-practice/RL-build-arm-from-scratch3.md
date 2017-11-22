---
youku_id:
youtube_id:
bilibili_id:
title: 从头开始做一个机器手臂3 写动态环境
description: "上次我们搭建好了一个静态的环境, 整个环境还没有动起来.
这次我们结合手臂的运动部分和手臂的成像部分来写全整个手臂的摆动规则. 并且通过不断地可视化来测试是否写错."
publish-date: 2017-11-22
thumbnail: "/static/thumbnail/ML-practice/arm3.jpg"
chapter: 1
post-headings:
  - 建立手臂信息
  - 矩形手臂的点坐标
  - 手臂移动方式
  - 添加随机动作
---

学习资料:
  * [强化学习系列教程]({% link _tutorials/machine-learning/reinforcement-learning/1-1-A-RL.md %})
  * [本节学习代码](https://github.com/MorvanZhou/train-robot-arm-from-scratch/tree/master/part3){:target="_blank"}

[上次]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch2.md %})我们搭建好了一个静态的环境, 整个环境还没有动起来.
这次我们结合手臂的运动部分和手臂的成像部分来写全整个手臂的摆动规则. 并且通过不断地可视化来测试是否写错.

下面可以看到我们使用随机动作来测试手臂的运行情况.

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/ML-practice/arm3-1.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>


{% include assign-heading.html %}

要定义手臂, 我们就需要用一个表来存储手臂的所有信息. 这个表的信息是流通的,
我们也能将这个信息传送到 `Viewer` 来进行可视化处理. 所以这个表是非常重要的.
在 `ArmEnv` 中, 除了一些提前定义的环境属性, 就是在 `__init__` 中定义手臂的表格了.

```python
# env.py

class ArmEnv(object):
    viewer = None
    dt = 0.1                                # 转动的速度和 dt 有关
    action_bound = [-1, 1]                  # 转动的角度范围
    goal = {'x': 100., 'y': 100., 'l': 40}  # 蓝色 goal 的 x,y 坐标和长度 l
    state_dim = 2                           # 两个观测值
    action_dim = 2                          # 两个动作

    def __init__(self):
        self.arm_info = np.zeros(
            2, dtype=[('l', np.float32), ('r', np.float32)])
        # 生成出 (2,2) 的矩阵
        self.arm_info['l'] = 100        # 两段手臂都 100 长
        self.arm_info['r'] = np.pi/6    # 两段手臂的端点角度
```

`self.arm_info` 是一个 2x2 的表, `self.arm_info['l']` 有两个信息, 都是两段手臂的长度,
`self.arm_info['r']` 记录的则是当前两段手臂的旋转角度. 之后手臂做动作时, 都只是这个旋转角度的变化.

接着我们在 `Viewer` 中将 `arm_info` 和 `goal` 传入, 并确定手臂的初始中心点. 手臂将围绕这个中心点旋转.
这里我们按在上面定义的 `goal` 的坐标重新画了 `goal` 位置信息. 这样 goal 就会出现在左下角.


```python
# env.py

class Viewer(pyglet.window.Window)
    def __init__(self, arm_info, goal):
        ...
        # 添加 arm 信息
        self.arm_info = arm_info
        # 添加窗口中心点, 手臂的根
        self.center_coord = np.array([200, 200])

        ...
        # 蓝色 goal 的信息包括他的 x, y 坐标, goal 的长度 l
        self.goal = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,    # 4 corners
            ('v2f', [goal['x'] - goal['l'] / 2, goal['y'] - goal['l'] / 2,
                     goal['x'] - goal['l'] / 2, goal['y'] + goal['l'] / 2,
                     goal['x'] + goal['l'] / 2, goal['y'] + goal['l'] / 2,
                     goal['x'] + goal['l'] / 2, goal['y'] - goal['l'] / 2]),
            ('c3B', (86, 109, 249) * 4))    # color
```







{% include google-in-article-ads.html %}

{% include assign-heading.html %}

看下面不要被吓到了, 下面一大堆, 但是说的就一件事, 给我了 `self.arm_info` 的手臂角度信息, 我怎么样在屏幕上显示手臂的移动信息.
下面都是一些三角函数的计算, 找出每段手臂4个端点的坐标, 然后将坐标赋值给 `self.arm1.vertices` 和 `self.arm2.vertices`.
这样手臂就能自由摆动了, 无论摆动到哪个角度, 我们都能找到对应的点坐标. 我觉得我这应该都不是最优的换算方法, 三角函数学得好的朋友们应该能写出更好的方法.

```python
# env.py

class Viewer(pyglet.window.Window)
    def _update_arm(self):
        (a1l, a2l) = self.arm_info['l']     # radius, arm length
        (a1r, a2r) = self.arm_info['r']     # radian, angle
        a1xy = self.center_coord            # a1 start (x0, y0)
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy   # a1 end and a2 start (x1, y1)
        a2xy_ = np.array([np.cos(a1r+a2r), np.sin(a1r+a2r)]) * a2l + a1xy_  # a2 end (x2, y2)

        # 第一段手臂的4个点信息
        a1tr, a2tr = np.pi / 2 - self.arm_info['r'][0], np.pi / 2 - self.arm_info['r'].sum()
        xy01 = a1xy + np.array([-np.cos(a1tr), np.sin(a1tr)]) * self.bar_thc
        xy02 = a1xy + np.array([np.cos(a1tr), -np.sin(a1tr)]) * self.bar_thc
        xy11 = a1xy_ + np.array([np.cos(a1tr), -np.sin(a1tr)]) * self.bar_thc
        xy12 = a1xy_ + np.array([-np.cos(a1tr), np.sin(a1tr)]) * self.bar_thc

        # 第二段手臂的4个点信息
        xy11_ = a1xy_ + np.array([np.cos(a2tr), -np.sin(a2tr)]) * self.bar_thc
        xy12_ = a1xy_ + np.array([-np.cos(a2tr), np.sin(a2tr)]) * self.bar_thc
        xy21 = a2xy_ + np.array([-np.cos(a2tr), np.sin(a2tr)]) * self.bar_thc
        xy22 = a2xy_ + np.array([np.cos(a2tr), -np.sin(a2tr)]) * self.bar_thc

        # 将点信息都放入手臂显示中
        self.arm1.vertices = np.concatenate((xy01, xy02, xy11, xy12))
        self.arm2.vertices = np.concatenate((xy11_, xy12_, xy21, xy22))
```












{% include assign-heading.html %}

定义好了手臂的 update 规则, 我们就继续定义 update 规则时, 需要用到的手臂角度信息更新原则. 这个更新原则体现在 `ArmEnv` 中.
如果你还记得, 我们把手臂的运动和手臂的画图分开了. 所以运动的部分写在 `ArmEnv` 里. 这里我们会要用到手臂的 `self.arm_info` 信息,
加上 `step()` 功能传入的一个 `action` 来更新手臂的在下一时刻的 info 信息.

```python
# env.py

class ArmEnv(object):
    def step(self, action):
        done = False
        r = 0.

        # 计算单位时间 dt 内旋转的角度, 将角度限制在360度以内
        action = np.clip(action, *self.action_bound)
        self.arm_info['r'] += action * self.dt
        self.arm_info['r'] %= np.pi * 2    # normalize

        # 我们可以将两截手臂的角度信息当做一个 state (之后会变)
        s = self.arm_info['r']

        # 如果手指接触到蓝色的 goal, 我们判定结束回合 (done)
        # 所以需要计算 finger 的坐标
        (a1l, a2l) = self.arm_info['l']  # radius, arm length
        (a1r, a2r) = self.arm_info['r']  # radian, angle
        a1xy = np.array([200., 200.])    # a1 start (x0, y0)
        a1xy_ = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy  # a1 end and a2 start (x1, y1)
        finger = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a1xy_  # a2 end (x2, y2)

        # 根据 finger 和 goal 的坐标得出 done and reward
        if self.goal['x'] - self.goal['l']/2 < finger[0] < self.goal['x'] + self.goal['l']/2:
            if self.goal['y'] - self.goal['l']/2 < finger[1] < self.goal['y'] + self.goal['l']/2:
                done = True
                r = 1.      # finger 在 goal 以内
        return s, r, done
```








{% include google-in-article-ads.html %}

{% include assign-heading.html %}

为了完成所有任务, 我们需要让环境产生一些随机动作, 用来测试现在的这个环境可行性.
还有每次开始回合的时候, 手臂的初始状态也可以在这里设置. 有了这些设置, 我们就能测试旋转的手臂啦.

```python
# env.py

class ArmEnv(object):
    def reset(self):
        self.arm_info['r'] = 2 * np.pi * np.random.rand(2)
        return self.arm_info['r']

    def sample_action(self):
        return np.random.rand(2)-0.5    # two radians
```

最后测试的时候, 在 env.py 最下面写一个简单的循环, 直接在 env.py 里进行测试.

```python
if __name__ == '__main__':
    env = ArmEnv()
    while True:
        env.render()
        env.step(env.sample_action())
```

<video class="tut-content-video" controls loop autoplay muted>
  <source src="/static/results/ML-practice/arm3-1.mp4" type="video/mp4">
  Your browser does not support HTML5 video.
</video>

上面这个基础环境的[全部代码在这](https://github.com/MorvanZhou/train-robot-arm-from-scratch/tree/master/part3/env.py){:target="_blank"}.
这就是我们一个抛开 RL 的环境, 手臂经测试, 能够用, 而且每个关节都正常. 接着我们就[套上一个 RL 的方法]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch4.md %}), 来测试一下整体效果.

*实战:从头开始搭建训练机器人手臂*

* *[搭建结构]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})*
* *[写静态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch2.md %})*
* *[写动态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch3.md %})*
* *[加入强化学习算法]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch4.md %})*
* *[完善测试]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch5.md %})*