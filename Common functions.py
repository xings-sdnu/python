import os
import random
# 冒泡排序
list = [56, 12, 1, 8, 354, 10, 100, 34, 56, 7, 23, 456, 234, -58]


def sortport():
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


result = sortport()


# print(result)


# 计算x的n次方的方法
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# print(power(2, 3))


# 计算 a*a + b*b +c*c + ...
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


# print(calc(1, 2))


# 计算阶乘
def fac():
    num = int(input("请输入一个数字："))
    factorial = 1
    # 查看数字是负数，0或正数
    if num < 0:
        print("抱歉，负数没有阶乘")
    elif num == 0:
        print("0的阶乘为1")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f'{num}的阶乘为{factorial}')


# fac()

# 列出当前目录下的所有文件和目录名
# [print(d) for d in os.listdir('.')]


# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']


# [print(s.lower()) for s in L]


# 输出某个路径下的所有文件和文件夹的路径
def print_dir():
    filepath = input("请输入一个路径：")
    if filepath == "":
        print("请输入正确的路径")
    else:
        # 获取目录中的文件及子目录列表
        for i in os.listdir(filepath):
            # 把路径组合起来
            print(os.path.join(filepath, i))


# print(print_dir())


# 输出某个路径及其子目录下所有以.html为后缀的文件
def print_dir(filepath):
    for i in os.listdir(filepath):
        path = os.path.join(filepath, i)
        if os.path.isdir(path):
            print_dir(path)
        if path.endswith(".html"):
            print(path)


filepath = "D:\学校\第一学期"
# print(print_dir(filepath))


# 把字典的键值对颠倒并生产新的字典
dict1 = {"A": "a", "B": "b", "C": "c"}
dict2 = {y: x for x, y in dict1.items()}
# print(dict2)

# 打印九九乘法表
# for i in range(1, 10):
#     for j in range(1, i+1):
#         # print(('{}x{}={}\t.format(j,i,i*j'), end='')
#         print('%d x %d = %d \t' % (i, j, i*j), end='')
# print()

# 替换列表中所有的3为3a
num = ["harden", "lampard", 3, 34, 45, 56, 76, 87, 78, 45, 3, 3, 3, 87686, 98, 76]
# 获取3出现的次数
for i in range(num.count(3)):
    # 获取首次出现3的坐标
    ele_index = num.index(3)
    # 修改3为3a
    num[ele_index] = "3a"
    # print(num)

# 打印每个名字
L = ["James", "Meng", "Xin"]
# for i in range(len(L)):
#     print("Hello,%s" % L[i])

# 合并去重
list1 = [2, 3, 8, 4, 9, 5, 6]
list2 = [5, 6, 10, 17, 11, 2]
list3 = list1 + list2
# print(list3)
# print(set(list3))

# 随机生成验证码的两种方式
list1 = []
for i in range(65, 91):
    list1.append(chr(i))
for j in range(97, 123):
    list1.append(chr(j))
for k in range(48, 58):
    list1.append(chr(k))
ma = random.sample(list1, 6)
# print(ma)
ma = ''.join(ma)
# print(ma)

import string
str1 = "0123456789"
str2 = string.ascii_letters
str3 = str1+str2
ma1 = random.sample(str3, 6)
ma1 = ''.join(ma1)
# print(ma1)

# 计算平方根
# num = float(input('请输入一个数字：'))
# num_sqrt = num ** 0.5
# print('%0.2f 的平方根为 %0.2f' % (num, num_sqrt))

# 判断奇偶数
# num = int(input("输入一个数字:"))
# if (num % 2) == 0:
#     print("{0}是偶数".format(num))
# else:
#     print("{0} 是奇数".format(num))

# while True:
#     try:
#         num = int(input('输入一个整数:'))
#     except ValueError:
#         print("输入的不是整数")
#         continue
#     if num % 2 == 0:
#         print('偶数')
#     else:
#         print('奇数')
#     break


# 判断闰年
# year = int(input("输入一个年份："))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("{0}是闰年".format(year))
#         else:
#             print("{0}不是闰年".format(year))
#     else:
#         print("{0}是闰年".format(year))
# else:
#     print("{0}不是闰年".format(year))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("{0}是闰年".format(year))
# else:
#     print("{0}不是闰年".format(year))

# import calendar
# check_year = calendar.isleap(year)
# if check_year:
#     print("%d是闰年%" %year)
# else:
#     print("%d是平年" %year)

# 获取最大值
N = int(input('输入需要对比大小数字的个数：'))
num = []
for i in range(1, N+1):
    temp = int(input("输入第{}个数字：") .format(i))
    num.append(temp)
print('您输入的数字为：', num)
print('最大值为：', max(num))