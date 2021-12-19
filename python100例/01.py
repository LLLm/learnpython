#!/usr/bin/python
#-*- coding: UTF-8 -*-


#题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

#程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
for i in range(1,5):#放入数字1到5的循环(循环中不包括5)
    for j in range(1,5):
        for k in range(1,5):#多次取1到5的循环，将四个数字全部进行循环，这样可以做出每一位都有不同数字的效果
            if(i!=k) and (i !=j) and (j!=k):#确保每一位的数字不会重复
                print(i,j,k)