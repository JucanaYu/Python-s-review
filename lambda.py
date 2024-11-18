#lambda函数小型的，它可以具有任意数量的参数，但只能有一个表达式
#lambda arguments:expression
x=1
y=2

sum1=lambda x,y:x+y

def sum2(x,y):
    return(x+y)

print("sum1:",sum1(x,y))
print("sum2:",sum2(x,y))