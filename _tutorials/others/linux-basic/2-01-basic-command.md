---
youku_id: XMzExNzE1MDgyNA
youtube_id: 9sIbn9xVdlk
bilibili_id: 15981060
chapter: 2
title: Linux 基本指令 ls 和 cd
publish-date: 2017-10-11
thumbnail: /static/thumbnail/linux-basic/2-01.jpg
post-headings:
  - cd 指令
  - ls 指令
description: "Linux 的深度玩家, 基本上都是用 Terminal 和指令 (command) 来超控电脑的.
有些时候甚至你的电脑没有屏幕, 也只能用指令来超控. 比如服务器, 树莓派(raspberry pi).
如果你只是为了想 '轻度使用' Linux, 前面的教程就已经够了, 不过如果你想要 '重度使用', 哈哈, 就接着看吧. "
---

Linux 的深度玩家, 基本上都是用 Terminal 和指令 (command) 来超控电脑的.
有些时候甚至你的电脑没有屏幕, 也只能用指令来超控. 比如服务器, 树莓派(raspberry pi).

{% include tut-image.html image-name="02-01-01.jpg" %}


如果你只是为了想 "轻度使用" Linux, 前面的教程就已经够了, 不过如果你想要 "重度使用", 哈哈, 就接着看吧.

其实计算机指令大部分都是和文件打交道, 比如把文件 A 移动到 文件夹B, 新建一个文件 C, 改写文件 A 的内容等.
你想黑客黑你电脑, 多半也就是找你电脑里重要的文件, 然后 copy 去他的电脑. 或者整个互联网都是一个文件传输器, 将你的网页以文件的形式发送到你的电脑.
所以学 Linux, 学会怎么样摆弄文件最重要. 接下来几节内容, 我们就介绍一些基础的摆弄文件方法.



{% include assign-heading.html %}

第一个要知道的指令就是怎么样去到你想去的地方. `cd` (Change Directory) 就是干这个的. 找到 Linux 的 terminal 窗口,
然后他默认跳出来是在你的用户目录 (Home). Terminal 中的 `~ $` 就是说你输入指令将在 `~` 这个目录下执行.
而 `~` 这个符号代表的是你的 Home 目录. 如果在文件管理器中可视化出来, 就是下面图中那样.

{% include tut-image.html image-name="02-01-02.png" %}

使用 `cd` 指令, 我们能在 Terminal 中轻松切换到不同的文件夹. 想从 Home 去 `Documents` 这个文件夹?
输入下面的命令就可以了.

```shell
~$ cd Documents/
```

接着你会看到它在下一行跳出了这个东西, 在 `$` 前面的 `~/Documents` 就说明你现在已经在 Documents 这个文件夹里了.
你现在要执行的命令将会在这个目录下生效.

```shell
~/Documents$
```

接着我们来列举另外一些常用的 `cd` 命令.

1 返回上一级目录

```shell
~/Documents$ cd ..
~$
```

2 去往子文件夹

```shell
~$ cd Documents/folder1/
~/Documents/folder1$
```

3 返回你刚刚所在的目录

```shell
~/Documents/folder1$ cd -
/home/morvan
~$
```

4 向上返回两次

```shell
~/Documents/folder1$ cd ../../
~$
```

5 去往 Home

```shell
~/Documents/folder1$ cd ~
~$
```

6 去往电脑任何地方, 你需要的是一个绝对路径

```shell
~$ cd /home/morvan/Documents/folder1
~/Documents/folder1$
```



{% include google-in-article-ads.html %}

{% include assign-heading.html %}

我们现在能在电脑的文件中移动来移动去了, 这还没什么意思, 接着我们就来移动去一个地方, 再看看那个地方有些什么.
(有种黑客在偷窥人家文件的感觉, 哈哈).

我在 Documents 目录里放了个文件夹(`folder1`)和文件(`file1`). 我们将目录导去 Documents,
然后使用 `ls` (list 的简写) 看看这里面的东西.

{% include tut-image.html image-name="02-01-03.png" %}


```shell
~/Documents$ ls
file1  folder1
```

我们再来看看 `ls` 的其他使用方式.

1 输出详细信息 `-l` (long 的简写). 这个指令会打印出文件的权限 (`-rw-rw-r--` 之后我们在细说这个), 用户名, 文件大小, 修改日期, 文件名

```shell
~/Documents$ ls -l
total 4
-rw-rw-r-- 1 morvan morvan    0 Oct 12 07:38 file1
drwxrwxr-x 2 morvan morvan 4096 Oct 12 07:26 folder1
```

2 `-a` (all 的简写) 显示所有文件 . 这里还会显示隐藏的文件 (以 `.` 开头的)

```shell
$ ls -a
.  ..  file1  folder1  .hidden_file
```

3 `-lh` (human), 直接 `-l` 不方便人看, 这个指令是为了方便给人观看的. 注意这里的文件大小使用了 K, MB, GB 之类概括

```shell
$ ls -lh
total 4.0K
-rw-rw-r-- 1 morvan morvan    0 Oct 12 07:38 file1
drwxrwxr-x 2 morvan morvan 4.0K Oct 12 07:26 folder1
```

4 还有很多其他的功能, 我们可以通过 `--help` 来查看

```shell
$ ls --help
```
