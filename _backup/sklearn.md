---
layout: tutorial-post
name: sklearn
---

# Sklearn 学习目录 (莫烦Python)
<img src="{{site.baseurl}}/static/img/course_cover/sklearn.jpg" height="200">


Sklearn 是汇集了多种机器学习方法的 python 包. 如果是入门机器学习, 这里面总能有适合你问题的机器学习方法. 而且他以高度统一的学习模式规范了所有学习方法. 我们知道用一种, 就知道使用其他所有种的学习方法. Sklearn 是一款很好上手的机器学习包.

* 这套教材主要包含了:
 * 了解 sklearn 的使用规范和原则;
 * 知道怎么去找合适的机器学习方法;
 * 如何按照规范调整个个参数;
 * 运用它强大的数据库;
 * 机器学习的一些重要原则;


同时也需要大家的赞助一份力量, 让教学视频做得更加的优秀. (支付宝, 微信赞助请拉倒屏幕最下面~)

---

1. **Why?** [Youtube->](https://www.youtube.com/watch?v=7wWMP2elSvE&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO&index=2), [优酷链接->](http://v.youku.com/v_show/id_XMTYxMjg1NjQ4MA==.html?f=27469882&o=1)
  * Scikit-learn 简单介绍
  * 在这之前, "什么是机器学习" ([Youtube->](https://www.youtube.com/watch?v=YY7-VKXybjc&list=PLXO45tsB95cIFm8Y8vMkNNPPXAtYXwKin&index=1), [优酷->](http://v.youku.com/v_show/id_XMTYyMjk2NDIwOA==.html?f=27892935&o=1)), 这段简短的视频介绍都是很推荐的.


2. **安装** [Youtube->](https://www.youtube.com/watch?v=FG3W1_8ogBE&index=3&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO), [优酷链接->](http://v.youku.com/v_show/id_XMTYxMjg5MTYyOA==.html?f=27469882&o=1)
  * 介绍如何安装

3. **如何选择机器学习方法** [Youtube->](https://www.youtube.com/watch?v=GB8SNR-cT7w&index=4&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO), [优酷链接->](http://v.youku.com/v_show/id_XMTYxMjk0MzY3Ng==.html?f=27469882&o=1)
  * 机器学习的方法有很多, 我们如何[通过比较](http://scikit-learn.org/stable/tutorial/machine_learning_map/index.html)来选择适合的机器学习方法呢.

  <img src='http://scikit-learn.org/stable/_static/ml_map.png' height="250">


4. **通用学习模式** [Youtube->](https://www.youtube.com/watch?v=EvV99YhSsJU&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO&index=5), [优酷链接->](http://v.youku.com/v_show/id_XMTYxMzg0NzE5Mg==.html?f=27469882&o=1)
  * Sklearn 是一个高度统一的模块, 所有的学习方法都有类似的学习语句. 知一懂百. 
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk4_learning_pattern.py)


5. **sklearn 的数据库** [Youtube->](https://www.youtube.com/watch?v=lXznUoPCJLM&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO&index=6), [优酷链接->](http://v.youku.com/v_show/id_XMTYxNjU0NzU1Mg==.html?f=27469882&o=1)
  * sklearn 提供了很多[数据](http://scikit-learn.org/stable/modules/classes.html#module-sklearn.datasets)供你练习. 
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk5_datasets.py)


6. **model 的常用功能和属性** [Youtube->](https://www.youtube.com/watch?v=d2BMirIToF4&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO&index=7), [优酷链接->](http://v.youku.com/v_show/id_XMTYxNjU3MTQzMg==.html?f=27469882&o=1)
  * 每一种 model 都有自己的功能和属性, 而且这种功能属性也是高度统一的. 
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk6_model_attribute_method.py)


7. **Normalization 数据标准化** [Youtube->](https://www.youtube.com/watch?v=3GxT8n0ShsU&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO&index=8), [优酷链接->](http://v.youku.com/v_show/id_XMTYxNjgwNjkxNg==.html?f=27469882&o=1)
  * 请参考 "机器学习-简介系列" 中的 "数据标准化4分钟介绍" ([Youtube->](https://www.youtube.com/watch?v=1YpKUpitT98&list=PLXO45tsB95cIFm8Y8vMkNNPPXAtYXwKin&index=7). [优酷->](http://v.youku.com/v_show/id_XMTY5MjU1MTg0NA==.html?f=27892935&o=1)) 
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk7_normalization.py)


8. **Cross Validation 交叉验证1** [Youtube->](https://www.youtube.com/watch?v=UeyZX31VZE8&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO&index=9), [优酷链接->](http://v.youku.com/v_show/id_XMTYxNzcwOTc1Ng==.html?f=27469882&o=1)
  * 请参考 "机器学习-简介系列" 中的 "如何检验机器学习" [Youtube->](https://www.youtube.com/watch?v=vBJ_XbRnzKE&index=6&list=PLXO45tsB95cIFm8Y8vMkNNPPXAtYXwKin). [优酷->](http://v.youku.com/v_show/id_XMTY5MTk1NzIzMg==.html?f=27892935&o=1). 
  * [代码](https://github.com/MorvanZhou/tutorials/tree/master/sklearnTUT/sk8_cross_validation)


9. **Cross Validation 交叉验证2** [Youtube->](https://www.youtube.com/watch?v=VsLYdjiG5KQ&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO&index=10), [优酷链接->](http://v.youku.com/v_show/id_XMTYxNzgxODQzMg==.html?f=27469882&o=1)
  * 介绍learning curve 和他的使用方法. 
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk9_cross_validation2.py)


10. **Cross Validation 交叉验证3** [Youtube->](https://www.youtube.com/watch?v=nRVKdxfRFtA&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO&index=11), [优酷链接->](http://v.youku.com/v_show/id_XMTYxODA2Mzk0OA==.html?f=27469882&o=1)
  * 介绍 validation curve 和他的使用方法 
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk10_cross_validation3.py)


11. **Save 保存** [Youtube->](https://www.youtube.com/watch?v=8sMZkhWtdaI&index=12&list=PLXO45tsB95cI7ZleLM5i3XXhhe9YmVrRO), [优酷链接->](http://v.youku.com/v_show/id_XMTYyOTkwNzA2OA==.html?f=27469882&o=1)
  * 保存学好的 model. 
  * [代码](https://github.com/MorvanZhou/tutorials/blob/master/sklearnTUT/sk11_save.py)

