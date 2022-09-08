#!/usr/bin/env python
# coding=utf-8
import os, sys

# 直接调用原脚本，如果是浮动窗口则无需进行操作，如果不是则进行操作
status_code = os.system('~/.config/bspwm/scripts/move-window {}'.format(sys.argv[1]))

# 非浮动窗口情况下,运行bspc命令
if status_code == 2560:
    direction = sys.argv[1]
    if direction == "west" or direction == "edge-west" :
        #向左移动
        os.system("bspc node -z left -20 0")
        os.system("bspc node -z right -20 0")
    elif direction=='east' or direction == "edge-east":
        #向右移动
        os.system("bspc node -z left 20 0")
        os.system("bspc node -z right 20 0")
    elif direction=='south' or direction == "edge-south":
        #向下移动
        os.system("bspc node -z bottom 0 20")
        os.system("bspc node -z top 0 20")
    elif direction=='north' or direction == "edge-north":
        #向上移动
        os.system("bspc node -z bottom 0 -20")
        os.system("bspc node -z top 0 -20")
