import sys

list=[1,2,3,4]
it=iter(list)   #迭代器初始化

#使用for遍历
for i in it:
    print(i,end=" ")

#在这里重新初始化了一个迭代器，是因为迭代器在输出之后就不会保存内容了
list=[1,2,3,4]
it=iter(list)   #迭代器初始化
#使用next遍历
while True:
    try:
        print(next(it),end=" ")
    except StopIteration:
        sys.exit()
