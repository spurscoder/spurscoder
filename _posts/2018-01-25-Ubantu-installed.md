---
layout: post
title: "After ubuntu installed"
author: "Spurs"
date: 2018-01-25 12:00:00
tags:
  - dinary
  - everyday
---



## Ubuntu 安装后需要做的一些事

**注：频繁重装系统，记录一些必做的操作，个性化自己的操作系统。**

## 首先设置ROOT

```
sudo passwd root
```

## 更新一下系统

命令如下：

```
sudo apt-get update
sudo apt-get upgrade
```

## 卸载一些不必要的软件

**卸载 LibreOffice**

LibreOffice运行比较慢，体验并不是很好，我们可以安装WPS替代，卸载命令如下：

```
sudo apt-get remove --purge libreoffice*
```

**卸载一些不常用的软件**

```
sudo apt-get remove thunderbird totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot 
sudo apt-get remove gnome-mines cheese transmission-common gnome-orca webbrowser-app gnome-sudoku  landscape-client-ui-install  
sudo apt-get remove onboard deja-dup
```

## 安装一些软件

**安装sogou输入法**

官网：<http://pinyin.sogou.com/linux/>。下载deb包。双击deb安装，也可以通过以下命令安装：

```
sudo dpkg -i sogou-****.deb
```

**安装 rar**

这东西看名字就知道干什么的了。

```
sudo apt-get install rar
```

**安装 git**

这个不用多说，github程序猿必备。

```
sudo apt-get install git
```

**安装 Unity Tweak Tool**

在你能对Ubuntu外观做任何有效地修改之前，我们不得不安装[Unity Tweak Tool](https://apps.ubuntu.com/cat/applications/unity-tweak-tool/)。这是一个Unity桌面环境下特殊设置管理软件，并且通过它，我们可以实现替换系统图标和主题。可以使用下面的命令安装：

```
sudo apt-get install unity-tweak-tool
```

**安装 WPS**

除延续Windows版相同体验外，更加尊重Linux用户特定的使用习惯，深度兼容。可以到<http://linux.wps.cn/>下载WPS的安装包。切到安装包所在目录，用以下命令安装WPS：

```
sudo dpkg -i wps-office_10.1.0.5672-a21_amd64.deb
```

**安装 Typora**

Typora：极致简洁的 Markdown 编辑器。Markdown 是个好东西，用它写东西可以几乎不用考虑排版就可以得到还过得去的文章格式，作为学生党用来平时记东西很方便。Typora官网：<https://typora.io/>。Typora将「写字」和「预览」这两件事情合并了，你输入的地方，也是输出的地方，即现在很流行的 WYSIWYG（What You See Is What You Get）。一切都变得如此干净、纯粹。输入以下命令安装：

```
# optional, but recommended
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys BA300B7755AFCFAE
# add Typora's repository
sudo add-apt-repository 'deb https://typora.io ./linux/'
sudo apt-get update
# install typora
sudo apt-get install typora
```

**安装 Shadowsocks**

对于这个软件就不多做介绍了，知道的人应该都很熟悉。算是技术宅必备吧。安装命令如下：

```
sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5
```

- 先决条件 装 pip

```
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv
```

- 然后 装 genpac

```
sudo pip install genpac
pip install --upgrade genpac
```

- 可以在 <https://github.com/gfwlist/gfwlist> 查看 gfwlist.txt的网站，然后通过命令，产生 autoproxy.pac，SS务必打开 连接上服务器

```
genpac -p "SOCKS5 127.0.0.1:1080" --gfwlist-proxy="SOCKS5 127.0.0.1:1080" --output="autoproxy.pac" --gfwlist-url="https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
```

- 设置为网络代理模式 自动，记录输出的autoproxy.pac的位置。网络 -> 网络代理 -> 自动 -> "file:///home/ultraji/Something/4ss/autoproxy.pac"(例如这是我的位置) -> 应用到整个系统。

**安装 Chromium 浏览器**

个人更偏爱 Chromium 浏览器。能同步其他设备的浏览记录等等。安装命令如下：

```
sudo apt-get install chromium-browser
```

**安装 Flash 插件**

我装了 Chromium 浏览器，但是当打开视频网站的时候提示需要安装flash插件。安装 flash 插件命令如下：

```
sudo apt-get install adobe-flashplugin
```

**安装 Sublime Text 3 或 Atom**

Sublime Text 3 安装，官网：<https://www.sublimetext.com/>，下载安装包，安装命令如下：

```
sudo dpkg -i sublime-text_build-3126_amd64.deb
```

Sublime Text 3 自动安装 Package Control

```
import  urllib.request,os;pf='Package Control.sublime-package';ipp=sublime.installed_packages_path();urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler()));open(os.path.join(ipp,pf),'wb').write(urllib.request.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read())
```

Atom 安装，官网：<https://atom.io/>，下载安装包，安装命令如下：

```
sudo dpkg -i atom-amd64.deb
```

**安装网易云音乐**

这款良心软件就不多介绍了，体验和 windows 下一样。官网：<http://music.163.com/>。下载安装包，安装命令如下：

```
sudo dpkg -i netease-cloud-music_1.0.0_amd64_ubuntu16.04.deb
```

**安装 Teamviewer**

这是一款很不错的远程控制软件。官网：<https://www.teamviewer.com/zhcn/>。下载安装包，安装命令如下：

```
sudo dpkg -i teamviewer_12.0.71510_i386.deb
```

**安装 uGet**

uGet是个替代迅雷的下载工具。这东西大家都说好用，虽然我安装了，但并不怎么用到，没实际体验过。安装命令如下：

```
sudo add-apt-repository ppa:plushuang-tw/uget-stable
# 添加aria2的依赖
sudo add-apt-repository ppa:t-tujikawa/ppa

sudo apt-get update

sudo apt-get install uget
sudo apt-get install aria2
```

依次打开界面的编辑->设置，打开设置界面，切换到“插件”界面，然后勾选“启用aria2插件”启用aria2，这里只需要设置这个地方就行了。

**安装 gThumb**

gThumb 是一个 GNOME 桌面环境下的开源图像浏览器，遵循 GPL 版权协议。原先基于 GQView ，设计成为一个简洁的界面。它包含许多基本的图像编辑特性，如旋转，缩放，裁剪，图像增强过滤（如颜色，亮度，对比度调整）。gThumb也包含一些重要的特性，如拷贝，移动，删除，复制图像，打印，放大，格式转换，批量重命名。安装命令如下：

```
sudo add-apt-repository ppa:webupd8team/gthumb
sudo apt-get update
sudo apt-get install gthumb
```

**安装VLC播放器**

VLC 是一款自由、开源的跨平台多媒体播放器及框架，可播放大多数多媒体文件，以及 DVD、音频 CD、VCD 及各类流媒体协议。安装命令如下：

```
sudo apt-get install vlc browser-plugin-vlc
```

**安装 conky**

Conky是一个轻量级桌面系统监视软件。该软件本身是非常简单的，不过它是可定制的，这样一来它就可以显示很多的有用的信息。你可以通过在终端输入以下命令来安装Conky：

```
sudo apt-get install conky conky-all
```

你将会需要curl这个软件，你可以通过以下这个命令来安装该软件：

```
sudo apt-get install curl
```

## 安装主题

对于Ubuntu有很多定制的主题，这些主题可以影响应用和窗口的外观。

**安装 Numix Circle 图标集**

个人觉得圆形图标集 Numix Circle 很不错。你可以在<http://numixproject.org/>找到关于Numix主题和图标的更多信息。输入以下命令来安装 Numix 图标：

```
sudo add-apt-repository ppa:numix/ppa
sudo apt-get update
sudo apt-get install numix-icon-theme-circle
```

**安装 Flatabulous 主题**

Flatabulous: 一个超好看的扁平化 Ubuntu 桌面主题。对于 Ubuntu 自带的主题，我个人不太喜欢，个人比较喜欢扁平化的风格。Github 入口：<https://github.com/anmoljagetia/Flatabulous> 。输入以下命令来安装 Flatabulous 主题：

```
sudo add-apt-repository ppa:noobslab/themes
sudo apt-get update
sudo apt-get install flatabulous-theme
```

## 安装 JAVA 环境

新建java文件夹

```
sudo mkdir /usr/local/java
```

将下载的包复制到java文件夹下

```
sudo cp Downloads/jdk-8u101-linux-x64.tar.gz /usr/local/java/
```

进入文件夹下

```
cd /usr/local/java/
```

解压压缩包

```
sudo tar -zxvf jdk-8u101-linux-x64.tar.gz
```

删除压缩包

```
sudo rm jdk-8u101-linux-x64.tar.gz
```

设置环境变量

```
sudo gedit /etc/profile
```

末尾追加

```
export JAVA_HOME=/usr/local/java/jdk1.8.0_101  

export JRE_HOME=${JAVA_HOME}/jre  

export CLASSPATH=.:{JAVA_HOME}/lib:{JRE_HOME}/lib  

export PATH={JAVA_HOME}/bin:PATH
```

刷新变量

```
source /etc/profile
```

验证

```
java -version
```

若

> ultraji@JiJi:~$ java -version
>
> java version "1.8.0_101"_
>
> Java(TM) SE Runtime Environment (build 1.8.0_101-b13)
>
> Java HotSpot(TM) 64-Bit Server VM (build 25.101-b13, mixed mode)

则成功了。

## 瘦身

**清除已经卸载软件的配置文件**

切换到root用户下，用以下命令清除已经卸载软件的配置文件：

```
dpkg -l |grep "^rc"|awk '{print $2}' |xargs aptitude -y purge
```

**卸载旧内核**

通过以下命令查看当前内核。

```
uname -a
```

首先使用命令，列出所有安装的内核，下表中，带有image的就是内核文件，从中选择要卸载的包，用apt-get来卸载。

```
dpkg --get-selections|grep linux
```

通过类似如下命令卸载旧内核：

```
sudo apt-get remove linux-imge-2.6.15-23-386
```