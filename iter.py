import sys

list=[1,2,3,4]
it=iter(list)   #迭代器化
while True:
    try:
        print(next(it),end=" ")
    except StopIteration:
        sys.exit()