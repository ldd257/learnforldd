# -*- coding:utf-8 -*-
# Author:dongdong Liu

# 运算符优先级

print(not 1)
# not 颠倒黑白

print(0 and 3)
print(3 and 0)
# and 打假 看见false即为结束

print(3 or 0)
print(0 or 3)
# or 求真 看见true即为结束


# 优先级
"""
() [] {}        绑定或元组显示，列表显示，字典显示，集合显示
x[index] x[index:index] x(arguments...) x.attribute  下标、切片、函数调用、属性引用
await x         Await 表达式
**              指数
+x -x ~x        正号，负号，按位反转
*  @  /  // %   乘法 矩阵乘法  除法 地板除
+ -             加法 减法
<<  >>          位移
&               按位与
^               按位异或
|               按位或
in not in is is not < <= > >= != == 成员测试，同一性测试，比较
not x           布尔'非'
and             布尔'与'
or              布尔'或'
if-else         条件表达式
lambda          Lambda表达式


总结：之前总结，非算关逻条赋
包裹-切分-正负位移-乘加计算-成员逻辑
"""
