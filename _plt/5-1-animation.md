---
description: 使用 matplotlib 做动画也是可以的, 我们使用其中一种方式, function animation 来说说.
youtube_id: 0g-AuWBTnyg?list=PLXO45tsB95cKiBRXYqNNCw8AUo6tYen3l
youku_link: http://v.youku.com/v_show/id_XMTcyMTQ4MzQ5Mg==.html?f=28097045&o=1
chapter: 5
title: Animation 动画
date: 2016-11-3
---
* 学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt19_animation.py)
  * [reference](http://matplotlib.org/examples/animation/simple_anim.html)
  
使用 matplotlib 做动画也是可以的, 我们使用其中一种方式, function animation 来说说.

`import` 我们所需要的模块, 我们额外加入`animation` 来实现这次的动画效果. 

{% highlight python %}
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
{% endhighlight %}

下面的代码, 我们将生成一条基准的 sin 曲线.

{% highlight python %}
fig, ax = plt.subplots()
x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))
{% endhighlight %}

<img class="course-image" src="/static/results/plt/5_1_1.png">

接着我们将在这条曲线上面动手脚啦, 首先要定义一个方程 `def animate(i)` 
来移动我们的 `line`. 移动时, 是基于变化的 `i`, 不同的 `i` 
将会产生不同位置的 `line`.

{% highlight python %}
def animate(i):
    line.set_ydata(np.sin(x + i/10.0)) 
    return line,
{% endhighlight %}

我们还需要定义一个方程 `def init()`, 这个是 `animation` 中的初始化情况.

{% highlight python %}
def init():
    line.set_ydata(np.sin(x))
    return line,
{% endhighlight %}

有了初始化情况 `init()` 和动画的方程 `animate()`, 我们就能把它们当作参数传入进 
`plt` 的 `animation.FuncAnimation()` 中. `fig=` 是我们要输出到那一个 figure 中.
`func=` 是定义我们的动画方程, `frames=` 是每次循环这个方程多少步, 这个和上面的 `i` 有关,
`init_func=` 是放初始状态的地方, `interval=` 是显示动画的频率(20毫秒更新一次),
`blit=`需要注意, 如果你使用 mac 系统, `blit=False`才不会报错(plt 有 bug), 
 `blit=True` 的意思是只更新图中有变化的数, 这个可以节省系统资源.

{% highlight python %}
ani = animation.FuncAnimation(
    fig=fig, func=animate, 
    frames=100, init_func=init,
    interval=20, blit=False
    )
plt.show()
{% endhighlight %}

如果想保存制作好的动画, 需要安装额外的模块: `ffmpeg` 或者 `mencoder`. 
具体信息请查看这个[链接](http://matplotlib.sourceforge.net/api/animation_api.html).
设置好了以后, 就能运用下面的代码来保存动画啦.

{% highlight python %}
anim.save(
    'basic_animation.mp4', 
    fps=30, 
    extra_args=['-vcodec', 'libx264']
    )
{% endhighlight %}