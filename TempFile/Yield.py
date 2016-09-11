# -*- coding: utf-8 -*- 
'''
Created on 2016��8��21��

@author: xiong
'''

#yield 用于将每次输入内容保存到寄存器中，调用的时候直接遍历调用

def foo():
    a = list()
    a = [2,1,2,1,2,2,2]
    for i in a:
        yield i

a = foo()
for i in a:
    print i

    