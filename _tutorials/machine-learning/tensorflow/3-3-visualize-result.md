---
youku_id: XMTU5OTQzOTMzNg
youtube_id: nhn8B0pM9ls
bilibili_id: 16003111
description: 我们已经建立好了一个完整的神经网络,如果能够可视化训练的结果,就能够更好的理解神经网络是如何训练的.这次就提到了 matplotlib 这个模块,用它来进行结果可视化处理.我们看到了神经网络的模型是如何 fit 上原始的 data 的.
author: 赵孔亚
chapter: 3
title: 例子3 结果可视化
date: 2016-11-3
post-headings:
  - matplotlib 可视化
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/tree/master/tensorflowTUT/tf12_plot_result){:target="_blank"}
  * 为 TF 2017 打造的[新版可视化教学代码](https://github.com/MorvanZhou/Tensorflow-Tutorial){:target="_blank"}

{% include assign-heading.html %}

构建图形，用散点图描述真实数据之间的关系。
（注意：`plt.ion()`用于连续显示。）

```python
# plot the real data
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.scatter(x_data, y_data)
plt.ion()#本次运行请注释，全局运行不要注释
plt.show()
```

散点图的结果为：

{% include tut-image.html image-name="3_3_1.png" %}

接下来，我们来显示预测数据。

每隔50次训练刷新一次图形，用红色、宽度为5的线来显示我们的预测数据和输入之间的关系，并暂停0.1s。

```python
for i in range(1000):
    # training
    sess.run(train_step, feed_dict={xs: x_data, ys: y_data})
    if i % 50 == 0:
        # to visualize the result and improvement
        try:
            ax.lines.remove(lines[0])
        except Exception:
            pass
        prediction_value = sess.run(prediction, feed_dict={xs: x_data})
        # plot the prediction
        lines = ax.plot(x_data, prediction_value, 'r-', lw=5)
        plt.pause(0.1)
```

最后，机器学习的结果为：

{% include tut-image.html image-name="3_3_2.png" %}


