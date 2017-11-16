---
youku_id: XMTU4NTEwODYyNA
youtube_id: 4r_uaoulXLs
chapter: 5
title: 函数默认参数
date: 2016-11-3

author-link: http://gaufung.info/
author: 高峰
post-headings:
  - 基本使用
  - 实例
  - 进阶
---



我们在定义函数时有时候有些参数在大部分情况下是相同的，只不过为了提高函数的适用性，提供了一些备选的参数，
为了方便函数调用，我们可以将这些参数设置为默认参数，那么该参数在函数调用过程中可以不需要明确给出。


{% include assign-heading.html %}

```python
def function_name(para_1,...,para_n=defau_n,..., para_m=defau_m):
    expressions
```

函数声明只需要在需要默认参数的地方用 `=` 号给定即可, 但是要注意所有的默认参数都不能出现在非默认参数的前面。


{% include assign-heading.html %}

```python
def sale_car(price, color='red', brand='carmy', is_second_hand=True):
    print('price', price,
          'color', color,
          'brand', brand,
          'is_second_hand', is_second_hand,)
```

在这里定义了一个 `sale_car` 函数，参数为车的属性，但除了 `price` 之外，像 `color`, `brand` 和 `is_second_hand` 都是有默认值的，如果我们调用函数 `sale_car(1000)`, 那么与 `sale_car(1000, 'red', 'carmy', True)` 是一样的效果。当然也可以在函数调用过程中传入特定的参数用来修改默认参数。通过默认参数可以减轻我们函数调用的复杂度。


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

##### 3.1 自调用

如果想要在执行脚本的时候执行一些代码，比如[单元测试](https://en.wikipedia.org/wiki/Unit_testing){:target="_blank"}，可以在脚本最后加上单元测试
代码，但是该脚本作为一个模块对外提供功能的时候单元测试代码也会执行，这些往往我们不想要的，我们可以把这些代码放入脚本最后：

```python
if __name__ == '__main__':
    #code_here
```

如果执行该脚本的时候，该 `if` 判断语句将会是 `True`,那么内部的代码将会执行。
如果外部调用该脚本，`if` 判断语句则为 `False`,内部代码将不会执行。

##### 3.2 可变参数

顾名思义，函数的可变参数是传入的参数可以变化的，1个，2个到任意个。当然可以将这些
参数封装成一个 `list` 或者 `tuple` 传入，但不够 `pythonic`。使用可变参数可以很好解决该问题，注意可变参数在函数定义不能出现在**特定参数**和**默认参数**前面，因为可变参数会吞噬掉这些参数。

```python
def report(name, *grades):
    total_grade = 0
    for grade in grades:
        total_grade += grade
    print(name, 'total grade is ', total_grade)
```

定义了一个函数，传入一个参数为 `name`, 后面的参数 `*grades` 使用了 `*` 修饰，表明该参数是一个可变参数，这是一个可迭代的对象。该函数输入姓名和各科的成绩，输出姓名和总共成绩。所以可以这样调用函数 `report('Mike', 8, 9)`，输出的结果为
`Mike total grade is 17`, 也可以这样调用 `report('Mike', 8, 9, 10)`，输出的结果为 `Mike total grade is 27`

##### 3.3 关键字参数

关键字参数可以传入0个或者任意个含参数名的参数，这些参数名在函数定义中并没有出现，这些参数在函数内部自动封装成一个字典(dict).

```python
def portrait(name, **kw):
    print('name is', name)
    for k,v in kw.items():
        print(k, v)
```

定义了一个函数，传入一个参数 `name`, 和关键字参数 `kw`，使用了 `**` 修饰。表明该参数是关键字参数，通常来讲关键字参数是放在函数参数列表的最后。如果调用参数
`portrait('Mike', age=24, country='China', education='bachelor')`
输出:

```
name is Mike
age 24
country China
education bachelor
```

通过可变参数和关键字参数，任何函数都可以用 `universal_func(*args, **kw)` 表达。