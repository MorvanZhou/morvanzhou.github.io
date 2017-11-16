---
youku_id: XMTg0Mzg1MjE4OA
youtube_id: QEuqlpMOL9E
bilibili_id: 16378128
description: "之前我们使用 reset 的时候是针对整个版本库, 回到版本库的某个过去.
不过如果我们只想回到某个文件的过去, 又该怎么办呢?"
chapter: 3
title: 回到从前 (checkout 针对单个文件)
publish-date: 2016-12-01

thumbnail: /static/thumbnail/git/3-02.jpg
post-headings:
  - 改写文件 checkout
---

学习资料:
  * [这节例子的初始文件](/static/results/git/initial-files/for_gitTUT_3-2.zip)


之前我们使用 `reset` 的时候是针对整个版本库, 回到版本库的某个过去. 
不过如果我们只想回到某个文件的过去, 又该怎么办呢?

{% include assign-heading.html %}

其实 `checkout` 最主要的用途并不是让单个文件回到过去, 我们之后会继续讲 `checkout`
在分支 `branch` 中的应用, 这一节主要讲 `checkout` 让文件回到过去.

我们现在的版本库中有两个文件:

```
- gitTUT
    - 1.py
    - 2.py
```

我们仅仅要对 `1.py` 进行回到过去操作, 回到 `c6762a1 change 1` 这一个 `commit`.
使用 `checkout` + id `c6762a1` + `--` + 文件目录 `1.py`, 我们就能将 `1.py`
的指针 `HEAD` 放在这个时刻 `c6762a1`:

```shell
$ git log --oneline
# 输出
904e1ba change 2
c6762a1 change 1
13be9a7 create 1.py
---------------------
$ git checkout c6762a1 -- 1.py
```

这时 `1.py` 文件的内容就变成了:

```python
a = 1
```

我们在 `1.py` 加上一行内容 `# I went back to change 1`
然后 `add` 并 `commit` `1.py`:

```shell
$ git add 1.py
$ git commit -m "back to change 1 and add comment for 1.py"
$ git log --oneline

# 输出
47f167e back to change 1 and add comment for 1.py
904e1ba change 2
c6762a1 change 1
13be9a7 create 1.py
```

可以看出, 不像 `reset` 时那样, 我们的 `change 2` 并没有消失, 但是 `1.py` 却已经回去了过去, 并改写了未来.
