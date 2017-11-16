---
youku_id: XMTg0NDMwNjUxNg
youtube_id: gN0E9SQmySw
bilibili_id: 16378170
description: "今天的情况是这样, 想象不仅有人在做开发版 dev 的更新, 还有人在修改 master 中的一些 bug.
当我们再 merge dev 的时候, 冲突就来了. 因为 git 不知道应该怎么处理 merge 时, 在 master
和 dev 的不同修改.
当创建了一个分支后, 我们同时对两个分支都进行了修改. "
chapter: 4
title: merge 分支冲突
publish-date: 2016-12-01

thumbnail: /static/thumbnail/git/4-02.jpg
post-headings:
  - merge 分支冲突
---

学习资料:
  * [这节例子的初始文件](/static/results/git/initial-files/for_gitTUT_4-2.zip)
  
{% include assign-heading.html %}

今天的情况是这样, 想象不仅有人在做开发版 `dev` 的更新, 还有人在修改 `master` 中的一些 bug.
当我们再 `merge dev` 的时候, 冲突就来了. 因为 git 不知道应该怎么处理 `merge` 时, 在 `master`
和 `dev` 的不同修改.


当创建了一个分支后, 我们同时对两个分支都进行了修改. 

比如在:

* `master` 中的 `1.py` 加上 `# edited in master`.
* `dev` 中的 `1.py` 加上 `# edited in dev`.

在下面可以看出在 `master` 和 `dev` 中不同的 `commit`:

``` shell
# 这是 master 的 log
* 3d7796e change 4 in master # 这一条 commit 和 dev 的不一样
* 47f167e back to change 1 and add comment for 1.py
* 904e1ba change 2
* c6762a1 change 1
* 13be9a7 create 1.py
-----------------------------
# 这是 dev 的 log
* f7d2e3a change 3 in dev   # 这一条 commit 和 master 的不一样
* 47f167e back to change 1 and add comment for 1.py
* 904e1ba change 2
* c6762a1 change 1
* 13be9a7 create 1.py
```

当我们想要 `merge` `dev` 到 `master` 的时候:

```shell
$ git branch
  dev
* master
-------------------------
$ git merge dev

# 输出
Auto-merging 1.py
CONFLICT (content): Merge conflict in 1.py
Automatic merge failed; fix conflicts and then commit the result.
```

git 发现的我们的 `1.py` 在 `master` 和 `dev` 上的版本是不同的, 所以提示 `merge` 有冲突. 具体的冲突, 
git 已经帮我们标记出来, 我们打开 `1.py` 就能看到:

```python
a = 1
# I went back to change 1
<<<<<<< HEAD
# edited in master
=======
# edited in dev
>>>>>>> dev
```

{% include google-in-article-ads.html %}

所以我们只要在 `1.py` 中手动合并一下两者的不同就 OK 啦. 我们将当前 `HEAD` (也就是`master`) 中的描述 和 `dev` 中的描述合并一下.

```python
a = 1
# I went back to change 1

# edited in master and dev
```

然后再 `commit` 现在的文件, 冲突就解决啦.

```shell
$ git commit -am "solve conflict"
```

再来看看 `master` 的 `log`:

```shell
$ git log --oneline --graph

# 输出
*   7810065 solve conflict
|\  
| * f7d2e3a change 3 in dev
* | 3d7796e change 4 in master
|/  
* 47f167e back to change 1 and add comment for 1.py
* 904e1ba change 2
* c6762a1 change 1
* 13be9a7 create 1.py
```

回到这张图, 
他也诠释了两个分支都有更改的时候的样子, 在这种情况下 `merge`, 我们就要使用上述的流程.

{% include tut-image.html image-name="4-2-1.png" %}

