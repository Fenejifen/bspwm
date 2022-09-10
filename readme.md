# 我的bspwm配置
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->
- [这是什么](#这是什么)
- [我的bspwm配置](#我的bspwm配置)
  - [这是什么](#这是什么)
  - [各文件内容说明](#各文件内容说明)
  - [快捷键大全](#快捷键大全)
  - [额外安装](#额外安装)

<!-- /code_chunk_output -->
## 这是什么

基于[arcolinux自带的bspwm配置](https://github.com/arcolinux/arcolinux-bspwm)的自用改版

## 各文件内容说明

. </br>
├── autostart.sh                  |启动bspwm时启动的任务 </br>
├── bspwmrc                       |bspwm配置文件，随bspwm一起启动和autostart其实一样 </br>
├── picom.conf </br>
├── readme.md                     |readme文件 </br>
├── scripts </br>
│   ├── adjust-new-window </br>
│   ├── external_rules_command </br>
│   ├── move-window               |移动浮窗脚本 </br>
│   ├── move-window-py.py         |移动任何窗口脚本 </br>
│   ├── picom-toggle.sh </br>
│   └── pseudo_automatic_mode </br>
├── sxhkd </br>
│   ├── sxhkdrc                   |快捷键配置 </br>
│   └── sxhkdrc-azerty </br>
├── system-overview               |cronky配置 </br>
└── wall.png </br>

## 快捷键大全

`printscreen` 截图

`super+w` 浏览器

`super + shift + enter` 终端

`super + e` 文件管理器

`super + shift + d` 应用启动器

`ctrl + shift + esc` 任务管理器

`super + shift + s` 重新载入快捷键设置

`super + x` 退出界面(注销、重启、关机)

`super + esc` 鼠标选择窗口进行关闭

`super + hjkl` 切换注视窗口

`super + shift + hjkl`扩展减小窗口

`super + alt + hjkl` 窗口换位

`super + []` 放大缩小窗口，和按住super然后鼠标滚轮是一个效果

## 额外安装

- flameshot

