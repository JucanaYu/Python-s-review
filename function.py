#试着用函数版本的hello world
def hello():
    print("hello world")

hello()

#函数版本的比较数字大小
def compare_int(a,b):
    if a>b:
        print("a比b大")
    elif a==b:
        print("a等于b")
    elif a<b:
        print("a小于b")

a=input("输入a的值:")
b=input("输入b的值:")
compare_int(a,b)

#计算面积，长*宽
def area(width,height):
    return int(width*height)

width=int(input("输入长："))
height=int(input("输入宽："))
area_result=area(width,height)
print("面积为：",area_result)

##加入不定长参数
#加*的参数会以元组（tuple）的形式导入，但是记得放在最后一个参数
def printinfo_tuple(*vartuple):
    print("输出：",vartuple)

printinfo_tuple(40,50,60)

#加**的参数会以字典（dictionary）的形式导入，但是记得放在最后一个参数
def printinfo_dictionary(**vardictionary):
    print("输出：",vardictionary)

printinfo_dictionary(a=1,b=-2)