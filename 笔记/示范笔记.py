# -*- ecoding: utf-8 -*-
# @ModuleName: 示范笔记
# @Author: Kerris
# @Time: 2023/2/9 11:18
"""————————————————————循环示范————————————————————"""
print("----------计算x的n次方----------")
def power(x, n):    #X和n都是位置参数，有先后顺序，故给定默认指数的时候，默认指数在前的赋值就没有意义了
    s = 1
    while n > 0:    #当N大于0时重复执行下列操作
        n = n - 1   #次方数-1
        s = s * x   #s被重新赋值，重新计算，返回循环操作
    return s        #输出s

print(power(5,3))

print("----------计算各个数相乘的数值----------")
def mul(x,*s):
    m = x
    for n in s:
        m = m*n
    return m

print(mul(2,3,4,5))


