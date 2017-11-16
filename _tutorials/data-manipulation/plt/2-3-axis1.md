---
youku_id: XMTcxNjEyMDY4MA
youtube_id: 46EsDY8V6lQ
bilibili_id: 16378447
description: 在 matplotlib 中如何设置坐标轴(axis)的范围, 单位长度, 替代文字等等.
author: 黄伟
chapter: 2
title: 设置坐标轴1
date: 2016-11-3
post-headings:
  - 调整名字和间隔

---

学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/matplotlibTUT/plt5_ax_setting1.py){:target="_blank"}
  
在 matplotlib 中如何设置坐标轴的范围, 单位长度, 替代文字等等.

{% include assign-heading.html %}


使用`import`导入模块`matplotlib.pyplot`，并简写成`plt`
使用`import`导入模块`numpy`，并简写成`np`

```python
import matplotlib.pyplot as plt
import numpy as np
```

使用`np.linspace`定义x：范围是(-3,3);个数是50.
仿真一维数据组(`x` ,`y1`)表示曲线1.
仿真一维数据组(`x` ,`y2`)表示曲线2.

```python
x = np.linspace(-3, 3, 50)
y1 = 2*x + 1
y2 = x**2
```

使用`plt.figure`定义一个图像窗口.
使用`plt.plot`画(`x` ,`y2`)曲线.
使用`plt.plot`画(`x` ,`y1`)曲线，曲线的颜色属性(`color`)为红色;曲线的宽度(`linewidth`)为1.0；曲线的类型(`linestyle`)为虚线.

```python
plt.figure()
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
```

使用`plt.xlim`设置x坐标轴范围：(-1, 2)；
使用`plt.ylim`设置y坐标轴范围：(-2, 3)；
使用`plt.xlabel`设置x坐标轴名称：'I am x'；
使用`plt.ylabel`设置y坐标轴名称：'I am y'；

```python
plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')
plt.show()
```

{% include tut-image.html image-name="2_3_1.png" %}

使用`np.linspace`定义范围以及个数：范围是(-1,2);个数是5.
使用`print`打印出新定义的范围.
使用`plt.xticks`设置x轴刻度：范围是(-1,2);个数是5.

```python
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
```


使用`plt.yticks`设置y轴刻度以及名称：刻度为[-2, -1.8, -1, 1.22, 3]；对应刻度的名称为['really bad','bad','normal','good', 'really good'].
使用`plt.show`显示图像.

```python
plt.yticks([-2, -1.8, -1, 1.22, 3],[r'$really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])
plt.show()
```

{% include tut-image.html image-name="2_3_2.png" %}
