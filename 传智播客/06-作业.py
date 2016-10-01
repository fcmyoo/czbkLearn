# # 正序
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         if j * i < 10:
#             print('%d x %d = %d' % (i, j, i * j), end='    ')
#         else:
#             print('%d x %d = %d' % (i, j, i * j), end='   ')
#         j += 1
#     print('')
#     i += 1
#
# # 倒序
# i = 9
# while i >= 1:
#     j = 1
#     while j <= i:
#         if j * i < 10:
#             print('%d x %d = %d' % (i, j, i * j), end='    ')
#         else:
#             print('%d x %d = %d' % (i, j, i * j), end='   ')
#         j += 1
#     print('')
#     i -= 1

# # 这是一个算时候闰年的方法
# def IsLeapYear(year):
#     if year % 100 == 0:
#         if year % 400 == 0:
#             return True
#         else:
#             return False
#     else:
#         if year % 4 == 0:
#             return True
#         else:
#             return False
#
#
# year = int(input('输入年份:'))
# y = IsLeapYear(year)
# if y:
#     print('yes')
# else:
#     print('no')

# year = int(input("输入年份:"))
# if year % 100 == 0:
#     if year % 400 == 0:
#         print('是闰年')
#     else:
#         print('是闰年')
# else:
#     if year % 4 == 0:
#         print('是闰年')
#     else:
#         print('不是是闰年')
#
