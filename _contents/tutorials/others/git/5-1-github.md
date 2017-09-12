---
youku_id: XMTg0NDY5NDMzMg
youtube_id: oWUvXRheaeY
description: github 是一个大家都积极贡献的地方, 你可以和各种人合作创作. 也是开源的天堂~ 只要你愿意, 任何人都能下载, 或修改你的杰作.
chapter: 5
title: Github
comments: true
publish-date: 2016-12-02
thumbnail: /static/thumbnail/git/5-01.jpg
post-headings:
  - 建立 github 版本库
  - 连接本地版本库
  - 推送修改
---
{% assign post-heading-count = -1 %}
学习资料:
  * [这节例子的初始文件](/static/results/git/initial-files/for_gitTUT_5-1.zip)
  


github 是一个大家都积极贡献的地方, 你可以和各种人合作创作. 也是开源的天堂~
只要你愿意, 任何人都能下载, 或修改你的杰作.

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

在 [github](https://github.com/) 注册一个 github 账户, 这个不用我多说, 大家都知道注册.

然后添加你的一个 online 版本库 repository:
 
<img class="course-image" src="/static/results/git/5-1-1.png">

添加好了以后, 会出现下面的介绍, 你可以选择红框里的代码链接上你的本地版本库.

<img class="course-image" src="/static/results/git/5-1-2.png">

{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

使用这节内容的初始例子文件, 然后将本地的版本库推送到网上:

```shell
$ git remote add origin https://github.com/MorvanZhou/git-demo.git
$ git push -u origin master     # 推送本地 master 去 origin
$ git push -u origin dev        # 推送本地 dev  去 origin
```

现在网上就已经有了你推上去的版本库了.

<img class="course-image" src="/static/results/git/5-1-3.png">

你甚至能在这里观看之前有哪些 `commit` 和 `commit` 具体做了什么:

<img class="course-image" src="/static/results/git/5-1-4.png">


{% assign post-heading-count = post-heading-count | plus: 1 %}
<h4 class="tut-h4-pad" id="{{ page.post-headings[post-heading-count] }}">{{ page.post-headings[post-heading-count] }}</h4>

如果在本地再进行修改, 比如在 `1.py` 文件中加上 `# happy github`,
然后 `commit` 并推上去:

```shell
$ git commit -am "change 5"
$ git push -u origin master
```

github 中就会查到这个:

<img class="course-image" src="/static/results/git/5-1-5.png">

这样就有更多的人可以看到你的杰出作品啦~