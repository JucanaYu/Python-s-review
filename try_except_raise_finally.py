a=5.0
b=float(input("输入除数浮点数："))

try:
    if b==0.0:
        raise ZeroDivisionError("除数不能为0")
    a/b   #正常情况，输出的是try else finally
    print("输出try成功")
    
except ZeroDivisionError as z:
    print("输出except成功，但是为异常：",z)

else:
    print("输出else成功")

finally:
    print("输出finally成功")