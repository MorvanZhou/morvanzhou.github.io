---
youku_id: XMTg0NDU3ODYwMA
youtube_id: fLvr4BRoJ8I
bilibili_id: 16378187
description: "和上节内容一样, 不过我们今天来玩一个更高级的合并方式 rebase.
同样是合并 rebase 的做法和 merge 不一样.
假设共享的 branch 是 branch B, 而我在 branch A 上工作, 有一天我发现branch B已经有一些小更新,
我也想试试我的程序和这些小更新兼不兼容, 我也我想合并, 这时就可以用 rebase 来补充我的分支branch B的内容.
补充完以后, 和后面那张图的 merge 不同, 我还是继续在 C3 上工作, 不过此时的 C3 的本质却不一样了,
因为吸收了那些小更新. 所以我们用 C3' 来代替."
chapter: 4
title: rebase 分支冲突

publish-date: 2016-12-01
thumbnail: /static/thumbnail/git/4-03.jpg
post-headings:
  - 什么是 rebase
  - 使用 rebase
---

学习资料:
  * [这节例子的初始文件](/static/results/git/initial-files/for_gitTUT_4-3.zip)
  



{% include assign-heading.html %}

和上节内容一样, 不过我们今天来玩一个更高级的合并方式 `rebase`.
同样是合并 `rebase` 的做法和 `merge` 不一样. 

假设共享的 branch 是 `branch B`, 而我在 `branch A` 上工作, 有一天我发现`branch B`已经有一些小更新,
我也想试试我的程序和这些小更新兼不兼容, 我也我想合并, 这时就可以用 `rebase` 来补充我的分支`branch B`的内容.
补充完以后, 和后面那张图的 `merge` 不同, 我还是继续在 `C3` 上工作, 不过此时的 `C3` 的本质却不一样了, 
因为吸收了那些小更新. 所以我们用 `C3'` 来代替.

{% include tut-image.html image-name="4-3-1.png" %}

{% include tut-image.html image-name="4-3-2.png" %}

{% include tut-image.html image-name="4-3-3.png" %}

{% include tut-image.html image-name="4-3-4.png" %}

可以看出 `rebase` 改变了 `C3` 的属性, `C3` 已经不是从 `C1` 衍生而来的了. 
这一点和 `merge` 不一样. `merge` 在合并的时候创建了一个新的 `C5` `commit`. 
这一点不同, 使得在共享分支中使用 `rebase` 变得危险.
如果是共享分支的历史被改写. 别人之前共享内容的 `commit` 就被你的 `rebase` 修改掉了. 

{% include tut-image.html image-name="4-2-1.png" %}

所以需要强调的是 **!!! 只能在你自己的分支中使用 rebase, 和别人共享的部分是不能用 !!!**. 
如果你不小心弄错了. 没事, 我们还能用在 [reset 这一节]({% link _tutorials/others/git/3-1-reset.md %})
提到的 `reflog` 恢复原来的样子.
为了验证在共享分支上使用 `rebase` 的危险性, 我们在下面的例子中也验证一下.


{% include google-in-article-ads.html %}

{% include assign-heading.html %}

初始的版本库还是和上回一样, 在 `master` 和 `dev` 分支中都有自己的独立修改.

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

当我们想要用 `rebase` 合并 `dev` 到 `master` 的时候:

```shell
$ git branch

# 输出
  dev
* master
-------------------------
$ git rebase dev 

# 输出
First, rewinding head to replay your work on top of it...
Applying: change 3 in dev
Using index info to reconstruct a base tree...
M	1.py
Falling back to patching base and 3-way merge...
Auto-merging 1.py
CONFLICT (content): Merge conflict in 1.py
error: Failed to merge in the changes.
Patch failed at 0001 change 3 in dev
The copy of the patch that failed is found in: .git/rebase-apply/patch

When you have resolved this problem, run "git rebase --continue".
If you prefer to skip this patch, run "git rebase --skip" instead.
To check out the original branch and stop rebasing, run "git rebase --abort".
```

git 发现的我们的 `1.py` 在 `master` 和 `dev` 上的版本是不同的, 所以提示 `merge` 有冲突. 具体的冲突, 
git 已经帮我们标记出来, 我们打开 `1.py` 就能看到:

```python
a = 1
# I went back to change 1
<<<<<<< f7d2e3a047be4624e83c1265a0946e2e8790f79c
# edited in dev
=======
# edited in master
>>>>>>> change 4 in master
```

这时 `HEAD` 并没有指向 `master` 或者 `dev`, 而是停在了 `rebase` 模式上:

```shell
$ git branch
* (no branch, rebasing master) # HEAD 在这
  dev
  master
```

所以我们打开 `1.py`, 手动合并一下两者的不同.

```python
a = 1
# I went back to change 1

# edited in master and dev
```

然后执行 `git add` 和 `git rebase --continue` 就完成了 `rebase` 的操作了.

```shell
$ git add 1.py
$ git rebase --continue
```

再来看看 `master` 的 `log`:

```shell
$ git log --oneline --graph

# 输出
* c844cb1 change 4 in master    # 这条 commit 原本的id=3d7796e, 所以 master 的历史被修改
* f7d2e3a change 3 in dev       # rebase 过来的 dev commit
* 47f167e back to change 1 and add comment for 1.py
* 904e1ba change 2
* c6762a1 change 1
* 13be9a7 create 1.py
```

**!! 注意 !!**
这个例子也说明了使用 `rebase` 要万分小心, 千万不要在共享的 branch 中 `rebase`, 不然就像上面那样, 
现在 `master` 的历史已经被 `rebase` 改变了. `master` 当中别人提交的 `change 4` 就被你无情地修改掉了, 
所以千万不要在共享分支中使用 `rebase`.

