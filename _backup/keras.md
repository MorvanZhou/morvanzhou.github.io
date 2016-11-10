---
layout: tutorial-post
name: keras
---


# Keras 视频教程结构 (莫烦Python)
<img src="{{site.baseurl}}/static/img/course_cover/keras.jpg" height="200">

Keras 是一个兼容 Theano 和 Tensorflow 的神经网络高级包, 用他来组件一个神经网络非常的快速, 几条语句就搞定了. 而且广泛的兼容性能使 Keras 在 Windows 和 MacOS 或者 Linux 上穿梭自如.


* 内容主要包括:
  * Keras Beckend;
  * 处理分类, 回归问题, 深度学习;
  * CNN 卷积神经网络;
  * RNN 循环神经网络;
  * Autoencoder 自编码.
  
同时也需要大家的赞助一份力量, 让教学视频做得更加的优秀. (支付宝, 微信, paypal赞助请拉倒屏幕最下面~)

---

1. **Why?** [Youtube->](https://www.youtube.com/watch?v=AoK4zpsQN7M&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY&index=1), [优酷->](http://v.youku.com/v_show/id_XMTc3ODk2NjY5Mg==.html?f=28505797)
  * Keras 简介
  * 在这之前, 为了打下点有关基础, 这两段简短的视频介绍都是很推荐的: "什么是机器学习" ([Youtube->](https://www.youtube.com/watch?v=YY7-VKXybjc&list=PLXO45tsB95cIFm8Y8vMkNNPPXAtYXwKin&index=1), [优酷->](http://v.youku.com/v_show/id_XMTYyMjk2NDIwOA==.html?f=27892935&o=1)) 
  * 还有这个: "什么是神经网络" ([Youtube->](https://www.youtube.com/watch?v=RSRkp8VAavQ&index=2&list=PLXO45tsB95cIFm8Y8vMkNNPPXAtYXwKin). [优酷->](http://v.youku.com/v_show/id_XMTU5NDc3MDQwOA==.html?f=27892935&o=1))
  

2. **安装** [Youtube->](https://www.youtube.com/watch?v=glcqKUzr1ZM&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY&index=2), [优酷->](http://v.youku.com/v_show/id_XMTc3ODk5NjUyNA==.html?f=28505797)
  * 介绍如何安装
  * [说明](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/2-installation.py)


3. **兼容 Backend** [Youtube->](https://www.youtube.com/watch?v=FIZiuAM5kQo&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY&index=3), [优酷->](http://v.youku.com/v_show/id_XMTc3OTA0NDc5Mg==.html?f=28505797)
  * Keras 同时兼容 Tensorflow 和 Theano, 我们看看如何替换, 修改这些.
  * [说明](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/3-backend.py)


4. **Regressor 回归** [Youtube->](https://www.youtube.com/watch?v=I_on5dTY3d4&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY&index=4), [优酷->](http://v.youku.com/v_show/id_XMTc3OTEwMDk3Ng==.html?f=28505797)
  * 搭建 Regressor 神经网络的例子
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/4-regressor_example.py)  


5. **Classifier 分类** [Youtube->](https://www.youtube.com/watch?v=3mpDXAXFkfg&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY&index=5), [优酷->](http://v.youku.com/v_show/id_XMTc3OTE4NDc0OA==.html?f=28505797)
  * 搭建 Classifier 神经网络的例子
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/5-classifier_example.py)
  


6. **CNN 卷积神经网络** [Youtube->](https://www.youtube.com/watch?v=zHop6Oq757Y&index=6&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY), [优酷->](http://v.youku.com/v_show/id_XMTc4MDEyMDk0MA==.html?f=28505797&o=1)
  *  CNN 例子
  * 请参考在 "机器学习-简介系列" 中 CNN 的简短介绍 ([Youtube->](https://www.youtube.com/watch?v=hMIZ85t9r9A&list=PLXO45tsB95cIFm8Y8vMkNNPPXAtYXwKin&index=3), [优酷->](http://v.youku.com/v_show/id_XMTY4MzAyNTc4NA==.html?f=27892935&o=1))
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/6-CNN_example.py)
  


7. **RNN Classifier 循环神经网络** [Youtube->](https://www.youtube.com/watch?v=Zhy8NWAMT14&index=7&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY), [优酷->](http://v.youku.com/v_show/id_XMTc4MDE4MDE4OA==.html?f=28505797&o=1)
  *  RNN 做分类器
  * 请参考在 "机器学习-简介系列" 中 RNN 的简短介绍 ([Youtube->](https://www.youtube.com/watch?v=EEtf4kNsk7Q&list=PLXO45tsB95cIFm8Y8vMkNNPPXAtYXwKin&index=4), [优酷->](http://v.youku.com/v_show/id_XMTcyNzYwNjU1Ng==.html?f=27892935&o=1))
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/7-RNN_Classifier_example.py)
  


8. **RNN Regressor LSTM 循环神经网络** [Youtube->](https://www.youtube.com/watch?v=x5jjul-vLv4&index=8&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY), [优酷->](http://v.youku.com/v_show/id_XMTc4MDIxNTkwNA==.html?f=28505797&o=1)
  *  RNN 做回归 
  * 请参考在 "机器学习-简介系列" 中 LSTM 的简短介绍 ([Youtube->](https://www.youtube.com/watch?v=Vdg5zlZAXnU&list=PLXO45tsB95cIFm8Y8vMkNNPPXAtYXwKin&index=5), [优酷->](http://v.youku.com/v_show/id_XMTc0MzY5MTQxMg==.html?f=27892935&o=1))
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/8-RNN_LSTM_Regressor_example.py)
  


9. **Autoencoder 自编码** [Youtube->](https://www.youtube.com/watch?v=OubNgB-Fa4M&index=9&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY), [优酷->](http://v.youku.com/v_show/id_XMTc4MDI2MDg1Mg==.html?f=28505797&o=1)
  * 请参考在 "机器学习-简介系列" 中 Autoencoder 的简短介绍 ([Youtube->](https://www.youtube.com/watch?v=w8HmXgXnVEo&list=PLXO45tsB95cIFm8Y8vMkNNPPXAtYXwKin&index=6), [优酷->](http://v.youku.com/v_show/id_XMTgwNDc1NjYwMA==.html?f=27892935&o=1))
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/9-Autoencoder_example.py)


10. **Save 保存** [Youtube->](https://www.youtube.com/watch?v=e-ICAuGXw7k&index=10&list=PLXO45tsB95cKhCSIgTgIfjtG5y0Bf_TIY), [优酷->](http://v.youku.com/v_show/id_XMTc4MDI4NjIyNA==.html?f=28505797&o=1)
  * 保存和提取训练好的神经网络 
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/kerasTUT/10-save.py)
  
