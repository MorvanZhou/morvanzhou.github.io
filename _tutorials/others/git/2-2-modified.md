---
youku_id: XMTg0MjI5NTYwOA
youtube_id: qSql8KDTEuY
bilibili_id: 16378087
description: "在 git 中, 每一次提交(commit)的修改, 都会被单独的保存起来.
也可以说 git 的中的所有文件都是一次次修改累积起来的. 文件好比楼房, 每个 commit 记录
了盖楼需添加或者拿走的材料. 整个施工过程也被记录了下来."
chapter: 2
title: 记录修改 (log & diff)
publish-date: 2016-11-30

thumbnail: /static/thumbnail/git/2-02.jpg
post-headings:
  - 修改记录 log
  - 查看 unstaged
  - 查看 staged (--cached)
  - 查看 staged & unstaged (HEAD)
---

学习资料:
  * [这节例子的初始文件](/static/results/git/initial-files/for_gitTUT_2-2.zip)
  * [log 的详细参数](https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History){:target="_blank"}
  * [diff 的详细参数](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#Viewing-Your-Staged-and-Unstaged-Changes){:target="_blank"}
  
本节内容分为:



在 git 中, 每一次提交(commit)的修改, 都会被单独的保存起来. 
也可以说 git 的中的所有文件都是一次次修改累积起来的. 文件好比楼房, 每个 commit 记录
了盖楼需添加或者拿走的材料. 整个施工过程也被记录了下来.


{% include assign-heading.html %}

之前我们以`Morvan Zhou` 的名义对版本库进行了一次修改, 添加了一个 `1.py` 的文件.
接下来我们就来查看版本库的些施工的过程. 可以看到在 `Author` 那已经有我的名字和 email 信息了.

```shell
$ git log

# 输出
commit 13be9a7bf70c040544c6242a494206f240aac03c
Author: Morvan Zhou <mz@email.com>
Date:   Tue Nov 29 00:06:47 2016 +1100

    create 1.py # 这是我们上节课记录的修改信息
```

如果我们对`1.py`文件进行一次修改, 添加这行代码:

```python
a = 1
```

然后我们就能在 `status` 中看到修改还没被提交的信息了.

```shell
$ git status

# 输出
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   1.py    # 这里显示有一个修改还没被提交

no changes added to commit (use "git add" and/or "git commit -a")
```

所以我们先把这次修改添加 (add) 到可被提交 (commit) 的状态, 
然后再提交 (commit) 这次的修改:

```shell
$ git add 1.py
$ git commit -m "change 1"

# 输出
[master fb51216] change 1
 1 file changed, 1 insertion(+) # 提示文件有一处添加
```


再次查看 `log`, 现在我们就能看到 `create 1.py` 和 `change 1` 这两条修改信息了.
而且做出这两条 `commit` 的 ID, 修改的 `Author`, 修改 `Date` 也被显示在上面.

```shell
$ git log

# 输出
commit fb51216b081e00db3996e14edf8ff080fab1980a
Author: Morvan Zhou <mz@email.com>
Date:   Tue Nov 29 00:24:50 2016 +1100

    change 1

commit 13be9a7bf70c040544c6242a494206f240aac03c
Author: Morvan Zhou <mz@email.com>
Date:   Tue Nov 29 00:06:47 2016 +1100

    create 1.py
```

如果删除一部分代码, 也会被记录上, 比如把 `a = 1` 改成 `a = 2`, 再添加一个 `b = 1`.

```python
a = 2
b = 1
```

{% include google-in-article-ads.html %}

{% include assign-heading.html %}

如果想要查看这次还没 `add` (unstaged) 的修改部分 和上个已经 `commit` 的文件有何不同, 
我们将使用 `$ git diff`:

```shell
$ git diff

# 输出
diff --git a/1.py b/1.py
index 1337a53..ff7c36c 100644
--- a/1.py
+++ b/1.py
@@ -1 +1,2 @@
-a = 1  # 删除了 a = 1
+a = 2  # 添加了 a = 2
+b = 1  # 添加了 b = 1
```

{% include assign-heading.html %}

如果你已经 `add` 了这次修改, 文件变成了 "可提交状态" (staged), 我们可以在 `diff` 中添加参数 
`--cached` 来查看修改:

```shell
$ git add .   # add 全部修改文件
$ git diff --cached

# 输出
diff --git a/1.py b/1.py
index 1337a53..ff7c36c 100644
--- a/1.py
+++ b/1.py
@@ -1 +1,2 @@
-a = 1
+a = 2
+b = 1
```

{% include assign-heading.html %}

还有种方法让我们可以查看 `add` 过 (staged) 和 没 `add` (unstaged) 的修改, 
比如我们再修改一下 `1.py` 但不 `add`:

```python
a = 2
b = 1
c = b
```

目前 `a = 2` 和 `b = 1` 已被 `add`,  `c = b` 是新的修改, 还没被 `add`.

```shell
# 对比三种不同 diff 形式
$ git diff HEAD     # staged & unstaged

@@ -1 +1,3 @@
-a = 1  # 已 staged
+a = 2  # 已 staged
+b = 1  # 已 staged
+c = b  # 还没 add 去 stage (unstaged)
-----------------------
$ git diff          # unstaged

@@ -1,2 +1,3 @@
 a = 2  # 注: 前面没有 +
 b = 1  # 注: 前面没有 +
+c = b  # 还没 add 去 stage (unstaged)
-----------------------
$ git diff --cached # staged

@@ -1 +1,2 @@
-a = 1  # 已 staged
+a = 2  # 已 staged
+b = 1  # 已 staged
```

为了下节内容, 我们保持这次修改, 全部 `add` 变成 `staged` 状态, 并 `commit`.

```shell
$ git add .
$ git commit -m "change 2"

# 输出
[master 6cc6579] change 2
 1 file changed, 3 insertions(+), 1 deletion(-)
```