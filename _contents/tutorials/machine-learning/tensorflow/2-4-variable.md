---
youku_id: XMTYxMzY2MDM2OA
youtube_id: jGxK7gfglrI
description: "注意定义了变量以后, 一定要定义init = tf.initialize_all_variables(), 不然,变量就不会被初始.然后同样,在 sess里,也要 sess.run(init), 激活 init这一步."


chapter: 2
title: Variable 变量
date: 2016-11-3
---
* 学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/tensorflowTUT/tensorflow7_variable.py)
  
注意定义了变量以后, 一定要定义init = tf.initialize_all_variables().
不然,变量就不会被初始.
然后同样,在 sess里,也要 sess.run(init), 激活 init这一步.

