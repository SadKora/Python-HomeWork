# 判断是否为奇偶数
def isoddNum(num):
    if num % 2 == 0:
        print(f"{num} 是偶数")
    else:
        print(f"{num} 是奇数")

# 获取用户输入的数字
num = int(input("请输入一个整数："))
check_odd_even(num)
