#!/usr/bin/env python
#coding:utf-8
'''
class Alex:
    xx = '没心没肺'
    
class Person:
    
    xue = '血'
    
    def __init__(self,name,age):
        self.name = name
    
p1 = Person('李阳',18)
print p1.name
p2 = Person('老苟',16)
print p2.name
'''


class Province(object):
    #静态字段
    memo = '中国的23个省之一'
    
    def __init__(self,name,capital,leader,flag):
        #动态字段
        self.Name = name
        self.Capital = capital
        self.Leader = leader
        
        self.__Thailand = flag
    #动态方法 
    def sports_meet(self):
        print self.Name + '正在开运动会'
    
    #静态方法
    @staticmethod 
    def Foo():
        print '每个省要带头反腐'   
    
    @property
    def Bar(self):
        #print self.Name 
        return 'somthing'
    
    def show(self):
        print self.__Thailand
        
    def __sha(self):
        print '我是alex'
        
    def Foo2(self):
        self.__sha()
    
    #只读
    @property
    def Thailand(self):
        return self.__Thailand
    '''
    #只写
    @Thailand.setter
    def Thailand(self,value):
        self.__Thailand = value
    '''
        
#hb = Province('河北','石家庄','李扬')
#sd = Province('山东','济南','王胜辉')
#japan = Province('日本','济南','王胜辉',True)
#print japan.__Thailand
#japan.show()
#japan.__sha()
#japan.Foo2()
#japan._Province__sha()
#print japan.Thailand
#hb.Name
#hb.sports_meet()
#hb.Bar

#print hb.Capital
#print Province.memo

#类不能访问动态字段
#print Province.Name
#对象可以访问静态字段
#print hb.memo

#执行动态方法
#hb.sports_meet()
#sd.sports_meet()

#执行静态方法
#Province.Foo()

#执行特性
#hb.Bar


'''
japan = Province('日本','济南','王胜辉',True)
print japan.Thailand
japan.Thailand = False
print japan.Thailand
'''
'''  
class test1:
    
    def __init__(self):
        self.__pravite = 'alex 1'
    
    @property
    def Show(self):
        return self.__pravite
    
class test2(object):
    
    def __init__(self):
        self.__pravite = 'alex 2'
    
    @property
    def Show(self):
        return self.__pravite
    @Show.setter
    def Show(self,value):
        self.__pravite = value
    
t1 = test1()
print t1.Show
t1.Show = 'change 1'
print t1.Show

    
t2 = test2()
print t2.Show
t2.Show = 'change 3'
print t2.Show
''' 
''' 
import time
class Foo:
    def __init__(self):
        pass
    
    def __del__(self):
        print '解释器要销毁我了，我要做租后一次的呐喊！'
    
    def Go(self):
        print 'GO'
    def __call__(self):
        print 'call'
#f1 = Foo() #实例化类
#f1.Go()

#time.sleep(100)

#f1() #执行类的 __call__ 方法；实例化对象

Foo()()
f1 = Foo() 
f1()
''' 
# 
class Father(object):
    def __init__(self):
        self.Fname = 'ffff'
        print 'father.__init__'
        
    def Func(self): 
        print 'father.Func'
    def Bad(self):
        print 'father.抽烟喝酒烫头'
         
class Son(Father,):
    def __init__(self):
        self.Sname = 'ssss'  
        print 'son.__init__'
        #Father.__init__(self)
        super(Son,self).__init__()
    def Bar(self):
        print 'son.bar'
    '''
    def Bad(self):
        print 'son.抽烟喝酒'
    '''
    def Bad(self):
        Father.Bad(self)
        print 'son.赌博'
#父类，子类
#基类，派生类        
s1 = Son()
s1.Bar()
s1.Func()
s1.Bad()


from abc import ABCMeta, abstractmethod
class Alert:
    __metaclass__ = ABCMeta

    @abstractmethod
    def Send(self):pass
 
# 抽象类+抽象方法   = 接口（第二种接口，即：规范）
 
 
 
class Foo(Alert):
    def __init__(self):
        print '__init__'




        
        
                



        

    
    

    
