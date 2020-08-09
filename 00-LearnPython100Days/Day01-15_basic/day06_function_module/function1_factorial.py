"""
函数的定义和使用 - 计算组合数C(7,3)
x1 + x2 + x3 + x4 = 8 有几个正整数解

Version: 0.1
Author: 骆昊
Date: 2018-03-05
"""


# 将求阶乘的功能封装成一个函数
def factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


print(factorial(7) // factorial(3) // factorial(4))
