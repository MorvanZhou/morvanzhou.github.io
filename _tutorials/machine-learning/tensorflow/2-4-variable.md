---
youku_id: XMTYxMzY2MDM2OA
youtube_id: jGxK7gfglrI
bilibili_id: 16002704
description: "注意定义了变量以后, 一定要定义init = tf.initialize_all_variables(), 不然,变量就不会被初始.然后同样,在 sess里,也要 sess.run(init), 激活 init这一步."
author : 商晋
chapter: 2
title: Variable 变量
date: 2016-11-3
post-headings:
  - 简单运用
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tensorflowTUT/tensorflow7_variable.py){:target="_blank"}
  * 为 TF 2017 打造的[新版可视化教学代码](https://github.com/MorvanZhou/Tensorflow-Tutorial){:target="_blank"}

{% include assign-heading.html %}

这节课我们学习如何在 Tensorflow 中使用 `Variable` .

在 Tensorflow 中，定义了某字符串是变量，它才是变量，这一点是与 Python 所不同的。

定义语法： `state = tf.Variable()` 

```python
import tensorflow as tf

state = tf.Variable(0, name='counter')

# 定义常量 one
one = tf.constant(1)

# 定义加法步骤 (注: 此步并没有直接计算)
new_value = tf.add(state, one)

# 将 State 更新成 new_value
update = tf.assign(state, new_value)
```

如果你在 Tensorflow 中设定了变量，那么初始化变量是最重要的！！所以定义了变量以后, 
一定要定义 `init = tf.initialize_all_variables()` . 

到这里变量还是没有被激活，需要再在 `sess` 里, `sess.run(init)` , 激活 `init` 这一步.

```python
# 如果定义 Variable, 就一定要 initialize
# init = tf.initialize_all_variables() # tf 马上就要废弃这种写法
init = tf.global_variables_initializer()  # 替换成这样就好
 
# 使用 Session
with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
```

注意：直接 `print(state)` 不起作用！！

一定要把 `sess` 的指针指向 `state` 再进行 `print` 才能得到想要的结果！


以上就是我们今天所学的 `Variable` 打开模式，欢迎继续学习下一章 ———— Tensorflow 中的 `Placeholder`。
