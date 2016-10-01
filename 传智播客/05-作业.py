import time

# str1 = 'hello world'
# strPrint = []
# for i in str1:
#     num = str1.count(i)
#     strPrint.append(i)
#     strPrint.append(num)
#     print(i + ":", num)
#
# print(strPrint[0])
# print(strPrint[1])

# def jia(a,b):
#     c=a+b
#     print('你的结果是:%d' %c)
# def jian(a,b):
#     c = a - b
#     print('你的结果是:%d' % c)
# def cheng(a,b):
#     c = a * b
#     print('你的结果是:%d' % c)
# def chu(a,b):
#     c = a / b
#     print('你的结果是:%d' % c)
#
# while True:
#     print('-' * 30)
#     print('欢迎来到简洁版Python计算器')
#     print('-' * 30)
#     yunsuan = input('请输入+,-,*,/,如需退出请按q:')
#     print('-' * 30)
#     if yunsuan=='q':
#         break
#     a = int(input('请输入第一个数:'))
#     print('-' * 30)
#     b = int(input('请输入第二个数:'))
#     print('-' * 30)
#     if yunsuan=='+':
#         jia(a,b)
#     elif yunsuan=='-':
#         jian(a,b)
#     elif yunsuan=='*':
#         cheng(a,b)
#     elif yunsuan=='/':
#         chu(a,b)

# userStudent = {}
# tempInfo = []
#
#
# def add(name, age, stuNo):
#     userStudent['name'] = name
#     userStudent['age'] = int(age)
#     userStudent['stuNo'] = int(stuNo)
#     tempInfo.append(userStudent)
#     print('你的名字是%s,年龄%s,学号%s' % (userStudent['name'], userStudent['age'], userStudent['stuNo']))
#
# def delete(stuNo):
#     tempInfo.remove(stuNo)
#
#
# while True:
#     print('*' * 50)
#     print('欢迎来到python学生管理系统')
#     print('*' * 50)
#     print('''
#     1,添加;
#     2,删除;
#     3,修改;
#     4,查询;
#     5,退出;
#     ''')
#     tempSelect = int(input("请输入相应的选项;"))
#     if tempSelect == 1:
#         print('你选择的是添加,请输入下列信息:')
#         name = input('请输入你的姓名')
#         age = input('请输入你的年龄')
#         stuNo = input('请输入你的学号')
#         add(name, age, stuNo)
#         # time.sleep(2)
#     elif tempSelect == 2:
#         print('序号   学号  姓名   年龄')
#         i=0
#         for stu in tempInfo:
#             print('%d   %d  %s   %d' %(i,stu['stuNo'],stu['name'],stu['age']))
#             i+=1
#         stuNo=input('请输入你要删除的学生序号!')
#         if stuNo<len(tempInfo):
#             delete(stuNo)
#         else:
#             print('你输入有误.请输入序号!')
#     elif tempSelect == 3:
#         pass
#     elif tempSelect == 4:
#         pass
#     elif tempSelect == 5:
#         break
#
