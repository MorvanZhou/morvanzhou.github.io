---
youku_id: XMzExNzIzNzc2NA
youtube_id: 9BtAjh5s1Fw
bilibili_id: 15981253
chapter: 2
title: Linux 基本指令 touch, cp 和 mv
publish-date: 2017-10-12
thumbnail: /static/thumbnail/linux-basic/2-02.jpg
post-headings:
  - touch 新建
  - cp 复制
  - mv 剪切
description: "这次, 我们想要了解的是在 linux 中, 怎么样创建新文件, 复制, 粘贴, 剪切."
---


这次, 我们想要了解的是在 linux 中, 怎么样创建新文件, 复制, 粘贴, 剪切.



{% include assign-heading.html %}

`touch` 的使用很简单, 我们先去往 Documents 的文件夹, 里面已经有了 `folder1` 和 `file1`,
如果我们想新建一个 `file2` 使用下面的语句就好. 一个空文件就建立好了.

{% include tut-image.html image-name="02-01-03.png" %}


```shell
$ touch file2
```


如果你想同时建立多个文件, 输入多个文件的名字, 以空格分开.

```shell
$ touch file3 file4 file5
```







{% include google-in-article-ads.html %}

{% include assign-heading.html %}

`cp` (copy) 是复制文件或者文件夹的指令, 常用的方式是复制 "老文件" 到 "新文件".

```shell
$ cp 老文件 新文件
```

1 我们用上面建立好的 `file1` 来举例, 将 `file1` 复制成 `file1copy`

```shell
$ cp file1 file1copy
```

{% include tut-image.html image-name="02-02-01.png" %}

2 `-i` (interactive) **注意: 如果 file1copy 已经存在, 它将会直接覆盖已存在的 file1copy**, 如果要避免直接覆盖, 我们在 cp 后面加一个选项.

```shell
$ cp -i file1 file1copy
cp: overwrite 'file1copy'?
```

在这句问句后面打上 "Yes", "Y", 或者任何大小写形式的 "y" 和 "yes", 它将进行覆盖操作. 直接回车或者打其他字母, 就会放弃复制这项操作.

3 复制去文件夹

```shell
$ cp file1 folder1/
```

4 复制文件夹, 需要加上 `-R` (recursive)

```shell
$ cp -R folder1/ folder2/
```

5 复制多个文件. 复制名字部分相同的多个文件, `*` 是说"你就找文件前面是 file 的文件, 后面是什么名字无所谓"

```shell
$ cp file* folder2/
```

或者你可以单独选定几个文件, cp 会默认最后一个选项是要复制去的文件夹. 比如下面把 `file1copy` 和 `file2` 复制去 `folder1/`

```shell
$ cp file1copy file2 folder1/
```





{% include assign-heading.html %}

知道了 `cp`, `mv`就好理解多了, 基本是一样的.

1 移动去另一个文件夹

```shell
$ mv file1 folder1/
```

2 重命名文件

因为移动文件到原始的地点, 但是以不同的文件名. 这种做法不就是在重命名嘛!

```shell
$ mv  file1 file1rename
```

最后还是想要提一句, 如果想要查看使用说明, 直接在指令后面打上 `--help` 就能查看.