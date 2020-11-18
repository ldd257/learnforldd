# _*_ coding:utf-8 _*_
import random

"""
改造点
1、当用户猜错的时候，程序应给出提示
2、应该提供多次机会给用户
3、每次运行程序，答案应该是随机的
"""

# 该造点1(嵌套循环判断)
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
guess = int(temp)

if guess == 8:
    print("你是小甲鱼心里的蛀虫嘛？！")
    print("哼，猜中也没奖励！")
else:
    if guess > 8:
        print("猜大了...")
    else:
        print("猜小了...")
print("游戏结束，不玩了^-^")


# 改造点2(循环)
# while for 构成python循环结构
# break 跳出循环 continue 跳过本次循环

# 实现方式一
count = int(input("请输入循环次数"))
while count > 0:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)

    if guess == 8:
        print("你是小甲鱼心里的蛀虫嘛？！")
        print("哼，猜中也没奖励！")
        break
    else:
        if guess > 8:
            print("猜大了...")
        else:
            print("猜小了...")
        count -= 1
else:
    print("游戏结束，不玩了^-^")

# 实现方式二
count2 = int(input("请输入循环次数"))
for a in range(count2):
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)

    if guess == 8:
        print("你是小甲鱼心里的蛀虫嘛？！")
        print("哼，猜中也没奖励！")
        break
    else:
        if guess > 8:
            print("猜大了...")
        else:
            print("猜小了...")
        count2 -= 1
else:
    print("游戏结束，不玩了^-^")

# 改造点3
# 增加random获取随机数模块(random)
answer = random.randint(1, 10)
count = int(input("请输入循环次数"))
while count > 0:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    guess = int(temp)

    if guess == answer:
        print("你是小甲鱼心里的蛀虫嘛？！")
        print("哼，猜中也没奖励！")
        break
    else:
        if guess > answer:
            print("猜大了...")
        else:
            print("猜小了...")
        count -= 1
else:
    print("游戏结束，不玩了^-^")