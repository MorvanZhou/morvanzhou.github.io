---
youku_id: XMTcyMTQ4MzQ5Mg
youtube_id: 0g-AuWBTnyg
description: 使用 matplotlib 做动画也是可以的, 我们使用其中一种方式, function animation 来说说.
author: Jeff
chapter: 5
title: Animation 动画
date: 2016-11-3
post-headings:
  - 定义方程
  - 参数设置
---
{% assign post-heading-count = -1 %}
学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt19_animation.py)
  * [reference](http://matplotlib.org/examples/animation/simple_anim.html)

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

使用matplotlib做动画也是可以的，我们使用其中一种方式，function animation来说说，
具体可参考[matplotlib animation api](http://matplotlib.sourceforge.net/api/animation_api.html)。首先，我们做一些准备工作：

```python
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
fig, ax = plt.subplots()
```

我们的数据是一个0~2π内的正弦曲线：

```python
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
```

<img class="course-image" src="/static/results/plt/5_1_1.png">

接着，构造自定义动画函数`animate`，用来更新每一帧上各个`x`对应的`y`坐标值，参数表示第i帧：

```python
def animate(i):
    line.set_ydata(np.sin(x + i/10.0))
    return line,
```

然后，构造开始帧函数`init`：

```python
def init():
    line.set_ydata(np.sin(x))
    return line,
```

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>


接下来，我们调用`FuncAnimation`函数生成动画。参数说明：
1. `fig` 进行动画绘制的figure
2. `func` 自定义动画函数，即传入刚定义的函数`animate`
3. `frames` 动画长度，一次循环包含的帧数
4. `init_func` 自定义开始帧，即传入刚定义的函数`init`
5. `interval` 更新频率，以ms计
6. `blit` 选择更新所有点，还是仅更新产生变化的点。应选择`True`，但mac用户请选择`False`，否则无法显示动画

```python
ani = animation.FuncAnimation(fig=fig,
                              func=animate,
                              frames=100,
                              init_func=init,
                              interval=20,
                              blit=False)
```

显示动画：

```python
plt.show()
```

当然，你也可以将动画以mp4格式保存下来，但首先要保证你已经安装了`ffmpeg` 或者`mencoder`，
更多信息参考[matplotlib animation api](http://matplotlib.sourceforge.net/api/animation_api.html)：

```python
anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
```
  
  