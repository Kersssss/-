'''
Author: Kerrrs 2541822105@qq.com
Date: 2023-03-01 12:14:18
LastEditors: Kerrrs 2541822105@qq.com
LastEditTime: 2023-03-01 13:46:43
FilePath: \python_learn\笔记\面向对象编程笔记.py
Description: 

Copyright (c) 2023 by 2541822105@qq.com, All Rights Reserved. 
'''







"""   
----------类----------
————类的创建
class 类的名称:                             类的名称首字母大写（规范）
    native_place='湖北'                     直接写在类里的变量，称为类属性
    def __init__(self,name,age):
        self.name=name                      self.name称为实体属性，进行了一个赋值的操作，
        self.age=age                        将局部变量的name的值赋给实体属性。
        
    实例方法
    def eat(self):
        print('学生在吃饭...')
        
    静态方法
    @staticmethod
    def method():
        print('我使用了staticmethod进行修饰，所以我是静态方法')
        
    类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')
    
    
在类之外定义的称为函数，在类之内定义的称为方法。


————对象的创建
对象的创建又称为类的实例化。

实例名=类名()


































"""