---
layout: post
title: Install Arch Linux on MacBook Air
categories: arch
---

我的 MacBook Air 是 mid2012 的，这时的 MBA 已经是基于 UEFI，而非 BIOS 的了。我的目标是安装 MacOS 和 arch linux dual boot 的系统。

### 1. MacOS 中的操作

1. Resize MacOS partition using Disk utility.

   要留多一点，disk utility 显示我有 50G free space，其实 mac 在后面又偷偷用了一些，在装 Linux 时我发现少了近 3G

2. Make a usb installer for arch linux.

        diskutil unmountDisk /dev/diskN
        sudo dd if=/path/to/linux.iso of=/dev/diskN bs=1m

  /dev/diskN 是 usb。

3. Install rEFIt on mac.

   需要重启 mac 两次才能生效，真是奇葩阿

4. 插上你的 usb，你会在重启之后看到 rEFIt 的菜单中多出很多 usb 里包含的启动项

### 2. Install Arch Linux

1. boot from USB

   从 rEFIt 启动项中选 boot from EFI/boot/bootx64.efi，不要选 boot from EFI/archiso/vmlinuz.efi，选这个会有 kernel panic，启动不了。

2. Disk partition

   之前看到说 linux 的 udev 是异步的，今天就遇到这个异步带来的困扰，我准备 format mac 的磁盘时，发现我 mac 的磁盘居然是 /dev/sdb，(sda 是我的 u 盘)。开始还以为怎么了，后来想到可能因为 udev 是异步的原因，果然重启之后，磁盘又变成 /dev/sda 了。

        gdisk /dev/sda

  1. 不要 swap，大不了以后用 swapfile，对于有 4G 内存的机子，swap 不是太需要了
  2. 只创建了两个用于 / 和 /home 的分区，/boot/ 我直接 mount 在 EFI partition
  3. 在 mac os 的 recovery HD 后面留出了 128M 的 free space，据说不这么做 osx 可能会不爽

   另外，比较诡异的是，我 gdisk 完事，都已经w了，可是退出 gdisk 后，在 /dev/ 目录下没有 sda4 和 sda5，可是不管用 gdisk 还是 cgdisk 都显示有，然后我就重启了，重启完好使了。
   
3. make filesystem

        mkfs.ext4 /dev/sda4
        mkfs.ext4 /dev/sda5

   关于每个 partition 的情况你随时都可以 `lsblk /dev/sda` 看看

4. mount partitions

        mount /dev/sda4 /mnt
        mkdir /mnt/{boot，home}
        mount /dev/sda1 /mnt/boot
        mount /dev/sda5 /mnt/home

   我直接将 /boot mount 在已有的 EFI partition 上。

5. setup wireless

  1. 确认无线硬件已被识别，运行

            iw dev

  2. 得到 AP(access point) 列表

            iw dev wlp2s0 scan | less

     注意如果你是在一台同时有有线和无线的机子上，默认是开启有线的接口，这种情况下，你要先运行 `iw dev set wlp2s0 up` 来开启无线接口，然后才能运行 scan，否则会提示 network is down。

     可以参考 [arch wiki](https://wiki.archlinux.org/index.php/Wireless_Setup) 确定每个字段都是什么意思。

  3. 生成无线配置文件

     从显示的信息看无线是 WPA/WPA2 加密的。

     我家的网络提示的 Authentication suites 是 PSK，而我公司的提示 802.1x，也就是说我公司的网络需要输入用户名密码才行。

     对于 PSK 的网络直接用 wpa\_passphrase 生成 conf 即可，如下

            wpa_passphrase [SSID] [PASSWORD] > /etc/wpa_supplicant/[SSID].conf

  4. 对于 802.1x 的网络，你还得知道他的 key management 方法和 encapsulation 方法，我公司用的常用的 WPA-EAP 做 key management， PEAP 做 encapsulation，所以 conf 如下。

            network={
                    ssid="alibaba-inc"
                    key_mgmt=WPA-EAP
                    eap=PEAP
                    identity="..."
                    password="..."
            }

  5. 连接无线网

            wpa_supplicant -B -i wlp2s0 -c /etc/wpa_supplicant/[SSID].conf

  6. 确认 wireless is connected，运行

            iw dev wlp2s0 link 

  7. 获取 ip 地址，运行

            dhcpcd wlp2s0

  8. 确认一切 ok

            ping sina.com


6. 选取最快的 repository

        vi /etc/pacman.d/mirrorlist 

7. 安装基本包

        pacstrap /mnt base base-devel

8. 各种配置

        genfstab -p /mnt >> /mnt/etc/fstab
        arch-chroot /mnt /bin/bash
        echo juscodit > /etc/hostname
        ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
        useradd -m -g users -s /bin/bash juscodit
        passwd
        passwd juscodit
        vi /etc/locale.gen
        locale-gen
        pacman -S sudo
        visudo # add "juscodit ALL=(ALL) NOPASSWD: ALL
        pacman -S wpa_supplicant iw

9. 安装 grub

   我曾尝试用 efi\_stub 直接启动 kernel，不额外安装 boot loader，结果失败了，提示一个 firmware bug 然后一个 kernel panic，然后就没有然后了。这个我上面 usb boot 的时候遇到过，后来我尝试了用 usb 中 bootx64.efi 启动，发现可以，这个的意思就是你没法用 efi\_stub 来直接 boot 你的系统，需要依赖一个 boot loader 来载入 kernel。

   运行下面的命令安装 grub

        pacman -S grub-efi-x86_64 dosfstools efibootmgr
        grub-install --target=x86_64-efi --efi-directory=$esp --bootloader-id=grub --recheck --debug
        grub-mkconfig -o /boot/grub/grub.cfg

10. 完事重启

        exit
        umount -R /mnt/
        reboot

### 3. Post Install

1. 安装显卡驱动

   运行下面命令查看显卡信息

        lspci | grep VGA

   MBA 是 intel 的显卡，安装 `xf86-video-intel`

2. 声音

   install alsa-utils, run alsamixer and press 'm' to unmute master and up/down arrow to increase/decrease the volume

3. touchpad

   install xf86-input-synaptics to enable touchpad. (mouse pointer is much more stable with xf86-input-synaptics than xf86-input-mtrack-git)

