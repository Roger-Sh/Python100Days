"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素

Version: 0.1
Author: 骆昊
Date: 2018-03-06
"""


def main():

    # 定义列表
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']

    # 循环遍历列表元素
    for fruit in fruits:
        print(fruit.title(), end=' ') # 输出元素，没有列表的格式，只有内容
    print()

    # 列表切片
    fruits2 = fruits[1:4]
    print(fruits2)

    # 列表的复制
    fruit3 = fruits                     # 没有复制列表只创建了新的引用，改变原列表会同时改变新列表
    fruits3 = fruits[:]                 # 复制到一个新的列表, 改变原列表不会改变新列表
    print(fruit3)                       # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
    fruits.append('avocado')
    print(fruit3)                       # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango', 'avocado']
    print(fruits3)                      # ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']

    # 列表的逆向，倒数切片
    fruits4 = fruits[-3:-1]             # 复制原列表倒数第三到倒数第二，-1是开区间
    print(fruits4)

    # 列表 逆向，
    fruits5 = fruits[::-1]              # 从倒数第一到倒数最后
    print(fruits5)
    fruits6 = fruits[:-4:-1]            # 从倒数第一到倒数第三
    print(fruits6)


if __name__ == '__main__':
    main()
