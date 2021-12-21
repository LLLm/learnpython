#!/usr/bin/python

import time
#引入time模块
i = 1
#从1开始数起
while True:
#当前面灯饰成立的时候进入循环，使用了True使循环无限进行下去
    print(i)#输出第一个数字
    i = i + 1#输出之后+1
    time.sleep(1)#延时一秒，如果想要数字出现得更慢可以改大
