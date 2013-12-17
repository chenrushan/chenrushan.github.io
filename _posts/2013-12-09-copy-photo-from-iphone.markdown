---
layout: post
title: Copy Photo from Iphone
categories: arch
tags: arch, linux, gphoto2, iphone, photo
---

这里介绍如何利用 gphoto2 这个命令从 iphone 中拷几张自己想要的照片，大体使用过程如下：

1. 这个工具貌似不能预览 iphone 里的照片，看不到预览也就不知道自己想要的照片的文件名是什么，但又不想把所有的照片都拷进来，太大了，折衷的办法就是把 thumbnail 拷进来，由于 thumbnail 很小，所以拷它还是可以接受的。拷 thumbnail 的命令如下：

        gphoto2 --port=usb -R -T

2. 拷了所有 thumbnail 后，找到你要的照片，记下文件名，然后运行下面命令：

        gphoto2 --port=usb -R -L

   根据这个命令的输出找到你要的文件对应的 id。

3. 假设你要的照片 id 是 123 到 126 以及 200 到 205，那运行下面命令拷入这些照片：

        gphoto2 --port=usb -R -p 123-126 -p 200-205

最后，如果你想拷所有照片，运行下面命令：

    gphoto2 --port=usb -R -P

