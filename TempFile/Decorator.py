# -*- coding: utf-8 -*- 
'''
Created on 2016��8��24��

@author: xiong
'''

#文件编译的时候，函数被编译到装饰函数中，再执行相关函数的时候，其实是调用装饰函数



def Decorator(fun):
    def test():
        print 'header'
        fun()
    return test

@Decorator
def fun1():
    print "this is test 1"
@Decorator
def fun2():
    print 'this is test 2'
@Decorator
def fun3():
    print 'this is test 3'

fun1()
fun2()
fun3()
