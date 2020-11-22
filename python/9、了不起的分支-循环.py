# -*- coding:utf-8 -*-
# Author:dongdong Liu

# 循环分为俩类 while for
"""
while condition:
    满足条件执行体
else
    循环最后执行体
"""
age = 0
while age < 18:
    print("你还未成年~")
    age += 1
else:
    print("结束")

# 循环嵌套  乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, "*", i, "=", i * j, end="  ")
        j += 1
    print("")
    i += 1

# break continue
"""
break   跳出循环
continue    跳过本次循环
"""
num = 8
while True:
    num -= 1
    if num < 0:
        print("跳出循环")
        break
    print(num % 2 == 0)
    if num % 2 == 0:
        print("我是偶数")
    else:
        print("跳过本次循环")
        continue

# for 循环
"""
for 个体 in 迭代体:
    执行循环体

跌代体
字符串 列表  元组  字典  集合
"""
# 循环迭代体中每一个元素
for each in "liudongdong":
    print(each)

# 循环从一到十，步长为二的数
for each in range(1, 10, 2):
    print(each)
