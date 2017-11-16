---
youku_id: XMTg0NDYzNjUzNg
youtube_id: mqjAMciBrdU
bilibili_id: 16378209
description: "想想有天在开开心心地改进代码, 突然接到老板的一个电话说要改之前的一个程序.
怎么办? 虽然还需要很久时间才能改进完自己的代码,
可我有强迫症, 又不想把要改的程序和自己改进代码的部分一起 commit 了.
这时 stash 就是我的救星了. 用 stash 能先将我的那改进的部分放在一边分隔开来.
再另外单独处理老板的任务."
chapter: 4
title: 临时修改 (stash)
publish-date: 2016-12-01

thumbnail: /static/thumbnail/git/4-04.jpg
post-headings:
  - 暂存修改
  - 做其它任务
  - 恢复暂存
---

学习资料:
  * [这节例子的初始文件](/static/results/git/initial-files/for_gitTUT_4-4.zip)
  



想想有天在开开心心地改进代码, 突然接到老板的一个电话说要改之前的一个程序.
怎么办? 虽然还需要很久时间才能改进完自己的代码, 
可我有强迫症, 又不想把要改的程序和自己改进代码的部分一起 `commit` 了.

这时 `stash` 就是我的救星了. 用 `stash` 能先将我的那改进的部分放在一边分隔开来. 
再另外单独处理老板的任务.

{% include assign-heading.html %}

假设我们现在在 `dev` 分支上快乐地改代码:

```shell
$ git checkout dev
```

在 `dev` 中的 `1.py` 中加上一行 `# feel happy`, 然后老板的电话来了, 可是我还没有改进完这些代码.
所以我就用 `stash` 将这些改变暂时放一边.

```shell
$ git status -s
# 输出
 M 1.py
------------------ 
$ git stash
# 输出
Saved working directory and index state WIP on dev: f7d2e3a change 3 in dev
HEAD is now at f7d2e3a change 3 in dev
-------------------
$ git status
# 输出
On branch dev
nothing to commit, working directory clean  # 干净得很
```

{% include assign-heading.html %}

然后我们建立另一个 `branch` 用来完成老板的任务:

```shell
$ git checkout -b boss

# 输出
Switched to a new branch 'boss' # 创建并切换到 boss
```

然后苦逼地完成着老板的任务, 比如添加 `# lovely boss` 去 `1.py`. 然后 `commit`, 完成老板的任务.

```shell
$ git commit -am "job from boss"
$ git checkout master
$ git merge --no-ff -m "merged boss job" boss
```

`merge` 如果有冲突的话, 可以像[上次那样]({% link _tutorials/others/git/4-2-merge-conflict.md %})
解决.

```python
a = 1
# I went back to change 1
<<<<<<< HEAD

# edited in master and dev

=======
# edited in dev

# lovely boss
>>>>>>> boss
```

通过以下步骤来完成老板的任务, 并观看一下 `master` 的 log:

```shell
$ git commit -am "solve conflict"
$ git log --oneline --graph
*   1536bea solve conflict
|\  
| * 27ba884 job from boss
* | 2d1961f change 4 in master
|/  
* f7d2e3a change 3 in dev
* 47f167e back to change 1 and add comment for 1.py
* 904e1ba change 2
* c6762a1 change 1
* 13be9a7 create 1.py
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

轻松了, 现在可以继续开心的在 `dev` 上刷代码了.

```shell
$ git checkout dev
$ git stash list    # 查看在 stash 中的缓存

# 输出
stash@{0}: WIP on dev: f7d2e3a change 3 in dev
```

上面说明在 `dev` 中, 我们的确有 `stash` 的工作. 现在可以通过 `pop` 来提取这个并继续工作了.

```shell
$ git stash pop

# 输出
On branch dev
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   1.py

no changes added to commit (use "git add" and/or "git commit -a")
Dropped refs/stash@{0} (23332b7edc105a579b09b127336240a45756a91c)
----------------------
$ git status -s
# 输出
 M 1.py     # 和最开始一样了
```
