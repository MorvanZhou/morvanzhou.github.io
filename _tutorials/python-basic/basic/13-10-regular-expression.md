---
youku_id: XMzIzNTkzODYyOA
youtube_id: l1MAW1z641E
b_av: 16926522
b_cid: 28279154
b_page: 36
chapter: 13
title: 正则表达式
publish-date: 2017-11-29
thumbnail: /static/thumbnail-small/basic/13-10.jpg
post-headings:
  - 简单的匹配
  - 灵活匹配
  - 按类型匹配
  - 重复匹配
  - 分组
  - findall
  - replace
  - split
  - compile
  - 小抄
description: "正则表达式 (Regular Expression) 又称 RegEx, 是用来匹配字符的一种工具. 在一大串字符中寻找你需要的内容.
它常被用在很多方面, 比如网页爬虫, 文稿整理, 数据筛选等等. 最简单的一个例子, 比如我需要爬取网页中每一页的标题.
而网页中的标题常常是这种形式."
---

学习资料:
* [本节全部代码](https://github.com/MorvanZhou/tutorials/blob/master/basic/36_RegEx.py){:target="_blank"}
* [代码的 notebook 形式](https://github.com/MorvanZhou/tutorials/blob/master/basic/36_regex.ipynb){:target="_blank"}
* [网页爬虫教程](/tutorials/data-manipulation/scraping/)

正则表达式 (Regular Expression) 又称 RegEx, 是用来匹配字符的一种工具. 在一大串字符中寻找你需要的内容.
它常被用在很多方面, 比如网页爬虫, 文稿整理, 数据筛选等等. 最简单的一个例子, 比如我需要爬取网页中每一页的标题.
而网页中的标题常常是这种形式.

```
<title>我是标题</ title>
```

而且每个网页的标题各不相同, 我就能使用正则表达式, 用一种简单的匹配方法, 一次性选取出成千上万网页的标题信息.
正则表达式绝对不是一天就能学会和记住的, 因为表达式里面的内容非常多, 强烈建议,
现在这个阶段, 你只需要了解正则里都有些什么, 不用记住, 等到你真正需要用到它的时候, 再反过头来,
好好琢磨琢磨, 那个时候才是你需要训练自己记住这些表达式的时候.




{% include assign-heading.html %}

正则表达式无非就是在做这么一回事. 在文字中找到特定的内容, 比如下面的内容.
我们在 "dog runs to cat" 这句话中寻找是否存在 "cat" 或者 "bird".

```python
# matching string
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(pattern1 in string)    # True
print(pattern2 in string)    # False
```

但是正则表达式绝非不止这样简单的匹配, 它还能做更加高级的内容. 要使用正则表达式,
首先需要调用一个 python 的内置模块 `re`. 然后我们重复上面的步骤, 不过这次使用正则.
可以看出, 如果 `re.search()` 找到了结果, 它会返回一个 match 的 object. 如果没有匹配到,
它会返回 None. 这个 `re.search()` 只是 `re` 中的一个功能, 之后会介绍其它的功能.

```python
import re

# regular expression
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string))  # <_sre.SRE_Match object; span=(12, 15), match='cat'>
print(re.search(pattern2, string))  # None
```









{% include google-in-article-ads.html %}
{% include assign-heading.html %}

除了上面的简单匹配, 下面的内容才是正则的核心内容, 使用特殊的 pattern 来灵活匹配需要找的文字.

如果需要找到潜在的多个可能性文字, 我们可以使用 `[]` 将可能的字符囊括进来. 比如 `[ab]` 就说明我想要找的字符可以是 `a` 也可以是 `b`.
这里我们还需要注意的是, 建立一个正则的规则, 我们在 pattern 的 "" 前面需要加上一个 `r` 用来表示这是正则表达式, 而不是普通字符串.
通过下面这种形式, 如果字符串中出现 "run" 或者是 "ran", 它都能找到.

```python
# multiple patterns ("run" or "ran")
ptn = r"r[au]n"       # start with "r" means raw string
print(re.search(ptn, "dog runs to cat"))    # <_sre.SRE_Match object; span=(4, 7), match='run'>
```

同样, 中括号 `[]` 中还可以是以下这些或者是这些的组合. 比如 `[A-Z]` 表示的就是所有大写的英文字母.
`[0-9a-z]` 表示可以是数字也可以是任何小写字母.

```python
print(re.search(r"r[A-Z]n", "dog runs to cat"))     # None
print(re.search(r"r[a-z]n", "dog runs to cat"))     # <_sre.SRE_Match object; span=(4, 7), match='run'>
print(re.search(r"r[0-9]n", "dog r2ns to cat"))     # <_sre.SRE_Match object; span=(4, 7), match='r2n'>
print(re.search(r"r[0-9a-z]n", "dog runs to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='run'>
```







{% include google-in-article-ads.html %}

{% include assign-heading.html %}

除了自己定义规则, 还有很多匹配的规则时提前就给你定义好了的.
下面有一些特殊的匹配类型给大家先总结一下, 然后再上一些例子.

* \d : 任何数字
* \D : 不是数字
* \s : 任何 white space, 如 [\t\n\r\f\v]
* \S : 不是 white space
* \w : 任何大小写字母, 数字和 "_" [a-zA-Z0-9_]
* \W : 不是 \w
* \b : 空白字符 (**只**在某个字的开头或结尾)
* \B : 空白字符 (**不**在某个字的开头或结尾)
* \\\\ : 匹配 \
* . : 匹配任何字符 (除了 \n)
* ^ : 匹配开头
* $ : 匹配结尾
* ? : 前面的字符可有可无

下面就是具体的举例说明啦.

```python
# \d : decimal digit
print(re.search(r"r\dn", "run r4n"))           # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
# \D : any non-decimal digit
print(re.search(r"r\Dn", "run r4n"))           # <_sre.SRE_Match object; span=(0, 3), match='run'>
# \s : any white space [\t\n\r\f\v]
print(re.search(r"r\sn", "r\nn r4n"))          # <_sre.SRE_Match object; span=(0, 3), match='r\nn'>
# \S : opposite to \s, any non-white space
print(re.search(r"r\Sn", "r\nn r4n"))          # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
# \w : [a-zA-Z0-9_]
print(re.search(r"r\wn", "r\nn r4n"))          # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
# \W : opposite to \w
print(re.search(r"r\Wn", "r\nn r4n"))          # <_sre.SRE_Match object; span=(0, 3), match='r\nn'>
# \b : empty string (only at the start or end of the word)
print(re.search(r"\bruns\b", "dog runs to cat"))    # <_sre.SRE_Match object; span=(4, 8), match='runs'>
# \B : empty string (but not at the start or end of a word)
print(re.search(r"\B runs \B", "dog   runs  to cat"))  # <_sre.SRE_Match object; span=(8, 14), match=' runs '>
# \\ : match \
print(re.search(r"runs\\", "runs\ to me"))     # <_sre.SRE_Match object; span=(0, 5), match='runs\\'>
# . : match anything (except \n)
print(re.search(r"r.n", "r[ns to me"))         # <_sre.SRE_Match object; span=(0, 3), match='r[n'>
# ^ : match line beginning
print(re.search(r"^dog", "dog runs to cat"))   # <_sre.SRE_Match object; span=(0, 3), match='dog'>
# $ : match line ending
print(re.search(r"cat$", "dog runs to cat"))   # <_sre.SRE_Match object; span=(12, 15), match='cat'>
# ? : may or may not occur
print(re.search(r"Mon(day)?", "Monday"))       # <_sre.SRE_Match object; span=(0, 6), match='Monday'>
print(re.search(r"Mon(day)?", "Mon"))          # <_sre.SRE_Match object; span=(0, 3), match='Mon'>
```

如果一个字符串有很多行, 我们想使用 `^` 形式来匹配行开头的字符, 如果用通常的形式是不成功的.
比如下面的 "I" 出现在第二行开头, 但是使用 `r"^I"` 却匹配不到第二行, 这时候, 我们要使用
另外一个参数, 让 `re.search()` 可以对每一行单独处理. 这个参数就是 `flags=re.M`, 或者这样写也行 `flags=re.MULTILINE`.

```python
string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I", string))                 # None
print(re.search(r"^I", string, flags=re.M))     # <_sre.SRE_Match object; span=(18, 19), match='I'>
```







{% include assign-heading.html %}

如果我们想让某个规律被重复使用, 在正则里面也是可以实现的, 而且实现的方式还有很多.
具体可以分为这三种:

* `*` : 重复零次或多次
* `+` : 重复一次或多次
* `{n, m}` : 重复 n 至 m 次
* `{n}` : 重复 n 次

举例如下:

```python
# * : occur 0 or more times
print(re.search(r"ab*", "a"))             # <_sre.SRE_Match object; span=(0, 1), match='a'>
print(re.search(r"ab*", "abbbbb"))        # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

# + : occur 1 or more times
print(re.search(r"ab+", "a"))             # None
print(re.search(r"ab+", "abbbbb"))        # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

# {n, m} : occur n to m times
print(re.search(r"ab{2,10}", "a"))        # None
print(re.search(r"ab{2,10}", "abbbbb"))   # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>
```






{% include assign-heading.html %}

我们甚至可以为找到的内容分组, 使用 `()` 能轻松实现这件事. 通过分组, 我们能轻松定位所找到的内容.
比如在这个 `(\d+)` 组里, 需要找到的是一些数字, 在 `(.+)` 这个组里, 我们会找到 "Date: " 后面的所有内容.
当使用 `match.group()` 时, 他会返回所有组里的内容, 而如果给 `.group(2)` 里加一个数, 它就能定位你需要返回哪个组里的信息.

```python
match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group())                   # 021523, Date: Feb/12/2017
print(match.group(1))                  # 021523
print(match.group(2))                  # Date: Feb/12/2017
```

有时候, 组会很多, 光用数字可能比较难找到自己想要的组, 这时候, 如果有一个名字当做索引, 会是一件很容易的事.
我们字需要在括号的开头写上这样的形式 `?P<名字>` 就给这个组定义了一个名字. 然后就能用这个名字找到这个组的内容.

```python
match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group('id'))                # 021523
print(match.group('date'))              # Date: Feb/12/2017
```







{% include google-in-article-ads.html %}
{% include assign-heading.html %}

前面我们说的都是只找到了最开始匹配上的一项而已, 如果需要找到全部的匹配项, 我们可以使用 `findall`
功能. 然后返回一个列表. 注意下面还有一个新的知识点, `|` 是 or 的意思, 要不是前者要不是后者.

```python
# findall
print(re.findall(r"r[ua]n", "run ran ren"))    # ['run', 'ran']

# | : or
print(re.findall(r"(run|ran)", "run ran ren")) # ['run', 'ran']
```







{% include assign-heading.html %}
我们还能通过正则表达式匹配上一些形式的字符串然后再替代掉这些字符串.
使用这种匹配 `re.sub()`, 将会比 python 自带的 `string.replace()` 要灵活多变.

```python
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))     # dog catches to cat
```





{% include assign-heading.html %}

再来我们 Python 中有个字符串的分割功能, 比如想获取一句话中所有的单词.
比如 `"a is b".split(" ")`, 这样它就会产生一个列表来保存所有单词.
但是在正则中, 这种普通的分割也可以做的淋漓精致.

```python
print(re.split(r"[,;\.]", "a;b,c.d;e"))             # ['a', 'b', 'c', 'd', 'e']
```





{% include assign-heading.html %}

最后, 我们还能使用 compile 过后的正则, 来对这个正则重复使用. 先将正则 compile 进一个变量,
比如 `compiled_re`, 然后直接使用这个 `compiled_re` 来搜索.

```python
compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='ran'>
```




{% include assign-heading.html %}

为了大家方便记忆, 我很久以前在网上找到了一份小抄, 这个小抄的原出处应该是[这里](https://www.cnblogs.com/huxi/archive/2010/07/04/1771073.html){:target="_blank"}.
 小抄很有用, 不记得的时候回头方便看.

{% include tut-image.html image-name="13-10-01.png" %}
