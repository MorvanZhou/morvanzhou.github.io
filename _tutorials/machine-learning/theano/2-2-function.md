---
youku_id: XMTY2MjY5NTI5Ng
youtube_id: 2exmT0L-QV0
title: Function 用法
description: theano 当中的function 就和 python 中的 function 类似,不过因为要被用在多进程并行运算中,所以他的 function 有他自己的一套使用方式.
author: 灰猫
chapter: 2
date: 2016-11-3
post-headings:
  - 激励函数例子
  - 多输入/输出的 function
  - function 的名字
  - 总结
---


学习资料:
  * [相关代码](https://github.com/MorvanZhou/tutorials/blob/master/theanoTUT/theano5_function.py){:target="_blank"}

theano 当中的 `function` 就和 python 中的 function 类似, 不过因为要被用在多进程并行运算中,所以他的 `function` 有他自己的一套使用方式.
  

这是涉及的是Theano 的function 用法。在theano中由于涉及到GPU加速以及CPU 的并行的运算，所以他的function会有不同。

这次介绍了function的三种用法，并且各举一个例.


首先 ， 导入所需要的python包：

```python
import numpy as np
import theano.tensor as T
import theano
```

{% include assign-heading.html %}


使用activation function(激励函数)的例子。
activation function 的例子是使用 function 最简单的形式。
首先需要定义一个 tensor `T`:

```python
x = T.dmatrix('x')
```

然后声明了概率计算方式，这里需要注意这里的计算方式要用到Theano里面的计算方式。而不能使用numpy包里面的`exp()`。

```python
s = 1/(1+T.exp(-x)) # logistic or soft step 
```

最后。调用 theano 定义的计算函数 `logistic`

```python
logistic = theano.function([x], s)
print(logistic([[0,1],[-2,-3]]))

"""
[[ 0.5         0.73105858]
 [ 0.26894142  0.11920292]]
"""
```

{% include assign-heading.html %}


假定我们的 theano 函数中的输入值是两个，输出也是两个。
指定输入的值是矩阵`a`,`b`

```python
a,b = T.dmatrices('a','b')
```

计算输入a，b 之间的差（`diff`）, 差的绝对值（`abs_diff`），差的平方（`diff_squared`）

```python
diff=a-b
abs_diff=abs(diff)
diff_squared = diff**2
```

在这次使用`theano.function`的时候可以指定两个输，并且输出这两个数值的差（`diff`），差的绝对值（`abs_diff`），
差的平方（`diff_squared`）。当我们在调用这个函数的时候会将这三个结果作为输出值。

```python 
f = theano.function([a,b], [diff,abs_diff,diff_squared])
```

最后调用函数`f`, 并且向函数传递初始化之后的参数。

```python

x1,x2,x3= f(
    np.ones((2,2)), # a
    np.arange(4).reshape((2,2))  # b
)
print(x1, x2, x3)

"""
array([[ 1.,  0.],
       [-1., -2.]]),
array([[ 1.,  0.],
       [ 1.,  2.]]),
array([[ 1.,  0.],
       [ 1.,  4.]])   
"""
```


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

首先，我们可以使用 `T.dscalars()` 里面同时定义三个纯量的容器。 以及输出值`z`

```python
x,y,w = T.dscalars('x','y','w')
z = (x+y)*w
```


接下来应该是定义 theano 的函数了， 在定义函数的并且指定输入值的时候，我们期望能够有默认值，
于是我们使用 theano 的默认值书写方式来指定

```python
# name for a function
f = theano.function([x,
                     theano.In(y, value=1),
                     theano.In(w,value=2)],
                    z)

print(f(23))    # 使用默认
print(f(23,1,4)) # 不使用默认
"""
48.0
100.0
"""
```

同时，我们还可以在定义默认值的时候，可以指定参数名字。
这样做的目的是防止我们定义的参数过于多的情况下，忘记函数的顺序。

```python
f = theano.function([x,
                     theano.In(y, value=1),
                     theano.In(w,value=2,name='weights')],
                    z)
                    
print (f(23,1,weights=4)) ##调用方式

"""
100.0
"""
```


{% include assign-heading.html %}

这节中，我们介绍了function的三种方式：
首先，一个theanod的function的简单用法;
其次在使用theano的function中可以有多个input和output;
最后是theano的function中可以有默认值并且可以给参数指定名称。

在 fucntion 的参数会在CPU/GPU中共享，下一期会提到 shared value 。敬请期待。

















