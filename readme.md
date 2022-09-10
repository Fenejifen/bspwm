# 我的bspwm配置
<!-- @import "[TOC]" {cmd="toc" depthFrom=1 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->
- [这是什么](#这是什么)
- [我的bspwm配置](#我的bspwm配置)
  - [这是什么](#这是什么)
  - [各文件内容说明](#各文件内容说明)
  - [快捷键大全](#快捷键大全)
  - [安装依赖](#安装依赖)

<!-- /code_chunk_output -->
## 这是什么

基于[arcolinux自带的bspwm配置](https://github.com/arcolinux/arcolinux-bspwm)的自用改版

## 各文件内容说明

.
├── autostart.sh                  |启动bspwm时启动的任务
├── bspwmrc                       |bspwm配置文件，随bspwm一起启动和autostart其实一样
├── picom.conf
├── readme.md                     |readme文件
├── scripts
│   ├── adjust-new-window
│   ├── external_rules_command
│   ├── move-window               |移动浮窗脚本
│   ├── move-window-py.py         |移动任何窗口脚本
│   ├── picom-toggle.sh
│   └── pseudo_automatic_mode
├── sxhkd
│   ├── sxhkdrc                   |快捷键配置
│   └── sxhkdrc-azerty
├── system-overview               |cronky配置
└── wall.png

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

## 安装依赖

- flameshot

