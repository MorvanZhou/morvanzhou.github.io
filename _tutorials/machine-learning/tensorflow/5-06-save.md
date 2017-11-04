---
youku_id: XMTYyNzE2MDUwOA
youtube_id: R-22pnDezHU
bilibili_id: 16008452
description: 我们做好了一个神经网络,训练好了,肯定也想保存起来,再次加载. 那今天我们就来说说怎样用 Tensorflow 中的 saver 保存和加载吧
chapter: 5
title: Saver 保存读取 
post-headings:
  - 保存
  - 提取
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tensorflowTUT/tf19_saver.py){:target="_blank"}
  * 为 TF 2017 打造的[新版可视化教学代码](https://github.com/MorvanZhou/Tensorflow-Tutorial){:target="_blank"}

我们搭建好了一个神经网络, 训练好了, 肯定也想保存起来, 用于再次加载. 
那今天我们就来说说怎样用 Tensorflow 中的 saver 保存和加载吧.


{% include assign-heading.html %}

`import`所需的模块, 然后建立神经网络当中的 `W` 和 `b`, 并初始化变量.

```python
import tensorflow as tf
import numpy as np

## Save to file
# remember to define the same dtype and shape when restore
W = tf.Variable([[1,2,3],[3,4,5]], dtype=tf.float32, name='weights')
b = tf.Variable([[1,2,3]], dtype=tf.float32, name='biases')

# init= tf.initialize_all_variables() # tf 马上就要废弃这种写法
# 替换成下面的写法:
init = tf.global_variables_initializer()
```

保存时, 首先要建立一个 `tf.train.Saver()` 用来保存, 提取变量. 再创建一个名为`my_net`的文件夹, 用这个 `saver` 来保存变量到这个目录 `"my_net/save_net.ckpt"`.

```python
saver = tf.train.Saver()

with tf.Session() as sess:
    sess.run(init)
    save_path = saver.save(sess, "my_net/save_net.ckpt")
    print("Save to path: ", save_path)

"""    
Save to path:  my_net/save_net.ckpt
"""
```


{% include assign-heading.html %}

提取时, 先建立零时的`W` 和 `b`容器. 找到文件目录, 并用`saver.restore()`我们放在这个目录的变量.

```python
# 先建立 W, b 的容器
W = tf.Variable(np.arange(6).reshape((2, 3)), dtype=tf.float32, name="weights")
b = tf.Variable(np.arange(3).reshape((1, 3)), dtype=tf.float32, name="biases")

# 这里不需要初始化步骤 init= tf.initialize_all_variables()

saver = tf.train.Saver()
with tf.Session() as sess:
    # 提取变量
    saver.restore(sess, "my_net/save_net.ckpt")
    print("weights:", sess.run(W))
    print("biases:", sess.run(b))

"""
weights: [[ 1.  2.  3.]
          [ 3.  4.  5.]]
biases: [[ 1.  2.  3.]]
"""
```