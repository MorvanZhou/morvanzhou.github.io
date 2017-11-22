---
youku_id:
youtube_id:
bilibili_id:
title: 从头开始做一个机器手臂2 写静态环境
description: "上次我们已经搭建好了三个主要部分, 包括
main.py, rl.py, env.py. 强化学习最重要的部分之一就是怎样定义你的环境. 做出来一个可视化的模拟环境能大大减轻不可见的负担. 有一个机器人在你屏幕上跑来跑去,
你能看见它, 根据他的行为来调整程序, 比看不见任何东西, 不知道是哪除了问题要好得多. 所以做一个可视化的环境变得重要起来. "
publish-date: 2017-11-22
thumbnail: "/static/thumbnail/ML-practice/arm2.jpg"
chapter: 1
post-headings:
  - 做一个 Viewer
  - 初始化 Viewer
  - 显示图像
---

学习资料:
  * [强化学习系列教程]({% link _tutorials/machine-learning/reinforcement-learning/1-1-A-RL.md %})
  * [本节学习代码](https://github.com/MorvanZhou/train-robot-arm-from-scratch/tree/master/part2){:target="_blank"}


[上次]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})我们已经搭建好了三个主要部分, 包括
main.py, rl.py, env.py. 强化学习最重要的部分之一就是怎样定义你的环境. 做出来一个可视化的模拟环境能大大减轻不可见的负担. 有一个机器人在你屏幕上跑来跑去,
你能看见它, 根据他的行为来调整程序, 比看不见任何东西, 不知道是哪除了问题要好得多. 所以做一个可视化的环境变得重要起来.

这一次, 我们先熟悉一下如何用 pyglet 来画一些手臂的必要组建, 看到了画出来的东西, 我们就更加能确信我们走在了正确的道路上.

{% include tut-image.html image-name="arm2-1.png" %}


{% include assign-heading.html %}

其实 env.py 光有一个 `ArmEnv` 的 class 是不够的, 这个 `ArmEnv` 和可视化的部分分开来处理会更好管理你的代码.
所以, 我在 env.py 中, 除了 `ArmEnv`, 我还加入了一个叫 `Viewer` 的 class 来单独处理可视化的部分. 而 `ArmEnv` 来处理逻辑运行.

env.py
* `class ArmEnv` 手臂的运动
* `class Viewer` 手臂的可视化

这个 `Viewer` 包含了下面这些功能, 在可视化之前, 我们引入了 `pyglet` 这个 python 做可视化的模块.
如果你安装过 [gym](https://gym.openai.com/docs/){:target="_blank"}, gym 也是使用 `pyglet` 搭建的模拟环境.
安装过 gym 的朋友就没有必要再安装 `pyglet` 了, 没有安装过的, 你只要在 terminal 或者是 cmd 里面输入下面这个就能安装了.
同样, 我们还是用了 `numpy` 来做数据运算, 没有安装的朋友也可以自行安装.

```shell
$ pip3 install pyglet numpy
```

安装好之后, 我们就能 import 这个 `pyglet` 模块. 并继承给 `Viewer`. 让 `Viewer` 可以使用 `pyglet` 的功能.

```python
# env.py

import pyglet
class Viewer(pyglet.window.Window):
    def __init__(self, arm_info):
        # 画出手臂等
    def render(self):
        # 刷新并呈现在屏幕上
    def on_draw(self):
        # 刷新手臂等位置
    def _update_arm(self):
        # 更新手臂的位置信息
```

上面的 `__init__` 和 `_update_arm` 是最主要的部分. 其它两个部分都是可以通用的, 换个环境还能是一样. 所以接下载我们重点说 `__init__` 和 `_update_arm`.









{% include google-in-article-ads.html %}
{% include assign-heading.html %}

在看 `__init__` 之前, 我们来分析一下, 我们要在什么时候建立这个 `Viewer`. 为了减少运算, 没有用到可视化的时候, 我们完全不用调用这个 `Viewer` 类.
所以在调用可视化的 `env.render()` 时, 我们才需要可视化, `Viewer` 这时候被调用生成最科学. 所以在 `ArmEnv` 中, 我们这样修改.

```python
class ArmEnv(object):
    viewer = None       # 首先没有 viewer

    def render(self):
        if self.viewer is None: # 如果调用了 render, 而且没有 viewer, 就生成一个
            self.viewer = Viewer()
        self.viewer.render()    # 使用 Viewer 中的 render 功能
```

找好了这个调用可视化的时机, 我们就能安心在 `Viewer` 中开始画手臂的样子了.
画手臂的时候我们要用到 pyglet 模块当中的一些内容, 想提前了解 pyglet 的使用方法的朋友, 可以戳[这里](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/#){:target="_blank"}.

```python
# env.py

class Viewer(pyglet.window.Window):
    bar_thc = 5     # 手臂的厚度

    def __init__(self):
        # 创建窗口的继承
        # vsync 如果是 True, 按屏幕频率刷新, 反之不按那个频率
        super(Viewer, self).__init__(width=400, height=400, resizable=False, caption='Arm', vsync=False)

        # 窗口背景颜色
        pyglet.gl.glClearColor(1, 1, 1, 1)

        # 将手臂的作图信息放入这个 batch
        self.batch = pyglet.graphics.Batch()    # display whole batch at once

        # 添加蓝点
        self.point = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,    # 4 corners
            ('v2f', [50, 50,                # x1, y1
                     50, 100,               # x2, y2
                     100, 100,              # x3, y3
                     100, 50]),             # x4, y4
            ('c3B', (86, 109, 249) * 4))    # color

        # 添加一条手臂
        self.arm1 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [250, 250,              # 同上, 点信息
                     250, 300,
                     260, 300,
                     260, 250]),
            ('c3B', (249, 86, 86) * 4,))    # color

        # 按理添加第二条手臂...
```

上面我们设置了手臂和目标点的信息, 因为他们都可以理解为是一个长方形, 有四个顶点, 我们就能使用 `GL_QUADS` 这种形式.
在 pyglet 中, 还有很多其他的多边形形式或者是线形式, 具体可以参考这个[链接](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/graphics.html){:target="_blank"}.
我们将所有的形状信息加入一个 `batch`, 然后在刷新的时候整个 batch 都会刷新, 节约时间. 上面的 `v2f` 是每个点的 x, y 信息, 一共有四个点, 所以有8个数字.
除了 `v2f` 的形式, 还有其他的形式能在[这里](https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/programming_guide/graphics.html#vertex-attributes){:target="_blank"}找到对应的说明.
`c3B` 表示的是这个物体的颜色, 每个点都有个颜色, 而每个颜色用3原色来代表, 我们这个物体是纯色的, 所以每个点, 我用相同的颜色, 在 `point` 中 `(86, 109, 249)` 就是蓝色, 然后 `*4` 就是4个顶点都是蓝色.

为了简化这里的代码, 第二条手臂的形式和第一条一样, 第二条手臂的代码我就没写上了,
在[这里](https://github.com/MorvanZhou/train-robot-arm-from-scratch/blob/master/part2/env.py){:target="_blank"}能看到全部代码.








{% include google-in-article-ads.html %}

{% include assign-heading.html %}

写好了代码, 我们就来显示他们. pyglet 是一个实时刷新的做动画模块, 所以每次刷新的时候, 会调用一个功能,
`on_draw()` 就是 pyglet 刷新时本身需要的一个功能. 而 `render()` 是我们在 `env.render()` 中调用的功能.
它们这两个功能在你建立另外的环境时可以不用变化, 因为这算是必要功能.

```python
# env.py

class Viewer(pyglet.window.Window):
    def render(self):
        self._update_arm()  # 更新手臂内容 (暂时没有变化)
        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()

    def on_draw(self):
        self.clear()        # 清屏
        self.batch.draw()   # 画上 batch 里面的内容
```

有了这两个功能, pyglet 就知道如何画图, 刷新图像了. 最后, 我们要在 `env.py` 最下面写上一个测试代码.
当运行 `env.py` 时, 我们就能测试画图画得怎样了. 记得每改动一点, 就运行看看, 这样才知道你的图到底画对没.

```python
if __name__ == '__main__':
    env = ArmEnv()
    while True:
        env.render()
```

{% include tut-image.html image-name="arm2-1.png" %}

这一次我们还只是看到了一些不会动的图像, [下一次]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch3.md %})我们就把这些不会动的让它动起来.


*实战:从头开始搭建训练机器人手臂*

* *[搭建结构]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch1.md %})*
* *[写静态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch2.md %})*
* *[写动态环境]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch3.md %})*
* *[加入强化学习算法]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch4.md %})*
* *[完善测试]({% link _tutorials/machine-learning/ML-practice/RL-build-arm-from-scratch5.md %})*