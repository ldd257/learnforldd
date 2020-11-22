
# 简单分支
"""
if condition:
    满足条件执行体
"""
age = 26
if 0 < age <= 18:
    print("你已经成年~")

# 增加分支
"""
if condition:
    满足条件执行体
else:
    不满足条件执行体
"""
age = 26
if 0 < age <= 18:
    print("你已经成年~")
else:
    print("你还未成年~")

# 增加分支
"""
if condition:
    满足条件执行体1
elif condition:
    满足条件执行体2
else:
    不满足条件执行体
"""
age = 26
if 0 < age <= 18:
    print("你已经成年~")
elif 18 <= age <= 60:
    print("你正直壮年~")
else:
    print("你还未成年~")


# 分支嵌套
age = 26
if 0 < age <= 18:
    print("你已经成年~")
elif 18 <= age <= 60:
    print("你正直壮年~")
    if 18 <= age <= 30:
        print("你该成家了~")
else:
    print("你还未成年~")


# 三目运算符
"""
满足条件体 if condition else 不满足条件体
"""
age = 26
print("你已经成年~" if 0 < age <= 18 else "你还未成年~")


