# 打印欢迎信息
print("欢迎使用Python入门程序！")

# 获取用户输入并将其存储在变量中
name = input("请输入您的名字: ")

# 打印个性化的问候语
print("你好, " + name + "! 很高兴见到你。")

# 演示基本的数据类型
# 整数类型
age = 25

# 浮点数类型
height = 1.75

# 字符串类型
hobby = "编程"

# 布尔类型
is_student = True

# 打印变量的值
print("年龄:", age)
print("身高:", height)
print("爱好:", hobby)
print("是否是学生:", is_student)

# 进行简单的算术运算
num1 = 10
num2 = 5

# 加法
sum_result = num1 + num2
print("加法结果:", sum_result)

# 减法
subtraction_result = num1 - num2
print("减法结果:", subtraction_result)

# 乘法
multiplication_result = num1 * num2
print("乘法结果:", multiplication_result)

# 除法
division_result = num1 / num2
print("除法结果:", division_result)

# 使用条件语句
if age >= 18:
    print("您是成年人。")
else:
    print("您未满18岁。")

# 使用循环语句
# 打印从1到5的数字
for i in range(1, 6):
    print("数字:", i)

# 定义一个简单的函数
def greet_user(username):
    """打印问候语"""
    print("你好, " + username + "! 欢迎回来。")

# 调用函数
greet_user(name)
