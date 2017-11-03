---
youku_id: XMzEyMDk5MDEwMA
youtube_id: L5YgJbgufPc
bilibili_id: 15981402
chapter: 2
title: Linux 基本指令 mkdir, rmdir 和 rm
publish-date: 2017-10-12
thumbnail: /static/thumbnail/linux-basic/2-03.jpg
post-headings:
  - mkdir 建立文件夹
  - rmdir 移除文件夹
  - rm 移除文件
description: "这次, 我们想要了解的是在 linux 中, 怎么样创建新文件夹, 移除文件夹, 移除文件."
---


这次, 我们想要了解的是在 linux 中, 怎么样创建新文件夹, 移除文件夹, 移除文件.



{% include assign-heading.html %}


`mkdir` (make directory) 就是创建一个文件夹的意思, 使用起来很简单.

```shell
$ mkdir folder2
```

{% include tut-image.html image-name="02-03-01.png" %}

如果你想在这个目录给 `folder2` 里面再建一个文件夹也是 Ok.

```shell
$ mkdir folder2/f2
```

这样, `f2` 这个文件夹就被新建在了 `folder2` 里面.








{% include assign-heading.html %}

`rmdir` (remove directory) 也就是字面意思, 移除文件夹. 不过这有一个前提条件.
这些要移除的文件夹必须是空的. 不然会失败. 所以如果想刚刚建立的那个 `folder2` 就不能被移除, 因为里面有个 `f2` 文件夹.

要移除个空文件夹, 比如我在新建一个 `folder3`, 然后移除

```shell
$ rmdir folder3
```






{% include google-in-article-ads.html %}

{% include assign-heading.html %}

那文件夹里面有文件的这种情况, 或者是移除单个文件的情况, 我们都能用 `rm` 来实现.
**注意: 执行了 rm 以后是不能进行返回操作的, 请确保别执行像这样的操作 `rm /`, 这会清空你的电脑.**

1 移除单个文件

```shell
$ rm file1
```

2 `-i` 或 `-I` 有提示地移除文件 (为了避免误删)

* `-i` 会每个要移除的文件都进行提示
* `-I` 超过3个文件才进行提示

```shell
$ rm -i f1 f2 f3 f4
rm: remove regular empty file 'f1'?
rm: remove regular empty file 'f2'? y
rm: remove regular empty file 'f3'?
rm: remove regular empty file 'f4'? y
```

```shell
$ rm -I f1 f2 f3 f4
rm: remove 4 arguments? y
```

3 `-r` 或 `-R` (recursively) 用来删文件夹

和 `rmdir` 不同, `rm -r` 可以在文件夹中有文件的情况下删除这个文件夹. 比如我的 `folder1` 里有 `file1` 和 `file2` 两个文件.

```shell
$ rm -r folder1
```

