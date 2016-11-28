---
youku_id: 
youtube_id: 
description: 
chapter: 1
title: 记录修改
comments: true
---
* 学习资料:
  * [上节内容的文件]()
  
本节内容分为:
  
* [log](#log)
* [commit 的返回信息](#commit-return)


在 git 中, 每一次提交(commit)的修改, 都会被单独的保存起来. 
也可以说 git 的中的所有文件都是一次次修改累积起来的. 文件好比楼房, 每个 commit 记录
了盖楼需添加或者拿走的材料. 整个施工过程也被记录了下来.


<h4 class="tut-h4-pad" id="log">log</h4>

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

<h4 class="tut-h4-pad" id="commit-return">commit 的返回信息</h4>

如果删除一部分代码, 也会被记录上, 比如把 `a = 1` 改成 `a = 2`, 再添加一个 `b = 1`.

```python
a = 2
b = 1
```

重复上面的 `add` 和 `commit` 步骤, 我们看到 git 同时还记录了每次更改有多少添加和减少:

```shell
$ git add 1.py
$ git commit -m "change 2"

# 输出
[master eb08ac5] change 2
 1 file changed, 2 insertions(+), 1 deletion(-) # 显示有多少添加和减少
```

