#!/usr/bin/python
# coding=utf-8
# 上边这条语句规定了python的解释器  http://www.jianshu.com/p/96d02f07423d


print("Hello, World!")
print ("你好，China")
print '第一次接触python'

# 学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
if True:
    print "true"
else:
    print "false"

# 变量
counter = 100
name = '王宁'
print (name)
print (counter)

# 字符串
country = 'android application'
print(country)
print country[2:5]

# python List
numberList = ['apple', 'cup', 'cigarette', 'hello', 'teacher']
print numberList
print numberList[2:4]

# python 元祖
aaa = ('apple', 786, 2.23, 'john', 70.2)

print aaa  # 输出完整元组
print aaa[0]  # 输出元组的第一个元素
print aaa[1:3]  # 输出第二个至第三个的元素

# python 字典
dictionary = {'name': '王宁', 'age': 26, 'country': 'china'}
print dictionary
print dictionary.keys()
print dictionary.values()

